Feature: 148 Add instances to container and generate the section
@TC_EPE_PE_CP_0023
Scenario Outline: Generate from Containers pane
When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
Then I Verify the facet generation status of all facets in Assignments Dock
And Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
Examples:
  | SlNo. | containerinstance  | container dock3 |
  | 1     | System_1$$Generate | Generate        |
@TC_EPE_PE_CP_0024
Scenario Outline: Generate from Control Project Browser pane
When I RClick control project browser project browser in project explorer as '<containerinstance>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item>'
Then Verify Message from notification panel AE Notification Pannel in message box
And I Verify the facet generation status of all facets in Assignments Dock
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | ControlProject_1  | Generate         |

@TC_EPE_PE_CP_00
Scenario Outline: Double Click on Container sections
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser1>'
@Double_Click_Containers
Examples:
  | SlNo. | projectBrowser1 |
  | 1     | Containers      |
@Double_Click_System
Examples:
  | SlNo. | projectBrowser1 |
  | 1     | System_1        |
@DoubleClick_M580_Standalone_1_Checkes_weather_expanded_and_expands
Examples:
  | SlNo. | projectBrowser1 |
  | 1     | M580_Standalone |
@DoubleClick_M580_Standalone_2_Checkes_weather_expanded_and_expands
Examples:
  | SlNo. | projectBrowser1  |
  | 1     | M580_Standalone2 |
@DoubleClick_M580_Standalone_3_Checkes_weather_expanded_and_expands
Examples:
  | SlNo. | projectBrowser1  |
  | 1     | M580_Standalone3 |
@DoubleClick_ControlExecutable_1_Checkes_weather_expanded_and_expands
Examples:
  | SlNo. | projectBrowser1     |
  | 1     | ControlExecutable_1 |
@TC_EPE_PE_CP_0024
Scenario Outline: Right Click Controllers and select Expand All,Collapse All
When I RClick control project browser project browser in project explorer as '<containerinstance>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item>'
@Right_Click_M580_Standalone_ExpandAll
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | M580_Standalone   | Expand All       |
@Right_Click_ControlProject_1_ExpandAll
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | ControlProject_1  | Expand All       |
@Right_Click_M580_Standalone_Collapse_All
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | M580_Standalone   | Collapse All     |
@Right_Click_M580_Standalone2_ExpandAll
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | M580_Standalone2  | Expand All       |
@Right_Click_M580_Standalone2_Collapse_All
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | M580_Standalone2  | Collapse All     |
@Right_Click_M580_Standalone3_ExpandAll
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | M580_Standalone3  | Expand All       |
@Right_Click_System_Collapse_All
Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | System_1   | Collapse All     |
@TC_EPE_SWF_0000
@test0025
Scenario Outline: Generate from Containers pane and Click on Modal Dialogue Window
When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
#Then I Verify the Generation PopUp Window Message
When I click modal dialog window project browser in project explorer as '<Button>'
#Then I Verify the facet generation status of all facets in Assignments Dock
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
@System_generate
Examples:
  | SlNo. | containerinstance  | Button | container dock3 |
  | 1     | System_1$$Generate | Yes    | Generate        |
@M580Standalone_generate
Examples:
  | SlNo. | containerinstance        | Button | container dock3 |
  | 1     | M580_Standalone$$Generate | Yes    | Generate        |
@TC_EPE_SWF_0000
@test0000
Scenario Outline: Verify Generation Status
Then I Verify the facet generation status of all facets in Assignments Dock
Examples:
  | SlNo. |
  | 1     |
  
@TC_EPE_SWF_0000
@test0025
Scenario Outline: Generate from Containers pane and Click on Modal Dialogue Windowss
When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
@M580Standalone_generate_without_popop
Examples:
  | SlNo. | containerinstance         | container dock3 |
  | 1     | M580_Standalone$$Generate | Generate        |