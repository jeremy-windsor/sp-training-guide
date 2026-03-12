# Module 05 Review — Traffic Engineering

## Summary
- **Files reviewed**: 11/11
- **Issues found**: 11 total
  - **Critical**: 3
  - **Minor**: 8
  - **Cosmetic**: 0
- **Files needing fixes**:
  - `5.1-te-fundamentals.md`
  - `5.2-rsvp-te-advanced-theory.md`
  - `5.3-segment-routing-te.md`
  - `5.3-segment-routing-te-theory.md`
  - `5.3-segment-routing-te-answers.md`
  - `5.4-te-deployment-and-design.md`
  - `5.4-te-deployment-and-design-answers.md`
- **Clean files**:
  - `5.1-te-fundamentals-theory.md`
  - `5.1-te-fundamentals-answers.md`
  - `5.2-rsvp-te-advanced.md`
  - `5.2-rsvp-te-advanced-answers.md`

### 5.1-te-fundamentals.md — Affinity semantics are described as path-wide instead of per-link
- **Severity**: critical
- **Location**: `### Link Coloring / Administrative Groups (Affinities)`
- **Current text**: "`affinity / include-any`: Path MUST traverse at least one link matching any set bit"
- **Correction**: "Affinity/admin-group tests are applied during CSPF link pruning, i.e. against each candidate link as the path is computed. `include-any`, `include-all`, and `exclude-any` are not satisfied by a single matching hop somewhere in the path. Rewrite this section to say that every traversed link must satisfy the relevant admin-group test."
- **Source**: RFC 3209; RFC 5305; RFC 7308

### 5.1-te-fundamentals.md — OSPF inter-area TE is incorrectly tied to Type 11 Opaque LSAs
- **Severity**: minor
- **Location**: `### OSPF TE Extensions (RFC 3630)`
- **Current text**: "Inter-area TE requires Type 11 (AS-scoped) Opaque LSAs or PCE"
- **Correction**: "RFC 3630 is an intra-area TE extension and uses Type 10 Opaque LSAs. Inter-area MPLS-TE is handled through loose-hop/ABR procedures and later inter-area requirements/solutions (for example RFC 4105 / RFC 5152 / PCE workflows). Type 11 AS-scoped Opaque LSAs are associated with inter-AS TE extensions, not the generic answer for inter-area OSPF-TE."
- **Source**: RFC 3630; RFC 4105; RFC 5392

### 5.2-rsvp-te-advanced-theory.md — Inter-area TE limitation overstates bandwidth behavior
- **Severity**: minor
- **Location**: `### 5. Inter-Area TE`
- **Current text**: "No end-to-end bandwidth guarantee (each area reserves independently)."
- **Correction**: "The real limitation is lack of global visibility and optimality during loose-hop/per-domain computation. RSVP still reserves bandwidth on the actual end-to-end path that is finally signaled; the head-end simply cannot guarantee globally optimal constraint satisfaction up front without coordinated procedures such as BRPC/PCE."
- **Source**: RFC 3209; RFC 5152; RFC 5441

### 5.3-segment-routing-te.md — Segment type table uses nonstandard and internally inconsistent terminology
- **Severity**: minor
- **Location**: `### Segment Types in SR-TE`
- **Current text**: "`| Type F | BSP (Binding SID) | Steers into another SR policy | Policy chaining across domains |` / `| Type H | Prefix-SID of BGP peer | Inter-domain steering | BGP PeerNode SID |`"
- **Correction**: "Use standard SR terminology instead of invented letter-types: Node SID (Prefix-SID), Adjacency SID, Flex-Algo Prefix-SID, Binding SID (BSID), and PeerNode SID. `BSP` should be `BSID`, and PeerNode SID should not be described as a generic `Type H` Prefix-SID."
- **Source**: RFC 8402; RFC 9256

### 5.3-segment-routing-te.md — SR-specific PCEP reference is missing from the PCE section
- **Severity**: minor
- **Location**: `### PCE / PCEP (RFC 5440, 8231, 8281)`
- **Current text**: "`### PCE / PCEP (RFC 5440, 8231, 8281)`"
- **Correction**: "Add RFC 8664 to the section heading/reference set because it defines the PCEP extensions for Segment Routing and is the SR-specific standards reference for carrying SR paths/segment lists via PCEP."
- **Source**: RFC 8664; RFC 8231; RFC 8281

