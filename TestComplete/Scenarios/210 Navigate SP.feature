Feature: 210 Navigate SP

@TC_EPE_SWF_0000
@test0030
Scenario Outline: Navigate SP
When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
Then I Verify Navigation tab in project explorer

Examples:
  | SlNo. | CP_SP_Tab          |
  | 1     | SupervisionProject |
  

@TC_EPE_SWF_0000
@test0030
Scenario Outline: Navigate CP
When I Navigate to '<CP_SP_Tab>' tab in project explorer tab 
Then I Verify Navigation tab in project explorer

Examples:
  | SlNo. | CP_SP_Tab            |
  | 1     | UnityProjectTreePane |
  
  
@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Create a Supervision Project 
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I rename the ControlProject as '<controller_name>'
Examples:
  | SlNo. | project browser1 | context menu               | controller_name  |
  | 1     | System_1         | Create Supervision Project | Supervision_Test |
  
@TC_EPE_PE_CP_0002
@test0001
Scenario Outline: Expand Supervision Executables 
When I Expand control project browser PE project browser in project explorer as '<Pane_item>'
Examples:
  | SlNo. | Pane_item   |
  | 1     | Executables |
  

@TC_EPE_PE_CP_00
Scenario Outline: Double Click on Executable sections
When I Dclick Control project broswer project browser in project explorer as '<Executables>' 

Examples:
  | SlNo. | Executables  |
  | 1     | Executable_1 |
  
  
@TC_EPE_PE_CP_00
Scenario Outline: Map the workstation and verify nic cards available for mapping
When I Map workstation available for respective service and engine for supervision project as '<Service_Engine>' 

Examples:
  | SlNo. | Service_Engine            |
  | 1     | Alarm_1_P$$Workstation_1  |
  | 2     | IOServer_1$$Workstation_1 |
  | 3     | Report_1_P$$Workstation_1 |
  
  



  
  
