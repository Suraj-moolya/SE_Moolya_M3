Feature: 148 Add instances to container and generate the section

@TC_EPE_PE_CP_0023
Scenario Outline: Generate from Containers pane 
When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
Then Verify Message from notification panel AE Notification Pannel in message box 
And I Verify the facet generation status of all facets in Assignments Dock 

Examples:
  | SlNo. | containerinstance  |
  | 1     | System_1$$Generate |
  

@TC_EPE_PE_CP_0024
Scenario Outline: Generate from Control Project Browser pane
When I RClick control project browser project browser in project explorer as '<containerinstance>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item>'
Then Verify Message from notification panel AE Notification Pannel in message box
And I Verify the facet generation status of all facets in Assignments Dock  

Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | ControlProject_1  | Generate         |