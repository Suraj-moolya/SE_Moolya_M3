Feature: 144 Open control project

@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Create a Control Project for M580_Standalone
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer

@Create_standalone_Control_Project_1
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name |
  | 1     | System_1         | Create Control Project | M580       | M580_Standalone |
  
@Create_standalone_Control_Project_2
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name  |
  | 1     | System_1         | Create Control Project | M580       | M580_Standalone2 |
  
@Create_standalone_Control_Project_3
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name  |
  | 1     | System_1         | Create Control Project | M580       | M580_Standalone3 |
  
@Create_standalone_Control_Project_4
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name  |
  | 1     | System_1         | Create Control Project | M580       | M580_Standalone4 |
  
@TC_EPE_PE_CP_0003
@test0003
Scenario Outline: Create a Control Project for M580_HSBY_1
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name |
  | 1     | System_1         | Create Control Project | M580       | M580_HSBY_1     |
  
  
    
@TC_EPE_PE_CP_0005
@test0005
Scenario Outline: Create a Control Project for M580_Safety_Standalone
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer
Examples:
  | SlNo. | project browser1 | context menu           | controller  | controller_name        |
  | 1     | System_1         | Create Control Project | M580 Safety | M580_Safety_Standalone |
  
  
  
  
@TC_EPE_PE_CP_0007
@test0007
Scenario Outline: Rename Controller
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer
@Rename_controller_M580_Safety_Redundant
Examples:
  | SlNo. | project browser1 | context menu | controller_name       |
  | 1     | ControlProject_1 | Rename       | M580_Safety_Redundant |
  
@Rename_controller_M580_Safety 
Examples:
  | SlNo. | project browser1 | context menu | controller_name |
  | 1     | ControlProject_1 | Rename       | M580_Safety     |
  
  
@TC_EPE_PE_CP_0009
@test0009
Scenario Outline: Create a Control Project for M340 Controller
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name |
  | 1     | System_1         | Create Control Project | M340       | M340_Controller |
  
  
  
@TC_EPE_PE_CP_0011
@test0011
Scenario Outline: Create a Control Project for Quantum
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
Then I verifies that '<controller_name>' Created in Project Explorer
Examples:
  | SlNo. | project browser1 | context menu           | controller | controller_name    |
  | 1     | System_1         | Create Control Project | Quantum    | Quantum_Controller |
