# Module 09 Math/Scaling Review

## Summary
- Files reviewed: 14
- Findings: 6
- Critical: 5
- Minor: 1

## Findings

### 1)
- Severity: critical
- File: `modules/09-transport/9.2-dwdm-fundamentals-answers.md`
- Line: 44
- Current text: "The Raman doesn't just add 2 dB — it adds 2 dB per amplifier site, which is multiplicative across the chain."
- Why it's wrong: This is a scaling error. In the same dB-domain OSNR approximation used in the answer, reducing amplifier NF by 2 dB improves end-to-end OSNR by about 2 dB total, not 2 dB multiplied by span count. Treating it as multiplicative overstates reach/margin dramatically.
- Corrected text: "A 2 dB effective NF improvement from Raman improves end-to-end OSNR by roughly 2 dB in this simplified model (not multiplicative per span), with additional real-world benefit depending on span design and nonlinear regime."
- Source/reasoning: From the stated model `OSNR(dB) ≈ P_launch - NF - 10·log10(N) + C`, NF enters once in dB form; `ΔNF = -2 dB` gives `ΔOSNR ≈ +2 dB`.

### 2)
- Severity: critical
- File: `modules/09-transport/9.4-packet-optical-integration-answers.md`
- Line: 121
- Current text: "...a two-week trend from 1e-5 to 5e-4 is a 50× increase — if it continues linearly in log space, you'll hit the FEC threshold in about 6-8 more weeks."
- Why it's wrong: The extrapolation is off by a large factor. A 50× increase in 2 weeks is very steep. From `5e-4` to 400ZR cFEC threshold (~`4.5e-3`) is only 9× more, which projects to about ~1.1 weeks at the same log-linear slope (not 6–8 weeks).
- Corrected text: "...a two-week trend from 1e-5 to 5e-4 is a 50× increase — if that log-linear trend continues, you'd likely hit the 400ZR cFEC threshold in roughly 1–2 weeks, not months."
- Source/reasoning: Log-slope method: `time_to_threshold = 2 weeks × log10(4.5e-3/5e-4) / log10(50) ≈ 1.12 weeks`.

### 3)
- Severity: critical
- File: `modules/09-transport/9.5-coherent-optics-answers.md`
- Line: 206
- Current text: "Set alarms at 50% and 75% of the FEC threshold. If threshold is 1.25e-2, alarm at 6e-3 (critical) and 3e-3 (warning)."
- Why it's wrong: The percentages are miscalculated and mislabeled. `3e-3` is only 24% of `1.25e-2`, not 75%. Also warning/critical ordering should increase with BER severity.
- Corrected text: "Set alarms at 50% and 75% of the FEC threshold. If threshold is 1.25e-2, use ~6.25e-3 (warning) and ~9.38e-3 (critical)."
- Source/reasoning: `0.5 × 1.25e-2 = 6.25e-3`; `0.75 × 1.25e-2 = 9.375e-3`.

### 4)
- Severity: critical
- File: `modules/09-transport/9.5-coherent-optics-theory.md`
- Line: 45
- Current text: "400G at 50 GBaud or 200G at 32 GBaud"
- Why it's wrong: `DP-16QAM` carries 8 bits/symbol. At 50 GBd, gross line rate is `50 × 8 = 400 Gb/s` before FEC. Net client payload after FEC overhead is below 400G, so this cannot represent a true 400G client rate.
- Corrected text: "400G typically uses ~60–64 GBaud DP-16QAM-class operation (implementation/FEC dependent); 200G can be carried at lower baud rates."
- Source/reasoning: Coherent payload math: `gross = baud × bits/symbol`; FEC overhead reduces net client rate.

### 5)
- Severity: critical
- File: `modules/09-transport/9.5-coherent-optics-theory.md`
- Line: 53
- Current text: "800G at ~65 GBaud"
- Why it's wrong: With `DP-64QAM` (12 bits/symbol), 65 GBd gives 780 Gb/s gross before FEC, so net payload is substantially below 800G. This is a direct arithmetic mismatch.
- Corrected text: "800G generally requires either higher single-carrier baud rates (roughly 100–130+ GBd, modulation/FEC dependent) or dual-carrier designs (e.g., 2×~65 GBd)."
- Source/reasoning: `65 × 12 = 780 Gb/s gross`; net after FEC is less than 780 Gb/s.

### 6)
- Severity: minor
- File: `modules/09-transport/9.2-dwdm-fundamentals-theory.md`
- Line: 102
- Current text: "400G DP-16QAM: ~22dB"
- Why it's wrong: This conflicts with other module content that uses ~18 dB for DP-16QAM planning thresholds, creating contradictory numeric guidance in the same module.
- Corrected text: "400G DP-16QAM: typically ~18–22 dB OSNR (depends on baud rate, FEC, implementation margin, and measurement assumptions)."
- Source/reasoning: Cross-file consistency check: `9.2-dwdm-fundamentals.md` line 158 uses ~18 dB; answer key scenario in `9.2-dwdm-fundamentals-answers.md` is built on 18 dB.
