Feature: 199 copy instances and paste in other container

@TC_EPE_SWF_0009
@test0009
Scenario Outline: Copy Instance by Context Menu
When I Click on FBDSection in Container Section '<FBDSection>'
And I Right Click on the Facet in Assignments Section as '<facet_name>'
And I Select context menu item as '<action>'
And I RClick on FBDSection in Container Section and select menu item as '<Param1>'
Then I verify Status updated in Generation Section as '<param2>'
Examples:
  | SlNo. | FBDSection   | facet_name           | action         | Param1                        | param2                              |
  | 1     | FBDSection_1 | SSMotorGP_15_MotorGP | Copy Instances | FBDSection_3$$Paste Instances | SSMotorGP_15_MotorGP$$Non Generated |
  
  
@TC_EPE_SWF_0009
@test0009
Scenario Outline: Copy Instance by Keyboard Action
When I Copy instances from FBDSection and paste in another FBDSection as '<Param1>'
Then I verify Status updated in Generation Section as '<param2>'
Examples:
  | SlNo. | Param1                                          | param2                |
  | 1     | FBDSection_2$$SSMotorGP_1_MotorGP$$FBDSection_4 | MotorGP$$NonGenerated |