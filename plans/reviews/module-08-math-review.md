# Module 08 Math/Scaling Review

## Summary
- Files reviewed: 14
- Findings: 5
- Critical: 1
- Minor: 4

## Findings

1. **Severity:** Critical  
   **File:** `8.3-evpn-mpls-vs-vxlan-answers.md`  
   **Line:** 85 (also impacts baseline at lines 75–77)  
   **Current text:** `- Total: ~1568 bytes for 1500-byte customer MTU`  
   **Corrected text/value:** `- Total: ~1564 bytes on wire for 1500-byte customer MTU (1514-byte inner Ethernet frame + 50-byte VXLAN outer overhead)`  
   **Reasoning/source:** For 1500-byte customer MTU, the inner Ethernet frame is 1514 bytes (header + payload, no FCS in payload transport). VXLAN outer overhead is 50 bytes on wire (14 outer Ethernet + 20 IP + 8 UDP + 8 VXLAN). 1514 + 50 = 1564. The current value is +4 bytes high and conflicts with module math in `8.3-evpn-mpls-vs-vxlan.md` line 133.

2. **Severity:** Minor  
   **File:** `8.3-evpn-mpls-vs-vxlan.md`  
   **Line:** 517  
   **Current text:** `VXLAN adds 50 bytes — a 1500-byte customer frame becomes 1550 on the wire.`  
   **Corrected text/value:** Either:  
   - `...a 1500-byte customer IP payload becomes ~1550 on the wire.` **or**  
   - `...a 1514-byte customer Ethernet frame becomes ~1564 on the wire.`  
   **Reasoning/source:** Current sentence mixes units/baselines. 1550 is consistent with 1500-byte IP payload + 50-byte VXLAN wire overhead, not a 1500-byte Ethernet frame. Same file line 133 already distinguishes these baselines correctly.

3. **Severity:** Minor  
   **File:** `8.5-evpn-dci.md`  
   **Line:** 940  
   **Current text:** `60km apart on dark fiber, 0.3ms RTT`  
   **Corrected text/value:** `60km apart on dark fiber, ~0.6ms RTT` (or keep `~0.3ms one-way latency`)  
   **Reasoning/source:** Fiber propagation is ~5 microseconds/km one-way. 60 km ≈ 300 microseconds one-way (~0.3 ms), so RTT is roughly double: ~0.6 ms before device/switching overhead.

4. **Severity:** Minor  
   **File:** `8.5-evpn-dci-answers.md`  
   **Line:** 10 (inconsistent with lines 81 and 111–115)  
   **Current text:** `Four common EVPN DCI ... models are:` with 4-item list including RFC 9014 model  
   **Corrected text/value:** Make the section internally consistent by either:  
   - Expanding body/table to actually cover 4 models, **or**  
   - Changing opener to `Three common ... models` and removing the extra model from the numbered list.  
   **Reasoning/source:** The answer claims 4 models, but the detailed sections and summary table only present 3. This is a count/label mismatch that can mislead planning comparisons.

5. **Severity:** Minor  
   **File:** `8.4-evpn-multi-homing-answers.md`  
   **Line:** 27 and 30  
   **Current text:**  
   - `ESI values 0x00-0xFF are reserved; 0x00 means "single-homed"`  
   - `Type 0 (0x00): Single-homed (no multi-homing)`  
   **Corrected text/value:**  
   - `All-zero ESI (00:00:00:00:00:00:00:00:00:00) denotes single-homed.`  
   - `Type 0 is Arbitrary/Manual ESI (valid for multi-homing).`  
   **Reasoning/source:** Numeric/type mapping conflicts with module’s own `8.4-evpn-multi-homing.md` lines 66 and 74, where Type 0 is Arbitrary and all-zero ESI is single-homed special value. This is a mislabeled numeric default/type-value claim.
