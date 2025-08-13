Feature: XX Workstation Settings 

@test0002b
Scenario Outline: Close Workstation  in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<nodes>' in Topology Explorer is Expanded
@Close_Workstation_1_in_Topology_Explorer
Examples:
  | SlNo. | button               | nodes         |
  | 1     | Workstation_1$$Close | Workstation_1 |
  
@Close_Workstation_2_in_Topology_Explorer
Examples:
  | SlNo. | button               | nodes         |
  | 1     | Workstation_2$$Close | Workstation_1 |
  
  

@TC_EPE_TE_CS_000
@test000
Scenario Outline: Change safety settings of Workstation to Disable
When I Right Click on nodes System Explorer Node in system explorer as '<Workstation>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
When I Select button in the modal dialoge window as '<Button name>'
@Change_safety_settings_of_Workstation_1_to_Disable
Examples:
  | SlNo. | context menu | options          | Button name | Workstation   |
  | 1     | Properties   | Simulator$$False | Yes         | Workstation_1 |
  
@Change_safety_settings_of_Workstation_2_to_Disable
Examples:
  | SlNo. | context menu | options          | Button name | Workstation   |
  | 1     | Properties   | Simulator$$False | Yes         | Workstation_2 |
  
  
@test0002b
Scenario Outline: Open Workstation_1  in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded

Examples:
  | SlNo. | button              | FolderName  |
  | 1     | Workstation_1$$Open | Workstation |
  
@test0002b
Scenario Outline: Open Workstation_2  in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded

Examples:
  | SlNo. | button              | FolderName  |
  | 1     | Workstation_2$$Open | Workstation |