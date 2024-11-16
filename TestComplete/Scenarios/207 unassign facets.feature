Feature: 207 unassign facets

@TC_EPE_SWF_0025
@test0025
Scenario Outline: Trying to Unassign Before Generating
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify '<facet_name>' disappered in assignments
Examples:
  | SlNo. | facet_name       | action   |
  | 1     | ValveGP_1_ValveGP | Unassign |
  

@TC_EPE_SWF_0026
@test0026
Scenario Outline: Trying to Unassign After Generating
When I Right Click on the Facet in Assignments Section as "<facet_name1>" "<action>"
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
Examples:
  | SlNo. | facet_name1       | action   | container dock3 |
  | 1     | MotorGP_1_MotorGP | Unassign | Unassign        |
  
  
  
@TC_EPE_SWF_0027
@test0027
Scenario Outline: Trying to Unassign Multiple Facets Before Generating
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify '<facet_name>' disappered in assignments
Examples:
  | SlNo. | facet_name1                          | action   |
  | 1     | MotorGP_1_MotorGP$$ValveGP_1_ValveGP | Unassign |
  
@TC_EPE_SWF_0028
@test0028
Scenario Outline: Unassign Multiple Facet after Generating
When I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'
Examples:
  | SlNo. | facet_name                           | action   | container dock3 |
  | 1     | MotorGP_1_MotorGP$$ValveGP_1_ValveGP | Unassign | Unassign        |
  
  



