# Module 06 — RFC Cross-Reference Audit

**Auditor**: Sentinel (RFC accuracy pass)
**Date**: 2026-03-12
**Scope**: All markdown files in `modules/06-sr/`
**Methodology**: Every RFC number cited was verified against IETF Datatracker / rfc-editor.org for existence, title, content, and attribution accuracy.

---

## Summary

| Severity | Count |
|----------|-------|
| **Critical** | 2 |
| **Minor** | 2 |

**18 files scanned. ~33 unique RFC references checked.**

Two critical issues found:
1. **RFC 9602 is consistently misidentified** as "Compressed SRv6 Segment List Encoding (uSID)" across 3 files (6 occurrences). RFC 9602 is actually "SRv6 Segment Identifiers in the IPv6 Addressing Architecture." The compressed SRv6 / uSID RFC is **RFC 9800**.
2. **Color 0 prohibition misattributed to RFC 9012** when it actually comes from RFC 9256 Section 2.1.

Two minor title abbreviation issues in RFC tables.

---

## Critical Issues

### 6.5-srv6-network-programming.md — RFC 9602 is NOT the uSID/Compression RFC
- **Severity**: critical
- **Current text** (line 215): `"Micro-SID (RFC 9602, "Compressed SRv6 Segment List Encoding," published 2024) compresses multiple logical SIDs into a single 128-bit container."`
- **Also affected** (line 905): `"RFC 9602 — Compressed SRv6 Segment List Encoding (uSID)"`
- **Also affected** (line 926): `"RFC 9602 (Compressed SRv6 Segment List Encoding / uSID)"`
- **Correction**: RFC 9602 (October 2024) is actually titled **"Segment Routing over IPv6 (SRv6) Segment Identifiers in the IPv6 Addressing Architecture"** — an Informational RFC about how SRv6 SIDs relate to the IPv6 addressing architecture and allocating a dedicated prefix for SRv6 SIDs. The actual "Compressed SRv6 Segment List Encoding" is **RFC 9800** (June 2025, Standards Track), which defines the REPLACE-CSID container format and new SRv6 endpoint flavors enabling segment list compression.
- **Source**: [RFC 9602](https://datatracker.ietf.org/doc/rfc9602/) vs [RFC 9800](https://datatracker.ietf.org/doc/rfc9800/)

### 6.5-srv6-network-programming-theory.md — Same RFC 9602 Error
- **Severity**: critical
- **Current text** (line 276): `"| RFC 9602 | 2024 | Compressed SRv6 Segment List Encoding (uSID) | SRv6 micro-segment compression |"`
- **Correction**: Should be `| RFC 9800 | 2025 | Compressed SRv6 Segment List Encoding | SRv6 segment list compression via REPLACE-CSID containers |`. RFC 9602 could optionally remain in the table with its correct title ("SRv6 Segment Identifiers in the IPv6 Addressing Architecture") if addressing architecture is relevant context.
- **Source**: [RFC 9800](https://datatracker.ietf.org/doc/rfc9800/)

### 6.6-sr-migration-strategies.md — Same RFC 9602 Error
- **Severity**: critical
- **Current text** (line 705): `"Use uSID compression (RFC 9602)"`
- **Also affected** (line 824): `"RFC 9602 — SRv6 Compressed SIDs (uSID)"`
- **Also affected** (line 846): `"RFC 9602"`
- **Correction**: All references to RFC 9602 in the context of uSID compression should be changed to **RFC 9800**.
- **Source**: [RFC 9800](https://datatracker.ietf.org/doc/rfc9800/)

### 6.2-sr-te-policies.md — Color 0 Prohibition Misattributed to RFC 9012
- **Severity**: critical
- **Current text** (line 140): `"0: INVALID (RFC 9012 reserves color 0, do not use)"`
- **Correction**: RFC 9012 Section 4.3 defines the Color Extended Community format but explicitly says "The Color Value field is encoded as a 4-octet value by the administrator and is outside the scope of this document." It does NOT reserve color 0. The non-zero requirement comes from **RFC 9256 Section 2.1**: "The color is an unsigned non-zero 32-bit integer value that associates the SR Policy with an intent or objective." Fix attribution to RFC 9256.
- **Source**: [RFC 9012 §4.3](https://www.rfc-editor.org/rfc/rfc9012.html#section-4.3) and [RFC 9256 §2.1](https://www.rfc-editor.org/rfc/rfc9256.html#section-2.1)

---

## Minor Issues

### 6.3-ti-lfa-theory.md — RFC 9855 Title Abbreviated
- **Severity**: minor
- **Current text** (line 144): `"| RFC 9855 | 2025 | TI-LFA Using Segment Routing | ..."`
- **Correction**: The actual title is **"Topology Independent Fast Reroute Using Segment Routing"**. The abbreviated form "TI-LFA Using Segment Routing" is understandable but drops "Topology Independent Fast Reroute" which is the formal name.
- **Source**: [RFC 9855](https://datatracker.ietf.org/doc/rfc9855/) (October 2025)

### 6.5-srv6-network-programming-theory.md — RFC 9352 Title Abbreviated
- **Severity**: minor
- **Current text** (line 275): `"| RFC 9352 | 2023 | IS-IS Extensions to Support Segment Routing over IPv6 | ..."`
- **Correction**: The actual title is **"IS-IS Extensions to Support Segment Routing over the IPv6 Data Plane"** — missing "the" and "Data Plane".
- **Source**: [RFC 9352](https://datatracker.ietf.org/doc/rfc9352/) (February 2023)

---

## Verified Clean References

The following RFC references were verified as correct in number, title (or reasonable abbreviation), year, and content attribution:

| RFC | Title | Verdict |
|-----|-------|---------|
| RFC 8402 | Segment Routing Architecture (2018) | ✅ Correct |
| RFC 8667 | IS-IS Extensions for Segment Routing (2019) | ✅ Correct |
| RFC 8665 | OSPF Extensions for Segment Routing (2019) | ✅ Correct |
| RFC 8666 | OSPFv3 Extensions for Segment Routing (2019) | ✅ Correct |
| RFC 8660 | Segment Routing with the MPLS Data Plane (2019) | ✅ Correct |
| RFC 8661 | Segment Routing MPLS Interworking with LDP (2019) | ✅ Correct |
| RFC 7684 | OSPFv2 Prefix/Link Attribute Advertisement (2015) | ✅ Correct (used as transport for OSPF SR) |
| RFC 9350 | IGP Flexible Algorithm (2023) | ✅ Correct |
| RFC 5440 | PCEP (2009) | ✅ Correct |
| RFC 8231 | Stateful PCE Extensions (2017) | ✅ Correct |
| RFC 8281 | PCE-Initiated LSP Setup (2017) | ✅ Correct |
| RFC 7752 | BGP-LS (2016) | ✅ Correct |
| RFC 9085 | BGP-LS Extensions for Segment Routing (2021) | ✅ Correct |
| RFC 9012 | BGP Tunnel Encapsulation Attribute (2021) | ✅ Correct (but color 0 claim misattributed — see above) |
| RFC 9256 | Segment Routing Policy Architecture (2022) | ✅ Correct |
| RFC 4360 | BGP Extended Communities (2006) | ✅ Correct |
| RFC 8664 | PCEP Extensions for Segment Routing (2019) | ✅ Correct |
| RFC 5286 | Basic LFA (2008) | ✅ Correct |
| RFC 7490 | Remote LFA (2015) | ✅ Correct |
| RFC 9855 | TI-LFA / Topology Independent Fast Reroute Using SR (2025) | ✅ Correct (minor title abbreviation noted above) |
| RFC 5880 | BFD (2010) | ✅ Correct |
| RFC 5881 | BFD for IPv4/IPv6 Single Hop (2010) | ✅ Correct |
| RFC 8333 | Micro-loop Prevention by Local Convergence Delay (2018) | ✅ Correct |
| RFC 4193 | Unique Local IPv6 Unicast Addresses (2005) | ✅ Correct |
| RFC 8754 | IPv6 Segment Routing Header (2020) | ✅ Correct |
| RFC 8986 | SRv6 Network Programming (2021) | ✅ Correct |
| RFC 9252 | BGP Overlay Services Based on SRv6 (2022) | ✅ Correct |
| RFC 8200 | IPv6 Specification (2017) | ✅ Correct |
| RFC 9259 | SRv6 OAM (2022) | ✅ Correct |
| RFC 9352 | IS-IS Extensions for SRv6 (2023) | ✅ Correct (minor title abbreviation noted) |
| RFC 7665 | SFC Architecture (2015) | ✅ Correct |
| RFC 8300 | Network Service Header (2018) | ✅ Correct |

## Draft References (Correctly Labeled as Drafts)

The following were correctly identified as IETF drafts, not RFCs:
- `draft-ietf-idr-sr-policy-safi` — SR Policy SAFI for BGP (correctly noted as "progressing toward RFC")
- `draft-ietf-spring-sr-service-programming` — End.AD/End.AM/End.AS service chaining functions (correctly noted as "not RFC 8986" and "not yet RFC-track")
- `draft-ietf-spring-srv6-network-programming-ext` — End.DT2/End.DT46 extensions (correctly noted as draft)

---

## Files Scanned

1. `6.1-sr-mpls-fundamentals.md`
2. `6.1-sr-mpls-fundamentals-answers.md`
3. `6.1-sr-mpls-fundamentals-theory.md`
4. `6.2-sr-te-policies.md`
5. `6.2-sr-te-policies-answers.md`
6. `6.2-sr-te-policies-theory.md`
7. `6.3-ti-lfa.md`
8. `6.3-ti-lfa-answers.md`
9. `6.3-ti-lfa-theory.md`
10. `6.4-srv6-fundamentals.md`
11. `6.4-srv6-fundamentals-answers.md`
12. `6.4-srv6-fundamentals-theory.md`
13. `6.5-srv6-network-programming.md`
14. `6.5-srv6-network-programming-answers.md`
15. `6.5-srv6-network-programming-theory.md`
16. `6.6-sr-migration-strategies.md`
17. `6.6-sr-migration-strategies-answers.md`
18. `README.md`
