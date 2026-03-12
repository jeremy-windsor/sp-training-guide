# Module 06 Review — Segment Routing

## Summary
- **Files reviewed**: 17
- **Files needing fixes**: 14
- **Clean files**: 3
- **Issues found**: 24 total
  - **Critical**: 12
  - **Minor**: 12
  - **Cosmetic**: 0

### Files needing fixes
- `6.1-sr-mpls-fundamentals.md`
- `6.1-sr-mpls-fundamentals-theory.md`
- `6.1-sr-mpls-fundamentals-answers.md`
- `6.2-sr-te-policies.md`
- `6.2-sr-te-policies-answers.md`
- `6.3-ti-lfa.md`
- `6.3-ti-lfa-theory.md`
- `6.4-srv6-fundamentals.md`
- `6.4-srv6-fundamentals-theory.md`
- `6.4-srv6-fundamentals-answers.md`
- `6.5-srv6-network-programming.md`
- `6.5-srv6-network-programming-theory.md`
- `6.6-sr-migration-strategies.md`
- `6.6-sr-migration-strategies-answers.md`

### Clean files
- `6.2-sr-te-policies-theory.md`
- `6.3-ti-lfa-answers.md`
- `6.5-srv6-network-programming-answers.md`

### Recurring themes
- Heterogeneous **SRGB** behavior is misunderstood in multiple places.
- **PCEP/PCE** message direction and **BGP-LS** requirements are overstated or reversed.
- Several **SRv6** sections misuse behavior names or cite the wrong RFCs.
- A few places still describe **IPv6 fragmentation** like it’s IPv4 wearing a fake mustache.

---

### 6.1-sr-mpls-fundamentals.md — Heterogeneous SRGBs Do Not Automatically Blackhole Traffic
- **Severity**: critical
- **Location**: Troubleshooting / "Problem: SRGB Mismatch Between Routers"
- **Current text**: "R1 (SRGB 16000–23999) sends label 16003 for prefix 10.3.3.3/32. R2 (SRGB 20000–27999) calculates label 20003 for the same prefix. R2 doesn't have a forwarding entry for label 16003 → traffic is dropped."
- **Correction**: "Different SRGBs are supported. Upstream nodes must impose/swap the label value expected by the next hop for the advertised SID index; labels may change hop-by-hop when SRGBs differ. A mismatched SRGB by itself should not cause a drop unless SRGB/SID advertisements are missing, stale, or incorrectly programmed."
- **Source**: RFC 8402; RFC 8660

### 6.1-sr-mpls-fundamentals-theory.md — Mapping Server Does Not Turn LDP-Only Transit into Native SR Transit
- **Severity**: minor
- **Location**: "LDP Interworking and Migration"
- **Current text**: "SR-capable routers can then build end-to-end SR-MPLS LSPs through the mixed network."
- **Correction**: "In mixed SR/LDP networks, the Mapping Server supplies Prefix-SID mappings for prefixes, but legacy routers still forward with LDP. The data plane across non-SR islands is via SR/LDP interworking or stitching at the boundary, not native end-to-end SR forwarding across LDP-only transit."
- **Source**: RFC 8661

### 6.1-sr-mpls-fundamentals-answers.md — SR Capability Is Not Advertised in IS-IS Hellos
- **Severity**: critical
- **Location**: Question 2 / Cause 1
- **Current text**: "If SR isn't enabled in the IGP, the router won't advertise SR capabilities in its IS-IS Hello (IIH) packets"
- **Correction**: "SR capability is advertised in IS-IS Link State PDUs using the Router Capability TLV and SR sub-TLVs, not in IIHs."
- **Source**: RFC 8667

### 6.1-sr-mpls-fundamentals-answers.md — SRGB Expansion Should Not Be Presented as Universally Non-Disruptive
- **Severity**: minor
- **Location**: Question 1 answer
- **Current text**: "This is non-disruptive — Junos re-indexes existing SIDs into the expanded range."
- **Correction**: "Changing a router's SRGB changes the label values that router associates with global segments. Treat SRGB expansion as a planned control-plane/data-plane change that requires validation after IGP re-advertisement; do not present it as universally non-disruptive."
- **Source**: RFC 8402; RFC 8660

