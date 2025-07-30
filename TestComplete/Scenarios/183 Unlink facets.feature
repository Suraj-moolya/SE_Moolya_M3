Feature: 183 Unlink facets

@TC_EPE_SWF_0007
@test0007
Scenario Outline: Unlink Facet by Right Click Context menu
When I Right Click on the Facet in Assignments Section as "<facet_name1>" "<action>"
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
Examples:
  | SlNo. | facet_name1       | action | container dock3 |
  | 1     | MotorGP_1_MotorGP | Unlink | Unlink          |



@TC_EPE_SWF_0008
@test0008

Scenario Outline: Unlinking Multiple facets
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name1                                 | action | container dock3 |
  | 1     | AnalogInputGP_1_AInputGP$$ValveGP_1_ValveGP | Unlink | Unlink          |