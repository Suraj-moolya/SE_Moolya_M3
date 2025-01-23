Feature: 220 Create new page and assign some instances

@TC_EPE_SP_011
@test003
Scenario Outline: Create new page and assign some instances. Drag and Drop
When I drag instance drop container page SP instance dock in supervision project as '<instance dock1>'
And I Select value list view SVP instance dock in supervision project as '<instance dock2>'
And I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

Examples:
  | SlNo. | instance dock1 | instance dock2 |
  | 1     | MotorGP_1      | Motor          |

@TC_EPE_SP_011a
@test003
Scenario Outline: Create new page and assign some instances. save and close - create page
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
And I click modal dialog window project browser in project explorer as '<Button>'
And I click container dock in project explorer

Examples:
  | SlNo. | container dock1               | Button |
  | 1     | Supervision_Test$$Create Page | OK     |
  
  
@TC_EPE_SP_011b
@test003
Scenario Outline: Create new page and assign some instances. save and close - open page
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'

Examples:
  | SlNo. | container dock1 |
  | 1     | Page_1$$Edit    |