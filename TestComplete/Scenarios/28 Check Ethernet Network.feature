Feature: Check Ethernet Network
  
@TC_EPE_TE_0002
@test0001
Scenario Outline: Check Ethernet Network
When I Double Click open the '<node>' in Topology Explorer
And I Double Click open the '<ethernet network>'
Then I Expand '<physical interface>' and Verify it is mapped to '<controller>'

Examples:
  | SlNo. | node     | ethernet network | physical interface     | controller      |
  | 1     | Networks | Lab_Network      | PhysicalInterfaceLink2 | M580_Standalone |
  
  