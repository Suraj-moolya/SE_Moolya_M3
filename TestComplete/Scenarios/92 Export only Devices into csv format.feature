Feature: 92 Export only Devices into csv format


@TC_EPE_DTM_0020
@test0001
Scenario Outline: Export Topology from root folder 
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.sbk'
And I Click on Button in TE Explorer Window Export in ec windows explorer as 'Save'
Then Verify notification panel message Notification Pannel in message box as '<Notification Panne>'

Examples:
  | SlNo. | Controllers | context menu | sub_context_menu | Notification Panne         |
  | 1     | System_2    | Export       | Devices          | Export Devices (Completed) |