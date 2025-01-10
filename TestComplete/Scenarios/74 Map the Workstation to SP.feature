Feature: 74 Map the Workstation to SP



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