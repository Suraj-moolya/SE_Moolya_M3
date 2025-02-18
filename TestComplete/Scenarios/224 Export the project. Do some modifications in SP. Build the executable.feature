Feature: 224 Export the project. Do some modifications in SP. Build the executable

@TC_EPE_SP_015
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
  
  
