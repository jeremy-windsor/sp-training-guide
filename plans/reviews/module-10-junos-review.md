# Module 10 Junos CLI Validation Report

**Reviewer:** Sentinel (Junos CLI Validator)
**Date:** 2026-03-13
**Scope:** All markdown files under `modules/10-slicing/`

## Summary
- Files reviewed: 8
- Total findings: 13
- Critical: 5
- Minor: 8

## Detailed Findings

---

### Finding 1
- **Severity:** critical
- **File:** `10.1-network-slicing-concepts.md`
- **Lines:** 583–598
- **Current text:**
  ```
  flex-algorithm 128 {
      metric-type igp;
      advertise-definition;
  }
  flex-algorithm 129 {
      metric-type delay;
      advertise-definition;
      admin-group {
          exclude high-latency;
      }
  }
  flex-algorithm 130 {
      metric-type igp;
      advertise-definition;
      admin-group {
          exclude premium;
      }
  }
  ```
- **Correct text:**
  ```
  flex-algorithm 128 {
      definition {
          metric-type igp;
          priority 128;
      }
  }
  flex-algorithm 129 {
      definition {
          metric-type min-unidirectional-link-delay;
          priority 128;
          admin-group {
              exclude high-latency;
          }
      }
  }
  flex-algorithm 130 {
      definition {
          metric-type igp;
          priority 128;
          admin-group {
              exclude premium;
          }
      }
  }
  ```
- **Source:** Junos 23.x Flex-Algorithm configuration guide; also consistent with the correct pattern used in `10.3-5g-xhaul-requirements.md` lines 444–456.
- **Notes:** Three issues compounded:
  1. **Missing `definition` sub-block.** In Junos, Flex-Algo parameters (metric-type, priority, admin-group constraints) must be wrapped in a `definition { }` block. Without it, the router participates in the algo but does not define/advertise the FAD.
  2. **`advertise-definition` is an IOS-XR keyword, not Junos.** In Junos, having the `definition` block with a `priority` value causes the router to advertise the FAD. There is no `advertise-definition` statement.
  3. **`metric-type delay` is not valid Junos.** The correct keyword is `min-unidirectional-link-delay` (full form). Some Junos versions accept `min-delay` but `delay` alone is not accepted.

  Note: The 10.3 file gets this right with `definition { metric-type min-delay; priority 100; }` — the inconsistency between files compounds the issue.

---

### Finding 2
- **Severity:** critical
- **File:** `10.1-network-slicing-concepts.md`
- **Lines:** 636–648
- **Current text:**
  ```
  protocols {
      isis {
          interface lo0.0 {
              level 2 {
                  node-segment {
                      ipv4-index 1;
                      algorithm [ 128 129 130 ];
                      ipv4-index-algorithm {
                          128 index 128;
                          129 index 129;
                          130 index 130;
                      }
                  }
              }
          }
      }
  }
  ```
- **Correct text:**
  ```
  protocols {
      isis {
          source-packet-routing {
              node-segment {
                  ipv4-index 1;
                  flex-algorithm 128 {
                      ipv4-index 128;
                  }
                  flex-algorithm 129 {
                      ipv4-index 129;
                  }
                  flex-algorithm 130 {
                      ipv4-index 130;
                  }
              }
          }
      }
  }
  ```
- **Source:** Junos 23.x SR/Flex-Algorithm documentation; consistent with the correct pattern used in `10.3-5g-xhaul-requirements.md` lines 457–466.
- **Notes:** Multiple issues:
  1. **Wrong hierarchy.** Per-Flex-Algo prefix SIDs in Junos are configured under `protocols isis source-packet-routing node-segment`, not under `protocols isis interface lo0.0 level 2 node-segment`.
  2. **`algorithm [ 128 129 130 ]` is not valid Junos syntax.** There is no `algorithm` list keyword under `node-segment`.
  3. **`ipv4-index-algorithm` is not a Junos keyword.** The correct structure uses nested `flex-algorithm <id> { ipv4-index <value>; }` blocks.
  
  The 10.3 file demonstrates the correct pattern. This section appears to use an IOS-XR mental model (where per-algo prefix-SIDs are configured under the loopback interface) translated into pseudo-Junos syntax.

