Feature: 156 Navigate to varibale mapping editor and check the mapping is available

@TC_EPE_PE_CP_0041
@test0041
Scenario Outline: Navigate to Communication mapping Tab, check the mapping is available and map
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser7>'
And I Dclick Control project broswer project browser in project explorer as '<projectBrowser8>'
And I Dclick Control project broswer project browser in project explorer as '<projectBrowser9>'
And I Click '<tabname>' on service mapping edittor window
And I Right Click on the Communication Channels section of Communication Mapping Editor as '<server>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I Verify if the Network Variables are available in network variable window as '<identifiers>'
And I Drag and Drop variables from network variables to read from server pane as '<identifiers>'
Then I Verify all '<identifiers>' are mapped in read from server pane
Examples:
  | SlNo. | projectBrowser7  | projectBrowser8 | projectBrowser9     | tabname               | server                  | project browser2 | identifiers        |
  | 1     | ControlProject_2 | Executables     |ControlExecutable_1  | Communication Mapping | Standalone_Controller_2 | Map Variables    | guna$$guna2$$guna3 |