# Module 06 — Math & Numerical Audit

**Auditor:** Sentinel (subagent)  
**Date:** 2026-03-12  
**Scope:** All markdown files in `modules/06-sr/`  
**Focus:** Arithmetic, formulas, numerical claims, cross-file consistency  

---

## Summary

**19 files audited. 3 issues found (1 critical, 2 minor).**

All core arithmetic — SRGB label math, SRH overhead calculations, uSID compression ratios, MTU payload calculations, BFD timing math, label stack depth overhead — is **correct**. The formulas (`Label = SRGB_base + index`, SRH size = `8 + 16×N`, uSID carrier capacity, weight-based ECMP splits) all check out.

The issues found are **cross-file inconsistencies** in stated default values, not wrong arithmetic.

---

## Issues

### 6.1 (theory + design + answers) — Junos Old Default SRGB: Three Different Values

- **Severity**: critical
- **Current text**:
  - `6.1-sr-mpls-fundamentals-theory.md`: *"Junos defaults to 16000-16999 (but configurable)"*
  - `6.1-sr-mpls-fundamentals-answers.md` Q1: *"old Junos default SRGB of 16000–17999"*
  - `6.1-sr-mpls-fundamentals.md` (SRGB Sizing): *"Junos: 100,000 labels (800000–899999)"*
  - `6.1-sr-mpls-fundamentals.md` (Interop): *"Older Junos versions (pre-18.1) had a default SRGB of 800000–899999"*
