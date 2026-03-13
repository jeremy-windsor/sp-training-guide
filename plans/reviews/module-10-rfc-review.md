# Module 10 RFC Audit

## Summary
- Files reviewed: 8
- Total findings: 10
- Critical: 2
- Minor: 8

## Detailed Findings

---

### Finding 1
- **Severity:** critical
- **File:** `10.1-network-slicing-concepts-answers.md`
- **Line:** 72
- **Current text:** `Flex-Algo 129 min-delay relies on IGP TE delay metrics (RFC 7810).`
- **Correction:** RFC 7810 ("IS-IS Traffic Engineering (TE) Metric Extensions", May 2016, Informational) was **obsoleted by RFC 8570** ("IS-IS Traffic Engineering (TE) Metric Extensions", March 2019, Standards Track). The reference should cite RFC 8570 instead.
- **Source:** IETF Datatracker — RFC 7810 page explicitly states "Obsoleted by: RFC 8570"

---

### Finding 2
- **Severity:** critical
- **File:** `10.2-flexe-theory.md`
- **Line:** 127
- **Current text:** `| OIF-FLEXE-02.1 | 2020 | Flex Ethernet Implementation Agreement 2.1 | ...`
- **Correction:** OIF-FLEXE-02.1 was published **July 2019**, not 2020. The main FlexE design file (`10.2-flexe-flexible-ethernet.md`, line 786) correctly states 2019. The theory file's table has a one-year-off date error.
- **Source:** OIF Implementation Agreements page (oiforum.com/technical-work/implementation-agreements-ias/) — "OIF-FLEXE-02.1 – Flex Ethernet 2.1 Implementation Agreement (July 2019)"

---

### Finding 3
- **Severity:** minor
- **File:** `10.1-network-slicing-concepts.md`
- **Line:** 313
- **Current text:** `| PCE (RFC 8231) | Centralized slice path computation | Module 5 |`
- **Correction:** RFC 8231 is "Path Computation Element Communication Protocol (PCEP) Extensions for Stateful PCE" (September 2017). The shorthand "PCE (RFC 8231)" implies RFC 8231 defines the PCE architecture, but it defines PCEP extensions for stateful operation. The PCE architecture is defined in RFC 4655 ("A Path Computation Element (PCE)-Based Architecture") and the base PCEP protocol in RFC 5440. While RFC 8231 is contextually appropriate for centralized path computation in slicing (stateful PCE is indeed used for this), the label should be more precise, e.g., "Stateful PCE (RFC 8231)" or "PCE/PCEP (RFC 8231, RFC 5440)".
- **Source:** IETF RFC Editor — RFC 8231 title confirmed as "PCEP Extensions for Stateful PCE"

---

### Finding 4
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Line:** 786
- **Current text:** `- **OIF-FLEXE-02.1** (2019): FlexE 2.1 — 50G PHYs, 25G slot option`
- **Correction:** The 25G coarser calendar allocation option was introduced in **FlexE 2.0** (June 2018), not FlexE 2.1. The version history table earlier in the same file (line ~46) correctly attributes "optional coarser 25G calendar allocation" to FlexE 2.0. FlexE 2.1 added "50GBASE-R group support, clarifications." The Quick Reference line for 2.1 should read: `FlexE 2.1 — 50GBASE-R (50G) PHY support, clarifications`
- **Source:** Internal inconsistency within `10.2-flexe-flexible-ethernet.md` — version history table (line ~46) vs Quick Reference (line 786). OIF confirms 25G allocation is a FlexE 2.0 feature.

---

### Finding 5
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Line:** 52
- **Current text:** `- **ITU-T G.8023** (2018, amended 2024): FlexE in OTN transport context`
- **Correction:** The official title of ITU-T G.8023 is "Characteristics of equipment functional blocks supporting Ethernet physical layer and Flex Ethernet interfaces" — it covers Ethernet PHY and FlexE functional blocks in general, not specifically "OTN transport context." Additionally, the latest amendment is Amendment 3 (05/2025), not 2024 as stated. There may have been a 2024 amendment, but the guide should reference the most current.
- **Source:** ITU-T publication record — G.8023 (2018) Amd. 3 (05/2025)

