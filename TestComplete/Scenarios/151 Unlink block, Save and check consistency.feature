Feature: Control Expert


@TC_EPE_PE_CP_0031
@test002
Scenario Outline: Open any section and unlink the block.
When I RClick on Block Refine Offline project browser in project explorer as '<project browser1>'
And I selected Unlock in refine offline
And I Unlock Dialog popup Unlock in refine offline as 'Yes'
And I Delete link Refine Offline Unlock in refine offline as 'ChOut'

Examples:
  | SlNo. | project browser1 |
  | 1     | AOUTPUTGP        |

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
Scenario Outline: Open any section and unlink the block. Save and check the consistency
When I selected Consistency Check in refine offline


Examples:
  | SlNo. |
  | 1     |

#Total No. of Test Cases : 4

@TC_EPE_PE_CP_0032c
@test005
Scenario Outline: Open any section and unlink the block. Save and check the consistency. 
When I Consistency Check Select All Consistency Check in refine offline
And I Click on export System1 Export Popup AE buttons Consistency Check in refine offline as 'Unlink'
Then Verify Message from notification panel AE Consistency Check in refine offline as 'Check Consistency (Completed)'


Examples:
  | SlNo. |
  | 1     |

#Total No. of Test Cases : 5