### 6.2-sr-te-policies.md — BGP-LS Is Common, Not Mandatory, for PCE Topology Learning
- **Severity**: minor
- **Location**: Architecture / PCE section
- **Current text**: "**CRITICAL**: Without BGP-LS, PCE cannot compute paths (blind controller)"
- **Correction**: "A PCE needs topology/state information, but BGP-LS is only one way to supply it. PCE computation is not inherently impossible without BGP-LS."
- **Source**: RFC 4655; RFC 7752

### 6.2-sr-te-policies.md — PCInitiate Direction Is Reversed
- **Severity**: critical
- **Location**: "Example PCE Workflow (ODN)"
- **Current text**: "PE1 sends PCEP PCInitiate request to PCE: 'I need a path to PE2 with color 100'" and "PCE sends PCEP PCInitiate reply with segment list"
- **Correction**: "A PCC requests computation with PCReq/related stateful procedures; PCInitiate is sent from the PCE to the PCC for PCE-initiated LSP setup/deletion workflows."
- **Source**: RFC 5440; RFC 8281

### 6.2-sr-te-policies-answers.md — ODN Is Not Required for Steering to an Existing Matching Policy
- **Severity**: minor
- **Location**: Question 1 / Check 3
- **Current text**: "Is automatic steering / ODN enabled for the address-family? ... Without it, the router receives the colored route but doesn't look up a matching SR-TE policy."
- **Correction**: "Color-based steering can use an already-instantiated matching SR Policy. ODN is specifically for on-demand policy instantiation when no matching policy exists; it is not a prerequisite for steering to an existing valid policy."
- **Source**: RFC 9256

### 6.3-ti-lfa.md — TI-LFA RFC Number Is Wrong
- **Severity**: critical
- **Location**: Overview; Key RFCs; Sources
- **Current text**: "TI-LFA (RFC 9514)" and "RFC 9514 — TI-LFA"
- **Correction**: "Use RFC 9855 for TI-LFA."
- **Source**: RFC 9855

### 6.3-ti-lfa.md — RLFA Does Not Wait for LDP Convergence to Repair Traffic
- **Severity**: minor
- **Location**: LFA evolution comparison
- **Current text**: "Remote LFA (RLFA, RFC 7490) ... Requires LDP, relies on LDP convergence"
- **Correction**: "RLFA typically uses a pre-established tunnel/LSP to a PQ node; it requires an underlying tunnel mechanism, but repair traffic does not wait for LDP convergence after the failure."
- **Source**: RFC 7490

### 6.3-ti-lfa-theory.md — RFC 8333 Is Mischaracterized
- **Severity**: minor
- **Location**: Core Mechanisms / "Microloop Avoidance (RFC 8333)"
- **Current text**: "Microloop Avoidance (RFC 8333): An extension where, during IGP convergence, all routers temporarily use SR segment lists to route traffic along post-convergence paths."
- **Correction**: "RFC 8333 defines micro-loop prevention by introducing a local convergence delay (a two-step convergence method). It is not the RFC for a network-wide temporary SR segment-list mechanism."
- **Source**: RFC 8333

### 6.3-ti-lfa-theory.md — Coverage Claim Needs the Connectivity Caveat
- **Severity**: minor
- **Location**: Protocol Overview
- **Current text**: "TI-LFA (Topology-Independent Loop-Free Alternate) is the fast reroute mechanism for Segment Routing. It provides 100% node and link protection coverage for any network topology"
- **Correction**: "State that TI-LFA can provide complete coverage when a post-convergence repair path exists and the topology remains connected; if the failure partitions the graph or no repair path exists, protection is impossible."
- **Source**: RFC 9855

