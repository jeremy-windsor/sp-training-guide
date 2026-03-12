# Module 12 Technical Review v2

## Summary
- Reviewed all 10 target markdown files in `modules/12-case-studies/`.
- **Issues found:** 10 issue entries across 6 files (5 unique technical issues mirrored in answer files).
- Previous fixes were **mostly correct**: the earlier 12.3 transport fixes, the 12.4 RFC 8326 fix, and the 12.5 RFC 8214 / tLDP-session fixes all check out.
- **Still not clean:**
  - `12.1-isp-backbone-design.md`
  - `12.1-isp-backbone-design-answers.md`
  - `12.4-internet-exchange-point-design.md`
  - `12.4-internet-exchange-point-design-answers.md`
  - `12.5-evpn-l2vpn-migration.md`
  - `12.5-evpn-l2vpn-migration-answers.md`
- **Verified clean:**
  - `12.2-dci-with-evpn.md`
  - `12.2-dci-with-evpn-answers.md`
  - `12.3-mobile-backhaul-5g-transport.md`
  - `12.3-mobile-backhaul-5g-transport-answers.md`

### 12.1-isp-backbone-design.md — SRGB Uniformity Is Still Presented as Mandatory
- **Severity**: minor
- **Current text**: "Rule: Every router in the network uses the SAME SRGB range — this is the whole point"
- **Correction**: "Using the same SRGB on every router is an operational simplification, not a protocol requirement. The SRGB is locally configured and may differ across nodes; if the design wants uniform SRGBs, present it as a local policy choice rather than a standards requirement."
- **Source**: RFC 8402; RFC 8660

### 12.1-isp-backbone-design.md — TI-LFA Activation Timeline Is Internally Inconsistent
- **Severity**: minor
- **Current text**: "T=120ms  TI-LFA pre-computed backup path activates (NY-P1 → DEN-P → LA-P)" / "TI-LFA means: traffic reroutes at T=100ms, before SPF even completes."
- **Correction**: "Make the timeline consistent: TI-LFA local repair activates at the point of local repair when the failure is detected, before IGP reconvergence/SPF completes. If failure detection is ~100 ms, the TI-LFA switchover should be shown at that point, with SPF completion afterward."
- **Source**: RFC 9855

### 12.1-isp-backbone-design-answers.md — SRGB Uniformity Is Still Presented as Mandatory
- **Severity**: minor
- **Current text**: "Rule: Every router in the network uses the SAME SRGB range — this is the whole point"
- **Correction**: "Using the same SRGB on every router is an operational simplification, not a protocol requirement. The SRGB is locally configured and may differ across nodes; if the design wants uniform SRGBs, present it as a local policy choice rather than a standards requirement."
- **Source**: RFC 8402; RFC 8660

### 12.1-isp-backbone-design-answers.md — TI-LFA Activation Timeline Is Internally Inconsistent
- **Severity**: minor
- **Current text**: "T=120ms  TI-LFA pre-computed backup path activates (NY-P1 → DEN-P → LA-P)" / "TI-LFA means: traffic reroutes at T=100ms, before SPF even completes."
- **Correction**: "Make the timeline consistent: TI-LFA local repair activates at the point of local repair when the failure is detected, before IGP reconvergence/SPF completes. If failure detection is ~100 ms, the TI-LFA switchover should be shown at that point, with SPF completion afterward."
- **Source**: RFC 9855

### 12.4-internet-exchange-point-design.md — IPv6 Peering Examples Still Use an Invalid Hextet
- **Severity**: minor
- **Current text**: "2001:db8:basx::1"
- **Correction**: "Replace every `2001:db8:basx::/64` example with a syntactically valid documentation prefix such as `2001:db8:100::/64`, and update all derived addresses consistently (for example `2001:db8:100::1`, `::2`, `::b`, `::c`)."
- **Source**: RFC 4291; RFC 3849

### 12.4-internet-exchange-point-design.md — RTBH Description Conflicts with Transparent Route-Server Behavior
- **Severity**: minor
- **Current text**: "Route server re-advertises 203.0.113.100/32 with next-hop set to the discard address to all members"
- **Correction**: "For an IXP route server, either (a) preserve the advertising member's NEXT_HOP and rely on receiving members to map community `65535:666`/BLACKHOLE to a local discard route, or (b) explicitly document and configure a special RTBH next-hop rewrite design. The current text describes discard-next-hop rewriting, but the surrounding RS design is transparent (`rs client` / next-hop preservation)."
- **Source**: RFC 7947; RFC 7999

### 12.4-internet-exchange-point-design-answers.md — IPv6 Peering Examples Still Use an Invalid Hextet
- **Severity**: minor
- **Current text**: "2001:db8:basx::1"
- **Correction**: "Replace every `2001:db8:basx::/64` example with a syntactically valid documentation prefix such as `2001:db8:100::/64`, and update all derived addresses consistently (for example `2001:db8:100::1`, `::2`, `::b`, `::c`)."
- **Source**: RFC 4291; RFC 3849

### 12.4-internet-exchange-point-design-answers.md — RTBH Description Conflicts with Transparent Route-Server Behavior
- **Severity**: minor
- **Current text**: "Route server re-advertises 203.0.113.100/32 with next-hop set to the discard address to all members"
- **Correction**: "For an IXP route server, either (a) preserve the advertising member's NEXT_HOP and rely on receiving members to map community `65535:666`/BLACKHOLE to a local discard route, or (b) explicitly document and configure a special RTBH next-hop rewrite design. The current text describes discard-next-hop rewriting, but the surrounding RS design is transparent (`rs client` / next-hop preservation)."
- **Source**: RFC 7947; RFC 7999

### 12.5-evpn-l2vpn-migration.md — EVPN-VPWS Route Counts Are Undercounted by 2×
- **Severity**: minor
- **Current text**: "Type-1 (per-EVI AD): 5,000 (one per PW endpoint)" / "EVPN-VPWS Type-1: ~2,500" / "EVPN-VPWS Type-1: ~5,000"
- **Correction**: "For ~5,000 VPWS services, EVPN-VPWS requires a pair of per-EVI Ethernet A-D routes per service instance (one advertisement from each endpoint PE). Network-wide control-plane counts should therefore be ~10,000 Type-1 routes at full migration, and ~5,000 at the midpoint if ~2,500 services have migrated. Update the dependent phase totals accordingly."
- **Source**: RFC 8214

### 12.5-evpn-l2vpn-migration-answers.md — EVPN-VPWS Route Counts Are Undercounted by 2×
- **Severity**: minor
- **Current text**: "Type-1 (per-EVI AD): 5,000 (one per PW endpoint)" / "EVPN-VPWS Type-1: ~2,500" / "EVPN-VPWS Type-1: ~5,000"
- **Correction**: "For ~5,000 VPWS services, EVPN-VPWS requires a pair of per-EVI Ethernet A-D routes per service instance (one advertisement from each endpoint PE). Network-wide control-plane counts should therefore be ~10,000 Type-1 routes at full migration, and ~5,000 at the midpoint if ~2,500 services have migrated. Update the dependent phase totals accordingly."
- **Source**: RFC 8214
