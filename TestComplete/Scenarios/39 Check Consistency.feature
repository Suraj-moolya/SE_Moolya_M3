Feature: 39 Check Consistency

@TC_EPE_TE_0007
Scenario Outline: Check the consistency.
When I selected Save Refine Offline in refine offline
And I click modal dialog window project browser in project explorer as '<Button>'
And I selected Consistency Check in refine offline
Then Verify modal dialog window text Modal Dialog Window 1 in message box as 'Project is consistent.'
When I click modal dialog window project browser in project explorer as '<Button>'
Then Verify notification panel message Notification Pannel in message box as '<content>' 

Examples:
  | SlNo. | Button | content                       |
  | 1     | OK     | Check Consistency (Completed) |