# Module 11 IOS-XR CLI Validation Report

## Summary
- Files reviewed: 12
- Total findings: 9
- Critical: 4
- Minor: 5

---

## Detailed Findings

### Finding 1 — `auto-route announce include-all` (SR-TE Policy Autoroute)

- **Severity:** critical
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** 655–656
- **Current text:**
  ```
  auto-route announce
   include-all
  ```
- **Correct text:**
  ```
  autoroute
   include ipv4 all
  ```
- **Source:** IOS-XR SR-TE policy `autoroute` is a single keyword (no hyphen), not the legacy MPLS-TE tunnel `autoroute announce` form. Under SR-TE policies, `include ipv4 all` (or `include ipv6 all`) is the correct sub-command — `include-all` is not a valid keyword. Entering `auto-route announce` under an SR policy would produce a CLI parse error. Reference: Cisco IOS-XR Segment Routing Configuration Guide, "Autoroute Include" section for SR-TE policies.

---

### Finding 2 — `bandwidth 10000` Commented as "10 Gbps"

- **Severity:** critical
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** 399
- **Current text:**
  ```
  bandwidth 10000             ! 10 Gbps minimum available BW
  ```
- **Correct text:**
  ```
  bandwidth 10000             ! 10 Mbps minimum available BW (value in Kbps)
  ```
  Or, if 10 Gbps is actually intended:
  ```
  bandwidth 10000000          ! 10 Gbps minimum available BW (value in Kbps)
  ```
- **Source:** IOS-XR SR-TE `constraints bandwidth` value is specified in **Kbps**. 10000 Kbps = 10 Mbps, not 10 Gbps. The same parameter is used correctly on line 666 with comment `! Initial BW reservation (Kbps)`. The ODN example's comment is off by a factor of 1,000. A student configuring `bandwidth 10000` expecting 10 Gbps enforcement would get 10 Mbps — a 1000× error.

---

### Finding 3 — `te-topology bgp-ls` (Non-Existent IOS-XR Command)

- **Severity:** critical
- **File:** `11.3-sr-te-controller-integration-answers.md`
- **Line:** 240
- **Current text:**
  ```
  segment-routing
    traffic-eng
      te-topology bgp-ls    ! Use BGP-LS TED for local computation
  ```
- **Correct text:** This command does not exist on IOS-XR. The recommended design (making headend PEs use BGP-LS for local CSPF fallback) is not achievable with a single CLI knob. The answer should describe that this requires:
  1. Configuring BGP-LS address-family on the headend PE to receive the global TED via BGP
  2. IOS-XR SR-TE headend inherently uses the IGP TED for local path computation — it does not natively consume BGP-LS for CSPF
  3. The practical solution is redundant PCE (already covered) or pre-configured explicit fallback segment lists, not a `te-topology` knob

  Remove the fabricated command and replace with a note that IOS-XR headend CSPF uses the IGP TED only; BGP-LS consumption is a PCE function, not a headend function.
- **Source:** IOS-XR `segment-routing traffic-eng` CLI hierarchy does not include a `te-topology` sub-command. Verified against IOS-XR 7.x/24.x SR-TE configuration guides. This command would produce a CLI error if entered.

---

### Finding 4 — `show mpls label tables detail` (Pluralization Error)

- **Severity:** critical
- **File:** `11.5-lab-gnmi-sr-te-automation.md`
- **Line:** 762
- **Current text:**
  ```
  show mpls label tables detail
  ```
- **Correct text:**
  ```
  show mpls label table detail
  ```
- **Source:** IOS-XR uses `show mpls label table` (singular). The plural `tables` is not recognized and would produce a parse error. This is in the "Useful Debug Commands" section of the lab, so a student following along would hit an immediate failure.

---

### Finding 5 — `show yang models` (Non-Standard IOS-XR Command)

- **Severity:** minor
- **File:** `11.1-model-driven-networking.md`
- **Line:** 106
- **Current text:**
  ```
  # IOS-XR: List YANG models
  show yang models | include bgp
  ```
- **Correct text:**
  ```
  # IOS-XR: List YANG models (command varies by release)
  # On IOS-XR 7.x, verify available YANG models via:
  show netconf-yang capabilities | include bgp
  # Or list schema files directly:
  run ls /pkg/yang/ | grep bgp
  ```
- **Source:** `show yang models` is not a universally available IOS-XR command. Some versions use `show netconf-yang capabilities` or expose models through the YANG library. A student on a standard IOS-XR 7.x image would likely get "Invalid input" at `yang`. Low impact since YANG model discovery is also covered via NETCONF capabilities exchange and `gnmic capabilities` elsewhere in the document.

---

### Finding 6 — `global-block` / `local-block` Shown as Sub-Containers

- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** 878–884
- **Current text:**
  ```
  segment-routing
   global-block
    16000 23999                ! SRGB: ...
   !
   local-block
    15000 15999                ! SRLB: ...
   !
  ```
