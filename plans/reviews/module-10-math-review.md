# Module 10 Math/Scaling Review

## Summary
- Files reviewed: 8
- Findings: 5
- Critical: 0
- Minor: 5

## Findings

---

### Finding 1
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Lines:** 201, 208
- **Current text:**
  - Line 201: `│    32 frames = 5,237,216 blocks                     │`
  - Line 208: `One **multiframe** (32 frames): 5,237,216 blocks ≈ **3.35 ms**`
- **Why it's wrong:** Arithmetic error. The text establishes one overhead frame = 8 × 20,461 = 163,688 blocks (correct). One multiframe = 32 × 163,688 = **5,238,016** blocks, not 5,237,216. The difference is 800 blocks. The timing estimate (~3.35 ms) is unaffected because 5,238,016 / 1.5625×10⁹ ≈ 3.352 ms, which still rounds to 3.35 ms.
- **Corrected text:**
  - Line 201: `│    32 frames = 5,238,016 blocks                     │`
  - Line 208: `One **multiframe** (32 frames): 5,238,016 blocks ≈ **3.35 ms**`
- **Source/reasoning:** 32 × 163,688 = 5,238,016 (verified with calculator).

---

### Finding 2
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Lines:** 329–357 (config) vs 601 (verification)
- **Current text (config):** Bonds 4 × 100G PHYs into a 400G FlexE Group (80 total slots) but only allocates 20 slots worth of clients: slots 0–7 (40G) + 8–13 (30G) + 14–17 (20G) + 18–19 (10G) = 100G total, leaving 300G/60 slots unallocated.
- **Current text (verification):** `Total Bandwidth: 400 Gbps` / `Allocated: 400 Gbps (100%)` / `Unallocated: 0 Gbps`
- **Why it's wrong:** The config example allocates only 25% of the 400G group (100G out of 400G), but the verification output directly below claims 100% allocation. A student following the config and checking against the verification output would see a mismatch. The lab exercise correctly uses 200G+100G+100G=400G for a fully-allocated group, but the config example doesn't match the verification.
- **Corrected text:** Either (a) change the config to use all 80 slots (e.g., slots 0–31=160G eMBB, 32–51=100G URLLC, 52–67=80G mMTC, 68–79=60G mgmt), or (b) change the verification output to show `Allocated: 100 Gbps (25%)` / `Unallocated: 300 Gbps`. Option (b) is simpler and keeps the 100G example consistent with the channelization diagram above it.
- **Source/reasoning:** 4 PHYs × 20 slots/PHY = 80 slots = 400G; config allocates slots 0–19 = 20 slots = 100G.

---

### Finding 3
- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Lines:** 770, 778
- **Current text:**
  - Line 770: `transmit-rate percent 60;   ## Align with IOS-XR: 60% of remaining`
  - Line 778: `transmit-rate percent 20;   ## Align with IOS-XR: 20% of remaining`
- **Why it's wrong:** The comment claims alignment with IOS-XR's `bandwidth remaining percent` semantics, but Junos `transmit-rate percent` is a percentage of **total port rate**, not percentage of remaining bandwidth after priority classes. IOS-XR allocates 60% of the 85% remaining after URLLC priority (= 51% of port rate to eMBB). Junos as written allocates 60% of the total port rate to eMBB — a materially different value (60% vs 51% of port). The Junos config itself is valid, but the inline comments are misleading about what the numbers mean relative to IOS-XR.
- **Corrected text:**
  - Line 770: `transmit-rate percent 60;   ## 60% of port rate (NOTE: IOS-XR uses 'bandwidth remaining percent', which is % of capacity after priority classes — not directly equivalent)`
  - Line 778: `transmit-rate percent 20;   ## 20% of port rate`
- **Source/reasoning:** Junos `transmit-rate percent` is documented as percentage of interface rate. IOS-XR `bandwidth remaining percent` is percentage of bandwidth remaining after priority classes (15% URLLC → 85% remaining → 60% of 85% = 51% of port).

---

