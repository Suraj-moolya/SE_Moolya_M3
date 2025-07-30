Feature: 199 copy instances and paste in other container

@TC_EPE_SWF_0009
@test0009
Scenario Outline: Copy Instance by Context Menu
When I Click on FBDSection in Container Section '<FBDSection>'
When I Right Click on the Facet in Assignments Section as "<facet_name>" "<action>"
And I RClick on FBDSection in Container Section and select menu item as '<Param1>'
Then I Verify the facet generation status of all facets in Assignments Dock 
Examples:
  | SlNo. | FBDSection | facet_name        | action         | Param1                        |
  | 1     | System_1   | MotorGP_1_MotorGP | Copy Instances | FBDSection_1$$Paste Instances |
  
  
@TC_EPE_SWF_0009
@test0009
Scenario Outline: Copy Instance by Keyboard Action
When I Copy instances from FBDSection and paste in another FBDSection as '<Param1>'
Then I verify Status updated in Generation Section as '<param2>'
Examples:
  | SlNo. | Param1                                      | param2                |
  | 1     | System_1$$SSMotorGP_1_MotorGP$$FBDSection_1 | MotorGP$$NonGenerated |