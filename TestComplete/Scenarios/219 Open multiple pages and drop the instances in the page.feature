Feature: 219 Open multiple pages and drop the instances in the page

@TC_EPE_SP_011
@test003
Scenario Outline:  Open multiple pages and drop the instances in the page.
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
When I drag instance drop container page SP instance dock in supervision project as '<instance dock1>'
And I Select value list view SVP instance dock in supervision project as '<instance dock2>'
When I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

Examples:
  | SlNo. | instance dock1 | instance dock2 |container dock1 |
  | 1     | MotorGP_1      | Motor          |Page_1$$Edit|