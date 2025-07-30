Feature: 225 Import the project and check the project is updated properly.

@TC_EPE_SP_016
@test004
Scenario Outline: Import Supervision
When I RClick control project browser project browser in project explorer as '<Supervision>'
Then verify context menu items from Rclick menu items in system explorer
When I Select context menu item EC project browser in project explorer as '<context menu>'
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'
When I click modal dialog window project browser in project explorer as '<Button1>'
And I Click popup button object project browser in project explorer as '<project browser4>'
Examples:
  | SlNo. | Supervision | context menu | Button1 | Import3        | project browser4                          | project browser3                             |
  | 1     | System_1    | Import       | OK      | ExpoSuper3.sbk | MessageBox$$modaldialogwindow1textbox$$OK | Obtaining project data to import (Completed) |
  