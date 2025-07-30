Feature: 204 create 10 Sections with each Section having 10 assets in Containers

@TC_EPE_SWF_0001
@test0001
Scenario Outline: Creating 1 section and verify
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the new fbd section created

Examples:
  | SlNo. | assignmentsdock1                    | Button |
  | 1     | M580_Standalone$$Create FBD Section | OK     |
  

@TC_EPE_SWF_0002
@test0001
@WIP
Scenario Outline: Creating Multiple section and verify
When I Create multiple FBD Sections and Verify as '<assignmentsdock2>'

Examples:
  | SlNo. | assignmentsdock2                       |
  | 1     | M580_Standalone$$Create FBD Section$$8 |
  
  
@TC_EPE_SWF_000
@test0001
Scenario Outline: Creating 1 tag container and verify
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the new fbd section created

Examples:
  | SlNo. | assignmentsdock1                       | Button |
  | 1     | Supervision_Test$$Create Tag Container | OK     |
  