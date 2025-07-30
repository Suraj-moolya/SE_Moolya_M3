Feature: 92 Export only Devices into csv format


@TC_EPE_DTM_0020
@test0001
Scenario Outline: Export Topology from root folder 
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
When I Select button in the modal dialoge window as '<button name>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<format>'
And I Click on Button in TE Explorer Window Export in ec windows explorer as 'Save'
Then Verify notification panel message Notification Pannel in message box as '<Notification Panne>'

@Export_Topology
Examples:
  | SlNo. | Controllers | context menu | sub_context_menu | Notification Panne          | button name | format |
  | 1     | System_1    | Export       | Topology         | Export Topology (Completed) | OK          | .csv   |

@Export_Device
Examples:
  | SlNo. | Controllers | context menu | sub_context_menu | Notification Panne        | button name | format |
  | 1     | System_1    | Export       | Device           | Export Device (Completed) | OK          | .sbk   |