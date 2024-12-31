Feature: 162 Check P2P with the controllers(M580 safety and non safety, M580 non safety and non safety) use both READ and WRITE functionalities

#Creating Variables in Refine Offline Window for Both Control Projects and Opening Peer to Peer

@TC_EPE_PE_CP_00
@test00
Scenario Outline: Double click on Elementary variables 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'

@Double_click_on_Elementary_variables_with_path_Programs-PROCESS$$Variables_&_FB_instances
Examples:
  | SlNo. | Project Browser RO1                                              |
  | 1     | Programs-PROCESS$$Variables & FB instances$$Elementary Variables |
  
@Double_click_on_Elementary_variables_with_path_Variables_&_FB_instances
Examples:
  | SlNo. | Project Browser RO1                            |
  | 1     | Variables & FB instances$$Elementary Variables |
  
@TC_EPE_PE_CP_00
@test00
Scenario Outline: enter variable and select HMI option under Data Editor window when the table is blank
When I Enter Variable name and select HMI option under Data Editor window
Examples:
  | SlNo. |
  | 1     |
  
  
@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Manage Peer to Peer
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I click modal dialog window project browser in project explorer as '<Button>'
Examples:
  | SlNo. | project browser1 | context menu        | Button |
  | 1     | M580_Safety      | Manage Peer to Peer | Next   |
  
  
  
   