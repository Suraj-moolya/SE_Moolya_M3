Feature: 232 Go to instance logic section and check the status on section(should open in online_run)

@TC_EPE_SP_0017
@test0017
Scenario Outline: Instance logic section viewer online must be opened from Operation Client
When I double-click on a '<identifier>' in the Instnace Information tab
And I double-click on a '<identifier2>' in the Instnace Information tab
Then I verify the statusbar tab in the Section Viewer window

Examples:
  | SlNo. | identifier | identifier2               |
  | 1     | Control    | System_1 (Workstation_1 ) |