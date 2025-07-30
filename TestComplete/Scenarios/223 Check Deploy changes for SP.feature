Feature: 223 Check Deploy changes for SP

@TC_EPE_SP_0017
@test0017
Scenario Outline: Creating
When I double-click on a '<identifier>' in the Containers tab
And I drag and drop the '<facetnames>' onto the edit page and click on the '<option>' option afterward 
And I click on the '<button1>' in Edit Page Properties 
And I click on the '<button2>' in Edit Page Properties
And I RClick control project browser project browser in project explorer as '<sp_project>'
And I Select context menu item EC project browser in project explorer as '<sp_project2>'
And I click modal dialog window project browser in project explorer as '<sp_project3>'
And I RClick control project browser project browser in project explorer as '<sp_project>'
And I Select context menu item EC project browser in project explorer as '<sp_project4>'
And I click modal dialog window project browser in project explorer as '<sp_project5>'
And I click modal dialog window project browser in project explorer as '<sp_project3>'


Examples:
  | SlNo. | identifier | facetnames | option | button1  | button2 | sp_project   | sp_project2 | sp_project3 | sp_project4          | sp_project5 |
  | 1     | Page_1     | MotorGP_1  | Motor  | Save All | Close   | Executable_1 | Build All   | OK          | Deploy Build Changes | Yes         |