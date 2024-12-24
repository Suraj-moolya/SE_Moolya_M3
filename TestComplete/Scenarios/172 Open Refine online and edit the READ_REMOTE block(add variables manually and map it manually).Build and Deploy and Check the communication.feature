Feature: 172 Open Refine online and edit the READ_REMOTE block(add variables manually and map it manually).Build and Deploy and Check the communication

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Unlock the Block in refine online 
When I RClick on Block Refine Offline project browser in project explorer as '<Block>'
And I selected Unlock in refine offline
When I Click on Yes in Modification Window
And I Click on Yes in Modification Window

Examples:
  | SlNo. | context menu  | Block        |
  | 1     | Refine Online | WRITE_REMOTE |
  
@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Initialize Animation Table 
When I Right Click on Variables from elementary variables tab named as '<Variable>'
And I select Initialze Animation Table in refine offline

Examples:
  | SlNo. | Variable | Block        |
  | 1     | Var5     | WRITE_REMOTE |
  

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Click on Modification Button after Animation Initialization 
When I Click on Modification button after initialization of Animation Table
And I select Initialze Animation Table in refine offline

Examples:
  | SlNo. | Variable | Block        |
  | 1     | Var5     | WRITE_REMOTE |
  
  


  
  
  