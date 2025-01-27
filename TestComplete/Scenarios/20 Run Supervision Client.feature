Feature: 20 Run Supervision Client

@TC_EPE_
Scenario Outline: Run Supervision Client
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel>'

Examples:
  | SlNo. | MainToolBar1                 | Notification Pannel                |
  | 1     | Run Local Supervision Client | Run Supervision Client (Completed) |

@TC_EPE_
Scenario Outline: Run Supervision Client - Enter the User name and Password 
When I Enters the '<username>' and '<password>' in Aveva Plant Scada Window
And I clicks the '<button>' in the login dialog box
And I clicks the '<button>' in the Plant Scada popup dialog box
Then I verifies that the Master (startup) page for HD1080 res window is opened

Examples:
  | SlNo. | username | password   | button |
  | 1     | viewonly1    | Moolya@123 | OK     |