### 5.3-segment-routing-te-theory.md — Flex-Algo text incorrectly implies a separate SRGB per algorithm
- **Severity**: minor
- **Location**: `### 6. Flexible Algorithm (Flex-Algo)`
- **Current text**: "They allocate Prefix-SIDs in a separate SRGB range for Algo 128."
- **Correction**: "State that Flex-Algo uses algorithm-specific Prefix-SID advertisements/indices; it does not require a separate SRGB range per algorithm. The algorithm association is carried in the SR/Flex-Algo advertisements, while the SRGB remains the label block used for SR-MPLS label computation."
- **Source**: RFC 8667; RFC 9350

### 5.3-segment-routing-te-answers.md — MSD is treated as a transit-node parser limit instead of an imposition capability
- **Severity**: minor
- **Location**: `## Question 3 / ### Answer`
- **Current text**: "The Maximum SID Depth (MSD) advertised by that node is probably 4-6, and at that point in the path, the remaining stack depth exceeds what the ASIC can process."
- **Correction**: "Advertised Base MSD is primarily an imposition capability used by an ingress/head-end or any node that must add labels (for example, a BSID anchor or repair point). If you want to explain a transit drop from a deep label stack, call it a platform forwarding/parser limit or other stack-depth constraint — do not equate it directly with the dropping node's advertised MSD."
- **Source**: RFC 8491; RFC 8476; RFC 8814

### 5.4-te-deployment-and-design.md — LDPoRSVP mechanics incorrectly describe remote targeted LDP sessions over the TE tunnel
- **Severity**: critical
- **Location**: `### LDP-over-RSVP (LDPoRSVP)`
- **Current text**: "`LDP sessions run over RSVP tunnels (LDP targeted sessions or IGP autoroute)` ... `LDP sees the tunnel endpoint as directly connected (IGP distance = 0 via tunnel)` ... `LDP establishes targeted session over the tunnel`"
- **Correction**: "Reframe LDPoRSVP as transport/next-hop resolution, not 'directly connected' PE-to-PE targeted LDP by default. RSVP-TE supplies the transport LSP; labeled FECs recurse to that LSP via IGP/inet.3/autoroute resolution. LDP control traffic is not automatically 'inside the tunnel,' and remote targeted sessions are not the generic mechanism for classic LDPoRSVP."
- **Source**: RFC 5036; RFC 3209

### 5.4-te-deployment-and-design.md — FRR bypass example has the wrong merge point/tail router
- **Severity**: minor
- **Location**: `### Fast Reroute (FRR) — RFC 4090 / Facility Backup`
- **Current text**: "`At P4 (bypass tunnel tail): Pop bypass-label, forward [RSVP-label-B] | [LDP] | [VPN] to PE5`"
- **Correction**: "For the preceding link-protection example (`PE1 → P2 → P3 → PE5` with bypass via `P4`), the merge point/tail is downstream at P3, not P4. Either change the text to `At P3 (merge point)` or redraw the example so the bypass actually terminates on P4."
- **Source**: RFC 4090

### 5.4-te-deployment-and-design.md — TI-LFA RFC reference is wrong
- **Severity**: minor
- **Location**: `## Quick Reference` / `Sources`
- **Current text**: "`RFC 9514 (TI-LFA)`"
- **Correction**: "Replace this with `RFC 9855 (Topology Independent Fast Reroute Using Segment Routing)`. RFC 9514 is for BGP-LS extensions for SRv6, not TI-LFA."
- **Source**: RFC 9855; RFC 9514

### 5.4-te-deployment-and-design-answers.md — BFD timer example contradicts the sub-50ms claim
- **Severity**: critical
- **Location**: `## Question 2 / ### Answer`
- **Current text**: "`3 × 50 ms` for a safer production default ... `That yields detection in roughly ... 150 ms ... so with BFD + FRR you can get to sub-50 ms total`"
- **Correction**: "Keep 3×10 ms (or similarly fast hardware-supported detection) for a sub-50 ms example. A 3×50 ms profile yields roughly 150 ms detection before FRR and cannot be presented as sub-50 ms total convergence."
- **Source**: RFC 5880
