# Module 08 RFC Audit

## Summary
- Files reviewed: 14
- Findings: 4
- Critical: 0
- Minor: 4

## Findings

1) **Severity:** Minor  
**File:** `modules/08-l2vpn-evpn/8.1-legacy-l2vpn.md`  
**Line:** 131  
**Current text:** `RFC 8469 (2018) makes CW mandatory for Ethernet PWs`  
**Correction:** Reword to reflect RFC 8469 normative language: Ethernet PW CW support is **SHOULD**, and when both ends support it, CW **MUST** be used; implementations still **MUST** interoperate without CW for backward compatibility.  
**Source:** RFC 8469 §4 and §3 — https://www.rfc-editor.org/rfc/rfc8469.txt

2) **Severity:** Minor  
**File:** `modules/08-l2vpn-evpn/8.1-legacy-l2vpn.md`  
**Line:** 931  
**Current text:** `RFC 4762 — Virtual Private LAN Service Using LDP (Martini)`  
**Correction:** Use official title/attribution: `RFC 4762 — Virtual Private LAN Service (VPLS) Using Label Distribution Protocol (LDP) Signaling` (edited by M. Lasserre and V. Kompella, not “Martini”).  
**Source:** RFC 4762 title block — https://www.rfc-editor.org/rfc/rfc4762.txt

3) **Severity:** Minor  
**File:** `modules/08-l2vpn-evpn/8.1-legacy-l2vpn.md`  
**Line:** 937  
**Current text:** `... RFC 8214 ... (EVPN-VPWS, the modern replacement for RFC 6624)`  
**Correction:** Avoid “replacement” wording; RFC 8214 is a newer EVPN-based VPWS standard but does **not** obsolete/update RFC 6624. Suggested wording: `modern EVPN-based alternative to RFC 6624 deployments`.  
**Source:** RFC 8214 header (no obsoletes/updates to RFC 6624) and RFC 6624 header/status — https://www.rfc-editor.org/rfc/rfc8214.txt , https://www.rfc-editor.org/rfc/rfc6624.txt

4) **Severity:** Minor  
**File:** `modules/08-l2vpn-evpn/8.2-evpn-fundamentals.md`  
**Line:** 622  
**Current text:** `RFC 8584 — EVPN Designated Forwarder Election (preference-based AND HRW algorithms)`  
**Correction:** Attribute algorithms accurately: RFC 8584 defines the DF-election extensibility framework and HRW; preference-based DF election is specified by RFC 9785 (which updates RFC 8584).  
**Source:** RFC 8584 title/scope and RFC 9785 (`Updates: 8584`, preference-based DF) — https://www.rfc-editor.org/rfc/rfc8584.txt , https://www.rfc-editor.org/rfc/rfc9785.txt
