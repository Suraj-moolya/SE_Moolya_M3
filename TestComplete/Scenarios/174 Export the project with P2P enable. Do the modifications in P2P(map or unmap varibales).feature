Feature: 174 Export the project with P2P enable. Do the modifications in P2P(map or unmap varibales)

@TC_EPE_P2P_0014
Scenario Outline: Export instance - Rclick instance, Export, save and cancel in export window
When I RClick control project browser project browser in project explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.xml'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Cancel'
Then I verify the file existance

Examples:
  | SlNo. | Application browser4 | Application browser5 |
  | 1     | System_1             | Export               |