---

### Finding 3
- **Severity:** critical
- **File:** `10.1-network-slicing-concepts.md`
- **Line:** 624
- **Current text:**
  ```
  protocols {
      isis {
          interface et-0/0/0 {
              level 2 {
                  delay-measurement;
              }
          }
      }
  }
  ```
- **Correct text:**
  ```
  protocols {
      performance-monitoring {
          traceroute {
              interface et-0/0/0.0;
          }
      }
  }
  ```
  Or for IS-IS TE advertisement of delay metrics, delay is measured via RPM/TWAMP probes and advertised into IS-IS via TE link attributes. The exact mechanism depends on Junos version, but `delay-measurement` is NOT a valid keyword under `protocols isis interface <name> level <n>`.
- **Source:** Junos performance monitoring and IS-IS TE documentation.
- **Notes:** In Junos, link delay measurement for use by Flex-Algo is handled through the performance monitoring subsystem (TWAMP-light probes or hardware-assisted timestamping), not via an IS-IS interface sub-command. The `delay-measurement` keyword under IS-IS interface hierarchy does not exist in Junos. This is an IOS-XR concept (`performance-measurement interface <name> delay-measurement`) incorrectly mapped to Junos hierarchy.

---

### Finding 4
- **Severity:** critical
- **File:** `10.3-5g-xhaul-requirements.md`
- **Lines:** 434, 438
- **Current text:**
  ```
  protocols {
      isis {
          interface ge-0/0/0.0 {
              level 1;                    # Access domain
              point-to-point;
          }
          interface ge-0/0/1.0 {
              level 2;                    # Aggregation domain
              point-to-point;
          }
  ```
- **Correct text:**
  ```
  protocols {
      isis {
          interface ge-0/0/0.0 {
              level 2 disable;            # Access domain (L1 only)
              point-to-point;
          }
          interface ge-0/0/1.0 {
              level 1 disable;            # Aggregation domain (L2 only)
              point-to-point;
          }
  ```
- **Source:** Junos IS-IS configuration reference.
- **Notes:** In Junos, `level 1;` and `level 2;` as bare statements under an IS-IS interface are not valid configuration. Junos IS-IS interfaces participate in both levels by default. To restrict an interface to Level 1 only, you disable Level 2: `level 2 disable;`. To restrict to Level 2 only: `level 1 disable;`. The bare `level 1;` statement would be accepted by the parser only as a hierarchy container (expecting sub-statements like `metric`, `disable`, etc.), not as a level restriction directive.

---

### Finding 5
- **Severity:** critical
- **File:** `10.1-network-slicing-concepts.md`
- **Line:** 587
- **Current text:** `metric-type delay;`
- **Correct text:** `metric-type min-unidirectional-link-delay;`
- **Source:** Junos Flex-Algorithm configuration; RFC 9350 §6.1 defines the metric types as IGP, Min Unidirectional Link Delay, and TE Default Metric.
- **Notes:** Covered in Finding 1 above but called out separately since it appears in multiple places (lines 342, 587). The keyword `delay` is not a recognized Junos metric-type value. Valid values: `igp`, `min-unidirectional-link-delay` (or `min-delay` in some versions), `te-metric`. The 10.3 file uses `min-delay` which is closer but may also need the full form depending on Junos version.

---

### Finding 6
- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Lines:** 770, 776
- **Current text:**
  ```
  embb-sched {
      transmit-rate percent 60;   ## Align with IOS-XR: 60% of remaining
      ...
  }
  miot-sched {
      transmit-rate percent 20;   ## Align with IOS-XR: 20% of remaining
      ...
  }
  ```
- **Correct text:** The comments are misleading. Should read:
  ```
  embb-sched {
      transmit-rate percent 60;   ## 60% of interface rate (NOT "remaining" — Junos semantics differ from IOS-XR)
      ...
  }
  miot-sched {
      transmit-rate percent 20;   ## 20% of interface rate
      ...
  }
  ```
