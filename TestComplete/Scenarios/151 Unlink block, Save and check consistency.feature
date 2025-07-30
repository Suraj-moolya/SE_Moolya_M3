Feature: Control Expert


@TC_EPE_PE_CP_0031
@test002
Scenario Outline: Open any section and unlink the block.
When I RClick on Block Refine Offline project browser in project explorer as '<project browser1>'
And I selected Unlock in refine offline
#And I Unlock Dialog popup Unlock in refine offline as 'Yes'
And I select '<button>' in New Device PopUp Window
#And I Delete link Refine Offline Unlock in refine offline as 'ChOut'

@Unlock_for_AnalogOutPut
Examples:
  | SlNo. | project browser1 | button |
  | 1     | AOUTPUTGP        | Yes    |
  
@Unlock_for_MotorGp
Examples:
  | SlNo. | project browser1 | button |
  | 1     | MOTORGP          | Yes    |

#Total No. of Test Cases : 2

@TC_EPE_PE_CP_0032a
@test003
Scenario Outline: Open any section and unlink the block. Save and check the consistency.
When I selected Save Refine Offline in refine offline
Examples:
  | SlNo. |
  | 1     |

#Total No. of Test Cases : 3

@TC_EPE_PE_CP_0032b
@test004
Scenario Outline: Open any section and unlink the block. Consistency Check button in refine offline
When I selected Consistency Check in refine offline
Examples:
  | SlNo. |
  | 1     |

#Total No. of Test Cases : 4

@TC_EPE_PE_CP_0032c
@test005
Scenario Outline: Open any section and unlink the block. Click on select all and click on unlink button. 
When I Consistency Check Select All Consistency Check in refine offline
And I Click on export System1 Export Popup AE buttons Consistency Check in refine offline as 'Unlink'
Then Verify notification panel message Notification Pannel in message box as '<content>'
Examples:
  | SlNo. | content                       |
  | 1     | Check Consistency (Completed) |

#Total No. of Test Cases : 5


