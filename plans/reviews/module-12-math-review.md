# Module 12 Math/Scaling Review

## Summary

| Metric | Count |
|--------|-------|
| Files reviewed | 10 (README + 4 study files + 4 answer files + 1 migration file) |
| Total findings | 9 |
| Critical | 5 |
| Minor | 4 |

---

## Findings

### Finding 1 — CRITICAL

- **Severity:** Critical
- **File:** `12.5-evpn-l2vpn-migration-answers.md`
- **Section:** Phase 0 → Control-Plane Impact Assessment → EVPN-VPWS projection
- **Current text:**
  ```
  EVPN-VPWS:
    Type-1 (per-EVI AD): 10,000 (one pair per service — each endpoint PE advertises a Type-1 route)
    Type-3 (IMET):       0 (VPWS doesn't use Type-3)
    Subtotal:             5,000 routes
  ```
- **Why wrong:** The Type-1 count is explicitly stated as 10,000 (5,000 services × 2 endpoints = 10,000 routes), but the subtotal immediately below says 5,000. These are contradictory. The subtotal should match the Type-1 count since Type-3 is 0.
- **Corrected:** Subtotal should be **10,000** routes (matching the Type-1 count). This cascades:
  - Total EVPN: 10,000 + 16,000 + 1,200 = **~27,200** (not 22,200)
  - Peak during migration: ~3,000 legacy + ~27,200 EVPN = **~30,200** (not 25,200)
  - RR memory: ~30K × 500 bytes ≈ ~15 MB (not 12.5 MB — still negligible)
- **Source:** Arithmetic from the stated Type-1 count two lines above the subtotal. Also confirmed by the Phase-by-Phase analysis later in the same file which correctly says "EVPN-VPWS Type-1: ~10,000 (5,000 services × 2 routes per service)"

---

### Finding 2 — CRITICAL

- **Severity:** Critical
- **File:** `12.5-evpn-l2vpn-migration-answers.md`
- **Section:** Phase 1 → VPWS Migration Capacity Plan → Batch optimization
- **Current text:**
  ```
  Batch optimization:       Group PWs by PE pair — all PWs between PE-A↔PE-B
    migrated in same window. Average 8 PWs per PE pair.
    → 625 PE-pair batches / 40 per night / 4 nights = ~16 weeks (4 months)
  ```
