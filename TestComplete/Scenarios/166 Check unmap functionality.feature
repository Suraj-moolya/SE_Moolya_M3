Feature: 166 Check unmap functionality

@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Unmap P2P variable by context menu
When I Unmap variable in P2P communication configuration window by Context menu as '<identifier>'
Examples:
  | SlNo. | identifier          |
  | 1     | ValveGP_1_OPV       |
  | 2     | ValveGP_1_ClosePosV |
  | 3     | ValveGP_1_OpenPosV  |
  
  
@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Unmap P2P variable by keyboard action
When I Unmap variable in P2P communication configuration window by keyboard action as '<identifier2>'
Examples:
  | SlNo. | identifier2        |
  | 1     | ValveGp_1_OpenPosV |