﻿Feature: nn Refine Online

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
  
  
  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Navigate Through Project Browser
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
@Double_click_on_PLC_Bus_EIO 
Examples:
  | SlNo. | Project Browser RO1                                  |
  | 1     | Programs$$Tasks$$MAST$$Logic$$Write_M580_Stand_P2P_1 |
  