- **Correct text:**
  ```
  segment-routing
   global-block 16000 23999   ! SRGB: for node/prefix SIDs (shared globally)
   local-block 15000 15999    ! SRLB: for adjacency SIDs
  !
  ```
- **Source:** On IOS-XR, `global-block` and `local-block` are single-line commands that take the range as inline arguments — they are not container modes with the range on a subordinate line. Entering `global-block` alone (without range values) would either produce an incomplete command error or enter a sub-mode that doesn't accept the range on the next line. The current representation may confuse a student about the CLI hierarchy.

---

### Finding 7 — `show isis distribute link-state` / `show ospf distribute link-state`

- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** 834–835
- **Current text:**
  ```
  ! On router, verify IGP is exporting to BGP-LS
  show isis distribute link-state
  show ospf distribute link-state
  ```
- **Correct text:**
  ```
  ! On router, verify IGP is exporting to BGP-LS
  ! Check IS-IS link-state distribution config:
  show running-config router isis | include distribute
  ! Verify BGP-LS is receiving topology from IGP:
  show bgp link-state link-state summary
  ```
- **Source:** `distribute link-state` is a *configuration* command under `router isis`, not a `show` command. IOS-XR does not have `show isis distribute link-state` or `show ospf distribute link-state` as executable show commands. To verify BGP-LS distribution, check the running config for the `distribute link-state` stanza, or verify received NLRIs via `show bgp link-state link-state`.

---

### Finding 8 — `show grpc trace xtc`

- **Severity:** minor
- **File:** `11.5-lab-gnmi-sr-te-automation.md`
- **Line:** 326, 758
- **Current text:**
  ```
  PE1# show grpc trace xtc
  ```
- **Correct text:**
  ```
  PE1# show grpc trace ems
  ```
  Or for XTC/SR-TE specific traces:
  ```
  PE1# show segment-routing traffic-eng forwarding
  ```
- **Source:** The gRPC trace subsystem on IOS-XR uses `show grpc trace ems` (Extensible Manageability Services) to show gRPC server-level traces. `xtc` is not a valid trace module under `show grpc trace`. XTC (the SR-TE process) has its own traces via `show xtc trace` or `show segment-routing traffic-eng` commands. Low impact — used in a verification context, and the student would simply get an "invalid input" error and try `show grpc trace ?` to discover the correct sub-command.

---

### Finding 9 — `show segment-routing traffic-eng policy color 100 name CLOUD-A-TO-EAST detail`

- **Severity:** minor
- **File:** `11.3-sr-te-controller-integration.md`
- **Line:** 342
- **Current text:**
  ```
  show segment-routing traffic-eng policy color 100 name CLOUD-A-TO-EAST detail
  ```
- **Correct text:**
  ```
  show segment-routing traffic-eng policy name CLOUD-A-TO-EAST detail
  ```
  or:
  ```
  show segment-routing traffic-eng policy color 100
  ```
- **Source:** On IOS-XR, `show segment-routing traffic-eng policy` accepts either `name <name>` or `color <color>` as filters, but combining both `color` and `name` in the same command may not be valid syntax depending on the IOS-XR release. The safer and more standard approach is to filter by one or the other. Low impact — the command may work on some versions but is non-standard.

---

## Files Reviewed (No Issues Found)

The following files were reviewed and contain no IOS-XR CLI syntax errors:

| File | Notes |
|------|-------|
| `README.md` | Module overview, no CLI content |
| `11.1-model-driven-networking-theory.md` | Protocol theory, minimal CLI — all correct |
| `11.1-model-driven-networking-answers.md` | Answer key — IOS-XR references are accurate |
| `11.2-streaming-telemetry.md` | MDT dial-out/dial-in config is correct; show commands are valid |
| `11.2-streaming-telemetry-theory.md` | Protocol theory, no CLI content |
| `11.4-cicd-network-config.md` | `commit confirmed 300` is correct (seconds); pipeline content is conceptual |
| `11.4-cicd-network-config-answers.md` | Conceptual answers, no IOS-XR CLI |
| `11.5-lab-gnmi-sr-te-automation-answers.md` | Conceptual answers, no additional CLI errors |

---

## Notes

- All NETCONF XML payloads reviewed (edit-config, lock/unlock, commit, validate) are structurally correct with proper namespaces.
- The lab Python code (11.5) correctly uses `Cisco-IOS-XR-segment-routing-ms-cfg` as the root namespace and `Cisco-IOS-XR-infra-xtc-agent-cfg` as the augmenting namespace — a common gotcha that the document handles well.
- gRPC/gNMI configuration blocks (`grpc port 57400`, `no-tls`, `max-request-per-user`, etc.) are syntactically correct across all files.
- SR-TE policy configurations (segment-lists, candidate-paths, binding-sid, color/endpoint) are correct in 11.5's lab topology.
- Telemetry sensor paths (`Cisco-IOS-XR-infra-xtc-agent-oper:xtc/policies/policy`, `openconfig-interfaces:interfaces/...`) are valid for IOS-XR 7.x.
