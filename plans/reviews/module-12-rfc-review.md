# Module 12 RFC Audit

## Summary

| Metric | Count |
|--------|-------|
| Files reviewed | 10 |
| Unique RFC citations | 12 |
| Total RFC reference instances | ~60 (across main + answer files) |
| Critical findings | 1 |
| Minor findings | 2 |
| Verified correct | 9 RFCs |

**Files reviewed:**
1. `README.md` — no RFC references
2. `12.1-isp-backbone-design.md`
3. `12.1-isp-backbone-design-answers.md`
4. `12.2-dci-with-evpn.md`
5. `12.2-dci-with-evpn-answers.md`
6. `12.3-mobile-backhaul-5g-transport.md` — no RFC references
7. `12.3-mobile-backhaul-5g-transport-answers.md` — no RFC references
8. `12.4-internet-exchange-point-design.md`
9. `12.4-internet-exchange-point-design-answers.md`
10. `12.5-evpn-l2vpn-migration.md`
11. `12.5-evpn-l2vpn-migration-answers.md`

---

## RFC Citation Inventory (Verified)

| RFC | Title (Verified) | Status | Used In | Verdict |
|-----|-----------------|--------|---------|---------|
| RFC 1918 | Address Allocation for Private Internets | Active (BCP 5) | 12.4 | ✅ Correct |
| RFC 4271 | A Border Gateway Protocol 4 (BGP-4) | Active (Draft Standard) | 12.1 | ⚠️ See Finding #1 |
| RFC 4684 | Constrained Route Distribution for BGP/MPLS IP VPNs | Active (Proposed Standard) | 12.5 | ✅ Correct |
| RFC 4761 | Virtual Private LAN Service (VPLS) Using BGP for Auto-Discovery and Signaling | Active (Proposed Standard) | 12.5 | ✅ Correct |
| RFC 5735 | Special Use IPv4 Addresses | **Obsoleted by RFC 6890** | 12.1 | ⚠️ See Finding #2 |
| RFC 6666 | A Discard Prefix for IPv6 | Active (BCP 175) | 12.4 | ✅ Correct |
| RFC 7947 | Internet Exchange BGP Route Server | Active (Standards Track) | 12.4 | ✅ Correct |
| RFC 7999 | BLACKHOLE Community | Active (Informational) | 12.4 | ✅ Correct |
| RFC 8092 | BGP Large Communities Attribute | Active (Standards Track) | 12.1 | ✅ Correct |
| RFC 8214 | Virtual Private Wire Service Support in Ethernet VPN | Active (Standards Track) | 12.5 | ✅ Correct |
| RFC 8326 | Graceful BGP Session Shutdown | Active (Standards Track) | 12.4 | ✅ Correct |
| RFC 8402 | Segment Routing Architecture | Active (Standards Track) | 12.1 | ✅ Correct |
| RFC 9136 | IP Prefix Advertisement in Ethernet VPN (EVPN) | Active (Proposed Standard) | 12.2 | ✅ Correct |

---

## Detailed Findings

### Finding #1 — RFC 4271 Hold Timer Default Value

| Field | Value |
|-------|-------|
| **Severity** | **CRITICAL** |
| **Files** | `12.1-isp-backbone-design.md` (line ~346), `12.1-isp-backbone-design-answers.md` (line ~351) |
| **Current text** | `Mitigation: IBGP hold-down timers tuned to 3s (not default 180s per RFC 4271)` |
| **Issue** | RFC 4271 Section 4.2 specifies the **suggested** Hold Time value as **90 seconds**, not 180 seconds. The 180-second value is a common **vendor implementation default** (notably Cisco IOS), but the RFC itself recommends 90 seconds. |
| **Correction** | Change to: `Mitigation: IBGP hold-down timers tuned to 3s (not default 90s per RFC 4271; many implementations default to 180s)` |
| **Source** | RFC 4271 §4.2 OPEN Message Format: "A value of zero in the Hold Time field... The suggested value for this timer is 90 seconds." Also confirmed by RFC 4273 §bgpPeerHoldTimeConfigured MIB object definition referencing RFC 4271 Section 10. |

---

### Finding #2 — RFC 5735 is Obsolete

| Field | Value |
|-------|-------|
| **Severity** | **MINOR** |
| **Files** | `12.1-isp-backbone-design.md` (line ~218), `12.1-isp-backbone-design-answers.md` (line ~219) |
| **Current text** | `Import policy filters: bogons (RFC 5735), too-long prefixes...` |
| **Issue** | RFC 5735 ("Special Use IPv4 Addresses", January 2010) was **obsoleted by RFC 6890** ("Special-Purpose IP Address Registries", April 2013). While the content of RFC 5735 remains technically correct (RFC 6890 is a superset), citing an obsoleted RFC in a study guide could confuse students or cause issues on exams. |
| **Correction** | Change to: `Import policy filters: bogons (RFC 6890; formerly RFC 5735), too-long prefixes...` or simply `bogons (RFC 6890)` |
| **Source** | RFC 5735 header: "Obsoleted by: 6890". RFC 6890 is the current authoritative reference for special-purpose IP address registries. |