- **Source:** Junos CoS scheduler documentation.
- **Notes:** In Junos, `transmit-rate percent 60` means 60% of the **total interface rate**, not 60% of remaining bandwidth after priority classes. In IOS-XR, `bandwidth remaining percent 60` means 60% of bandwidth remaining after strict-priority traffic is served. These are semantically different. With 15% consumed by the URLLC strict-priority queue:
  - IOS-XR: eMBB gets 60% × 85% remaining = 51% of total
  - Junos: eMBB gets 60% of total
  
  The Junos config over-allocates (60% + 20% + 15% priority = 95%), which is valid as `transmit-rate` is a guaranteed minimum, not a hard ceiling. But the comment "Align with IOS-XR" suggests they behave identically, which they do not.

---

### Finding 7
- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Line:** 822
- **Current text:** `show performance-monitoring`
- **Correct text:** `show services rpm probe-results` or `show performance-monitoring tracking` (varies by Junos version and feature)
- **Source:** Junos RPM/performance monitoring documentation.
- **Notes:** The generic `show performance-monitoring` is not a standard top-level Junos show command for link delay measurements. Junos delay measurement results are typically accessed via `show services rpm probe-results` (for TWAMP/RPM probes) or platform-specific performance monitoring commands. The exact command depends on which delay measurement method is deployed.

---

### Finding 8
- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Line:** 820
- **Current text:** `show route table slice-urllc`
- **Correct text:** `show route table slice-urllc.inet.0`
- **Source:** Junos routing table naming convention.
- **Notes:** In Junos, routing instance tables include the address family suffix. `show route table slice-urllc` may work as a partial match in some Junos versions, but the canonical form is `show route table slice-urllc.inet.0` (for IPv4) or `slice-urllc.inet6.0` (for IPv6). The IOS-XR equivalent `show cef vrf slice-urllc` implicitly targets IPv4, so the Junos equivalent should be explicit.

---

