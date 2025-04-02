Feature: 205 delete 2 Section

@TC_EPE_SWF_0038
Scenario Outline: Delete two Sections
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
And I click modal dialog window container dock in project explorer as '<container dock2>'
Then Verify Section Deleted in Control Project containers container dock in project explorer as '<container dock3>'

Examples:
  | SlNo. | container dock1      | container dock2 | container dock3 |
  | 1     | FBDSection_3$$Delete | Yes             | FBDSection_3    |
  | 2     | FBDSection_7$$Delete | Yes             | FBDSection_7    |

