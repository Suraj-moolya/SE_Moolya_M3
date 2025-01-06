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
  
@TC_EPE_PE_CP_00
@test00
Scenario Outline: Create Consecutive variable and select HMI option under Data Editor window when the table is blank
When I Enter Consecutive Variable name and select HMI option under Data Editor window and enter parameters as '<param>'
@Create_consecutivevariable_as_Moolya
Examples:
  | SlNo. | param                    |
  | 1     | ValveGP_1_OPV$$7$$Moolya |
  
@Create_consecutivevariable_as_SE
Examples:
  | SlNo. | param                |
  | 1     | ValveGP_1_OPV$$7$$SE |
  
@TC_EPE_PE_CP_00
@test00
Scenario Outline: Change Data type in Data Editor in Configure window Window
When I change Data type in Data Editor as '<param>'
@Change_SE1_bool_value_to_INT
Examples:
  | SlNo. | param    |
  | 1     | SE1$$INT |
  
@Change_SE2_bool_value_to_INT
Examples:
  | SlNo. | param    |
  | 1     | SE2$$INT |
  
@Change_Moolya1_bool_value_to_INT
Examples:
  | SlNo. | param        |
  | 1     | Moolya1$$INT |
  
@Change_Moolya2_bool_value_to_INT
Examples:
  | SlNo. | param        |
  | 1     | Moolya2$$INT |

  
  
@TC_EPE_PE_CP_0001
@test0001
Scenario Outline: Manage Peer to Peer
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I click modal dialog window project browser in project explorer as '<Button>'
Examples:
  | SlNo. | project browser1 | context menu        | Button |
  | 1     | M580_Standalone  | Manage Peer to Peer | Next   |
  

@TC_EPE_PE_CP_0039
@test0039
Scenario Outline: Drag remote variable to sorce variable PES_CONST_TRUE$$PES_CONST_TRUE with pop up
When I Drag and drop from remote varaibles to source variables in P2P as '<server>'
And I selected Rename Pop up Ok in message box
Examples:
  | SlNo. | server                         |
  | 1     | PES_CONST_TRUE$$PES_CONST_TRUE |
  
@TC_EPE_PE_CP_0039a
@test0039
Scenario Outline: Drag remote variable to sorce variable from Moolya to SE
When I Drag and drop from remote varaibles to source variables in P2P as '<server>'
Examples: 
  | SlNo. | server                                                   |
  | 2     | AnalogOutputGP_1_AOGP_AOSV$$AnalogOutputGP_1_AOGP_AOSV   |
  | 3     | AnalogInputGP_1_AInput_AISV$$AnalogInputGP_1_AInput_AISV |
  | 4     | MotorGP_1_RunV$$MotorGP_1_RunV                           |
  | 5     | ValveGP_1_OpenPosV$$ValveGP_1_OpenPosV                   |
  | 6     | Moolya1$$SE1                                             |
  | 7     | Moolya2$$SE2                                             |
  
  
@TC_EPE_PE_CP_0039b
@test0039
Scenario Outline: Drag remote variable to sorce variable from SE to Moolya
When I Drag and drop from remote varaibles to source variables in P2P as '<server>'
Examples: 
  | SlNo. | server                                                   |
  | 2     | AnalogOutputGP_1_AOGP_AOSV$$AnalogOutputGP_1_AOGP_AOSV   |
  | 3     | AnalogInputGP_1_AInput_AISV$$AnalogInputGP_1_AInput_AISV |
  | 4     | MotorGP_1_RunV$$MotorGP_1_RunV                           |
  | 5     | ValveGP_1_OpenPosV$$ValveGP_1_OpenPosV                   |
  | 6     | SE1$$Moolya1                                             |
  | 7     | SE2$$Moolya2                                             |

  
  
@TC_EPE_PE_CP_0039c
@test0039
Scenario Outline: Click on ok and verify P2P 
When I click modal dialog window project browser in project explorer as '<Button>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | Button | project browser2                              |
  | OK     | Manage Peer To Peer Communication (Completed) |
  
@TC_EPE_PE_CP_0039c
@test0039
Scenario Outline: Close tab 
When I Close the Tab by Clicking on Close in EC as '<tabname>'

@close_M580_Standalone2.ControlExecutable_1.Manage
Examples:
  | Button | tabname                                     |
  | OK     | M580_Standalone2.ControlExecutable_1.Manage |
  
@close_'M580_Standalone2'_Assignment_Editor
Examples:
  | Button | tabname                              |
  | OK     | 'M580_Standalone2' Assignment Editor |
  
@close_M580_Standalone.ControlExecutable_1.Manage
Examples:
  | Button | tabname                                    |
  | OK     | M580_Standalone.ControlExecutable_1.Manage |
  
@close_M580_Standalone_Assignment_Editor
Examples:
  | Button | tabname                             |
  | OK     | 'M580_Standalone' Assignment Editor |
  
@close_M580_Standalone
Examples:
  | Button | tabname                             |
  | OK     | M580_Standalone |


  
  
  
   