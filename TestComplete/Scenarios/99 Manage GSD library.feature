Feature: 99 Manage GSD library

@TC_EPE_DTM_0009
Scenario Outline: Open PRM Configuration window and open context menu of Additional functions
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window
And I selected '<option2>' from the submenu in the DTM Browser Modal Dialogue window
And I click '<option3>' in the DTM Browser Modal Dialogue window

Examples:
  | SlNo. | node_name | action    | prm             | option      | option2              | option3 |
  | 1     | PRM_1     | Configure | PRM_Master_0001 | Device menu | Additional functions | Add     |
  
  
@TC_EPE_DTM_0010
Scenario Outline: Add GSD in library
When I click the '<button>' button in the GSD Addition Window
And I click the '<button2>' button in the GSD Addition Window
And I select '<folder>' in the GSD Browser
And I click the '<button3>' button in the GSD Addition Window
And I click the '<button>' button in the GSD Additions Window
And I click the "<button4>" button in duplicate file window
And I click the '<button>' button in the GSD Addition Window
And I click the '<button5>' button in the GSD Addition Window
## Update Dtm

Examples:
  | SlNo. | button | button2 | button5 | button3 | folder            | button4 |
  | 1     | Next   | Browse  | Finish  | OK      | This PC/Documents | Close   |
  
  
@TC_EPE_DTM_0011
Scenario Outline: Remove GSD in library
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window
And I selected '<option2>' from the submenu in the DTM Browser Modal Dialogue window
And I click '<option3>' in the DTM Browser Modal Dialogue window
And I select the '<file_name>' in delete device library window
And I click '<button>' button in delete device library window
And I click '<button2>' button in delete device library popup window
And I click '<button3>' button in delete device library window

Examples:
  | SlNo. | node_name | action    | prm             | option      | option2              | option3 | file_name   | button | button2 | button3 |
  | 1     | PRM_1     | Configure | PRM_Master_0001 | Device menu | Additional functions | Remove  | GSD Library | Delete | Yes     | Close   |