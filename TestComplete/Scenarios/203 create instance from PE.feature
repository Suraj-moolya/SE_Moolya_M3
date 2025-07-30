Feature: 203 create instance from PE

@TC_EPE_PE_SWF_0036
@test0036
Scenario Outline: Create Instance from PE by Context menu
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock3>'
And I Search and select a template in the Template Section as '<template>'
And I Select button in the modal dialoge window as '<button>'
Then I verify that the template is available in the instance window as '<template>'
Examples:
  | SlNo. | assignmentsdock3              | template | button |
  | 1     | FBDSection_2$$Create Instance | $MotorGP | OK     |