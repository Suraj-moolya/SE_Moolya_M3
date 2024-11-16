Feature: Export the project. Do some modifications in SP. Build the executable

@TC_EPE_EC_000
@test004
Scenario Outline: Export Supervision
When I RClick control project browser project browser in project explorer as '<Supervision>'
Then verify context menu items from Rclick menu items in system explorer
When I Select context menu item EC project browser in project explorer as '<context menu>'
And I click modal dialog window project browser in project explorer as '<Button>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.sbk'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Examples:
  | SlNo. | Supervision      | context menu | Button |
  | 1     | Supervision_Test | Export       | OK     |
  
  
@TC_EPE_EC_000
@test004
Scenario Outline: Import Supervision
When I RClick control project browser project browser in project explorer as '<Supervision>'
Then verify context menu items from Rclick menu items in system explorer
When I Select context menu item EC project browser in project explorer as '<context menu>'
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'
When I click modal dialog window project browser in project explorer as '<Button1>'
And I Click popup button object project browser in project explorer as '<project browser4>'
Examples:
  | SlNo. | Supervision | context menu | Button1 | Import3        | project browser4                      | Import4 | project browser3                             |
  | 1     | System_1    | Import       | OK      | ExpoSuper2.sbk | MessageBox$$modaldialogwindow1textbox$$OK | Open    | Obtaining project data to import (Completed) |