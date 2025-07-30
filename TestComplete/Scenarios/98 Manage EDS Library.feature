Feature: 98 Manage EDS Library

@TC_EPE_DTM_0004
Scenario Outline: Open context menu of Additional functions in DTM Browser
When I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window
And I selected '<option2>' from the submenu in the DTM Browser Modal Dialogue window


Examples:
  | SlNo. | prm             | option      | option2              |
  | 1     | BMEP58_ECPU_EXT | Device menu | Additional functions |
  

@TC_EPE_DTM_0005
Scenario Outline: Add EDS to library
When I click '<option3>' in the DTM Browser Modal Dialogue window
When I click the '<button>' button in the GSD Addition Window
And I click the '<button2>' button in the GSD Addition Window
#And I select '<folder>' in the GSD Browser
And I click the '<button3>' button in the GSD Addition Window
And I click the '<button>' button in the GSD Additions Window
And I click the '<button>' button in the GSD Additions Window
And I click the '<button5>' button in the GSD Addition Window


Examples:
  | SlNo. | button | button2 | button5 | button3 | folder            | button4 | option3 |
  | 1     | Next   | Browse  | Finish  | Select  | This PC/Documents | Close   | Add     |
  
  
@TC_EPE_DTM_0006
Scenario Outline: Remove EDS in library
When I click '<option3>' in the DTM Browser Modal Dialogue window
And I select the '<file_name>' in delete device library window
And I click '<button>' button in delete device library window
And I click '<button2>' button in delete device library popup window
And I click '<button3>' button in delete device library window

Examples:
  | SlNo. | option3 | file_name   | button | button2 | button3 |
  | 1     | Remove  | EDS Library | Delete | Yes     | OK   |
  
  
