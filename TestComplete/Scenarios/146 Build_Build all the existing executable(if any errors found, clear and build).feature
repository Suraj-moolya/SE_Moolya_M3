Feature: 146 Build_Build all the existing executable(if any errors found, clear and build)


@TC_Build_All11
@test003
Scenario Outline: Build All from control executeable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'
Examples:
  | SlNo. | project browser1    | project browser2 | project browser3 |
  | 1     | ControlExecutable_1 | Build All        | OK               |




@TC_Generate_and_Build
@test004
Scenario Outline: Generate and Build from control executeable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1    | project browser2   | project browser3 |
  | 1     | ControlExecutable_1 | Generate and Build | OK               |



@TC_Build
@test005
Scenario Outline: Build from control executeable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1    | project browser2 | project browser3 |
  | 1     | ControlExecutable_1 | Build            | OK               |



@TC_build_disabled
@test007
Scenario Outline: Verify Build option disabled from control executable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
Then verify context menu item project browser in project explorer as '<menu_item>'

Examples:
  | SlNo. | project browser1    | menu_item    |
  | 1     | ControlExecutable_1 | Build$$False |

  
@TC_Generate_and_Build
@test004
Scenario Outline: Generate and Build from  executeable r-click
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1 | project browser2   | project browser3 |
  | 1     | Executable_1     | Generate and Build | OK               |
  
@TC_Build_All11
@test003
Scenario Outline: Build All from control executeable r-click click on yes and OK
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'
Then Verify Action message in notification pannel project browser in project explorer as '<message1>'
When I click modal dialog window project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1    | project browser2 | project browser3 | project browser4 | message1                                |
  | 1     | ControlExecutable_1 | Build All        | Yes              | OK               | BuildAll Control Executable (Completed) |
