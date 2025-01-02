Feature: 73 Configure Work Stations and it's services like CE, VJC and OFS

@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Create OFS,Control Service,Supervision in Workstation folder
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
Examples:
  | SlNo. | context menu           | project browser1       | button               |
  | 1     | Create OFS             | Create Service Handler | Workstation_1$$Close |
  | 2     | Create Control Service | Create Service Handler | Workstation_1$$Close |
  | 3     | Create Supervision     | Create Service Handler | Workstation_1$$Close |
  
  
@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Create OFS,Control Service,Supervision in Workstation_2 folder
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_2'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
Examples:
  | SlNo. | context menu           | project browser1       | button               |
  | 1     | Create OFS             | Create Service Handler | Workstation_1$$Close |
  | 2     | Create Control Service | Create Service Handler | Workstation_1$$Close |
  | 3     | Create Supervision     | Create Service Handler | Workstation_1$$Close |