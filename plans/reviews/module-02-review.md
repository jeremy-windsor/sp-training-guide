# Module 2 (IGP) — Accuracy Review

## Summary
- Files reviewed: 11
- Issues found: 13 (critical: 2, minor: 11, cosmetic: 0)
- Files needing TTS regeneration: [2.1-isis-deep-dive.md, 2.1-isis-deep-dive-theory.md, 2.2-ospf-in-sp-networks.md, 2.2-ospf-in-sp-networks-theory.md, 2.3-igp-convergence-tuning.md, 2.3-igp-convergence-tuning-answers.md, 2.4-isis-vs-ospf-decision-framework.md]

## Issues

### 2.1-isis-deep-dive-theory.md — IS-IS Ethernet encapsulation is described with a non-existent EtherType
- **Severity**: minor
- **Location**: Protocol Overview
- **Current text**: "IS-IS frames are encapsulated directly in the data link layer using a dedicated Ethertype (0x83FE for 802.3) or DSAP/SSAP (0xFEFE for 802.2 LLC)."
- **Correction**: "On Ethernet, IS-IS is carried in 802.3 frames with an 802.2 LLC header using DSAP/SSAP 0xFE and NLPID 0x83; 0x83 is the NLPID, not an EtherType."
- **Source**: ISO 10589; RFC 1195

### 2.1-isis-deep-dive.md — Adjacency checklist implies an OSPF-style MTU check that IS-IS does not perform
- **Severity**: minor
- **Location**: Adjacency Formation
- **Current text**: "Neighbor receives, checks: area match (L1), authentication, MTU"
- **Correction**: "IS-IS adjacency formation checks level/area compatibility, authentication, and 3-way state. There is no explicit MTU field/DBD-style MTU check; MTU problems surface indirectly through padded Hellos or oversized LSPs."
- **Source**: ISO 10589; RFC 3719

### 2.1-isis-deep-dive.md — Point-to-point recommendation uses the wrong term
- **Severity**: minor
- **Location**: P2P vs Broadcast
- **Current text**: "Use this for all SP links (even Ethernet — set `circuit-type point-to-point`)."
- **Correction**: "Use point-to-point network type on inter-router links. `circuit-type` in IS-IS refers to level participation (for example level-1, level-2, or level-1-2), not LAN-versus-point-to-point media type."
- **Source**: ISO 10589; RFC 1195

### 2.1-isis-deep-dive-answers.md — Clean
- No technical issues found.

### 2.2-ospf-in-sp-networks.md — OSPFv2 and OSPFv3 header fields are conflated
- **Severity**: critical
- **Location**: OSPF Packet Types
- **Current text**: "All packets carry the OSPF header with Router ID, Area ID, authentication, and instance ID (OSPFv3)."
- **Correction**: "Separate OSPFv2 and OSPFv3 packet headers. OSPFv2 uses a 24-byte header with AuType/Auth data; OSPFv3 uses a 16-byte header with Instance ID and no authentication fields in the packet header."
- **Source**: RFC 2328; RFC 5340

### 2.2-ospf-in-sp-networks.md — LSA type table mixes OSPFv2 opaque LSAs with OSPFv3 type numbers
- **Severity**: minor
- **Location**: LSA Types — The Full Picture
- **Current text**: "| 8 | Link LSA (v3) | ... | 9 | Opaque (link) | ... | 10 | Opaque (area) | ... | 11 | Opaque (AS) | ... |"
- **Correction**: "Do not combine OSPFv3 Type 8/9 LSAs with OSPFv2 opaque Type 9/10/11 LSAs in one flat numeric table. In OSPFv2, 9/10/11 are Opaque LSAs; in OSPFv3, Type 8 is Link-LSA and Type 9 is Intra-Area-Prefix-LSA, with flooding scope encoded in the LS type."
- **Source**: RFC 2328; RFC 5250; RFC 5340

### 2.2-ospf-in-sp-networks.md — NSSA troubleshooting points to a non-standard “router-id priority” knob
- **Severity**: minor
- **Location**: Common Issues
- **Current text**: "Check ABR router-id priority, NSSA config"
- **Correction**: "Check NSSA translator election/state, translator eligibility, P-bit/forwarding-address handling, and NSSA ABR configuration. There is no standard 'router-id priority' control for Type-7 translator election."
- **Source**: RFC 3101