### 6.4-srv6-fundamentals.md — RFC 9252 Does Not Define T.Encaps/T.Decaps Gateway Functions
- **Severity**: critical
- **Location**: SR-MPLS to SRv6 Interworking
- **Current text**: "**Gateway functions (RFC 9252):** - **T.Encaps** — SR-MPLS to SRv6 (encapsulate MPLS packet in IPv6 + SRH) - **T.Decaps** — SRv6 to SR-MPLS (decapsulate IPv6, expose MPLS label stack)"
- **Correction**: "RFC 9252 is BGP overlay service signaling for SRv6, not a data-plane interworking RFC for T.Encaps/T.Decaps. If you want an RFC-backed interworking reference, cite RFC 8986 End.BM where relevant, or explicitly mark MPLS↔SRv6 gateway translation as implementation-specific / draft-based."
- **Source**: RFC 9252; RFC 8986

### 6.4-srv6-fundamentals.md — IPv6 Routers Do Not Fragment Transit Packets
- **Severity**: critical
- **Location**: War Story / "What happened"
- **Current text**: "First-hop router fragmented the packet (IPv6 fragmentation)"
- **Correction**: "In IPv6, routers do not fragment transit packets. The correct behavior is to drop and send ICMPv6 Packet Too Big so the source can reduce packet size or perform source fragmentation."
- **Source**: RFC 8200

### 6.4-srv6-fundamentals-theory.md — SRH Is Not 'Extension Header Type 4'
- **Severity**: critical
- **Location**: "Segment Routing Header (SRH) — RFC 8754"
- **Current text**: "The SRH is an IPv6 Routing Extension Header (type 4) that carries the segment list."
- **Correction**: "The SRH is an IPv6 Routing Header with Routing Type 4. In the IPv6 Next Header chain, Routing Header is protocol number 43."
- **Source**: RFC 8754; RFC 8200

### 6.4-srv6-fundamentals-theory.md — 'T' Is Not a Standard SRv6 Function
- **Severity**: minor
- **Location**: "SRv6 Functions and Behaviors"
- **Current text**: "**Transit functions** (processed by non-SRv6-aware routers): - **T**: Transit. Normal IPv6 forwarding."
- **Correction**: "Normal IPv6 transit forwarding is just IPv6 forwarding based on the DA; RFC 8986 does not define a standalone SRv6 function named 'T' for non-SRv6 nodes."
- **Source**: RFC 8986; RFC 8754

### 6.4-srv6-fundamentals-answers.md — Locator Planning Is Too Rigid and Uses the Wrong ULA Half
- **Severity**: minor
- **Location**: Question 2 answer
- **Current text**: "An SRv6 locator is a /48 IPv6 prefix ..." and "Allocate `fc00:0::/32` as the SRv6 block (ULA space, common for internal SP use)."
- **Correction**: "Locator length is an operator design choice, not fixed at /48; RFC 8986 uses flexible locator allocation and commonly illustrates per-node /64s from a larger domain block. If ULA is used, locally assigned space comes from fd00::/8, not fc00::/8."
- **Source**: RFC 8986; RFC 4193

### 6.4-srv6-fundamentals-answers.md — SRH Segment List Order Is Wrong in the Packet Walkthrough
- **Severity**: critical
- **Location**: Question 4 / At PE-1 (ingress)
- **Current text**: "Builds an SRH with Segment List = [`fc00:0:5::`, `fc00:0:2:d400::`], Segments Left = 1" followed by "Copy Segment List[0] (`fc00:0:2:d400::`) into the IPv6 Destination Address"
- **Correction**: "Per RFC 8754, the SRH segment list is encoded in reverse order. For a path via R5 to PE-2's End.DT4 SID, the list should be encoded so that Segment List[0] holds the final SID and the initial DA is the last element (the first segment to visit). Keep the walkthrough internally consistent with that indexing."
- **Source**: RFC 8754; RFC 8986

### 6.5-srv6-network-programming.md — Standardized Behaviors Are Headend Behaviors, Not 'Transit Behaviors'
- **Severity**: critical
- **Location**: "Transit Behaviors"
- **Current text**: "| **T.Insert** | Transit with SRH insertion ... | **T.Encaps** | Transit with full encapsulation ..."
- **Correction**: "RFC 8986 standardizes H.Encaps/H.Encaps.Red as SR Policy headend behaviors. Do not present T.Insert/T.Encaps as standardized transit behaviors; if you want to discuss insert-style behavior, label it as non-RFC or implementation-specific."
- **Source**: RFC 8986

