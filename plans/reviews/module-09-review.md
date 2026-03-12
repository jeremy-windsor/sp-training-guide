# Module 09 Review Summary

- **Files reviewed**: 13
- **Files needing fixes**: 11
- **Clean files**: 2
- **Issue count**: 13 total
  - **Critical**: 8
  - **Minor**: 5
  - **Cosmetic**: 0

## Files needing fixes
- `9.2-dwdm-fundamentals.md`
- `9.2-dwdm-fundamentals-theory.md`
- `9.2-dwdm-fundamentals-answers.md`
- `9.3-otn-optical-transport-network.md`
- `9.3-otn-optical-transport-network-theory.md`
- `9.3-otn-optical-transport-network-answers.md`
- `9.4-packet-optical-integration.md`
- `9.4-packet-optical-integration-answers.md`
- `9.5-coherent-optics.md`
- `9.5-coherent-optics-theory.md`
- `9.5-coherent-optics-answers.md`

## Clean files
- `9.1-sp-transport-hierarchy.md`
- `9.1-sp-transport-hierarchy-answers.md`

### [9.2-dwdm-fundamentals.md] — C-band Channel Count Is Understated
- **Severity**: minor
- **Location**: Theory → The ITU-T Wavelength Grid → DWDM Frequency Grid
- **Current text**: "*The C-band covers roughly channels C17–C80 on the 50 GHz grid, yielding ~80 usable channels after guard bands.*"
- **Correction**: "ITU-T G.694.1 fixed-grid examples span the conventional C-band around 191.35-196.10 THz, which gives 96 nominal 50 GHz channels. If you want to teach a smaller vendor-specific usable subset, label it explicitly as a system-specific planning subset rather than the C-band total."
- **Source**: ITU-T G.694.1

### [9.2-dwdm-fundamentals.md] — OSNR Formula Omits Amplifier ASE/Gain Terms
- **Severity**: critical
- **Location**: Theory → Optical Amplifiers → EDFA — Erbium-Doped Fiber Amplifier
- **Current text**: "OSNR(dB) ≈ P_launch(dBm) - NF(dB) - 10·log10(N) + 58" and the worked example "= 43.5 dB" for 10 spans.
- **Correction**: "Do not present `OSNR ≈ P_launch - NF - 10·log10(N) + 58` as a general EDFA-chain formula. Accumulated ASE depends on amplifier output power/gain and reference bandwidth, not just launch power and span count. Rework the section using accumulated ASE at each amplifier output; a 10-span chain with +1 dBm/channel and 5.5 dB NF does not yield ~43.5 dB OSNR in a 0.1 nm reference bandwidth."
- **Source**: ITU-T G.661; ITU-T G.680

### [9.2-dwdm-fundamentals-theory.md] — EDFA OSNR Approximation Is Technically Incorrect
- **Severity**: critical
- **Location**: Core Mechanisms → 2. EDFA — Erbium-Doped Fiber Amplifier
- **Current text**: "OSNR ≈ 58 + P_in - NF - 10·log10(N) (in dB, per 0.1nm reference bandwidth)"
- **Correction**: "Replace this with an ASE-based explanation that includes amplifier gain/output power and accumulated noise. As written, the formula materially overstates end-of-line OSNR and is not suitable as a design rule."
- **Source**: ITU-T G.661; ITU-T G.680

### [9.2-dwdm-fundamentals-answers.md] — Worked OSNR Answer Overstates Margin by Using the Bad Formula
- **Severity**: critical
- **Location**: Question 1
- **Current text**: "OSNR ≈ 1 - 5.5 - 10·log₁₀(12) + 58 ≈ 42.71 dB" followed by "the link closes with comfortable margin."
- **Correction**: "Rework the answer using accumulated ASE from each amplifier rather than the simplified `+58` expression. The current calculation produces an unrealistically high OSNR for a 12-span route and therefore overstates the available margin and the Raman benefit."
- **Source**: ITU-T G.661; ITU-T G.680

### [9.3-otn-optical-transport-network-theory.md] — 100GbE to OPU4 Mapping Uses GMP, Not AMP
- **Severity**: minor
- **Location**: Core Mechanisms → 7. Client Signal Mapping
- **Current text**: "**IEEE 802.3 100GbE mapping into OPU4**: Direct mapping using 66B encoding. 100GbE's 103.125 Gbps line rate fits into OPU4's 104.794 Gbps payload capacity with AMP for rate adaptation."
- **Correction**: "For modern G.709 OTN, 100GbE into OPU4 should be taught as direct mapping using GMP. AMP/BMP are legacy mapping procedures and should not be presented as the normal 100GbE→OPU4 method."
- **Source**: ITU-T G.709

