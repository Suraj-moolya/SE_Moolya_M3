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
When I Dclick Control project broswer project browser in project explorer as '<Containers>' 

Examples:
  | SlNo. | Containers |
  | 1     | Containers |
  


@TC_EPE_SWF_0000
@test0025
Scenario Outline: Generate from Containers pane and Click on Modal Dialogue Window
When I RClick on FBDSection in Container Section and select menu item as '<containerinstance>'
Then I Verify the Generation PopUp Window Message
When I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock 
And Verify Action message in notification pannel container dock in project explorer as '<container dock3>' 

Examples:

  | SlNo. | containerinstance  | Button | container dock3 |
  | 1     | System_1$$Generate | Yes    | Generate        |
  

@TC_EPE_SWF_0000
@test0000
Scenario Outline: Verify Generation Status
Then I Verify the facet generation status of all facets in Assignments Dock   
Examples:
  | SlNo. |
  | 1     |