- **Correction**: The pre-18.1 Junos default SRGB was **800000–899999** (100,000 labels), per Juniper documentation and the interoperability section in the design file. The theory file's claim of "16000-16999" and the answers file's claim of "16000-17999" are both incorrect and should be changed to 800000–899999 (or at minimum made consistent with each other and with the design file's interop section). Pick one value and use it everywhere.
- **Source**: Juniper Junos SPRING documentation; the design file's own Interoperability section confirms 800000–899999.

### 6.1-sr-mpls-fundamentals.md — SRGB Sizing Section Lists Old Junos Default Without Version Context

- **Severity**: minor
- **Current text** (under "Design Considerations > SRGB Sizing > Default"):
  *"Junos: 100,000 labels (800000–899999)"*
- **Correction**: This is the **pre-18.1** default. The same file's SRGB section (earlier) states the current default is 16000–23999 (8,000 labels, Junos 18.1+). The Sizing section should either (a) show the current default (16000–23999) or (b) label this explicitly as "pre-18.1 default" to avoid confusion. As written, the two sections in the same file contradict each other about what the Junos "default" SRGB is.
- **Source**: Internal consistency within `6.1-sr-mpls-fundamentals.md`.

### 6.2-sr-te-policies-theory.md — Candidate Path Preference Range

- **Severity**: minor
- **Current text**: *"Each candidate path has a preference value (0-65535)."*
- **Correction**: RFC 9256 Section 2.7 defines preference as a non-negative integer. The BGP SR Policy SAFI encoding (draft-ietf-idr-sr-policy-safi) uses a **4-byte (32-bit)** preference sub-TLV, giving a range of 0–4,294,967,295. IOS-XR's CLI implementation limits input to 1–65535, so the stated range reflects vendor CLI constraints rather than the protocol spec. Consider noting this is an IOS-XR implementation limit, not an architectural one, or just say "unsigned integer" per RFC 9256.
- **Source**: RFC 9256 Section 2.7; draft-ietf-idr-sr-policy-safi preference sub-TLV encoding.

---

## Verified Calculations (Clean)

All of the following were checked and confirmed correct:

### SRGB / Label Math
- `SRGB 16000–23999 = 8,000 labels` → 23999 − 16000 + 1 = 8,000 ✓
- `Label = SRGB_base + index` → 16000 + 1 = 16001 ✓
- `Index 500, SRGB 16000–23999 → label 16500` → 16000 + 500 = 16,500 ✓
- `Index 2500, SRGB 16000–23999 → label 18500` → 16000 + 2500 = 18,500 ✓
- `SRGB 16000–16999 = 1,000 labels` → 16999 − 16000 + 1 = 1,000 ✓
- `Expand to index-range 16000 → labels 16000–31999` → 16000 + 16000 − 1 = 31,999 ✓
- `SRGB 800000–899999 = 100,000 labels` → 899999 − 800000 + 1 = 100,000 ✓

### SRv6 SRH Overhead
- `SRH base header = 8 bytes` (1+1+1+1+1+1+2) ✓
- `Each segment entry = 16 bytes` (128-bit IPv6 address) ✓
- `1 SID: SRH=24, Total=64, Payload(1500)=1436` ✓
- `3 SIDs: SRH=56, Total=96, Payload(1500)=1404` ✓
- `4 SIDs: SRH=72, Total=112` ✓
- `6 SIDs: SRH=104, Total=144, Payload(1500)=1356` ✓
- `9 SIDs: Total=192, Payload(1500)=1308` ✓
- `1500 + 112 = 1612` (4-SID encap over 1500-byte payload) ✓
- `9000 + 112 = 9112` (4-SID encap over 9000-byte payload) ✓

### uSID Compression
- `/32 block → 96 remaining bits ÷ 16 = 6 uSIDs per carrier` ✓
- `/48 block → 80 remaining bits ÷ 16 = 5 uSIDs per carrier` ✓
- `6 uSIDs in 1 carrier = 16 bytes vs 96 bytes standard → 83% reduction` ✓
- `uSID 1 carrier: Total overhead = 40+24 = 64 bytes, Payload(1500) = 1436` ✓
- `uSID 2 carriers: SRH = 40 bytes, Total = 80 bytes, Payload(1500) = 1420` ✓
- `9 SIDs → 2 carriers (6+3), overhead = 80 bytes` ✓
- `SR-MPLS 6 labels = 24 bytes; SRv6 6 SIDs = 144 bytes → 6× heavier` ✓
- `SR-MPLS 4 labels × 4 bytes = 16 bytes; SRv6 112 bytes → 7×` ✓
- `uSID 80 bytes vs standard 192 bytes → 58% reduction` ✓

### MPLS Label Stack Overhead
- `10 SIDs × 4 bytes = 40 bytes` ✓
- `4 labels × 4 bytes = 16 bytes` ✓

### BFD / TI-LFA Timing
- `50ms × 3 multiplier = 150ms detection` ✓
- `100ms × 3 = 300ms` ✓
- `300ms × 3 = 900ms` ✓

### ECMP Weight Splits
- `Weight 1 + Weight 1 = 50/50` ✓
- `Weight 3 + Weight 1 = 75/25` → 3/4 = 75%, 1/4 = 25% ✓

### SRv6 Forwarding Examples
- SRH segment list reverse ordering and Segments Left processing verified correct in all walk-through examples (6.4 design, 6.4 theory, 6.5 design) ✓

---

## Files Audited

1. `6.1-sr-mpls-fundamentals-theory.md`
2. `6.1-sr-mpls-fundamentals.md`
3. `6.1-sr-mpls-fundamentals-answers.md`
4. `6.2-sr-te-policies-theory.md`
5. `6.2-sr-te-policies.md`
6. `6.2-sr-te-policies-answers.md`
7. `6.3-ti-lfa-theory.md`
8. `6.3-ti-lfa.md`
9. `6.3-ti-lfa-answers.md`
10. `6.4-srv6-fundamentals-theory.md`
11. `6.4-srv6-fundamentals.md`
12. `6.4-srv6-fundamentals-answers.md`
13. `6.5-srv6-network-programming-theory.md`
14. `6.5-srv6-network-programming.md`
15. `6.5-srv6-network-programming-answers.md`
16. `6.6-sr-migration-strategies.md`
17. `6.6-sr-migration-strategies-answers.md`
18. `README.md`
19. `6.6-sr-migration-strategies-theory.md` — does not exist (no theory file for 6.6)
