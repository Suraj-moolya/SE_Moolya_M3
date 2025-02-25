Feature: nn Refine Online

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Refine Online of Controllers
When I Right Click on nodes System Explorer Node in system explorer as '<nodes>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I click modal dialog window project browser in project explorer as '<Button>'
And I Click on OK button from Reconfirm Deploy Built Project Popup window
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

Examples:
  | SlNo. | context menu  | nodes           | Button | project browser1                      |
  | 1     | Refine Online | M580_Standalone | OK     | Open Refine Online Editor (Completed) |
  
  
@TC_EPE_WS_0006
@test001
Scenario Outline: Refine Online of Workstation
When I Right Click on nodes System Explorer Node in system explorer as '<Workstation>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
When I click modal dialog window project browser in project explorer as '<Button>'
And I Click on OK button from Reconfirm Deploy Built Project Popup window
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

Examples:
  | SlNo. | context menu | Workstation   | Button | project browser1                      | Topology Explorer Tree1 |
  | 1     | Control      | Workstation_1 | OK     | Open Refine Online Editor (Completed) | Refine Online           |
  
  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Navigate Through Mast section and verify communaction is happening
When I Navigate through project browser CE Project Browser RO in refine offline and verify Communication is happening as '<Project Browser RO1>'
@Navigate_to_Read_M580_Stand_P2P
Examples:
  | SlNo. | Project Browser RO1                                 |
  | 1     | Programs$$Tasks$$MAST$$Logic$$Read_M580_Stand_P2P_1 |
  

@Navigate_to_FBDSection_1_in_refine
Examples:
  | SlNo. | Project Browser RO1                        |
  | 1     | Programs$$Tasks$$MAST$$Logic$$FBDSection_1 | 
  
Scenario Outline:Refine online control Popup
When I Select button in the modal dialoge window as '<Button name>'
Examples:
  | SlNo. | Button name |
  | 1     | Yes         |


  

