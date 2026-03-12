# Module 10 Technical Review (Standards Accuracy)

## Summary
- **Total issues**: 19
- **Critical**: 6
- **Minor**: 12
- **Cosmetic**: 1
- **Files needing fixes**:
  - `10.1-network-slicing-concepts.md`
  - `10.1-network-slicing-concepts-answers.md`
  - `10.2-flexe-flexible-ethernet.md`
  - `10.2-flexe-theory.md`
  - `10.2-flexe-flexible-ethernet-answers.md`
  - `10.3-5g-xhaul-requirements.md`
  - `10.3-5g-xhaul-requirements-answers.md`
- **Clean files**: none

### [10.1-network-slicing-concepts.md] — 3GPP Definition Misattributed to TS 23.501
- **Severity**: minor
- **Location**: `What Is a Network Slice?`
- **Current text**: "**3GPP Definition (TS 23.501):** \"A set of network function instances together with the required resources (e.g., compute, storage, networking) which form a complete instantiated logical network to meet certain network characteristics.\""
- **Correction**: "This definition is from 3GPP management specs (TS 28.530), not TS 23.501. Either (a) relabel to TS 28.530, or (b) replace with TS 23.501 network-slice-instance wording."
- **Source**: 3GPP TS 28.530 §4.4.1; 3GPP TS 23.501 §5.15.1

### [10.1-network-slicing-concepts.md] — TN Management Scope Overstated
- **Severity**: minor
- **Location**: `The Three Domains of 5G Slicing`
- **Current text**: "Each domain slices independently, coordinated by the 3GPP management system."
- **Correction**: "State that CN/AN are directly managed by 3GPP management; TN is a non-3GPP part managed by a TN management system that receives requirements from 3GPP management."
- **Source**: 3GPP TS 28.530 §4.4.1

### [10.1-network-slicing-concepts.md] — FlexE Guarantee Applied to Wrong Object
- **Severity**: minor
- **Location**: `Realization Models` → `Model 3: FlexE + VPN + QoS (Hard Slicing)`
- **Current text**: "- Each FlexE group gets guaranteed, non-preemptable bandwidth"
- **Correction**: "Guaranteed/non-preemptable bandwidth applies to FlexE client calendar-slot assignment; the FlexE group is the aggregate resource container."
- **Source**: OIF-FLEXE-03.0 §6.5 (calendar/client assignment model)

### [10.1-network-slicing-concepts.md] — URLLC Latency Framed as Fixed 3GPP One-Way 1 ms Target
- **Severity**: critical
- **Location**: `3GPP Slice Types (S-NSSAI)` / `Transport implications by slice type`
- **Current text**: "The 3GPP end-to-end target is <1 ms one-way"
- **Correction**: "Do not state a single fixed URLLC one-way target for all slices. In 5GS, latency treatment is QoS-flow specific via 5QI/PDB characteristics (Table 5.7.4-1)."
- **Source**: 3GPP TS 23.501 §5.7.2.1 and Table 5.7.4-1

### [10.1-network-slicing-concepts-answers.md] — 3GPP Slice Scope Incorrectly Includes TN as Mandatory Part
- **Severity**: critical
- **Location**: `Question 4` → `Answer`
- **Current text**: "A 3GPP slice is an **end-to-end logical network** spanning RAN, transport, and core."
- **Correction**: "Per TS 23.501, a network slice instance includes CN and at least one access component; TN is treated as non-3GPP part in management architecture (requirements handed to TN management system)."
- **Source**: 3GPP TS 23.501 §5.15.1; 3GPP TS 28.530 §4.4.1

### [10.2-flexe-theory.md] — Wrong OIF-FLEXE-02.1 Publication Year
- **Severity**: minor
- **Location**: `Protocol Overview`
- **Current text**: "published as OIF-FLEXE-02.1 (2020)."
- **Correction**: "OIF-FLEXE-02.1 publication date is July 2019."
- **Source**: OIF-FLEXE-02.1 Document Revision History

### [10.2-flexe-theory.md] — Overhead Frame Period Math/Structure Incorrect
- **Severity**: critical
- **Location**: `3. FlexE Overhead Frame`
- **Current text**: "**Overhead frame period**: One overhead frame per 1,023 × 20 × 66B blocks (approximately every ~100 microseconds at 100G)."
- **Correction**: "1,023×20 corresponds to calendar payload repetition unit; a 100G overhead block period is 20,461 blocks, and one overhead frame is 8 overhead blocks (~104.76 µs at 100G)."
- **Source**: OIF-FLEXE-03.0 §6.6 (Figure 30, overhead frame/multiframe timing)

### [10.2-flexe-theory.md] — “FlexE Unaware” Misclassified as Client Type
- **Severity**: critical
- **Location**: `4. FlexE Client Types`
- **Current text**: "A single PHY carries a single client at the PHY's native rate."
- **Correction**: "FlexE-Unaware is a transport-mode concept (how transport carries FlexE PHYs), not a FlexE client type limited to one client on one PHY."
- **Source**: OIF-FLEXE-03.0 §5.3 (router-to-transport modes)

### [10.2-flexe-theory.md] — ITU-T G.8312 Title Incorrect
- **Severity**: cosmetic
- **Location**: `Key RFCs & Standards` table
- **Current text**: "Interfaces for FlexE-Aware Equipment"
- **Correction**: "Use the standard title: ‘Interfaces for metro transport networks’."
- **Source**: ITU-T G.8312 title

