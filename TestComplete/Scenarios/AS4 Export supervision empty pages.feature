Feature: AS4 Export supervision empty pages


@TC_EPE_PE_AS4
Scenario Outline: Export supervision empty pages
When I RClick control project browser project browser in project explorer as '<Supervision>'
Then verify context menu items from Rclick menu items in system explorer
When I Select context menu item EC project browser in project explorer as '<context menu>'
#And I click modal dialog window project browser in project explorer as '<Button>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.csv'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'


Examples:
  | SlNo. | Supervision   | context menu | Button |
  | 1     | Supervision_Test | Export Empty Pages      | OK     |