### Finding 9
- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md` vs `10.3-5g-xhaul-requirements.md`
- **Lines:** 10.1 line 816 vs 10.3 line 541
- **Current text (10.1):** `show isis flex-algorithm 128`
- **Current text (10.3):** `show isis flex-algo 128`
- **Correct text:** Should be consistent across files. The likely correct Junos command is `show isis spring flex-algorithm 128` or `show isis flex-algorithm 128` (full word).
- **Source:** Junos IS-IS SR command reference.
- **Notes:** The two files use different forms of the same Junos command. 10.1 uses the full word `flex-algorithm` while 10.3 uses the abbreviated `flex-algo`. These should be reconciled. Additionally, in some Junos versions the command may require the `spring` keyword: `show isis spring flex-algorithm`.

---

### Finding 10
- **Severity:** minor
- **File:** `10.3-5g-xhaul-requirements.md`
- **Line:** 445
- **Current text:** `metric-type min-delay;`
- **Correct text:** `metric-type min-unidirectional-link-delay;`
- **Source:** Junos Flex-Algorithm configuration.
- **Notes:** While `min-delay` may be accepted as a shorthand in some Junos versions, the canonical keyword matching RFC 9350 terminology is `min-unidirectional-link-delay`. For a study guide targeting expert-level certification, the full canonical form is preferable. Lower severity than Finding 5 because `min-delay` is closer to valid than bare `delay`.

---

### Finding 11
- **Severity:** minor
- **File:** `10.3-5g-xhaul-requirements.md`
- **Line:** 540
- **Current text:** `show synchronization selection-process`
- **Correct text:** `show synchronization source-list` or `show synchronization status`
- **Source:** Junos SyncE/synchronization documentation.
- **Notes:** The Junos command to view the active synchronization source selection is typically `show synchronization source-list` or `show synchronization interfaces`. The keyword `selection-process` does not appear to be a standard Junos command argument.

---

### Finding 12
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Lines:** 415–430 (Junos FlexE Group config)
- **Current text:**
  ```
  chassis {
      fpc 0 {
          pic 0 {
              flexe-group fg0 {
                  member-interface et-0/0/0;
                  ...
              }
          }
      }
  }
  ```
- **Correct text:** Unknown — FlexE CLI on Junos MX is not publicly documented in detail.
- **Source:** Document's own caveat (lines ~399-404) acknowledges configurations are "conceptual and representative."
- **Notes:** The document appropriately caveats that FlexE configurations are conceptual. However, the Junos FlexE group hierarchy under `chassis { fpc { pic { flexe-group } } }` doesn't follow typical Junos chassis configuration patterns. Junos `chassis` hierarchy is used for hardware provisioning (port speeds, PIC types, FPC slots), not for logical group definitions. FlexE groups would more likely be configured under `interfaces` or a dedicated `flexe` stanza. This is informational given the explicit caveat, but readers should be warned the Junos CLI will differ significantly.

---

### Finding 13
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Lines:** 582–586 (Verification table)
- **Current text:**
  ```
  | `show flexe group` | Group state |
  | `show flexe client` | Client state |
  | `show flexe group fg0 calendar` | Calendar |
  | `show flexe group fg0 overhead` | Overhead stats |
  ```
- **Correct text:** These commands are unverifiable against public Junos documentation.
- **Source:** N/A — no public Junos FlexE show command reference available.
- **Notes:** The show commands for FlexE verification (`show flexe group`, `show flexe client`, etc.) are plausible but cannot be confirmed against publicly available Junos documentation. Given the conceptual caveat, this is informational. The Junos `show interfaces flexe-0/0/0/0` command (line 586) follows standard Junos interface show patterns and is likely correct in form.

---

## Files With No Junos Issues

- **`10.1-network-slicing-concepts-answers.md`** — Contains no Junos CLI; discusses concepts and references IOS-XR/Junos show commands only in prose. No Junos syntax to validate.
- **`10.2-flexe-flexible-ethernet-answers.md`** — Answer key with conceptual discussion. No Junos CLI blocks. References to Junos commands in prose are general and non-specific.
- **`10.2-flexe-theory.md`** — Protocol theory document with no vendor-specific configuration. Clean.
- **`10.3-5g-xhaul-requirements-answers.md`** — Answer key with conceptual discussion. References Junos show commands in troubleshooting prose but no CLI blocks to validate.
- **`README.md`** — Module index. No CLI content.

## Cross-File Consistency Issues

| Item | 10.1 | 10.3 | Correct |
|------|------|------|---------|
| Flex-Algo `definition` block | Missing | Present ✓ | 10.3 is correct |
| `advertise-definition` keyword | Used (wrong) | Not used ✓ | 10.3 is correct |
| Flex-Algo metric-type for delay | `delay` (wrong) | `min-delay` (close) | Full form: `min-unidirectional-link-delay` |
| Node-segment location | Under `interface lo0.0` (wrong) | Under `source-packet-routing` ✓ | 10.3 is correct |
| Per-algo SID syntax | `ipv4-index-algorithm` (wrong) | `flex-algorithm <n> { ipv4-index; }` ✓ | 10.3 is correct |
| Show flex-algo command | `show isis flex-algorithm 128` | `show isis flex-algo 128` | Inconsistent — pick one |

**Pattern:** The 10.1 Junos configuration appears to have been written first (or with less Junos familiarity), while 10.3 was written with better knowledge of actual Junos hierarchy. The 10.1 Junos config block needs a rewrite to match the patterns established in 10.3.

## Recommendation

The five critical findings are all concentrated in `10.1-network-slicing-concepts.md`. The Junos Flex-Algo configuration block (lines ~580–650) should be rewritten to match the correct patterns already demonstrated in `10.3-5g-xhaul-requirements.md`. The delay-measurement config also needs correction. The IS-IS level syntax in 10.3 (Finding 4) is a separate issue that's a quick two-line fix.
