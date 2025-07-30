Feature: 208 re assign facets

  
@TC_EPE_SWF_0030
@test0030
Scenario Outline: Reassign Folder After Generating
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name        | action   | status   |
  | 1     | MotorGP_1_MotorGP | Reassign | Assigned |
  
  
@TC_EPE_SWF_0031
@test0031
Scenario Outline: Reassingning Multiple Folders
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name                           | action   | status    |
  | 1     | MotorGP_1_MotorGP$$ValveGP_1_ValveGP | Reassign | Assingned |
