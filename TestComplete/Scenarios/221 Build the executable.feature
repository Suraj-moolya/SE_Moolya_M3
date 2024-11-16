Feature: 221 Build the executable

@TC_EPE_SP_0011
@test0011
Scenario Outline: Creating a Safety M580 Control Project
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'
Then Verify Action message in notification pannel container dock in project explorer as '<message>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3 | message  |
  | 1     | Executable_1     | Build All        | OK               | BuildAll |