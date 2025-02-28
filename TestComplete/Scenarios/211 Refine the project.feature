Feature: 211 Refine the project

@TC_EPE_PE_CP_00
Scenario Outline: Right Click on supervision project and click on Refine
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
@RefineSupervision
Examples:
  | SlNo. | project browser1 | context menu | container dock3                 |
  | 1     | Supervision_Test | Refine       | Open Supervision Project Editor |
 
@RefineControl 
Examples:
  | SlNo. | project browser1 | context menu | container dock3             |
  | 1     | M580_Safety      | Refine       | Open Control Project Editor |
  
  
  
@TC_EPE_PE_CP_00
Scenario Outline: Close Refine window and yes on popup
When I selected Close Refine Offline in refine offline
And I click modal dialog window project browser in project explorer as '<Button>'
And I wait in seconds Refine online window in refine offline
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'

Examples:
  | SlNo. | Button | container dock3                  |
  | 1     | Yes    | Close Supervision Project Editor |
  
@TC_EPE_PE_CP_00
Scenario Outline: Close Refine window
When I selected Close Refine Offline in refine offline
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'

Examples:
  | SlNo. | Button | container dock3   |
  | 1     | Yes    | Close Page Editor |