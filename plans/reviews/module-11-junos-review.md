# Module 11 Junos CLI Validation Report

## Summary
- Files reviewed: 12
- Total findings: 12
- Critical: 4
- Minor: 8

---

## Detailed Findings

### Critical Findings

---

#### Finding 1
- **Severity:** critical
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** ~105–120 (Junos BGP-LS Configuration block)
- **Current text:**
```junos
mpls {
    traffic-engineering {
        database {
            import {
                igp-topology {
                    bgp-ls;
                }
            }
        }
    }
}
```
- **Correct text:** This entire `protocols mpls traffic-engineering database import igp-topology bgp-ls` hierarchy does not exist in Junos. It appears fabricated or confused with another vendor's syntax. In Junos, BGP-LS is functional once `family traffic-engineering unicast` is enabled under the BGP group and IS-IS traffic-engineering is enabled. No separate "import igp-topology" command is needed — the TED is populated automatically. Remove this stanza entirely or replace with a note explaining that no additional MPLS-level import config is needed on Junos.
- **Source:** Juniper TechLibrary — BGP-LS configuration for Junos MX/PTX series; `[edit protocols mpls]` hierarchy reference.

---

#### Finding 2
- **Severity:** critical
- **File:** `11.1-model-driven-networking.md`
- **Line:** ~213 (Verification & Monitoring — Show Commands table)
- **Current text:**
```
show system rollback 1 compare 0
```
- **Correct text:**
```
show system rollback compare 1 0
```
- **Source:** Junos CLI Reference — `show system rollback compare` syntax. The `compare` keyword comes immediately after `rollback`, before the rollback indices. The form `show system rollback <n> compare <n>` is invalid syntax and will produce a CLI error.

---

#### Finding 3
- **Severity:** critical
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** ~103 (Junos BGP-LS Configuration — IS-IS stanza)
- **Current text:**
```junos
isis {
    interface all;
    traffic-engineering {
        advertisement always;
    }
}
```
- **Correct text:**
```junos
isis {
    interface all;
    traffic-engineering;
}
```
- **Source:** Juniper TechLibrary — IS-IS Traffic Engineering configuration. The `advertisement always` knob exists under `protocols ospf traffic-engineering` in Junos, not under `protocols isis traffic-engineering`. For IS-IS, TE is enabled simply by including the `traffic-engineering` stanza — there is no `advertisement always` sub-option. This appears to have been copied from OSPF TE configuration.

---

#### Finding 4
- **Severity:** critical
- **File:** `11.2-streaming-telemetry.md`
- **Line:** ~183 (Junos Dial-Out Telemetry JTI — ROUTING-STATE sensor)
- **Current text:**
```junos
set services analytics sensor ROUTING-STATE server-name COLLECTOR-1
set services analytics sensor ROUTING-STATE export-name GRPC-EXPORT
set services analytics sensor ROUTING-STATE resource /junos/routing-state/
```
- **Correct text:** The JTI native resource path `/junos/routing-state/` does not appear to be a valid `services analytics` sensor resource. JTI native resources (used with `services analytics sensor`) are typically under `/junos/system/linecard/...` (e.g., `/junos/system/linecard/interface/`, `/junos/system/linecard/npu/utilization/`). Routing protocol state is available via gNMI dial-in with OpenConfig paths or Junos native YANG models (`junos-state-*`), not via the `services analytics` framework. Remove this sensor definition or replace with a valid JTI native resource path, or add a note that routing state requires gNMI dial-in.
- **Source:** Juniper TechLibrary — Junos Telemetry Interface (JTI) Sensor Resource Paths; `services analytics` configuration reference.

---

### Minor Findings

---

#### Finding 5
- **Severity:** minor
- **File:** `11.1-model-driven-networking.md`
- **Line:** ~237 (Key Knobs table — "Max NETCONF sessions" row, Junos Default column)
- **Current text:**
```
Junos Default: 16
```
- **Correct text:**
```
Junos Default: 75 (MX Series; varies by platform)
```
- **Source:** Juniper TechLibrary — `connection-limit` under `[edit system services netconf ssh]`. The default connection limit on MX Series is 75. The value 16 appears to be confused with a recommendation from the same table's "Recommended" column.

---

#### Finding 6
- **Severity:** minor
- **File:** `11.2-streaming-telemetry.md`
- **Line:** ~205–210 (Junos Dial-In gNMI configuration)
- **Current text:**
```junos
set system services extension-service request-response grpc clear-text port 32767
...
set system services extension-service request-response grpc ssl port 32767
```
- **Correct text:** Both `clear-text` and `ssl` are configured on the same port (32767), which is a conflict. These should use different ports, or only one transport type should be configured. Example fix:
```junos
!! Lab/dev only:
set system services extension-service request-response grpc clear-text port 32767
!! Production (use a different port or replace clear-text):
set system services extension-service request-response grpc ssl port 50051
set system services extension-service request-response grpc ssl local-certificate <cert-name>
```
- **Source:** Juniper TechLibrary — gRPC extension service configuration. Clear-text and SSL listeners require separate ports.

