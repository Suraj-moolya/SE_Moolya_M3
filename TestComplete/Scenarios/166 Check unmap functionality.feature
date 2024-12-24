Feature: 166 Check unmap functionality

@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Unmap P2P variable by context menu
When I Unmap variable in P2P communication configuration window by context menu as '<identifier>'
Examples:
  | SlNo. | identifier   |
  | 1     | ValveGp_1_OPV |
  
  
@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Unmap P2P variable by keyboard action
When I Unmap variable in P2P communication configuration window by keyboard action as '<identifier2>'
Examples:
  | SlNo. | identifier2        |
  | 1     | ValveGp_1_OpenPosV |