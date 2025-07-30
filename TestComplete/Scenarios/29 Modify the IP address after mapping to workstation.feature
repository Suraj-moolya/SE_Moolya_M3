Feature: 29 Modify the IP address after mapping to workstation

@TC_EPE_TE_0003
@test002
Scenario Outline: Modify the IP address after mapping to workstation
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree4>'
When I Close the Tab by Clicking on Close as '<identifier>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3  | Topology Explorer Tree4 | identifier |
  | 1     | NIC                     | NIC Parameters          | IPAddress$$192.168.11.64 | SubnetMask$$255.255.0.0 | NIC        |


@TC_EPE_TE_0003a
@test008
Scenario Outline: To verify not built state
When I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
Then Verify build state of control executable PE project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                                |
  | 1     | ControlProject_1 | Executables      | ControlProject_1$$ControlExecutable_1$$OutOfDate |