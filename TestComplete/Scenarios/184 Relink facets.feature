Feature: 184 Relink facets
@TC_EPE_SWF_0009
@test0009
Scenario Outline: Relink by Right Click Context menu
When I Right Click on the Facet in Assignments Section as '<facet_name>' '<action>'
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name               | action | status    |
  | 1     | AnalogInputGP_1_AInputGP | Relink | Generated |
  
  
  
@TC_EPE_SWF_0010
@test0010
Scenario Outline: Relink Facet Multiple
When I Right Click on the Facet in Assignments Section as '<facet_name>' '<action>'
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name                                                     | action | status    |
  | 1     | MotorGP_1_MotorGP$$AnalogInputGP_1_AInputGP$$ValveGP_1_ValveGP | Relink | Generated |