Feature: 75 Create Work stations for client and add multiple NIC's and configure the IP, logical network

@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Create Control Service,Supervision in Workstation folder
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
Examples:
  | SlNo. | context menu           | project browser1       | button               |
  | 1     | Create Control Service | Create Service Handler | Workstation_1$$Close |
  
  
@TC_EPE_PE_CP_0004
@test001
Scenario Outline: Open Service Mapping Editor of M580_Redundant and map to Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                    |
  | 1     | M580_Redundant   | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Standalone |
