Feature: 154 Navigate to Communication mapping Tab and check the mapping is available

@TC_EPE_PE_CP_0039
@test0039
Scenario Outline: Navigate to Communication mapping Tab, check the mapping is available and map
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser1>'
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser2>'
And I Dclick Control project broswer project browser in project explorer as '<projectBrowser3>'
And I Click '<tabname>' on service mapping edittor window
And I Verify if the added device is available for mapping as '<server>'
And I Drag and drop the EPE Managed Device from devices to channels as '<server>'
And I Click on '<button>' in the dialog box
And I RClick control project browser project browser in project explorer as '<projectBrowser3>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item1>'
And I click modal dialog window project browser in project explorer as '<button>'
And I RClick control project browser project browser in project explorer as '<projectBrowser3>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item2>'
And I selected Tools button in menu bar
And I selected DTM Browser in menu bar
Then Verify Mapped DTM device present CE Project Browser RO in refine offline as '<Project Browser RO1>'
Examples:
  | SlNo. | projectBrowser1  | projectBrowser2 | projectBrowser3     | tabname               | server     | button | contextmenu_item1 | contextmenu_item2  | Project Browser RO1 |
  | 1     | ControlProject_1 | Executables     | ControlExecutable_1 | Communication Mapping | Advantys_1 | OK     | Build All         | Open Built Project | 192.168.0.1         |
  
