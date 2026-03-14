# Module 12 Junos CLI Validation Report

**Reviewer:** Sentinel (Junos CLI Validator)  
**Date:** 2026-03-14  
**Scope:** All markdown files under `modules/12-case-studies/`  
**Focus:** Junos CLI syntax errors, incorrect hierarchies, wrong show commands, Junos-specific defaults, platform misattribution  

---

## Summary

| Metric | Count |
|--------|-------|
| Files reviewed | 8 |
| Total Junos CLI blocks found | 12 (each duplicated across main + answers file) |
| Critical findings | 4 |
| Minor findings | 6 |
| Informational notes | 3 |

**Overall assessment:** The Junos CLI blocks are structurally reasonable and demonstrate correct conceptual intent, but several contain hierarchy errors that would prevent `commit` on a real device. The most systematic issue is nesting configuration elements in the wrong parent container — a pattern that suggests some blocks were composed from IOS-XR mental models and translated to Junos-like syntax rather than validated against actual Junos hierarchy.

---

## Detailed Findings

### CRITICAL-1: Flex-Algo prefix-SID placed inside flex-algorithm definition block

| Field | Value |
|-------|-------|
| **Severity** | 🔴 CRITICAL |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | Flex-Algo definition — Junos |

**Current (incorrect):**
```
protocols {
    isis {
        source-packet-routing {
            flex-algorithm 128 {
                definition {
                    metric-type delay;
                    affinity {
                        exclude high-delay;
                    }
                }
                prefix-sid {          ← WRONG: prefix-sid cannot be nested here
                    algorithm 128;
                    index 301;
                }
            }
        }
    }
}
```

**Correct:**
```
protocols {
    isis {
        source-packet-routing {
            flex-algorithm 128 {
                advertise-definition;
                metric-type delay;
                affinity {
                    exclude high-delay;
                }
            }
        }
        interface lo0.0 {
            level 2 {
                prefix-sid {
                    algorithm 128 index 301;
                }
            }
        }
    }
}
```

**Source:** In Junos, per-algorithm prefix-SIDs are configured on the loopback interface under `protocols isis interface lo0.0 level <n> prefix-sid algorithm <algo> index <idx>`, not inside the `flex-algorithm` definition block. The `flex-algorithm` block defines the algorithm parameters (metric-type, affinity constraints, priority); the SID binding happens on the interface. Additionally, `definition { ... }` is not a container in Junos flex-algo — the attributes `metric-type`, `affinity`, etc. are direct children of `flex-algorithm <id>`, and the node advertises the definition with `advertise-definition`.

---

### CRITICAL-2: Flex-Algo affinity-map at wrong hierarchy level

| Field | Value |
|-------|-------|
| **Severity** | 🔴 CRITICAL |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | Flex-Algo definition — Junos |

**Current (incorrect):**
```
segment-routing {                    ← WRONG: bare top-level, not a valid Junos hierarchy
    affinity-map {
        high-delay bit-position 0;
        capacity-constrained bit-position 1;
        dual-fiber-protected bit-position 2;
    }
}
```

**Correct (option A — under source-packet-routing):**
```
protocols {
    isis {
        source-packet-routing {
            affinity-map high-delay bit-position 0;
            affinity-map capacity-constrained bit-position 1;
            affinity-map dual-fiber-protected bit-position 2;
        }
    }
}
```

**Correct (option B — under routing-options):**
```
routing-options {
    segment-routing {
        affinity-map {
            high-delay bit-position 0;
            capacity-constrained bit-position 1;
            dual-fiber-protected bit-position 2;
        }
    }
}
```

**Source:** `segment-routing` is not a valid top-level Junos hierarchy. It must be nested under `routing-options` or the affinity-map defined under `protocols isis source-packet-routing`. The bare `segment-routing { }` block at root level would be rejected by `commit check`.

---

### CRITICAL-3: PTP master-only/slave-only hierarchy inverted

| Field | Value |
|-------|-------|
| **Severity** | 🔴 CRITICAL |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | PTP Configuration — Junos (Aggregation Hub Router) |

**Current (incorrect):**
```
protocols {
    ptp {
        clock-mode boundary;
        domain 24;
        profile-type g.8275.1;
        master-only {               ← WRONG: these are per-interface attributes,
            interface et-0/0/0;          not top-level containers
        }
        slave-only {
            interface et-0/0/1;
        }
        announce-interval 1;
        sync-interval -4;
        delay-request-interval -4;
    }
}
```

**Correct:**
```
protocols {
    ptp {
        clock-mode boundary;
        domain 24;
        profile-type g.8275.1;
        announce-interval 1;
        sync-interval -4;
        delay-request-interval -4;
        interface et-0/0/0 {
            master-only;
        }
        interface et-0/0/1 {
            slave-only;
        }
    }
}
```

**Source:** In Junos PTP, `master-only` and `slave-only` are per-interface knobs configured inside `protocols ptp interface <name> { master-only; }`. They are not top-level containers that list interfaces. The current config inverts the hierarchy — the interface is the container, and the role is the leaf.

