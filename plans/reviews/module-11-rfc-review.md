# Module 11 RFC Audit

**Auditor:** Sentinel (RFC Cross-Reference Auditor)
**Date:** 2026-03-13
**Scope:** All markdown files under `modules/11-automation/`

## Summary
- Files reviewed: 10
- Total findings: 3
- Critical: 1 (with 2 sub-items)
- Minor: 1

### Files Reviewed
1. `README.md` — no RFC citations
2. `11.1-model-driven-networking.md`
3. `11.1-model-driven-networking-theory.md`
4. `11.1-model-driven-networking-answers.md`
5. `11.2-streaming-telemetry.md`
6. `11.2-streaming-telemetry-theory.md`
7. `11.3-sr-te-controller-integration.md`
8. `11.3-sr-te-controller-integration-answers.md`
9. `11.4-cicd-network-config.md`
10. `11.4-cicd-network-config-answers.md`
11. `11.5-lab-gnmi-sr-te-automation.md`
12. `11.5-lab-gnmi-sr-te-automation-answers.md`

---

## Detailed Findings

### Finding 1 — PCEP SR-ERO NAI Type Values for IPv6 Are Wrong

- **Severity:** critical
- **File:** `11.3-sr-te-controller-integration.md`
- **Lines:** 215–216

- **Current text:**
  ```
      NT=1 = IPv4 node ID
      NT=3 = IPv4 adjacency
      NT=5 = IPv6 node ID
      NT=7 = IPv6 adjacency
      NT=0 = No NAI (SID only)
  ```

- **Correction:** Per IANA "PCEP SR-ERO NAI Types" registry (RFC 8664, Section 4.3.1 / Section 8.2), the correct values are:
  ```
      NT=0 = NAI is absent (SID only)
      NT=1 = IPv4 node ID
      NT=2 = IPv6 node ID
      NT=3 = IPv4 adjacency
      NT=4 = IPv6 adjacency (global IPv6 addresses)
      NT=5 = Unnumbered adjacency with IPv4 node IDs
      NT=6 = IPv6 adjacency (link-local IPv6 addresses)
      NT=7–15 = Unassigned
  ```
  The guide claims NT=5 is "IPv6 node ID" — it is actually NT=2. The guide claims NT=7 is "IPv6 adjacency" — it is actually NT=4 (global) or NT=6 (link-local); NT=7 is unassigned.