### Finding 4
- **Severity:** minor
- **File:** `10.3-5g-xhaul-requirements.md` (line 291) vs `10.3-5g-xhaul-requirements-answers.md` (line 190)
- **Current text (theory, line 291):** `roughly **10-15 km maximum** for fronthaul fiber runs`
- **Current text (answer Q4, line 190):** `Fronthaul latency limits the maximum distance between RU and DU (~15–20 km at fiber propagation speed).`
- **Why it's wrong:** The same module gives two different maximum fronthaul distances. The theory section's 10–15 km is derived from a careful calculation (100 µs budget minus 30–50 µs processing = 50–70 µs propagation ÷ 5 µs/km = 10–14 km). The answer's 15–20 km exceeds this calculation and is inconsistent. Using the upper latency budget (150 µs) with minimal processing could yield ~20 km, but the answer doesn't qualify this — it states 15–20 km without context, contradicting the more rigorous theory derivation.
- **Corrected text (answer Q4):** `Fronthaul latency limits the maximum distance between RU and DU (~10–20 km depending on latency budget and processing overhead; typically ≤15 km).`
- **Source/reasoning:** Theory calculation: (100–150 µs total − 30–50 µs processing) / 5 µs/km = 10–24 km theoretical max, but practical limit is 10–15 km as the theory states. The answer's lower bound of 15 km exceeds the theory's upper bound of 15 km.

---

### Finding 5
- **Severity:** minor
- **File:** `10.3-5g-xhaul-requirements.md` (lines 164, 260) vs `10.3-5g-xhaul-requirements-answers.md` (lines 100, 191)
- **Current text (theory):**
  - Line 164: `±1.5µs phase (G.8275.1)` (in xhaul requirements table for fronthaul)
  - Line 260: `Budget: ±1.5µs max |TE| at O-RU (ITU-T G.8271.1)`
- **Current text (answers):**
  - Line 100: `±130 ns end-to-end phase accuracy (per ITU-T G.8271.1 network limits)`
  - Line 191: `±130 ns phase accuracy at the O-RU`
- **Why it's wrong:** The theory section and the answer key cite the same standard (G.8271.1) for O-RU phase accuracy but give values that differ by 11.5× (1,500 ns vs 130 ns). G.8271.1 defines multiple categories: ±1.5 µs is the standard wide-area TDD category (applicable to most 5G NR deployments), while ±130 ns is a stricter category for specific use cases (e.g., DECT NR+, certain LLS scenarios). Both values exist in the standard, but using them interchangeably for the same "5G fronthaul" scenario within one module is contradictory and would confuse a student.
- **Corrected text:** Pick one value consistently, or explicitly distinguish the categories. For general 5G NR TDD fronthaul, ±1.5 µs is the standard requirement. If the answers intend a stricter scenario, they should state: `±130 ns end-to-end phase accuracy (per ITU-T G.8271.1 Category B — applicable to specific LLS/indoor scenarios; the standard wide-area TDD limit is ±1.5 µs)`.
- **Source/reasoning:** ITU-T G.8271.1 defines max |TE| categories: Category A (wide-area base stations) = ±1.5 µs; Category B (local-area, indoor) = ±130 ns (as of the 2022 amendment). The theory correctly uses ±1.5 µs for general 5G fronthaul; the answers use ±130 ns without qualification.

---

## Files Reviewed

| # | File | Findings |
|---|------|----------|
| 1 | `10.1-network-slicing-concepts.md` | 1 (Finding 3) |
| 2 | `10.1-network-slicing-concepts-answers.md` | 0 |
| 3 | `10.2-flexe-flexible-ethernet.md` | 2 (Findings 1, 2) |
| 4 | `10.2-flexe-flexible-ethernet-answers.md` | 0 |
| 5 | `10.2-flexe-theory.md` | 0 |
| 6 | `10.3-5g-xhaul-requirements.md` | 2 (Findings 4, 5 — contradictions with answer key) |
| 7 | `10.3-5g-xhaul-requirements-answers.md` | 2 (Findings 4, 5 — contradictions with theory) |
| 8 | `README.md` | 0 |

## Notes

- All CPRI/eCPRI bandwidth estimates are appropriately labeled as planning approximations and scale consistently (linear with antenna count for CPRI, sub-linear for eCPRI due to RU-side beamforming). No errors found.
- FlexE calendar slot math (5G granularity, 20 slots/100G instance) is consistent throughout.
- SRGB exhaustion math in Q3 answer (200 nodes × 50 algos = 10,000 SIDs vs 8,000 SRGB range) is correct.
- Fiber propagation constant (~5 µs/km) is used consistently and correctly.
- PTP sync interval encoding (2^-6 = 64/sec, 2^-3 = 8/sec) is correct.
- SyncE specifications (±4.6 ppm free-run, ±50 ppb locked) are correct per G.8262/G.8261.
- All QoS percentage allocations sum correctly within their respective semantics.
