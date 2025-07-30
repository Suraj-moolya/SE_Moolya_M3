Feature: 184 Relink facets
@TC_EPE_SWF_0009
@test0009
Scenario Outline: Relink by Right Click Context menu
When I Right Click on the Facet in Assignments Section as "<facet_name1>" "<action>"
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
Examples:
  | SlNo. | facet_name1       | action | container dock3 |
  | 1     | MotorGP_1_MotorGP | Relink | Relink          |
  
  
  
@TC_EPE_SWF_0010
@test0010
Scenario Outline: Relink Facet Multiple
When I Right Click on the Facet in Assignments Section as "<facet_name1>", "<action>"
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
Examples:
  | SlNo. | facet_name1                                                    | action | container dock3 |
  | 1     | MotorGP_1_MotorGP$$AnalogInputGP_1_AInputGP$$ValveGP_1_ValveGP | Relink | Relink          |