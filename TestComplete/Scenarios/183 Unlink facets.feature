Feature: 183 Unlink facets

@TC_EPE_SWF_0007
@test0007
Scenario Outline: Unlink Facet by Right Click Context menu
When I Right Click on the Facet in Assignments Section as '<facet_name>' '<action>'
Then I verify Unlinked Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name        | action | status   |
  | 1     | MotorGP_1_MotorGP | Unlink | Unlinked |


@TC_EPE_SWF_0008
@test0008
Scenario Outline: Unlinking Multiple facets2
When I Right Click on the Facet in Assignments Section as '<facet_name>' '<action>'
Then I verify Unlinked Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name                                                     | action | status   |
  | 1     | MotorGP_1_MotorGP$$AnalogInputGP_1_AInputGP$$ValveGP_1_ValveGP | Unlink | Unlinked |