### [9.3-otn-optical-transport-network.md] — G.7042 Is Misidentified as the ODUflex Resize Standard
- **Severity**: minor
- **Location**: Quick Reference → Key Standards
- **Current text**: "- ITU-T G.7042: LCAS for ODUflex"
- **Correction**: "G.7042 defines LCAS for virtually concatenated signals, not ODUflex. ODUflex hitless resizing is covered by G.7044."
- **Source**: ITU-T G.7042; ITU-T G.7044

### [9.3-otn-optical-transport-network-answers.md] — OTN Protection Uses SNC Terminology, Not SNCP at ODU Layer
- **Severity**: minor
- **Location**: Question 4
- **Current text**: "OTN provides SNCP (1+1) and shared ring protection at the ODU level with <50ms switchover."
- **Correction**: "Use OTN terminology from G.873.x here: ODU protection is described with SNC/I and SNC/N behaviors (including linear and ring protection functions). `SNCP` is not the right generic term for ODU-layer protection in this answer."
- **Source**: ITU-T G.873.1; ITU-T G.873.2

### [9.4-packet-optical-integration.md] — 400ZR Reach Is Misstated as 120 km Unamplified
- **Severity**: critical
- **Location**: Theory → Model 4: IPoDWDM — The Pluggable Revolution
- **Current text**: "| Reach | ~120 km (unamplified), point-to-point |"
- **Correction**: "OIF 400ZR targets amplified point-to-point DWDM links with reaches of 120 km or less, plus unamplified single-wavelength links subject to an 11 dB loss budget. Do not describe 120 km as the unamplified reach."
- **Source**: OIF 400ZR Implementation Agreement

### [9.4-packet-optical-integration.md] — RFC 4258 Is the Wrong OTN/GMPLS Reference
- **Severity**: minor
- **Location**: Quick Reference → Key Standards & Specifications
- **Current text**: "| RFC 4258 | IETF | GMPLS OTN framework |"
- **Correction**: "RFC 4258 is about GMPLS routing requirements for ASON. For OTN-specific GMPLS control/framework references, use RFC 4328 and/or RFC 7062."
- **Source**: RFC 4258; RFC 4328; RFC 7062

### [9.4-packet-optical-integration-answers.md] — 400ZR Is Taught with oFEC Instead of cFEC
- **Severity**: critical
- **Location**: Question 3
- **Current text**: "At 5e-4 pre-FEC BER with a 400ZR oFEC threshold around 1.25e-2..."
- **Correction**: "400ZR uses OIF cFEC, not oFEC. If you want to discuss margin, anchor the explanation to 400ZR/cFEC behavior instead of OpenZR+/OpenROADM oFEC thresholds."
- **Source**: OIF 400ZR Implementation Agreement

### [9.5-coherent-optics.md] — 400ZR Reach Is Again Misstated as 120 km Unamplified
- **Severity**: critical
- **Location**: Theory → The 400ZR/ZR+ Ecosystem
- **Current text**: "- **Reach**: ~120 km (unamplified, point-to-point)"
- **Correction**: "For 400ZR, teach two cases: amplified point-to-point DWDM links up to 120 km, and unamplified single-wavelength links governed by an 11 dB loss budget. `120 km unamplified` is not the OIF application definition."
- **Source**: OIF 400ZR Implementation Agreement

### [9.5-coherent-optics-theory.md] — 400ZR Is Incorrectly Framed as OTN/FlexO on the Line Side
- **Severity**: critical
- **Location**: Protocol Interactions
- **Current text**: "**Coherent optics ↔ OTN**: OTN framing (OTU4, OTUCn) wraps the client signal before coherent modulation. In pluggable coherent (400ZR), OTN framing may be simplified or replaced with FlexO framing."
- **Correction**: "400ZR should be described as an OIF-defined 400GBASE-R PHY with OIF framing/cFEC. It is not an OTN/FlexO line-side mode. FlexO belongs to ITU-T beyond-100G OTN interfaces, not to 400ZR interoperability."
- **Source**: OIF 400ZR Implementation Agreement; ITU-T G.709.1; ITU-T G.709.3

### [9.5-coherent-optics-answers.md] — 400ZR FEC and Reach Are Misstated in Multiple Answers
- **Severity**: critical
- **Location**: Questions 1 and 4
- **Current text**: "400ZR uses DP-16QAM at ~60 GBaud with oFEC... At 95 km unamplified, you're near the edge of 400ZR's rated reach (~120 km max)." and "400ZR is specified for point-to-point links up to ~120 km unamplified..." and "higher coding gain than oFEC"
- **Correction**: "Keep the answer aligned with the OIF 400ZR IA: 400ZR uses cFEC, and the 120 km application is the amplified point-to-point DWDM case. The unamplified case is defined by loss budget, not `120 km unamplified`. Any FEC comparison in Q4 should compare CFP2-DCO/vendor SD-FEC against 400ZR cFEC, not against oFEC."
- **Source**: OIF 400ZR Implementation Agreement
