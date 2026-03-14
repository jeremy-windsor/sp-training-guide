# Module 11 Math/Scaling Review

## Summary
- Files reviewed: 12
- Findings: 2
- Critical: 0
- Minor: 2

## Files Reviewed
1. `README.md`
2. `11.1-model-driven-networking.md`
3. `11.1-model-driven-networking-theory.md`
4. `11.1-model-driven-networking-answers.md`
5. `11.2-streaming-telemetry.md`
6. `11.2-streaming-telemetry-theory.md`
7. `11.3-sr-te-controller-integration.md`
8. `11.3-sr-te-controller-integration-answers.md`
9. `11.4-cicd-network-config.md`
10. `11.4-cicd-network-config-answers.md`
11. `11.5-lab-gnmi-sr-te-automation.md`
12. `11.5-lab-gnmi-sr-te-automation-answers.md`

## Verified Correct (selected spot-checks)
- gNMI sample_interval 10,000,000,000 ns = 10s ✓
- IOS-XR MDT sample-interval 30000 ms = 30s ✓
- SNMP polling: 1,000 OIDs × 500 devices × 12/hr = 6M ✓
- SNMP per-second: 10,000 interfaces / 300s = 33.3/s; /30s = 333.3/s ✓
- Per-interface updates: 30s sample → 2/min → 120/hr ✓
- Per-PE: 120 × 200 interfaces = 24,000 updates/hr ✓
- Per-PE bytes: 24,000 × 800 bytes = 19.2 MB ≈ ~19 MB ✓
- Per-network updates: 24,000 × 500 = 12M ✓
- BGP on-change: 100 changes/hr × 500 bytes = 50 KB/hr ✓
- Optics: 2,000 × 60/hr × 600 bytes = 72 MB/hr ✓
- Total rounded to ~10 GB/hr → 240 GB/day → 7 TB/month ✓
- Cardinality: 500 × 200 × 20 = 2M series ✓
- Color ext community 0x00000064 = 100 decimal ✓
- PCEP port 4189, BGP-LS AFI 16388 / SAFI 71 ✓
- Confirmed commit defaults: IOS-XR 600s, Junos 10 min (same value, different units) ✓
- SRGB 16000–23999 = 8,000 labels, SRLB 15000–15999 = 1,000 labels ✓
- Ring 1 at 10% of 2,000 PEs = 200 ✓
- Q4 answer: 500 peers / 30s = ~17 updates/s; 500/5s = 100/s ✓
- Lab utilization: (350M × 8) / (30 × 1G) = 9.33% ✓
- Prometheus optics alert: -25 dBm × 100 = -2500 (0.01 dBm units) ✓
- Lab 11.5 answer Q5 dwell timer: 240s oscillation + 30s poll = 270s minimum ✓

## Findings

### Finding 1

- **Severity:** minor
- **File:** `11.2-streaming-telemetry.md`
- **Line:** Scale Considerations → "How Much Data?" → "Per network (500 PEs)" line
- **Current text:** `24,000 × 500 = 12M updates/hr ≈ 9.3 GB/hr for interface counters alone`
- **Why it's wrong:** The stated inputs produce a different result. 12M updates × 800 bytes/update = 9,600,000,000 bytes = 9.6 GB (decimal). Using the rounded ~19 MB/hr per PE: 19 MB × 500 = 9,500 MB = 9.5 GB. The 9.3 GB figure doesn't match either calculation. It appears to come from mixing decimal megabytes with binary gibibytes (9,500 MB ÷ 1,024 = 9.28 GiB ≈ 9.3 GiB), which is a unit inconsistency in a capacity planning estimate.
- **Corrected text:** `24,000 × 500 = 12M updates/hr ≈ 9.6 GB/hr for interface counters alone`
- **Source/reasoning:** Direct arithmetic: 12,000,000 × 800 = 9,600,000,000 bytes = 9.6 GB. Alternatively, 19.2 MB × 500 = 9,600 MB = 9.6 GB. The total section already rounds to ~10 GB/hr, which is consistent with 9.6 GB for counters + 72 MB for optics.

### Finding 2

- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration-answers.md`
- **Line:** Question 4 answer, "Why this scales" paragraph
- **Current text:** `Without ODN, a 400-PE network with 50 color intents = 400 × 50 = 20,000 pre-provisioned policies.`
- **Why it's wrong:** The arithmetic 400 × 50 = 20,000 is correct, but the model assumption is oversimplified. The formula implies one policy per PE per color (one destination per color). In typical SP full-mesh VPN scenarios, each PE needs policies to multiple destination PEs per color. The realistic pre-provisioning burden is much larger — for full mesh: 400 PEs × 399 destinations × 50 colors ≈ 8M policies network-wide, or ~19,950 per PE. The 20,000 total figure underestimates the scaling challenge that ODN solves by roughly three orders of magnitude for full-mesh cases. This could mislead a student about the severity of the scaling problem.
- **Corrected text:** `Without ODN, a 400-PE network with 50 color intents needs up to 400 × 399 × 50 ≈ 8M pre-provisioned policies in a full-mesh design (each PE needs a policy per destination per color). Even in partial-mesh, the count grows rapidly — each PE potentially requires thousands of policies.`
- **Source/reasoning:** SR-TE policy is identified by (color, endpoint). In a full-mesh L3VPN, each of 400 headend PEs may need a policy to each of the other 399 PEs for each of 50 colors. The current text collapses the per-destination dimension, producing a figure that understates the real scaling by ~400×.

## Overall Assessment

Module 11 is numerically clean. All protocol port numbers, RFC dates, label ranges, utilization formulas, cardinality estimates, dwell timer math, and alert threshold conversions check out correctly. The two findings are minor rounding/modeling issues in capacity planning illustrations — neither would cause a student to misconfigure a system or fail an exam question. No critical errors found.
