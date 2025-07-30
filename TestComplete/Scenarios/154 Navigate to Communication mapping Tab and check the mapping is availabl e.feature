Feature: 154 Navigate to Communication mapping Tab and check the mapping is available
@TC_EPE_PE_CP_0039
@test0039
Scenario Outline: Navigate to Communication mapping Tab, check the mapping is available and map
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser2>'
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser3>'
And I Click '<tabname>' on service mapping edittor window
And I Verify if the added device is available for mapping as '<server>'
And I Drag and drop the EPE Managed Device from devices to channels as '<server>'
And I Click on '<button>' in the dialog box
Examples:
  | SlNo. | tabname               | server      | button | button1 | contextmenu_item1 | contextmenu_item2  | Project Browser RO1 | content                                | projectBrowser3     | projectBrowser2 |
  | 1     | Communication Mapping | ETesysTHW_1 | OK     | Yes     | Build All         | Open Built Project | ETesysTHW_1         | Close Built Project Editor (Completed) | ControlExecutable_1 |  Executables    |


@TC_EPE_PE_CP_0039A
@test0039
Scenario Outline: Navigate to Communication mapping Tab, map
When I RClick control project browser project browser in project explorer as '<projectBrowser3>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item2>'
And I selected Tools button in menu bar
And I selected DTM Browser in menu bar
Then Verify Mapped DTM device present CE Project Browser RO in refine offline as '<Project Browser RO1>'
When I selected Close Refine Offline in refine offline
Then Verify notification panel message Notification Pannel in message box as '<content>'
Examples:
  | SlNo. | tabname               | server      | button | button1 | contextmenu_item1 | contextmenu_item2  | Project Browser RO1 | content                                | projectBrowser3     | projectBrowser2 |
  | 1     | Communication Mapping | ETesysTHW_1 | OK     | Yes     | Build All         | Open Built Project | ETesysTHW_1         | Close Built Project Editor (Completed) | ControlExecutable_1 |  Executables    |