### 2.2-ospf-in-sp-networks-theory.md — Packet format section incorrectly presents one common header for both OSPFv2 and OSPFv3
- **Severity**: critical
- **Location**: 1. Packet Format
- **Current text**: "All OSPF packets share a common 24-byte header:" and "Version: 2 for OSPFv2, 3 for OSPFv3."
- **Correction**: "Split the packet-format discussion into OSPFv2 and OSPFv3. OSPFv2 has the 24-byte header with AuType/Auth data; OSPFv3 has a different 16-byte header with Instance ID and Reserved fields. If authentication is discussed, note that modern OSPFv3 also supports the Authentication Trailer."
- **Source**: RFC 2328; RFC 5340; RFC 7166

### 2.2-ospf-in-sp-networks-theory.md — TE LSA contents are labeled as sub-TLVs when they are TLVs
- **Severity**: minor
- **Location**: Types 9, 10, 11: Opaque LSAs
- **Current text**: "TE Router Address (sub-TLV 1)" / "TE Link (sub-TLV 2)"
- **Correction**: "In RFC 3630 these are top-level TLVs inside the TE LSA: Router Address TLV (type 1) and Link TLV (type 2). Sub-TLVs are carried inside the Link TLV."
- **Source**: RFC 3630

### 2.2-ospf-in-sp-networks-answers.md — Clean
- No technical issues found.

### 2.3-igp-convergence-tuning.md — TI-LFA failover claim ignores BFD detection math
- **Severity**: minor
- **Location**: TI-LFA section
- **Current text**: "TI-LFA + BFD = sub-50ms failover for any single failure."
- **Correction**: "TI-LFA removes SPF/RIB/FIB delay from the failover path, but failover is still bounded by detection. With BFD at 50 ms × 3, expected failover is about 150 ms; sub-50 ms requires faster local failure detection such as physical LOS or much faster BFD."
- **Source**: RFC 5880; RFC 9855

### 2.3-igp-convergence-tuning.md — `lsp-lifetime 65535` is presented as a generic convergence optimization
- **Severity**: minor
- **Location**: Complete Convergence-Optimized IS-IS (Junos)
- **Current text**: "lsp-lifetime 65535;"
- **Correction**: "Do not present `lsp-lifetime 65535` as a generic convergence-tuning setting. Extended LSP lifetime is a separate design tradeoff that increases stale-LSP persistence after ungraceful failure; leave lifetime at default unless the tradeoff is explicitly explained."
- **Source**: ISO 10589; RFC 3719; RFC 7987

### 2.3-igp-convergence-tuning-theory.md — Clean
- No technical issues found.

### 2.3-igp-convergence-tuning-answers.md — SRGB mismatch is overstated as a general TI-LFA failure cause
- **Severity**: minor
- **Location**: Question 3, Cause 3
- **Current text**: "Cause 3: SRGB mismatch across nodes... TI-LFA may fail to construct valid segment lists for backup paths."
- **Correction**: "Different SRGBs are operationally undesirable but are not, by themselves, a protocol-level reason TI-LFA fails. The headend can use the remote node's advertised SID/SRGB mapping to impose correct labels. Missing SIDs, unsupported segment depth, absent alternate topology, or interface protection gaps are stronger general causes."
- **Source**: RFC 8402; RFC 8667

### 2.4-isis-vs-ospf-decision-framework.md — IS-IS encapsulation value is wrong
- **Severity**: minor
- **Location**: Protocol Fundamentals table
- **Current text**: "Direct L2 frames (ethertype 0xFE)"
- **Correction**: "IS-IS over Ethernet uses 802.3/802.2 LLC encapsulation with DSAP/SSAP 0xFE and NLPID 0x83; 0xFE is not an EtherType."
- **Source**: ISO 10589; RFC 1195

### 2.4-isis-vs-ospf-decision-framework.md — IS-IS is described as not MTU-dependent, which overstates the difference with OSPF
- **Severity**: minor
- **Location**: Protocol Fundamentals table
- **Current text**: "Not MTU-dependent (no IP fragmentation)"
- **Correction**: "IS-IS has no explicit OSPF-style MTU check, but it is still constrained by Layer-2 MTU and can fail because of padded Hellos or oversized LSPs. A more accurate contrast is 'less operationally MTU-sensitive than OSPF, but still MTU-constrained.'"
- **Source**: ISO 10589; RFC 3719

### 2.4-isis-vs-ospf-decision-framework-answers.md — Clean
- No technical issues found.