---

### CRITICAL-4: RSTP bpdu-block as per-interface knob is invalid

| Field | Value |
|-------|-------|
| **Severity** | 🔴 CRITICAL |
| **Files** | `12.4-internet-exchange-point-design.md`, `12.4-internet-exchange-point-design-answers.md` |
| **Section** | Spanning tree avoidance strategy (IXP switch config), Switch-Level Security |

**Current (incorrect):**
```
protocols {
    rstp {
        bridge-priority 4096;
        interface ge-0/0/0-47 {     ← ALSO MINOR: range notation invalid (see MINOR-1)
            edge;
            bpdu-block;             ← WRONG: not a valid per-interface RSTP knob
        }
    }
}
```

**Correct (option A — global RSTP knob):**
```
protocols {
    rstp {
        bridge-priority 4096;
        bpdu-block-on-edge;          /* Blocks BPDUs on all edge ports globally */
        interface ge-0/0/5 {
            edge;
        }
    }
}
```

**Correct (option B — per-interface via ethernet-switching-options or switch-options):**
```
/* For ELS platforms (QFX5120): */
switch-options {
    bpdu-block {
        interface ge-0/0/5;
        disable-timeout 0;           /* Keep port disabled until manually cleared */
    }
}
```

**Source:** Junos RSTP does not support `bpdu-block` as a per-interface attribute under `protocols rstp interface`. BPDU blocking is either enabled globally for all edge ports via `protocols rstp bpdu-block-on-edge`, or configured per-interface under `ethernet-switching-options bpdu-block` (legacy) / `switch-options bpdu-block` (ELS). The per-interface `edge` knob is valid but `bpdu-block` next to it is not.

---

### MINOR-1: RSTP interface range notation not valid Junos

| Field | Value |
|-------|-------|
| **Severity** | 🟡 MINOR |
| **Files** | `12.4-internet-exchange-point-design.md`, `12.4-internet-exchange-point-design-answers.md` |
| **Section** | Spanning tree avoidance strategy |

**Current:**
```
interface ge-0/0/0-47 {     ← Not valid Junos interface naming
```

**Correct approach:**
```
/* Use interface-range under [edit interfaces] and reference individually,
   or list each interface separately under protocols rstp */
interfaces {
    interface-range MEMBER-PORTS {
        member-range ge-0/0/0 to ge-0/0/47;
    }
}
/* Then apply RSTP per range member or individually */
```

**Source:** Junos does not support the `ge-0/0/0-47` shorthand as an interface name. Interface ranges must be defined under `[edit interfaces interface-range]` using `member-range ... to ...` or `member` statements. Under `protocols rstp`, each interface must be listed individually or referenced via an apply-group.

---

### MINOR-2: SR-TE segment-list hop entry missing container braces

| Field | Value |
|-------|-------|
| **Severity** | 🟡 MINOR |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | Junos — SR-TE policy for URLLC slice |

**Current:**
```
segment-list URLLC-PATH-OMAHA {
    hop1 label 16901;               ← Flat inline — should be a container
}
```

**Correct:**
```
segment-list URLLC-PATH-OMAHA {
    hop1 {
        label 16901;
    }
}
```

**Source:** In Junos `protocols source-packet-routing`, each hop in a segment-list is a named container with `label` (or `ip-address`, `index`) as child attributes. The inline `hop1 label 16901` would fail commit.

---

### MINOR-3: MAC limiting uses legacy hierarchy for ELS platform

| Field | Value |
|-------|-------|
| **Severity** | 🟡 MINOR |
| **Files** | `12.4-internet-exchange-point-design.md`, `12.4-internet-exchange-point-design-answers.md` |
| **Section** | Switch-Level Security |

**Current:**
```
ethernet-switching-options {         ← Legacy (non-ELS) hierarchy
    secure-access-port {
        interface xe-0/0/5 {
            mac-limit 1 action drop;
        }
    }
}
```

**Correct for QFX5120 (ELS platform):**
```
switch-options {
    interface xe-0/0/5.0 {
        interface-mac-limit {
            1;
            packet-action drop;
        }
    }
}
```

**Source:** The QFX5120 runs Enhanced Layer 2 Software (ELS). MAC limiting under `ethernet-switching-options secure-access-port` is the legacy (non-ELS) hierarchy. ELS platforms use `switch-options` with `interface-mac-limit`. Additionally, the flat `mac-limit 1 action drop` syntax should use the hierarchical format with `packet-action`.

---

### MINOR-4: show isis fast-reroute is IOS-XR, not Junos

| Field | Value |
|-------|-------|
| **Severity** | 🟡 MINOR |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | Design Review Checklist — Redundancy |

**Current:**
```
Agg ring TI-LFA protection verified (run `show isis fast-reroute` / `show isis backup`)
```

**Issue:** `show isis fast-reroute` is an IOS-XR command, not Junos. The Junos equivalent is already listed as the second option (`show isis backup`), but the IOS-XR command should not be presented as a Junos alternative.