---

### Finding 6
- **Severity:** minor
- **File:** `10.2-flexe-theory.md`
- **Line:** 130
- **Current text:** `| ITU-T G.8312 | 2020 | Interfaces for metro transport networks | FlexE interworking with OTN |`
- **Correction:** The "What It Defines" column says "FlexE interworking with OTN" but the text at line 138 also says "ITU-T G.8312 defines the interworking [between FlexE and OTN]." The full title of G.8312 is "Interfaces for FlexE-aware metro transport networks" — it focuses on metro transport interfaces using FlexE, which includes OTN aspects but is broader than just "interworking." The description should align more closely with the actual scope. Additionally, G.8023 is the primary standard covering FlexE functional blocks, while G.8312 focuses on metro network interface characterization.
- **Source:** ITU-T G.8312 publication page

---

### Finding 7
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Line:** 788
- **Current text:** `- **OIF-FLEXE-03.0** (2025): FlexE 3.0 — 800G PHYs`
- **Correction:** OIF-FLEXE-03.0 (May 2025) is now listed as **"OBSOLETE"** on the OIF Implementation Agreements page. This likely means a subsequent revision (3.0.1 or 3.1) has superseded it. The guide should note this status if the material is updated, as readers attempting to reference FlexE 3.0 will find it superseded.
- **Source:** OIF website (oiforum.com/technical-work/implementation-agreements-ias/) — "OIF-FLEXE-03.0 – FlexE 3.0 Implementation Agreement (May 2025) OBSOLETE"

---

### Finding 8
- **Severity:** minor
- **File:** `10.2-flexe-theory.md`
- **Line:** 7
- **Current text:** `...first published as OIF-FLEXE-01.0 (2016), with subsequent revisions through OIF-FLEXE-02.1 (2019).`
- **Correction:** This omits FlexE 2.2 (October 2021) and FlexE 3.0 (May 2025), which are covered in the main design file (`10.2-flexe-flexible-ethernet.md`). While the theory file may intentionally scope to foundational versions, this creates an inconsistency with the companion file and may mislead readers about the current state of the specification. Consider updating to: "...with subsequent revisions through OIF-FLEXE-03.0 (2025)" or at minimum noting later versions exist.
- **Source:** OIF Implementation Agreements page confirms FlexE 2.2 (October 2021) and FlexE 3.0 (May 2025)

---

### Finding 9
- **Severity:** minor
- **File:** `10.3-5g-xhaul-requirements-answers.md`
- **Line:** 100
- **Current text:** `| 5G fronthaul | ±130 ns end-to-end phase accuracy (per ITU-T G.8271.1 network limits; node clocks per G.8273.2 Class C/D) | G.8275.1 (full on-path PTP) + SyncE |`
- **Correction:** Two issues: (1) **ITU-T G.8273.2** is cited here but is not listed in the Quick Reference or Key Standards section of `10.3-5g-xhaul-requirements.md`. Standards cited in answers should appear in the reference material. (2) The ±130 ns figure is a specific network-contribution budget achievable with short boundary clock chains using Class C/D clocks, not the general G.8271.1 network limit. The main body of 10.3 (line 260) correctly states "±1.5µs max |TE| at O-RU (ITU-T G.8271.1)" as the overall requirement. The ±130 ns answer should clarify this is a best-case network contribution budget, not the end-to-end requirement.
- **Source:** ITU-T G.8271.1 specifies ±1.5 µs as the overall max |TE| for 5G NR TDD; the network contribution depends on chain length and clock class per G.8273.2

---

### Finding 10
- **Severity:** minor
- **File:** `10.2-flexe-flexible-ethernet.md`
- **Line:** 52 and 789
- **Current text:** `(2018, amended 2024)` and `(2018, amd 2024)`
- **Correction:** The most recent ITU-T G.8023 amendment identified is **Amendment 3 (05/2025)**, not 2024. There may have been a 2024 amendment (Amd. 2), but the guide should reference the latest known amendment to avoid implying the standard hasn't been updated since 2024. If both 2024 and 2025 amendments exist, consider "(2018, amd. 2025)" or "(2018, multiple amendments through 2025)."
- **Source:** ITU-T publication record — "Recommendation ITU-T G.8023 (2018) Amd. 3 (05/2025)"