- **Source:** IANA PCEP Numbers registry, "PCEP SR-ERO NAI Types" sub-registry ([link](https://www.iana.org/assignments/pcep/pcep.xhtml#pcep-sr-ero-nai-types)); RFC 8664 §4.3.1 and §8.2.

- **Impact:** An exam candidate memorizing these values would get PCEP SR-ERO questions wrong. This is a factual error in protocol encoding values that could also cause confusion if used for packet analysis or implementation.

---

### Finding 2 — RFC 7752 (BGP-LS) Is Obsoleted by RFC 9552

- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Lines:** 19, 89

- **Current text (line 19):**
  ```
  - **BGP-LS** (BGP Link-State) — RFC 7752 — topology distribution to PCE
  ```
  **Current text (line 89):**
  ```
  BGP-LS (RFC 7752) exports IGP topology information into BGP so the PCE can build a global TED without running inside the IGP domain.
  ```

- **Correction:** RFC 7752 (March 2016) was obsoleted by RFC 9552 (December 2023), titled "Distribution of Link-State and Traffic Engineering Information Using BGP." The guide should note that RFC 7752 has been superseded, e.g.: `RFC 7752 (obsoleted by RFC 9552)`. The technical content remains accurate — RFC 9552 is an update/replacement, not a fundamental redesign — but for exam preparation and professional accuracy, the obsolescence should be noted.

- **Source:** RFC Editor info page for RFC 7752: "Obsoleted by: RFC 9552" ([link](https://www.rfc-editor.org/info/rfc7752)).

- **Impact:** Low. Vendor documentation and certifications still commonly reference RFC 7752. However, a study guide should note the current standard to avoid candidates citing an obsoleted RFC.

---

## RFCs Verified as Correct

The following RFC citations were audited and confirmed accurate (number, title, year, and contextual claims):

| RFC | Title (as cited) | Year | Verdict |
|-----|-----------------|------|---------|
| RFC 7950 | The YANG 1.1 Data Modeling Language | 2016 | ✅ Correct |
| RFC 6241 | Network Configuration Protocol (NETCONF) | 2011 | ✅ Correct |
| RFC 6242 | Using NETCONF over SSH | 2011 | ✅ Correct (abbreviated title acceptable) |
| RFC 8040 | RESTCONF Protocol | 2017 | ✅ Correct |
| RFC 8342 | Network Management Datastore Architecture (NMDA) | 2018 | ✅ Correct |
| RFC 8343 | A YANG Data Model for Interface Management | 2018 | ✅ Correct |
| RFC 8344 | (IPv4/IPv6 configuration — described, not formally titled) | 2018 | ✅ Acceptable description |
| RFC 8349 | (ietf-routing — described, not formally titled) | 2018 | ✅ Acceptable description |
| RFC 8525 | (ietf-yang-library — described, not formally titled) | 2019 | ✅ Acceptable description |
| RFC 8529 | YANG Data Model for Network Instances | 2019 | ✅ Correct |
| RFC 8795 | YANG for TE Topology | 2020 | ✅ Correct (abbreviated) |
| RFC 5277 | NETCONF Event Notifications | 2008 | ✅ Correct |
| RFC 8639 | Subscription to YANG Notifications | 2019 | ✅ Correct |
| RFC 8641 | Subscription to YANG Notifications for Datastore Updates | 2019 | ✅ Correct |
| RFC 7951 | JSON Encoding of Data Modeled with YANG | 2016 | ✅ Correct |
| RFC 5440 | PCEP (Path Computation Element Communication Protocol) | 2009 | ✅ Correct |
| RFC 8231 | Stateful PCE extensions | 2017 | ✅ Correct |
| RFC 8281 | PCE-Initiated LSP Setup | 2017 | ✅ Correct |
| RFC 8664 | PCEP Extensions for Segment Routing | 2019 | ✅ Correct |
| RFC 9012 | The BGP Tunnel Encapsulation Attribute | 2021 | ✅ Correct |
| RFC 9256 | Segment Routing Policy Architecture | 2022 | ✅ Correct |

### Additional Verified Claims

- **PCEP TCP port 4189** — ✅ Correct (IANA assigned)
- **BGP-LS AFI 16388 / SAFI 71** — ✅ Correct
- **Color Extended Community type 0x030B** (Transitive Opaque 0x03, sub-type Color 0x0B) — ✅ Correct per RFC 9012 §12
- **Color value 0x00000064 = color 100** — ✅ Correct
- **SR-ERO subobject Type 36 (0x24)** — ✅ Correct per RFC 8664
- **NT field is 4 bits** — ✅ Correct per RFC 8664 §4.3.1
- **RFC 8231 LSP Update Capability (U) flag** — ✅ Correct
- **RFC 8281 LSP Instantiation Capability (I) flag** — ✅ Correct
- **gNMI Specification ~2018** — ✅ Approximately correct (OpenConfig)
- **draft-ietf-idr-bgp-model still a draft** — ✅ Correct as of 2026
- **RFC 8040 §6 covers RESTCONF notifications/SSE** — ✅ Correct

---

## Assessment

Module 11 is **remarkably accurate** in its RFC citations. Across 12 files containing 25+ unique RFC references, only one factual error was found (the PCEP SR-ERO NAI Type values), plus one minor obsolescence notation gap. All RFC numbers, titles, publication years, and technical claims are otherwise correct.

The NAI Type error in Finding 1 should be corrected promptly — it's a protocol encoding detail that could trip up an exam candidate or developer.
