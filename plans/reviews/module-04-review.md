# Module 04 Review Summary

- **Total issues**: 16
- **Critical**: 8
- **Minor**: 8
- **Cosmetic**: 0

## Files needing fixes
- `4.1-ldp-and-label-distribution.md`
- `4.1-ldp-and-label-distribution-theory.md`
- `4.1-ldp-and-label-distribution-answers.md`
- `4.2-rsvp-te.md`
- `4.3-label-operations-theory.md`
- `4.4-mpls-oam-and-troubleshooting.md`
- `4.4-mpls-oam-and-troubleshooting-theory.md`
- `4.4-mpls-oam-and-troubleshooting-answers.md`

## Clean files
- `4.2-rsvp-te-theory.md`
- `4.2-rsvp-te-answers.md`
- `4.3-label-operations.md`
- `4.3-label-operations-answers.md`

---

### [4.1-ldp-and-label-distribution.md] — Active/Passive TCP Role Tied to the Wrong Field
- **Severity**: critical
- **Location**: Session Establishment
- **Current text**: "TCP session on port 646 (both ends use 646 — the router with the higher LDP Identifier becomes the passive/listening side)"
- **Correction**: "LDP session TCP role is determined by comparing the transport addresses used for the session, not the LDP Identifier generically. The LSR with the numerically larger transport address is the active side and initiates TCP; the lower transport address is passive."
- **Source**: RFC 5036 §2.5.2

### [4.1-ldp-and-label-distribution-theory.md] — FEC Type Table Uses Removed/Incorrect Base LDP FECs
- **Severity**: critical
- **Location**: FEC Types
- **Current text**: "Prefix FEC (Type 2) ... Host Address FEC (Type 1) ... Typed Wildcard FEC (Type 5)"
- **Correction**: "For base LDP per RFC 5036, describe Wildcard FEC Element (0x01) and Prefix FEC Element (0x02). Remove Host Address FEC from the base LDP discussion because it was removed from RFC 5036, and do not describe Type 5 as the base wildcard withdraw mechanism unless you explicitly cite the extension that defines it."
- **Source**: RFC 5036 §3.4.1 and §7

### [4.1-ldp-and-label-distribution-theory.md] — Vendor-Neutral Theory Claims a Universal Default for Liberal Retention
- **Severity**: minor
- **Location**: Label Retention: Liberal vs Conservative
- **Current text**: "This is the default and recommended mode."
- **Correction**: "State that liberal retention is common because it improves convergence, but RFC 5036 defines both liberal and conservative retention modes and does not set a universal default. In a theory file, defaults should be described as implementation-dependent."
- **Source**: RFC 5036 §2.6.2

### [4.1-ldp-and-label-distribution-theory.md] — Targeted LDP Incorrectly Restricted to Pseudowire FECs
- **Severity**: minor
- **Location**: Targeted LDP (tLDP)
- **Current text**: "The targeted session carries label bindings for pseudowire FECs (PW ID FEC, Type 128/129), not prefix FECs."
- **Correction**: "Targeted LDP is not limited to pseudowire FECs. RFC 5036 explicitly allows LDP sessions between non-directly connected LSRs for prefix-label use cases such as TE/LDP-over-LSP style forwarding, in addition to later pseudowire applications."
- **Source**: RFC 5036 §2.3

### [4.1-ldp-and-label-distribution-answers.md] — Retention-Mode Answer Gives Explicit-NULL Config That Does Something Else
- **Severity**: critical
- **Location**: Question 4 answer
- **Current text**: "Change IOS-XR from liberal to conservative ... `label local advertise` / `explicit-null`"
- **Correction**: "Remove this config example. Explicit NULL affects label disposition/QoS behavior at egress and is unrelated to liberal vs conservative label retention. If you want to discuss retention mode, keep it at the control-plane behavior level or replace it with a verified platform-specific retention-mode knob."
- **Source**: RFC 5036 §2.6.2; RFC 3032 §2.1

### [4.1-ldp-and-label-distribution-answers.md] — Targeted LDP Session Formation Incorrectly Made Dependent on MPLS Transport
- **Severity**: critical
- **Location**: Question 5 answer
- **Current text**: "Targeted LDP doesn't create its own transport — it rides on top of an existing MPLS label-switched path."
- **Correction**: "A targeted LDP session is still an LDP/TCP session established over IP reachability to the peer's targeted address. A pseudowire data plane may require an underlying transport LSP, but the targeted LDP control session itself does not 'ride on top of' a pre-existing MPLS LSP in RFC 5036."
- **Source**: RFC 5036 §2.3

### [4.2-rsvp-te.md] — Setup/Hold Priority Rule Is Invented and Self-Contradictory
- **Severity**: critical
- **Location**: Bandwidth Reservation and Preemption; Troubleshooting table
- **Current text**: "Hold priority must be ≤ setup priority" and later "ensure setup ≤ hold priority"
- **Correction**: "Remove both inequality rules. RSVP-TE defines setup priority and holding priority as independent 0-7 fields: setup controls ability to preempt others during establishment, and holding controls how easily the LSP itself can be preempted. RFC 3209 does not require one to be numerically less than or equal to the other."
- **Source**: RFC 3209 §4.7

### [4.3-label-operations-theory.md] — Explicit NULL Described as If the Penultimate Hop Pops It
- **Severity**: critical
- **Location**: Reserved Label Values
- **Current text**: "IPv4 Explicit NULL ... Tells the penultimate hop: pop this label, but I need to see it ... The egress router receives an IP packet."
- **Correction**: "Explicit NULL is an on-wire label value. The penultimate hop swaps the outgoing label to 0 (IPv4) or 2 (IPv6); the egress receives the labeled packet, pops the explicit-null label, and then forwards based on the exposed network-layer header."
- **Source**: RFC 3032 §2.1

