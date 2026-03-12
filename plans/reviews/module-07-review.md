# Module 07 Review — L3VPN

## Summary
- **Files reviewed**: 15/15
- **Issues found**: 10
  - **Critical**: 4
  - **Minor**: 5
  - **Cosmetic**: 1

### Files needing fixes
- `7.1-l3vpn-architecture-theory.md`
- `7.2-mp-bgp-vpnv4-vpnv6.md`
- `7.2-mp-bgp-vpnv4-vpnv6-theory.md`
- `7.3-inter-as-l3vpn.md`
- `7.3-inter-as-l3vpn-theory.md`
- `7.4-extranet-shared-services-theory.md`
- `7.5-l3vpn-scale-convergence-theory.md`
- `7.5-l3vpn-scale-convergence-answers.md`

### Clean files
- `7.1-l3vpn-architecture.md`
- `7.1-l3vpn-architecture-answers.md`
- `7.2-mp-bgp-vpnv4-vpnv6-answers.md`
- `7.3-inter-as-l3vpn-answers.md`
- `7.4-extranet-shared-services.md`
- `7.4-extranet-shared-services-answers.md`
- `7.5-l3vpn-scale-convergence.md`

---

### 7.1-l3vpn-architecture-theory.md — Vendor-neutral PE-CE protocol list overstates standards support
- **Severity**: minor
- **Location**: `VRF: The Foundation of L3VPN` / `Properties` (also repeated later in `PE-CE Routing Context`)
- **Current text**: "Each VRF can run its own PE-CE routing protocol (BGP, OSPF, IS-IS, static, RIP) independently."
- **Correction**: "For vendor-neutral theory, present the standards-based PE-CE options as static, RIP, BGP, and OSPF (with OSPF behavior specifically defined by RFC 4577). IS-IS/EIGRP should be called out as vendor-specific or non-standardized in this context, not presented as generic L3VPN theory."
- **Source**: RFC 4364 §§7-8; RFC 4577

### 7.2-mp-bgp-vpnv4-vpnv6.md — VPNv6 next-hop encoding is attributed to the wrong mechanism
- **Severity**: critical
- **Location**: `Three MP-BGP Details Everyone Forgets` and `VPNv4 vs VPNv6 — The Differences That Matter`
- **Current text**: "A 16-byte IPv4-mapped-IPv6 encoding (`::ffff:10.0.0.1`) exists but only when the BGP session itself runs over IPv6 (RFC 8950)." / "16-byte IPv4-mapped form only with IPv6 BGP sessions (RFC 8950)"
- **Correction**: "For VPNv6/6VPE over IPv4 transport, RFC 4659 requires the VPN-IPv6 next hop to encode the advertising PE's IPv4 address as an IPv4-mapped IPv6 address. This depends on the requested transport (IPv4 vs IPv6), not on whether the BGP session itself is 'an IPv6 BGP session'. RFC 8950 is about IPv4 NLRI with an IPv6 next hop and is not the governing rule here."
- **Source**: RFC 4659 §3.2.1.2; RFC 8950

### 7.2-mp-bgp-vpnv4-vpnv6-theory.md — VPNv4 next-hop length should not be shown as 24 bytes
- **Severity**: critical
- **Location**: `MP_REACH_NLRI Attribute` diagram
- **Current text**: "Next Hop: 12 bytes (RD 0:0 + IPv4 next-hop) or 24 bytes (RD 0:0 + IPv4 + RD 0:0 + IPv4)"
- **Correction**: "For VPNv4, show a single VPN-IPv4 next hop: 12 bytes (8-byte zero RD + 4-byte IPv4 address). The dual global+link-local next-hop form is an IPv6-family behavior, not a VPNv4 one."
- **Source**: RFC 4364 §4.3.4; RFC 4659 §3.2.1.1

### 7.3-inter-as-l3vpn.md — Option C resolution path incorrectly suggests IGP can carry the stitching route
- **Severity**: critical
- **Location**: `Option C: Multihop MP-eBGP Between RRs/PEs`
- **Current text**: "ASBR2 redistributes this into AS2's IGP (or iBGP) so PE2 can resolve PE1's next-hop"
- **Correction**: "In Option C, the remote PE /32 with label must be carried by labeled BGP (AFI 1 / SAFI 4) or another MPLS-capable mechanism; plain IGP does not carry the MPLS label binding. State that ASBR2 readvertises the route via labeled-unicast iBGP (or otherwise ensures an end-to-end labeled path), not 'into the IGP'."
- **Source**: RFC 4364 §10(c); RFC 8277