---

## Standards Verified as Correct

The following RFC/standard citations were audited and found **accurate** in number, title, date, and context:

| Standard | Where Cited | Status |
|----------|-------------|--------|
| RFC 9543 — "A Framework for Network Slices in Networks Built from IETF Technologies" (March 2024) | 10.1 lines 32, 88, 90, 1035 | ✅ Title, date, RFC number all correct |
| RFC 9889 — "A Realization of Network Slices for 5G Networks Using Current IP/MPLS Technologies" (November 2025) | 10.1 line 177, 1036 | ✅ Confirmed via IETF Datatracker |
| RFC 8402 — "Segment Routing Architecture" | 10.1 line 1042 | ✅ Correct (July 2018) |
| RFC 9350 — "IGP Flexible Algorithm" | 10.1 line 1043 | ✅ Correct (February 2023) |
| RFC 8453 — "Framework for Abstraction and Control of TE Networks (ACTN)" | 10.1 lines 108, 169 (answers) | ✅ Correct (August 2018) |
| 3GPP TS 23.501 — System Architecture for 5G | 10.1, 10.3 | ✅ Correct standard for S-NSSAI/slice definitions |
| 3GPP TS 28.530 — Management and Orchestration of Network Slicing | 10.1 line 1041 | ✅ Correct |
| 3GPP TR 38.801 — RAN functional split options | 10.3 lines 105, 130 | ✅ Correct |
| 3GPP TS 38.401 — NG-RAN architecture | 10.3 lines 50, 623 | ✅ Correct |
| OIF-FLEXE-01.0 (March 2016) — FlexE 1.0 | 10.2 multiple | ✅ Confirmed |
| OIF-FLEXE-01.1 (June 2017) — FlexE 1.1 | 10.2 version table | ✅ Confirmed via OIF |
| OIF-FLEXE-02.0 (June 2018) — FlexE 2.0 | 10.2 multiple | ✅ Confirmed |
| OIF-FLEXE-02.2 (October 2021) — FlexE 2.2 | 10.2 line 787 | ✅ Confirmed via OIF |
| OIF-FLEXE-03.0 (May 2025) — FlexE 3.0 | 10.2 line 788 | ✅ Date/content correct (but now marked OBSOLETE — see Finding 7) |
| ITU-T G.8275.1 / G.8275.2 — PTP telecom profiles | 10.3 | ✅ Correct references |
| ITU-T G.8271.1 — Network time/phase sync for 5G | 10.3 line 260, 630 | ✅ Correct |
| ITU-T G.8262 / G.8262.1 — SyncE / Enhanced EEC | 10.3 | ✅ Correct |
| IEEE 1914.1 / 1914.3 — Fronthaul architecture/RoE | 10.3 lines 626–627 | ✅ Correct |
| eCPRI Specification V2.0 | 10.3 | ✅ Correct |
| IEEE 802.3 (various) | 10.2, 10.3 | ✅ Correct generic reference |

## Notes

- All IETF drafts referenced (`draft-ietf-teas-5g-network-slice-application`, `draft-ietf-teas-ietf-network-slice-nbi-yang`, `draft-ietf-dmm-tn-aware-mobility`) are appropriately labeled as drafts and not cited as RFCs. Some may have been published as RFCs since the guide was written — a periodic check against the IETF Datatracker is recommended.
- The 3GPP specifications (TS 23.501, TS 28.530, TR 38.801, TS 38.401) are living documents updated with each 3GPP release. The guide does not pin specific release versions, which is appropriate for a study guide but means claims about content (e.g., SST values 5–6 in Rel-18+) should be periodically reverified.
- The SyncE free-run accuracy claim of "±4.6 ppm" (G.8262) and locked output of "±50 ppb" in `10.3` are technically correct per ITU-T G.8262 specifications.

---

*Audit performed: 2026-03-13 | Auditor: Sentinel RFC Cross-Reference Subagent*
