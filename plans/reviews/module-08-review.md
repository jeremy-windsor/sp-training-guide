# Module 08 Review — L2VPN & EVPN

## Summary
- **Files reviewed**: 13/13
- **Total issues**: 14
  - **Critical**: 6
  - **Minor**: 7
  - **Cosmetic**: 1
- **Files needing fixes**:
  - `8.1-legacy-l2vpn.md`
  - `8.2-evpn-fundamentals.md`
  - `8.3-evpn-mpls-vs-vxlan.md`
  - `8.3-evpn-mpls-vs-vxlan-answers.md`
  - `8.4-evpn-multi-homing-theory.md`
  - `8.4-evpn-multi-homing.md`
  - `8.4-evpn-multi-homing-answers.md`
  - `8.5-evpn-dci.md`
  - `8.5-evpn-dci-answers.md`
- **Clean files**:
  - `8.1-legacy-l2vpn-theory.md`
  - `8.1-legacy-l2vpn-answers.md`
  - `8.2-evpn-fundamentals-theory.md`
  - `8.2-evpn-fundamentals-answers.md`

### [8.1-legacy-l2vpn.md] — RFC 8469 does not make Ethernet CW universally mandatory
- **Severity**: minor
- **Location**: Key Knobs
- **Current text**: "Prevents ECMP polarization; mandatory per RFC 8469"
- **Correction**: "Prevents ECMP polarization; RFC 8469 strongly recommends the Ethernet control word in all but exceptional circumstances, but it does not make CW universally mandatory, and implementations must still interoperate without it."
- **Source**: RFC 8469 (Abstract, §§1 and 4)

### [8.2-evpn-fundamentals.md] — Route Type 1 per-ES vs per-EVI encoding is wrong
- **Severity**: critical
- **Location**: Route Type 1 — Ethernet Auto-Discovery (EAD)
- **Current text**: "Per-ES EAD (ESI, RD, ETI=0)" and "For per-EVI EAD, this is the aliasing label."
- **Correction**: "Per-ES Ethernet A-D routes use Ethernet Tag ID = MAX-ET and NLRI MPLS Label = 0; the split-horizon label is carried in the ESI Label Extended Community. Per-EVI Ethernet A-D routes are the optional aliasing routes, and their Ethernet Tag ID may be 0 or a specific Ethernet Tag depending on the service model."
- **Source**: RFC 7432 (§§8.2.1 and 8.4.1)

### [8.2-evpn-fundamentals.md] — Preference-based DF election cites the wrong RFC
- **Severity**: minor
- **Location**: Route Type 4 — Ethernet Segment / DF election process; Quick Reference
- **Current text**: "**Preference-based (RFC 8584):** PEs advertise a preference weight. Highest wins."
- **Correction**: "Keep RFC 8584 for HRW and DF-election extensibility. If you want preference-based DF election in a 2026 text, cite RFC 9785, which updates RFC 8584 and standardizes preference-based / non-revertive DF election."
- **Source**: RFC 8584; RFC 9785

### [8.3-evpn-mpls-vs-vxlan.md] — RFC 9135 is misidentified
- **Severity**: minor
- **Location**: Quick Reference — Key RFCs
- **Current text**: "RFC 9135 — EVPN Multi-Homing Procedures"
- **Correction**: "RFC 9135 — Integrated Routing and Bridging in EVPN. Multi-homing remains primarily RFC 7432, with DF-election extensions in RFC 8584 / RFC 9785."
- **Source**: RFC 9135; RFC 7432; RFC 8584; RFC 9785

### [8.3-evpn-mpls-vs-vxlan.md] — Symmetric IRB is overstated as a Type-5-only model
- **Severity**: minor
- **Location**: Integrated Routing and Bridging (IRB) Differences
- **Current text**: "EVPN-MPLS almost always uses symmetric IRB. The PE routes the frame into a VRF (Type 5 route, IP prefix), encapsulates with a VRF label, and the remote PE routes it out."
- **Correction**: "Symmetric IRB uses RT-2 MAC/IP routes plus the Router's MAC extended community for host reachability; RT-5 is used for subnet/external prefix advertisement and bootstrapping when a subnet is not instantiated on every PE, not for every routed packet."
- **Source**: RFC 9135 (§§5.1-5.3); RFC 9136

### [8.3-evpn-mpls-vs-vxlan-answers.md] — Anycast gateway failure is incorrectly blamed on missing Type-5 routes
- **Severity**: critical
- **Location**: Question 2 answer
- **Current text**: "The most likely cause is **missing or inconsistent EVPN Type-5 (IP prefix) routes** for the anycast gateway IP..."
- **Correction**: "Failure to reach the anycast default gateway is usually a Type-2 / IRB / default-gateway signaling problem: verify the SVI/IRB, anycast MAC, Type-2 MAC/IP route with the Default Gateway extended community, and router-MAC handling. Type-5 routes are not required just to ARP for or hit the local anycast gateway IP."
- **Source**: RFC 7432 (§10.1); RFC 9135 (§5.1)

