Feature: Eco Struxure Process Expert1

@TC_EPE_SWF_0005
@test001
Scenario Outline: Delete the Section from Context menu
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
And I click modal dialog window container dock in project explorer as '<container dock2>'
Then Verify Section Deleted in Control Project containers container dock in project explorer as '<container dock3>'

Examples:
  | SlNo. | container dock1    | container dock2 | container dock3 |
  | 1     | FBDSection$$Delete | Yes             | FBDSection      |


#Total No. of Test Cases :1

@TC_EPE_SWF_0006
@test002
Scenario Outline: Delete the Section by Keyboard actions
When I Delete Section in ControlProject by using Keyboard actions PE container dock in project explorer as '<container dock1>'
And I click modal dialog window container dock in project explorer as '<container dock2>'
Then Verify Section Deleted in Control Project containers container dock in project explorer as '<container dock3>'

Examples:
  | SlNo. | container dock1 | container dock2 | container dock3 |
  | 1     | FBDSection      | Yes             | FBDSection      |


#Total No. of Test Cases :2

