Feature: 36 Check build & deploy changes in refine online

@TC_EPE_TE_0007
Scenario Outline: Build and deploy the changes
When I click on the '<icon>' in the Refine Online window
And I select '<button>' in New Device PopUp Window
And I click modal dialog window project browser in project explorer as '<button2>'

Examples:
  | SlNo. | icon                         | button | button2 |
  | 1     | Build and deploy the changes | Yes    | OK      |
  

@TC_EPE_TE_0008
Scenario Outline: Close Refine Online window
When I selected Close in refine offline
Then Verify notification panel message Notification Pannel in message box as '<content>'
When I Click button Message Window Modification popup in message box as '<button>'

Examples:
  | SlNo. | button | content |
  | 1     | No     | Close Refine Online Editor (Completed) |