### [8.3-evpn-mpls-vs-vxlan-answers.md] — RD/RT do not solve duplicate MACs inside one stretched EVI
- **Severity**: minor
- **Location**: Question 3 answer
- **Current text**: "EVPN solves the **MAC overlap** problem through the **Route Distinguisher (RD)** and **Route Target (RT)** mechanism..."
- **Correction**: "RD/RT isolate different EVIs/tenants. They do not make duplicate MACs safe inside the same MAC-VRF / bridge domain. If the scenario is 'same VLAN IDs reused across different EVIs or tenants', say that explicitly; if the same customer wants one stretched EVI with overlapping MACs, EVPN does not solve that."
- **Source**: RFC 7432 (§§6, 7.9, 7.10)

### [8.4-evpn-multi-homing-theory.md] — Preference-based DF election is attributed to the wrong RFC
- **Severity**: minor
- **Location**: DF election algorithms; Key RFCs & Standards table
- **Current text**: "Algorithm 2 — Preference-based" and "RFC 8584 ... HRW, preference-based"
- **Correction**: "RFC 8584 defines the DF-election extensibility framework and HRW. Preference-based DF election was standardized later in RFC 9785. Update both the prose and the RFC table."
- **Source**: RFC 8584; RFC 9785

### [8.4-evpn-multi-homing.md] — RT-1 Ethernet Tag handling is misstated
- **Severity**: critical
- **Location**: Route Type Interactions / note below the table
- **Current text**: "per-ES (Ethernet Tag = 0, mass withdrawal)" and "per-EVI has a non-zero Ethernet Tag"
- **Correction**: "Per-ES Ethernet A-D routes use Ethernet Tag ID = MAX-ET. Per-EVI Ethernet A-D routes are the aliasing routes, and their Ethernet Tag ID may be 0 or a specific Ethernet Tag depending on VLAN-based vs VLAN-aware service models. Do not teach '0 vs non-zero' as the defining distinction."
- **Source**: RFC 7432 (§§8.2.1 and 8.4.1)

### [8.4-evpn-multi-homing.md] — RFC 8214 title is wrong
- **Severity**: cosmetic
- **Location**: Quick Reference — Key RFCs
- **Current text**: "RFC 8214 — Virtual Subnet: EVPN A-D Route Usage (aliasing details)"
- **Correction**: "RFC 8214 — Virtual Private Wire Service Support in Ethernet VPN. It is the EVPN-VPWS RFC, not an aliasing-specific A-D route document."
- **Source**: RFC 8214

### [8.4-evpn-multi-homing-answers.md] — Per-ES and per-EVI RT-1 roles are reversed
- **Severity**: critical
- **Location**: Question 1 answer — Route Types for Aliasing and Mass Withdrawal
- **Current text**: "Route Type 1A: EAD per-ES ... Used for: Aliasing" and "Route Type 1B: EAD per-EVI ... Used for: Mass withdrawal"
- **Correction**: "Reverse this. Per-ES Ethernet A-D routes are used for fast convergence / mass withdrawal and carry the ESI Label EC. Per-EVI Ethernet A-D routes are the optional aliasing routes used to build multi-homing ECMP next-hop sets."
- **Source**: RFC 7432 (§§8.2.1 and 8.4.1)

### [8.5-evpn-dci.md] — RFC 9014 is mischaracterized as a VIP-based anycast-BGW design
- **Severity**: critical
- **Location**: Model 3: EVPN Multi-Site (RFC 9014)
- **Current text**: "An evolution of Model 2 formalized in RFC 9014 ... BGWs advertise themselves using a **virtual IP (VIP)**..."
- **Correction**: "RFC 9014 is a generic interconnect solution for EVPN overlay networks and focuses on GW route processing between EVPN-Overlay and WAN L2VPN/EVPN domains, including I-ES/vES and the Unknown MAC Route (UMR). A VIP/anycast-VTEP BGW pattern is a vendor design option, not what RFC 9014 standardizes."
- **Source**: RFC 9014 (§§1-4)

### [8.5-evpn-dci.md] — Type-5 route reduction is framed as generic 'MAC summarization'
- **Severity**: critical
- **Location**: Model 3 discussion; Inter-Subnet DCI with Type-5 Routes
- **Current text**: "MAC summarization is natural — the BGW can advertise Type-5 (IP prefix) routes toward the WAN instead of individual Type-2 (MAC/IP) routes" and "10,000 RT-2 routes become 1 RT-5 route."
- **Correction**: "Type-5 routes summarize IP prefixes for routed inter-subnet reachability. They do not replace RT-2 for same-subnet L2 extension, host mobility, or MAC mobility procedures. Frame this as 'IP-prefix route reduction for routed DCI' rather than generic 'MAC summarization'."
- **Source**: RFC 9135 (§5.3); RFC 9136; RFC 9014

### [8.5-evpn-dci-answers.md] — DCI model taxonomy does not match the chapter
- **Severity**: minor
- **Location**: Question 1 answer — list of the three models
- **Current text**: "3. **L3-Only DCI with Type 5 Routes** — pure IP interconnect, no L2 extension"
- **Correction**: "Either align the answer key to the chapter's model numbering, or explicitly say this is a separate fourth design pattern. Right now the answer key's 'Model 3' conflicts with the chapter's 'Model 3 = RFC 9014 multi-site', which will confuse exam prep."
- **Source**: RFC 9014; RFC 9136
