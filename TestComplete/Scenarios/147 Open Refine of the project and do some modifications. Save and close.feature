Feature: 147 Open Refine of the project and do some modifications. Save and close


@TC_EPE_PE_CP_0019
@test001
Scenario Outline: Open Refine from the Context Menu of Control Project in Control Project Browser pane
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
Then verify displayed Project Browser RO in refine offline

@Open_Refine_offline_of_M580_Standalone_from_Context_Menu
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | M580_Standalone  | Refine           |
  
@Open_Refine_offline_of_M580_Standalone2_from_Context_Menu
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | M580_Standalone2 | Refine           |
  
@Open_Refine_offline_of_M580_Standalone3_from_Context_Menu
Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | M580_Standalone3 | Refine           |



@TC_EPE_PE_CP_0020
@test002
Scenario Outline: Open Refine by Double Clicking on Control Project in Containers section
When I double click container PE container dock in project explorer as '<container dock1>'
Then verify displayed Refine online window in refine offline

Examples:
  | SlNo. | container dock1 | content |
  | 1     | FBDSection_2    | NA      |



@TC_EPE_PE_CP_0021
@test003
Scenario Outline: Open Refine from the Context Menu of the Control Project in Containers section
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
Then verify displayed Refine online window in refine offline

Examples:
  | SlNo. | container dock1      | content |
  | 1     | FBDSection_1$$Refine | NA      |



@TC_EPE_PE_CP_0022
@test004
Scenario Outline: Do modifications in Refine
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I Modifications of sections CE FBD SectionWindow in refine offline
#Then Verify modifications available in Refine Offline FBD SectionWindow in refine offline

Examples:
  | SlNo. | Project Browser RO1                        | content |
  | 1     | Programs$$Tasks$$MAST$$Logic$$FBDSection_1 | NA      |



@TC_EPE_PE_CP_0022A
@test004
Scenario Outline: Do modifications in Section
When I Modifications of sections CE FBD SectionWindow in refine offline
#Then Verify modifications available in Refine Offline FBD SectionWindow in refine offline

Examples:
  | SlNo. | content |
  | 1     | NA      |



@TC_EPE_PE_CP_0022Aa
@test005
Scenario Outline: Save and Close CE
When I wait in seconds Refine online window in refine offline
And I selected Save Refine Offline in refine offline
And I wait in seconds Refine online window in refine offline
And I selected Close Refine Offline in refine offline
Then Verify notification panel message Notification Pannel in message box as '<content>'

Examples:
  | SlNo. | content                            |
  | 1     | Close Configure Editor (Completed) |
  
@TC_EPE_PE_CP_0022Aa
@test005
Scenario Outline:Close CE
When I selected Close Refine Offline in refine offline
Then Verify notification panel message Notification Pannel in message box as '<content>'

Examples:
  | SlNo. | content                                |
  | 1     | Close Refine Online Editor (Completed) |