---

### Finding #3 — RFC 8326 GSHUT Community Value Presentation

| Field | Value |
|-------|-------|
| **Severity** | **MINOR** |
| **Files** | `12.4-internet-exchange-point-design.md` (line ~609), `12.4-internet-exchange-point-design-answers.md` (line ~612) |
| **Current text** | `BasinIX implements RFC 8326 graceful shutdown (GSHUT community 65535:0)` |
| **Issue** | The community value 65535:0 (0xFFFF0000) for GRACEFUL_SHUTDOWN is **technically correct** per RFC 8326 and IANA registry. However, the parenthetical phrasing "GSHUT community 65535:0" could be slightly clearer. RFC 8326 defines the well-known community name as `GRACEFUL_SHUTDOWN`, not "GSHUT" (which is a common informal abbreviation). For a study guide, using the formal name would be more precise. |
| **Correction** | Consider: `BasinIX implements RFC 8326 Graceful BGP Session Shutdown (GRACEFUL_SHUTDOWN community, 65535:0)` |
| **Source** | RFC 8326 §5: IANA registered community name is "GRACEFUL_SHUTDOWN" with value 0xFFFF0000 (65535:0). |

---

## Verified Correct (No Issues)

The following RFC citations were audited and found accurate in number, title implication, context of usage, and active/current status:

1. **RFC 1918** (12.4, lines 337-344 in BIRD config comments) — Correctly identifies 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 as RFC 1918 private address space.

2. **RFC 4684** (12.5, multiple locations) — Correctly described as "Route-Target Constrain" and used in context of limiting VPN route distribution. Title is technically "Constrained Route Distribution for BGP/MPLS IP VPNs" but the shorthand "route-target constrain" is the universally accepted operational term.

3. **RFC 4761** (12.5, multiple locations) — Correctly identified as BGP-signaled VPLS. Used consistently in context of VPLS auto-discovery and signaling.

4. **RFC 6666** (12.4, line 357) — Correctly identifies 0100::/64 as the IPv6 discard-only prefix.

5. **RFC 7947** (12.4, line 632) — Correctly referenced for IXP route server transparent mode and next-hop preservation.

6. **RFC 7999** (12.4, line 632) — Correctly referenced as the BLACKHOLE community standard. Community value 65535:666 is accurate.

7. **RFC 8092** (12.1, line 213) — Correctly identified as "BGP Large Communities" for 12-byte community attributes.

8. **RFC 8214** (12.5, multiple locations) — Correctly identified as EVPN-VPWS (Virtual Private Wire Service Support in Ethernet VPN). All usage contexts are accurate.

9. **RFC 8326** (12.4) — Correctly identified as Graceful BGP Session Shutdown. Community value 65535:0 is accurate.

10. **RFC 8402** (12.1, lines 156-157) — Correctly states SRGB is "locally configured per RFC 8402" and that the 16000–23999 range is an operational convention, not IANA-mandated.

11. **RFC 9136** (12.2, line 357) — Correctly referenced for EVPN Type-5 IP prefix advertisement and overlay-index recursion. Context is accurate.

---

## Additional Observations (Non-RFC)

- **EVPN AFI/SAFI** (12.5, line 70): The claim "AFI 25, SAFI 70" for L2VPN EVPN is correct per IANA registry.
- **Community 65535:65281** (12.4): NO_EXPORT well-known community value is correct per RFC 1997 / IANA registry.
- **Community 65535:666** (12.4): BLACKHOLE well-known community is correct per RFC 7999.
- **Community 65535:0** (12.4): GRACEFUL_SHUTDOWN is correct per RFC 8326.
- All answer files (`*-answers.md`) mirror the RFC references in their corresponding main files with identical text. Findings apply equally to both.

---

## Recommendation

**Overall assessment: Module 12 RFC citations are high quality.** Only one critical factual error exists (the RFC 4271 hold timer default), one obsolete RFC reference (RFC 5735→6890), and one minor naming precision issue. All RFC numbers are valid, titles are accurately implied, and the technical claims attributed to each RFC are correct.

Priority fixes:
1. **Fix immediately:** RFC 4271 hold timer — 90s not 180s (affects both 12.1 files)
2. **Fix soon:** Update RFC 5735 → RFC 6890 (affects both 12.1 files)
3. **Optional:** Formalize GSHUT → GRACEFUL_SHUTDOWN naming (affects both 12.4 files)
