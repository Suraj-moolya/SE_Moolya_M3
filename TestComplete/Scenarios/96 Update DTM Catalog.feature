Feature: 96 Update DTM Catalog

@TC_EPE_DTM_0001
Scenario Outline: Installing the DTM Files,updating and checking it in refinement window in Topology Window
When I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window
And I Select '<tabname>' in hardware catalog window
And I double click on '<property>' in hardware catalog window
And I double click on '<property1>' in hardware catalog window
And I Verify '<smp>' in Hardware Catalog Window
And I click Update button on hardware catalog window
And I select '<button3>' on control expert popub window

Examples:
  | SlNo. | menu  | menu_item        | button3 | property  | property1     | smp      | tabname     |
  | 1     | Tools | Hardware Catalog | Yes     | Protocols | Profibus DPV1 | PRM Comm | DTM catalog |