### 7.3-inter-as-l3vpn-theory.md — Use the current labeled-unicast RFC
- **Severity**: minor
- **Location**: `Key RFCs & Standards` and `Protocol Interactions`
- **Current text**: "RFC 3107 | 2001 | Carrying Label Information in BGP-4 | Labeled unicast BGP (SAFI 4) — essential for Option C"
- **Correction**: "Reference RFC 8277 as the current standards-track specification for BGP labeled unicast, optionally noting that it obsoletes RFC 3107."
- **Source**: RFC 8277 (obsoletes RFC 3107)

### 7.4-extranet-shared-services-theory.md — RFC 4364 section numbers are wrong
- **Severity**: cosmetic
- **Location**: `Key RFCs & Standards`
- **Current text**: "RFC 4364 §7 | 2006 | Accessing the Internet from a VPN" and "RFC 4364 §8 | 2006 | Quality of Service"
- **Correction**: "These should point to RFC 4364 §11 (Accessing the Internet from a VPN) and RFC 4364 §14 (Quality of Service)."
- **Source**: RFC 4364 §§11, 14

### 7.5-l3vpn-scale-convergence-theory.md — PIC Edge/Core roles are swapped and the label-mode rule is too absolute
- **Severity**: critical
- **Location**: `Prefix-Independent Convergence (PIC)`
- **Current text**: "PIC Edge (PE failure):" and "Prerequisite — per-prefix label allocation: PIC Edge requires that the backup PE (PE3) has a distinct VPN label for the prefix. Per-prefix allocation naturally provides this. Per-VRF allocation doesn't"
- **Correction**: "A remote PE/core-reachability failure is PIC Core behavior, not PIC Edge. Also, do not present per-prefix labeling as a universal protocol prerequisite for L3VPN PIC. PIC is fundamentally about preinstalled alternate path recursion/indirection; label granularity is platform-specific and affects implementation trade-offs, but per-VRF labeling does not universally eliminate PIC support."
- **Source**: Cisco IOS/XR BGP PIC documentation; Juniper `BGP PIC for Layer 3 VPNs` documentation

### 7.5-l3vpn-scale-convergence-answers.md — Unique RDs are recommended, not mandatory, when ADD-PATH is in use
- **Severity**: minor
- **Location**: `Question 2` / `RD Allocation`
- **Current text**: "RD Allocation: Per-PE Unique RDs (Mandatory for PIC)" and "This requires the two egress PEs to advertise genuinely different NLRIs (different RDs) so the RR's ADD-PATH can deliver both."
- **Correction**: "Per-PE unique RDs are a strong operational design choice, but ADD-PATH can advertise multiple paths for the same NLRI. With RFC 7911 in use, multiple same-RD paths can still be delivered and used as backups. Present unique RDs as recommended/preferred, not protocol-mandatory."
- **Source**: RFC 7911

### 7.5-l3vpn-scale-convergence-answers.md — Source list maps PIC to the wrong RFC
- **Severity**: minor
- **Location**: `Sources` footer
- **Current text**: "RFC 5286 (PIC)"
- **Correction**: "RFC 5286 defines Loop-Free Alternates for IP Fast Reroute, not BGP PIC. Replace it with vendor BGP PIC documentation or remove the RFC citation entirely."
- **Source**: RFC 5286

### 7.5-l3vpn-scale-convergence-answers.md — Junos PIC guidance contradicts itself
- **Severity**: minor
- **Location**: `Question 1` / Junos PE guidance
- **Current text**: "Junos PEs — PIC requires explicit configuration (not automatic)" ... followed immediately by "Junos (PEs — PIC is enabled by default in recent Junos when multiple paths are available)"
- **Correction**: "Keep one position only. For a vendor-safe answer key, state that Junos L3VPN PIC should be explicitly enabled and verified per platform/release, and remove the 'enabled by default' sentence unless it is tied to a specific documented Junos release."
- **Source**: Juniper `BGP PIC for Layer 3 VPNs` documentation
