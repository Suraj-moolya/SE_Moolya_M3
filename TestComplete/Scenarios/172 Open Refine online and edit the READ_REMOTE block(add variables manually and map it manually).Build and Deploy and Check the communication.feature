Feature: 172 Open Refine online and edit the READ_REMOTE block(add variables manually and map it manually).Build and Deploy and Check the communication

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Unlock the Block in refine online 
When I RClick on Block Refine Offline project browser in project explorer as '<Block>'
And I selected Unlock in refine offline
When I Click on Yes in Modification Window
And I Click on Yes in Modification Window

Examples:
  | SlNo. | Block       |
  | 1     | READ_REMOTE |
  
@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Initialize Animation Table 
When I  Click on Variables from elementary variables tab to initiate animationtable editor window named as '<Variable>'
@Initialize_Animation_Table_for_varibale_SE1
Examples:
  | SlNo. | Variable |
  | 1     | SE1      |
  
@Initialize_Animation_Table_for_varibale_Moolya1  
Examples:
  | SlNo. | Variable |
  | 1     | Moolya1  |
  
@Initialize_Animation_Table_for_varibale_Moolya2  
Examples:
  | SlNo. | Variable |
  | 1     | Moolya2  |
  

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Click on Modification Button after Animation Initialization 
When I Click on Modification button after initialization of Animation Table
Examples:
  | SlNo. | Variable |
  | 1     | Var5     |
  
@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: change Data value in Animation Table 
When I change Data value in Data Editor as '<param>'
Examples:
  | SlNo. | param  |
  | 1     | 0$$162 |

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: change Data value in FBD Section 
When I change Data value in FBD Section as '<param>'
Examples:
  | SlNo. | param        |
  | 1     | L_VAR_6$$SE1 |
  
@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: verify variable in FBD section 
When I verify '<variable>' is reflected in FBD section
Examples:
  | SlNo. | variable |
  | 1     | 162      |
  
  

  
  
  


  
  
  