**Correct Junos commands:**
```
show isis backup spf results
show isis route <prefix> detail    /* Shows backup next-hop info */
```

---

### MINOR-5: Flex-Algo definition container naming

| Field | Value |
|-------|-------|
| **Severity** | 🟡 MINOR |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | Flex-Algo definition — Junos |

**Current:**
```
flex-algorithm 128 {
    definition {                 ← 'definition' is not a container in Junos
        metric-type delay;
        affinity {
            exclude high-delay;
        }
    }
}
```

**Correct:**
```
flex-algorithm 128 {
    advertise-definition;
    metric-type delay;
    affinity {
        exclude high-delay;
    }
}
```

**Source:** In Junos, `metric-type` and `affinity` are direct children of `flex-algorithm <id>`, not wrapped in a `definition { }` sub-container. The `advertise-definition` leaf statement is used to signal that this node is a definition-advertising node. The extra `definition { }` wrapper would cause a commit error.

---

### MINOR-6: PTP profile-type naming may vary by Junos release

| Field | Value |
|-------|-------|
| **Severity** | 🟡 MINOR |
| **Files** | `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md` |
| **Section** | PTP Configuration — Junos |

**Current:**
```
profile-type g.8275.1;
```

**Note:** Depending on Junos release and platform, the profile type identifier may be `g-8275-1` (dash-separated) or configured via `telecom-profile` knobs. Validate against the target Junos version. Some releases use:
```
protocols ptp {
    profile-type g-8275.1;
}
```
or require explicit `telecom-profile` configuration. This is a release-dependent nuance, not a hard error.

---

## Informational Notes

### INFO-1: EVPN QFX config intentionally presented as implementation intent

**Files:** `12.2-dci-with-evpn.md`, `12.2-dci-with-evpn-answers.md`

The Juniper QFX10K BGW configuration is explicitly presented as "implementation intent" with a disclaimer: *"Junos EVPN multi-site BGW feature set and exact syntax varies significantly by platform... always verify against target platform documentation."* The show commands listed (`show evpn database`, `show route table bgp.evpn.0`, `show ethernet-switching table`) are all valid Junos verification commands. **No action needed** — the disclaimer is appropriate and the approach is defensible for a study guide.

### INFO-2: EVPN proxy-macip-advertisement syntax is valid but release-dependent

**Files:** `12.2-dci-with-evpn.md`, `12.2-dci-with-evpn-answers.md`

```
set routing-instances EVPN-TRADING instance-type evpn
set routing-instances EVPN-TRADING protocols evpn proxy-macip-advertisement
```

This is valid Junos `set` syntax. The `proxy-macip-advertisement` knob exists under `protocols evpn` within a routing instance. The document already notes release-dependency. **No action needed.**

### INFO-3: TI-LFA configuration is correct

**Files:** `12.3-mobile-backhaul-5g-transport.md`, `12.3-mobile-backhaul-5g-transport-answers.md`

```
protocols {
    isis {
        interface et-0/0/0 {
            level 2 {
                post-convergence-lfa {
                    node-protection;
                }
            }
        }
    }
}
```

This is correct Junos hierarchy for TI-LFA (post-convergence LFA) with node protection. **No issues.**

---

## Files with No Junos CLI Findings

| File | Notes |
|------|-------|
| `12.1-isp-backbone-design.md` | No Junos CLI blocks — design discussion with pseudocode only |
| `12.1-isp-backbone-design-answers.md` | No Junos CLI blocks — pure design discussion |

---

## Remediation Priority

| Priority | Finding | Impact |
|----------|---------|--------|
| 1 | CRITICAL-1: Flex-Algo prefix-SID hierarchy | Config would not commit; misleads reader about where SIDs are bound |
| 2 | CRITICAL-3: PTP master-only/slave-only hierarchy | Config would not commit; inverted container/leaf relationship |
| 3 | CRITICAL-2: Affinity-map at root level | Config would not commit; missing parent hierarchy |
| 4 | CRITICAL-4: RSTP bpdu-block knob | Config would not commit; wrong location for BPDU blocking |
| 5 | MINOR-5: Flex-Algo definition wrapper | Config would not commit; extra container layer |
| 6 | MINOR-2: Segment-list hop format | Config would not commit; missing container braces |
| 7 | MINOR-1: Interface range notation | Config would not commit; invalid interface name |
| 8 | MINOR-3: Legacy MAC limiting hierarchy | Would commit on legacy Junos but not ELS; platform mismatch with QFX5120 |
| 9 | MINOR-4: IOS-XR show command mixed in | Confusing but not a config error |
| 10 | MINOR-6: PTP profile-type naming | May or may not commit depending on release |

---

## Cross-File Consistency Note

Each case study's main file and its `-answers` companion contain identical Junos CLI blocks. All findings above apply to **both** the main and answers files for each case study. Fixes should be applied to both files simultaneously.
