Feature: 229 Run Citect runtime

@TC_EPE_RTNS_0002
@test0002
Scenario Outline: Run Citect runtime from Standalone Plant SCADA Run Citect runtime from Engineering Client
When I clicks on the '<sidebar>' icon from the vertical menubar
And I Enters the '<username>' and '<password>' in Aveva Plant Scada Window
And I clicks the '<button>' in the login dialog box
And I clicks the '<button>' in the Plant Scada popup dialog box
Then I verifies that the Master (startup) page for HD1080 res window is opened

Examples:
  | SlNo. | sidebar                | username | password   | button |
  | 1     | Run the active project | admin    | Moolya@123 | OK     |
  
  
@TC_EPE_RTNS_0003
@test0003
Scenario Outline: Run Citect runtime from Engineering Client
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I click modal dialog window project browser in project explorer as '<button1>' 
And I Enters the '<username>' and '<password>' in Aveva Plant Scada Window
And I clicks the '<button>' in the login dialog box
And I clicks the '<button>' in the popup dialog box
Then I verifies that the Master (startup) page for HD1080 res window is opened

Examples:
  | SlNo. | sidebar                | username | password   | button | MainToolBar                  | button1 |
  | 1     | Run the active project | admin    | Moolya@123 | OK     | Run Local Supervision Client | Yes     |