- **Why wrong:** The arithmetic `625 / 40 / 4` = 3.9 ≈ **~4 weeks**, not ~16 weeks. The formula as written yields ~4, not ~16. The "~16 weeks (4 months)" answer doesn't match the formula shown.
- **Corrected:** Either:
  - (a) Fix the formula: if 40 means individual PWs/night (not batches), then each batch = 8 PWs, so batch rate = 40÷8 = 5 batches/night. Correct formula: `625 batches / 5 batches per night / 4 nights per week = 31 weeks` — same as accelerated plan (batching doesn't help in this model), OR
  - (b) Fix the result to match the formula: `625 / 40 / 4 = ~4 weeks`, OR
  - (c) Fix the divisor: `625 / 10 / 4 = ~16 weeks` (if 10 PE-pair batches per night is the intended rate, update "40" to "10")
- **Source:** Basic arithmetic: 625 ÷ 40 ÷ 4 = 3.906

---

### Finding 3 — CRITICAL

- **Severity:** Critical
- **File:** `12.1-isp-backbone-design.md` and `12.1-isp-backbone-design-answers.md`
- **Section:** Convergence and Protection Analysis → Failure Scenario 1 → Timeline
- **Current text:**
  ```
  T=0ms    BFD session to CHI-P detects loss (3×33ms = ~100ms)
  T=100ms  IS-IS P router deletes adjacency, begins SPF
  T=120ms  SPF completes (small topology, fast SPF)
  T=50ms   TI-LFA pre-computed backup path activates at failure detection
  ...
  TI-LFA means: traffic reroutes at failure detection (~50ms with BFD)
  ```
- **Why wrong:** Two issues:
  1. **Timeline ordering error:** T=50ms appears after T=120ms — chronologically impossible. TI-LFA activates at BFD detection time, which is ~100ms (3×33ms), not 50ms.
  2. **BFD timing contradiction:** The text claims TI-LFA activates "at failure detection (~50ms with BFD)" but the BFD timer is explicitly configured as 3×33ms = ~100ms everywhere in the document. 50ms does not match the 3×33ms configuration.
- **Corrected:** TI-LFA activates at BFD detection time = ~100ms. The timeline should read:
  ```
  T=0ms     Link/node failure occurs
  T≈100ms   BFD detects loss (3×33ms)
  T≈100ms   TI-LFA pre-computed backup activates (triggered by BFD)
  T≈100ms   IS-IS deletes adjacency, begins SPF
  T≈120ms   SPF completes
  T≈300ms   BGP path selection updates
  ```
- **Source:** BFD 3×33ms = 99ms ≈ 100ms; TI-LFA triggers on BFD failure detection event

---

### Finding 4 — CRITICAL

- **Severity:** Critical
- **File:** `12.1-isp-backbone-design.md` and `12.1-isp-backbone-design-answers.md`
- **Section:** IE-SP Design Review Questions → Q5 (traffic drain)
- **Current text:** `"Raise IS-IS metric on all NY-P1 links to maximum (65535 for wide metrics)"`
- **Why wrong:** 65,535 (2^16 − 1) is the OSPF maximum interface cost, not the IS-IS wide metric maximum. IS-IS wide metrics use a 24-bit field per TLV 22/135, giving a maximum interface metric of **16,777,215** (2^24 − 1). Some implementations reserve the top value, capping at 16,777,214. The document confuses OSPF and IS-IS metric ranges.
- **Corrected:** `"Raise IS-IS metric on all NY-P1 links to maximum (16777214 for wide metrics)"` — or reference `max-link-metric` / overload bit as the canonical drain mechanism.
- **Source:** ISO 10589 extended TLV 22 (RFC 5305) — 24-bit metric field. OSPF interface cost is 16-bit (RFC 2328).

---

### Finding 5 — CRITICAL

- **Severity:** Critical
- **File:** `12.3-mobile-backhaul-5g-transport-answers.md`
- **Section:** Q2 Discussion (Timing Failure) — holdover duration
- **Current text:** `"The 11.2-second calculation assumes worst-case free-running OCXO with no frequency assist"`
- **Why wrong:** The calculation just above correctly derives **11,200 seconds (~3.1 hours)** of holdover time. The sentence then refers to this as "11.2-second" — off by a factor of 1,000. This is a critical typo that changes the meaning from ~3 hours of safe holdover to ~11 seconds, which would imply near-instant failure.
- **Corrected:** `"The 11,200-second (~3.1-hour) calculation assumes worst-case free-running OCXO with no frequency assist"`
- **Source:** 130 ns ÷ 11.6 ps/s = 11,207 seconds ≈ 11,200 seconds ≈ 3.1 hours

---

### Finding 6 — MINOR

- **Severity:** Minor
- **File:** `12.1-isp-backbone-design.md` and `12.1-isp-backbone-design-answers.md`
- **Section:** Convergence → Failure Scenario 2 → PE Router Failure
- **Current text:** `"IBGP hold-down timers tuned to 3s (not default 180s per RFC 4271)"`
- **Why wrong:** RFC 4271 Section 10 recommends a default Hold Timer of **90 seconds**, not 180 seconds. The 180-second value is a Cisco IOS/IOS-XR implementation default, not the RFC recommendation. Attributing 180s to RFC 4271 is factually incorrect.
- **Corrected:** `"IBGP hold-down timers tuned to 3s (not default 90s per RFC 4271; some implementations default to 180s)"`
- **Source:** RFC 4271, Section 10: "The suggested default value for the Hold Timer is 90 seconds."

---

### Finding 7 — MINOR

- **Severity:** Minor
- **File:** `12.4-internet-exchange-point-design.md` and `12.4-internet-exchange-point-design-answers.md`
- **Section:** Growth Model → Financial Model → Year 1 OpEx
- **Current text:**
  ```
  OpEx:     Colocation ($4K/mo × 2 sites) + staff (0.5 FTE @ $60K) + bandwidth ($500/mo)
            = $8,500/month = $102,000/year
  ```
- **Why wrong:** The stated components don't sum to $8,500/month:
  - Colocation: $4,000/mo × 2 sites = $8,000/mo
  - Staff: 0.5 FTE × $60K/yr = $30K/yr = $2,500/mo
  - Bandwidth: $500/mo
  - **Actual sum: $11,000/month** ($132,000/year), not $8,500/month ($102,000/year)
- **Corrected:** Either fix the total to $11,000/month ($132,000/year), or adjust the component figures to sum to $8,500. If colo is $4K total (both sites combined, not per-site), then: $4,000 + $4,000 (staff at $48K/yr FTE rate) + $500 = $8,500 — but the text says "$4K/mo × 2 sites" which clearly means per-site.
- **Impact:** Year 1 net calculation ($204K + $20K − $210K − $102K = −$88K) is internally consistent with the $102K figure but not with the component breakdown. If the correct OpEx is $132K, the Year 1 net loss would be −$118K.
- **Source:** Arithmetic: $8,000 + $2,500 + $500 = $11,000 ≠ $8,500

---

### Finding 8 — MINOR

- **Severity:** Minor
- **File:** `12.3-mobile-backhaul-5g-transport.md` and `12.3-mobile-backhaul-5g-transport-answers.md`
- **Section:** QoS Design — DSCP and priority inconsistency between tiers
- **Current (cell site switch):**
  ```
  Queue 7 (strict priority): eCPRI traffic (DSCP 46 / PCP 7)
  Queue 6 (strict priority): PTP timing (DSCP 48 / PCP 6)
  ```
- **Current (aggregation router):**
  ```
  Queue 7: PTP/SyncE timing — CS7 (DSCP 56)
  Queue 6: eCPRI fronthaul — EF (DSCP 46)
  ```
- **Why wrong:** Two inconsistencies between tiers:
  1. **Priority reversal:** eCPRI > PTP at cell site (Queue 7 vs 6), but PTP > eCPRI at agg router (Queue 7 vs 6). Priority ordering should be consistent across the transport chain.
  2. **PTP DSCP mismatch:** PTP is marked DSCP 48 (CS6) at the cell site but classified as CS7 (DSCP 56) at the agg router. If DSCP is not remarked between tiers, the agg router won't classify PTP into Queue 7 (CS7) — it arrives as CS6 and would land in Queue 2 (Signaling/OAM, CS6).
- **Corrected:** Standardize PTP DSCP marking across all tiers (either CS6/48 or CS7/56 everywhere) and use a consistent queue priority assignment for eCPRI vs PTP at all tiers.
- **Source:** DSCP CS6 = 48, CS7 = 56 — these are different codepoints; consistent end-to-end marking is required for correct QoS classification.

---

### Finding 9 — MINOR

- **Severity:** Minor
- **File:** `12.3-mobile-backhaul-5g-transport.md` and `12.3-mobile-backhaul-5g-transport-answers.md`
- **Section:** QoS Design — cell site backhaul DSCP vs slice table
- **Current (cell site QoS):**
  ```
  Queue 5 (shaped): S1/N3 backhaul (DSCP 34)
  ```
- **Current (slice table):**
  ```
  eMBB → AF31 (DSCP 26)
  ```
- **Why wrong:** DSCP 34 = AF41, not AF31 (DSCP 26). The cell site classifies N3 backhaul into DSCP 34 (AF41), but the network slicing table maps eMBB to AF31 (DSCP 26). If N3 backhaul is primarily eMBB user-plane traffic, its DSCP marking at the cell site (34/AF41) doesn't match the slice mapping (26/AF31). This means eMBB traffic won't match the `class-map match-any EMBB / match dscp af31` at the aggregation router.
- **Corrected:** Align the cell site N3/S1 backhaul DSCP marking with the slice table: use AF31 (DSCP 26) consistently for eMBB across all tiers, or update the slice table to AF41 (DSCP 34).
- **Source:** AF31 = DSCP 26, AF41 = DSCP 34 — different PHBs in different DSCP AF classes.

---

## Notes

- All files were read in full. Junos/IOS-XR syntax issues were ignored per instructions unless they directly affected numeric/scaling claims.
- The 12.1 and 12.2 answer files are largely identical to their corresponding study files; errors present in both are counted once.
- RFC citation accuracy was only checked where it directly supported a numeric claim (e.g., RFC 4271 hold timer default).