### 6.5-srv6-network-programming.md — Base End Behavior with SL=0 Is Not an Error
- **Severity**: critical
- **Location**: Flavors / "Ultimate Segment Pop (USP)"
- **Current text**: "The base END behavior per RFC 8986 requires SL > 0 ... if a packet arrives at an END SID with SL=0 and USP is not enabled, the packet is dropped."
- **Correction**: "In RFC 8986, the base End behavior with Segments Left = 0 stops SRH processing and proceeds to upper-layer processing. USP changes how the exhausted SRH is removed at the ultimate segment; it does not turn an otherwise-invalid base End packet into a valid one."
- **Source**: RFC 8986

### 6.5-srv6-network-programming-theory.md — End.B6 Is Not One of the RFC 8986 Standard Behavior Names
- **Severity**: minor
- **Location**: Encapsulation / Binding Behaviors and Key RFC table
- **Current text**: "**End.B6** — Insert a new SRH into the packet" and "RFC 8986 ... Standard SRv6 behaviors: ... End.B6 ..."
- **Correction**: "RFC 8986 defines End.B6.Encaps and End.B6.Encaps.Red. If you want to discuss pure SRH insertion without outer encapsulation, do not label it as RFC 8986 End.B6 unless you explicitly cite non-RFC/draft behavior names."
- **Source**: RFC 8986

### 6.5-srv6-network-programming-theory.md — RFC Table Uses Wrong RFC Numbers/Titles for SRv6 Service and Compression Work
- **Severity**: critical
- **Location**: Key RFCs & Standards
- **Current text**: "RFC 8980 | 2021 | SRv6 Endpoint Behaviors for Service Programming" and "RFC 9352 | 2023 | SRv6 Compression Requirements and Analysis"
- **Correction**: "RFC 8980 is unrelated to SRv6 endpoint behaviors, and RFC 9352 is IS-IS extensions for SRv6. If you want a compression RFC, use RFC 9602 for compressed SRv6 SIDs/uSID. If you want SRv6 control-plane RFCs, use RFC 9352/9350 in their actual roles."
- **Source**: RFC 8980; RFC 9352; RFC 9602

### 6.6-sr-migration-strategies.md — Mapping Server Does Not Create Native End-to-End SR Across LDP-Only Transit
- **Severity**: minor
- **Location**: Migration Path 1 / Phase 1: Enable SR-MPLS (Coexistence)
- **Current text**: "This allows SR-capable routers to build end-to-end SR paths even when some transit nodes only speak LDP."
- **Correction**: "SRMS provides SID mappings, but LDP-only transit still forwards with LDP. Describe this as SR/LDP interworking/stitching rather than native end-to-end SR forwarding across legacy transit."
- **Source**: RFC 8661

### 6.6-sr-migration-strategies.md — MTU Warning Overstates Fragmentation Behavior
- **Severity**: minor
- **Location**: Migration Anti-Patterns
- **Current text**: "If your MTU is 1500, you will fragment. Plan for 9100+ on all core links."
- **Correction**: "Do MTU math based on actual encapsulation overhead. SR-MPLS may still fit within 1500 for shallow stacks, and IPv6 routers do not fragment transit traffic—they send Packet Too Big. Recommend larger MTUs where needed, not as an unconditional rule."
- **Source**: RFC 3032; RFC 8200

### 6.6-sr-migration-strategies-answers.md — Different SRGBs Do Not Cause the Ingress PE to Push the Wrong Label by Default
- **Severity**: critical
- **Location**: Question 1 answer
- **Current text**: "if one P router has SRGB 17000-24999 ... The ingress PE pushes 16500, which on that router maps to a DIFFERENT prefix"
- **Correction**: "In a heterogeneous-SRGB domain, upstream nodes are expected to impose/swap the label value that is meaningful to the next hop for the advertised SID index. Different SRGBs alone are not a default explanation for intermittent loss."
- **Source**: RFC 8402; RFC 8660
