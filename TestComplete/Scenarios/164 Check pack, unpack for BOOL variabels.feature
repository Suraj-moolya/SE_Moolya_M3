Feature: 164 Check pack, unpack for BOOL variabels

@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Unpack for BOOL variables
When I Uncheck the pack CheckBox in P2P Communication Configuration window for variable '<identifier>'
Examples:
  | SlNo. | identifier          |
  | 1     | ValveGP_1_OPV       |
  | 2     | ValveGP_1_ClosePosV |
  | 3     | ValveGP_1_OpenPosV  |
