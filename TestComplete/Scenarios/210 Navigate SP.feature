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
Then Verify Action message in notification pannel container dock in project explorer as '<notification panel>'
When I RClick control project browser project browser in project explorer as '<project>'
And I Select context menu item EC project browser in project explorer as '<context menu 1>'
When I rename the ControlProject as '<controller_name>'
Examples:
  | SlNo. | project browser1 | context menu               | controller_name  | notification panel                     | project       | context menu 1 |
  | 1     | System_1         | Create Supervision Project | Supervision_Test | Create Supervision Project (Completed) | Supervision_1 | Rename         |
  
@TC_EPE_PE_CP_0002
@test0001
Scenario Outline: Expand Supervision Executables 
When I Expand control project browser PE project browser in project explorer as '<Pane_item>'

@Expand_Executables
Examples:
  | SlNo. | Pane_item   |
  | 1     | Executables |
  
@Expand_M580_safety
Examples:
  | SlNo. | Pane_item   |
  | 1     | M580_Safety |
  
  

@TC_EPE_PE_CP_00
Scenario Outline: Double Click on Executable sections
When I Dclick Control project broswer project browser in project explorer as '<Executables>' 

Examples:
  | SlNo. | Executables  |
  | 1     | Executable_1 |
  
  
@TC_EPE_PE_CP_00
Scenario Outline: Map the workstation and verify nic cards available for mapping
When I Map workstation available for respective service and engine for supervision project as '<Service_Engine>' 
Then Verify Action message in notification pannel container dock in project explorer as '<notification panel>'

@Map_service_engines_to_workstation_1
Examples:
  | SlNo. | Service_Engine                          | notification panel                 |
  | 1     | Alarm_1_P$$Not Assigned$$Workstation_2  | Map Service Executable (Completed) |
  | 2     | IOServer_1$$Not Assigned$$Workstation_2 | Map Service Executable (Completed) |
  | 3     | Report_1_P$$Not Assigned$$Workstation_2 | Map Service Executable (Completed) |

  
  



  
  