### [4.3-label-operations-theory.md] — LSP Ping Incorrectly Tied to MPLS Router Alert Label 1
- **Severity**: critical
- **Location**: Protocol Interactions
- **Current text**: "LSP Ping uses label 1 (Router Alert) to force mid-path processing."
- **Correction**: "Do not describe RFC 8029 LSP Ping/Traceroute as using MPLS label 1. MPLS Echo is an IP/UDP packet carried over the MPLS path and, for transit processing, uses the IP Router Alert Option/IPv6 Router Alert handling defined in RFC 8029. Label 1 has separate MPLS Router Alert semantics and is not the generic demultiplexing mechanism for LSP Ping."
- **Source**: RFC 8029 §2.2 and §3; RFC 3032 §2.1

### [4.4-mpls-oam-and-troubleshooting.md] — Reply Mode Table Uses the Wrong RFC 8029 Meanings
- **Severity**: minor
- **Location**: LSP Ping → Reply Modes
- **Current text**: "Mode 3 = Reply via control channel" and "Mode 4 = Reply via specified path (Reverse LSP)"
- **Correction**: "Per RFC 8029, Mode 3 is 'Reply via an IPv4/IPv6 UDP packet with Router Alert' and Mode 4 is 'Reply via application-level control channel'. Remove the 'specified path / Reverse LSP' entry because it is not an RFC 8029 reply mode."
- **Source**: RFC 8029 §3

### [4.4-mpls-oam-and-troubleshooting.md] — Return Code 10 Uses the Wrong Meaning
- **Severity**: minor
- **Location**: LSP Ping → Return Codes
- **Current text**: "10 | Mapping for this FEC not associated with receiving interface"
- **Correction**: "Update code 10 to the RFC 8029 meaning: 'Mapping for this FEC is not the given label at stack-depth <RSC>'. If you want an interface-association failure description, use the exact current return-code wording from RFC 8029 instead of the obsolete phrasing."
- **Source**: RFC 8029 §3.1

### [4.4-mpls-oam-and-troubleshooting.md] — Claimed L3VPN OAM Example Only Tests an LDP Transport FEC
- **Severity**: minor
- **Location**: IOS-XE Configuration
- **Current text**: "LSP Ping for L3VPN (testing VPN label path) ... `ping mpls ipv4 10.0.0.5/32 fec-type ldp`"
- **Correction**: "Relabel this as a transport-LDP FEC test, or replace it with a true VPN-aware MPLS OAM example that uses a VPN FEC/VRF-specific probe. Testing a VPN label path requires a VPN FEC in the echo request, not an LDP prefix FEC to the PE loopback."
- **Source**: RFC 8029 §3.2.5

### [4.4-mpls-oam-and-troubleshooting.md] — 'BFD for MPLS LSPs' Section Actually Shows LDP-IGP/BFD Knobs, Not RFC 5884 LSP BFD
- **Severity**: critical
- **Location**: IOS-XE Configuration → BFD for MPLS LSPs (LDP)
- **Current text**: "`mpls ldp igp sync bfd` ... `mpls ldp neighbor 10.0.0.2 targeted ldp`"
- **Correction**: "Do not present LDP-IGP synchronization or targeted-LDP neighbor configuration as BFD for MPLS LSPs. RFC 5884 describes end-to-end MPLS LSP BFD bootstrapped with LSP Ping; this section should either be replaced with verified platform-specific LSP-BFD configuration or clearly renamed as per-link LDP/BFD/LDP-IGP-sync assistance."
- **Source**: RFC 5884 §6 and §7

### [4.4-mpls-oam-and-troubleshooting-theory.md] — Reply Mode Definitions Are Outdated/Incorrect
- **Severity**: minor
- **Location**: LSP Ping (RFC 8029)
- **Current text**: "Mode 3: Reply via an LSP (label-switched reply path)" and "Mode 4: Reply via control channel"
- **Correction**: "Update the reply modes to the RFC 8029 definitions: Mode 3 = reply via IPv4/IPv6 UDP packet with Router Alert; Mode 4 = reply via application-level control channel."
- **Source**: RFC 8029 §3

### [4.4-mpls-oam-and-troubleshooting-theory.md] — Return Code 5 Still Uses Obsolete DSCP/Short-Pipe Text
- **Severity**: minor
- **Location**: MPLS Echo Reply → Return Code table
- **Current text**: "5 | DSCP/Short Pipe mapping error"
- **Correction**: "Update return code 5 to the current RFC 8029 meaning: 'Downstream Mapping Mismatch'."
- **Source**: RFC 8029 §3.1

### [4.4-mpls-oam-and-troubleshooting-answers.md] — Answer Maps CLI Letter 'N' to the Wrong RFC Return Code Semantics
- **Severity**: minor
- **Location**: Question 2 answer
- **Current text**: "`N` means 'mapping for this FEC is not associated with the receiving interface'"
- **Correction**: "Do not equate vendor shorthand `N` with that obsolete/incorrect RFC meaning. Either describe the RFC 8029 code correctly by number (code 10 = 'mapping for this FEC is not the given label') or rewrite the answer to match the platform legend consistently if `N` is intended to mean 'no label entry'."
- **Source**: RFC 8029 §3.1