---

#### Finding 7
- **Severity:** minor
- **File:** `11.1-model-driven-networking.md`
- **Line:** ~175 (Junos Configuration — OpenConfig models)
- **Current text:**
```junos
set system schema openconfig
```
- **Correct text:** This is not a standard or widely documented Junos command. OpenConfig YANG models in Junos are typically either pre-bundled in the base image (Junos 18.3R1+) or installed via:
```
request system yang add package junos-openconfig
```
The enablement mechanism varies by Junos version. Consider replacing with a version-appropriate note or removing the specific `set` command.
- **Source:** Juniper TechLibrary — Installing and Managing YANG Packages on Junos; OpenConfig support documentation.

---

#### Finding 8
- **Severity:** minor
- **File:** `11.1-model-driven-networking.md`
- **Line:** ~210 (Verification — Show Commands table, second row)
- **Current text:**
```
| `show system processes extensive | match mgd` | RPC counts, errors |
```
- **Correct text:**
```
| `show system processes extensive | match mgd` | mgd process CPU/memory usage |
```
- **Source:** This command shows the mgd (management daemon) process resource statistics (CPU, memory, threads), not NETCONF RPC counts or errors. RPC statistics are not directly available via a single Junos show command; mgd process health is a reasonable proxy but the description is inaccurate.

---

#### Finding 9
- **Severity:** minor
- **File:** `11.2-streaming-telemetry.md`
- **Line:** ~111 (Vendor-Native Sensor Paths — Junos Native section)
- **Current text:**
```
# RPD (routing protocol daemon) memory
/junos/system/linecard/npu/memory
```
- **Correct text:**
```
# NPU (Network Processing Unit) memory on linecard
/junos/system/linecard/npu/memory
```
- **Source:** The path `/junos/system/linecard/npu/memory` refers to NPU memory on the linecard/PFE, not RPD (routing protocol daemon) memory. RPD runs on the Routing Engine (RE), not on a linecard NPU. The description should match the actual resource being monitored.

---

#### Finding 10
- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** ~264 (Paragon PCEP Client Config — `pcc-address` attribute)
- **Current text:**
```junos
pcc-address 10.0.0.1;
```
- **Correct text:** The attribute `pcc-address` inside a `protocols pcep pce <name>` stanza is not standard Junos PCEP syntax. The local PCC source address for the PCEP TCP session is typically derived from the router-id or configured at the `protocols pcep` level, not per-PCE. Verify against your Junos release; consider using `local-address` if available at the appropriate hierarchy level.
- **Source:** Juniper TechLibrary — PCEP configuration reference for MX/PTX.

---

#### Finding 11
- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** ~260 (Paragon PCEP Client Config — `destination-address` attribute)
- **Current text:**
```junos
destination-address 10.200.0.1;
```
- **Correct text:** Some Junos versions use `destination-ipv4-address` rather than `destination-address` for PCEP peer configuration. The attribute name varies by Junos release. Verify against your target platform version. Example:
```junos
destination-ipv4-address 10.200.0.1;
```
- **Source:** Juniper TechLibrary — `protocols pcep pce` hierarchy varies across Junos releases (19.x vs 21.x+ naming differences).

---

#### Finding 12
- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** ~276 (Paragon PCEP Client Config — `delegation-cleanup-timeout`)
- **Current text:**
```junos
delegation-cleanup-timeout 60;
```
- **Correct text:** The standard Junos attribute name is `delegation-cleanup-timer`, not `delegation-cleanup-timeout`. Example:
```junos
delegation-cleanup-timer 60;
```
- **Source:** Juniper TechLibrary — `[edit protocols pcep]` configuration reference. Junos uses `-timer` suffix for this knob, not `-timeout`.

---

## Notes

- Files with **no Junos CLI issues**: `11.1-model-driven-networking-theory.md`, `11.1-model-driven-networking-answers.md`, `11.2-streaming-telemetry-theory.md`, `11.3-sr-te-controller-integration-answers.md`, `11.4-cicd-network-config-answers.md`, `11.5-lab-gnmi-sr-te-automation.md` (IOS-XR focused lab), `11.5-lab-gnmi-sr-te-automation-answers.md`, `README.md`.
- IOS-XR configuration blocks, RFC citations, and non-Junos content were intentionally excluded from this review per task scope.
- Several Junos configurations carry appropriate caveats about version/platform variance already present in the source text, which is good practice.
