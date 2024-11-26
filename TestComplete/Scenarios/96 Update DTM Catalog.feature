Feature: 96 Update DTM Catalog

@TC_EPE_DTM_0001
Scenario Outline: Installing the DTM Files,updating and checking it in refinement window in Topology Window
When I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window  
And I select '<protocol>' and '<device>' in DTM Browser Add device window
And I select '<button1>' in DTM Browser property device window
And I right click on the installed '<prm>' on DTM Browser
And I selected '<option>' in DTM Browser Modal Dialogue window 
And I select '<protocol>' and '<device1>' in DTM Browser Add device window
And I select '<button1>' in DTM Browser property device window
And I click '<menu1>' in Tool Bar
And I click '<menu_item1>' in Tool Bar popup window
#And I select '<button3>' in New Device PopUp Window
And I wait for the Build Project window to disappear
And I selected Save PRM Configuration in Configuration Window
And I selected Close Configuration window in Topology Explorer

Examples:
  | SlNo. | menu  | prm             | option | protocol    | device       | device1      | menu_item   | menu_item1          | menu1 | num | button3 |
  | 1     | Tools | BMEP58_ECPU_EXT | Add... | EtherNet IP | BME AHI 0812 | BME AHO 0412 | DTM Browser | Rebuild All Project | Build | 0   | Yes     |