### [10.2-flexe-theory.md] — Non-Standard “Sub-Slot” (<5G) Claim
- **Severity**: minor
- **Location**: `Edge Cases & Gotchas`
- **Current text**: "Sub-slot mechanisms exist but aren't universally implemented."
- **Correction**: "OIF standard calendar description is 5G granularity, with optional coarser implementation constraints (25G/100G), not standardized finer-than-5G sub-slots."
- **Source**: OIF-FLEXE-03.0 §6.5; OIF-FLEXE-02.0 §6.7

### [10.2-flexe-theory.md] — FlexE Overhead ppm Value Too High
- **Severity**: minor
- **Location**: `Edge Cases & Gotchas`
- **Current text**: "The FlexE overhead frame consumes a small amount of bandwidth (~200 ppm)."
- **Correction**: "Nominal rate reduction is about 0.011% (~110 ppm), not ~200 ppm."
- **Source**: OIF-FLEXE-03.0 (rate relationship text: nominal rate about 0.011% less)

### [10.2-flexe-flexible-ethernet.md] — 25G Calendar Granularity Attributed to Wrong Release (Version Table)
- **Severity**: minor
- **Location**: `FlexE Version History`
- **Current text**: "| FlexE 2.1 | July 2019 | 50G PHY support, 25G calendar slot granularity option |"
- **Correction**: "25G calendar granularity appears in FlexE 2.0; FlexE 2.1 primarily added 50GBASE-R group support."
- **Source**: OIF-FLEXE-02.0 §6.7 (25G granularity); OIF-FLEXE-02.1 revision history

### [10.2-flexe-flexible-ethernet.md] — FlexE-Unaware Routing Guidance Conflicts with OIF
- **Severity**: critical
- **Location**: `FlexE Transport Modes`
- **Current text**: "Legacy DWDM transport; PHYs routed independently"
- **Correction**: "OIF states PHYs in a FlexE group are intended to be carried over the same fiber route; diverse routing is not envisioned in FlexE-unaware case."
- **Source**: OIF-FLEXE-03.0 §5.3

### [10.2-flexe-flexible-ethernet.md] — Repeated Wrong Release Attribution for 25G Granularity
- **Severity**: minor
- **Location**: `Bandwidth Planning with FlexE`
- **Current text**: "**FlexE 2.1 added 25G slot granularity**"
- **Correction**: "25G slot granularity is present in FlexE 2.0; keep FlexE 3.0 note for 100G granularity."
- **Source**: OIF-FLEXE-02.0 §6.7; OIF-FLEXE-03.0 §6.5

### [10.2-flexe-flexible-ethernet-answers.md] — Unused Slot Handling Incorrect in Sub-Rate Example
- **Severity**: minor
- **Location**: `Question 2` → `Answer`
- **Current text**: "Those 20 calendar slots are marked as **unavailable** in the FlexE overhead calendar. They carry idle blocks."
- **Correction**: "Do not equate all residual slots to ‘unavailable’; standard handling fills unused/unavailable slots with Ethernet Error control blocks (not generic idle payload)."
- **Source**: OIF-FLEXE-03.0 §5.2.1.7; §7.4

### [10.2-flexe-flexible-ethernet-answers.md] — Fault Signaling Terminology Not Aligned to FlexE IA
- **Severity**: minor
- **Location**: `Question 3` → `Cause 3`
- **Current text**: "Client-level fault signaling (CS-LF or CS-RF)."
- **Correction**: "FlexE IA fault behavior is described via overhead/RPF conditions and client-facing continuous Ethernet Local Fault Ordered Sets."
- **Source**: OIF-FLEXE-03.0 §7.5.2 and Figure 41

### [10.3-5g-xhaul-requirements.md] — “Separate VPNs for N2/N3 per 3GPP recommendation” Unsupported
- **Severity**: minor
- **Location**: `Backhaul: The Familiar Territory`
- **Current text**: "Separate VPNs for N2 (control) and N3 (user) per 3GPP recommendation."
- **Correction**: "3GPP defines N2/N3 functional interfaces and QoS behavior, but does not prescribe separate VPN constructs as a normative recommendation."
- **Source**: 3GPP TS 23.501 (architecture/interfaces and QoS model); 3GPP TS 28.530 (management concepts)

### [10.3-5g-xhaul-requirements-answers.md] — Fronthaul Timing Requirement Misstated as “±130 ns (G.8273.2 Class C)”
- **Severity**: critical
- **Location**: `Question 2` → `Timing architecture` table
- **Current text**: "| 5G fronthaul | ±130 ns phase accuracy (ITU-T G.8273.2 Class C) | G.8275.1 (full on-path PTP) + SyncE |"
- **Correction**: "Do not present ±130 ns as a Class C RU requirement. G.8273.2 specifies clock-class performance (T-BC/T-TSC), while network/RU phase budgets are handled via network-limit framework (e.g., G.8271.1) and deployment-specific 3GPP timing requirements."
- **Source**: ITU-T G.8273.2 scope (clock characteristics); ITU-T G.8271.1 (network limits)

### [10.3-5g-xhaul-requirements-answers.md] — Absolute “G.8275.1 Mandatory / G.8275.2 Not Sufficient” Statement
- **Severity**: minor
- **Location**: `Question 2` → `Timing design` item 3
- **Current text**: "This is mandatory for fronthaul — G.8275.2 (partial timing) doesn't achieve the phase accuracy required for 5G NR TDD."
- **Correction**: "Present as deployment/profile choice rather than universal mandate; G.8275.1 and G.8275.2 are different telecom PTP profiles (full vs partial timing support) and suitability depends on target accuracy/architecture."
- **Source**: ITU-T G.8275.1 and G.8275.2 profile scopes; 3GPP TS 23.501 (no universal profile mandate)
