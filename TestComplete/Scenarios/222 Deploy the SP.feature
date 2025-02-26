Feature: 222 Deploy the SP

@TC_EPE_SP_0012
@test0012
Scenario Outline: Deploy SP without Sharing of OPSC
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'
And I click modal dialog window project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1 | project browser2     | project browser3 | project browser4 |
  | 1     | Executable_1     | Deploy Built Project | No               | OK               |
  
  
@TC_EPE_SP_0013
@test0013
Scenario Outline: Deploy SP with Sharing of OPSC
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I click modal dialog window project browser in project explorer as '<project browser3>'
And I Check Any of the files to be added in Deployment File Section as '<instance_names>'
And I click modal dialog window project browser in project explorer as '<button3>'
And I click modal dialog window project browser in project explorer as '<button3>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I Click on the '<button>' in Scada properties and Click '<drop_button>'
And I Click on the '<button2>' in Restore project window 
And I Select the '<file_name>' in Backup-Restore window
And I Click on the '<button3>' in Restore project window 
And I Click on the '<project browser3>' in Restore project window

Examples: 
  | SlNo. | project browser1 | project browser2     | project browser3 | instance_names | MainToolBar                     | button | drop_button | button2 | file_name                         | button3 |
  | 1     | Executable_1     | Deploy Built Project | Yes              | Includes       | Release Supervision Participant | Backup | Restore     | Browse  | Supervision_Test_Executable_1.ctz | OK      |