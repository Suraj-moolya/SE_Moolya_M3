Feature: AS 16 Add customized page style template in project settings and select the customized page as default


@EPE_TC_AS_16
Scenario Outline: Add customized page style template in project settings and select the customized page as default
When I RClick control project browser project browser in project explorer as '<Supervision>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select page templates sp settings button in project explorer
And I click add page template button in project explorer
When I Click popup button object Modal Dialog Window 1 in message box as '<Button2>'
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import>'
And I check new page template radio button in project explorer 
And I click modal dialog window Modal dialog window in message box as '<Button>'
When I Click popup button object Modal Dialog Window 1 in message box as '<Button1>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'

Examples:
  | SlNo. | Supervision      | context menu | Button | Import                | Button1                                    | message                                       | Button2                                   |
  | 1     | Supervision_Test | Settings     | OK     | New_Page_Template.zip | MessageBox$$modaldialogwindow1textbox$$Yes | Save Supervision Project Settings (Completed) | MessageBox$$modaldialogwindow1textbox$$OK |
