Feature: 58 Configure PRM and map it to control project

@TC_EPE_TE_0004
@test004
Scenario Outline: Configure PRM and map it to control project
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action2>'
And I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window
And I Select '<tabname>' in hardware catalog window
And I double click on '<property>' in hardware catalog window
And I double click on '<property1>' in hardware catalog window
And I click Update button on hardware catalog window
And I select '<button>' on control expert popub window
And I selected '<button2>' Button in hardware catalog window
And I double click on the installed '<prm>' on DTM Browser
And I double click on '<settings>' in PRM Window
And I update the '<ip_address>' in PRM Window
And I click '<button1>' on PRM Window
And I selected Close Configuration window in Topology Explorer
And I click modal dialog window '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<notification pannel>'
When I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action3>'
And I Select particular '<network>' for each  Controller in physical connection
And I Select button in the modal dialoge window as '<button1>'

############################ End test case here ###################

And I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I RClick control project browser project browser in project explorer as '<node_name>'
And I Select context menu item EC project browser in project explorer as '<contextmenu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
And I Dclick Control project broswer project browser in project explorer as '<projectbrowser2>'
And I Dclick Control project broswer project browser in project explorer as '<projectbrowser3>'
And I Control executable dropdown PE project browser in project explorer as '<network2>'

############################ 

And I Click '<tabname2>' on service mapping edittor window
And I Drag and drop the EPE Managed Device from devices to channels as '<server>'
And I Click on '<button1>' in the dialog box
And I RClick control project browser project browser in project explorer as '<projectbrowser3>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item1>'
And I click modal dialog window project browser in project explorer as '<button1>'

Examples:
  | SlNo. | node_name | action                 | node_name2 | action2   | tabname     | property  | property1     | button | prm             | settings         | ip_address     | button1 | button2 | action3              | network           | MainToolBar           | contextmenu            | controller | controller_name  | projectbrowser2 | projectbrowser3     | network2                         | tabname2              | server | contextmenu_item1 | menu  | menu_item        | notification pannel |
  | 1     | Devices   | Create PRM Profibus DP | PRM_1      | Configure | DTM catalog | Protocols | Profibus DPV1 | Yes    | PRM_Master_0001 | General Settings | 182.179.244.99 | OK      | Close   | Physical Connections | EthernetNetwork_1 | Open Project Explorer | Create Control Project | M580       | M580_Standalone2 | Executables     | ControlExecutable_1 | ControlExecutive_1$$Controller_1 | Communication Mapping | PRM_1  | Build All         | Tools | Hardware Catalog | Configure Editor    |
  
  
@TC_EPE_TE_0004a
@test004
Scenario Outline: Configure PRM 
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action2>'
And I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window
And I Select '<tabname>' in hardware catalog window
And I double click on '<property>' in hardware catalog window
And I double click on '<property1>' in hardware catalog window
And I click Update button on hardware catalog window
And I select '<button>' on control expert popub window
And I selected '<button2>' Button in hardware catalog window
And I double click on the installed '<prm>' on DTM Browser
And I double click on '<settings>' in PRM Window
And I update the '<ip_address>' in PRM Window
And I click '<button1>' on PRM Window
And I selected Close Configuration window in Topology Explorer
And I click modal dialog window '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<notification pannel>'

Examples:
  | SlNo. | node_name | action                 | node_name2 | action2   | tabname     | property  | property1     | button | prm             | settings         | ip_address     | button1 | button2 | action3              | network            | menu  | menu_item        | notification pannel          |
  | 1     | Devices   | Create PRM Profibus DP | PRM_1      | Configure | DTM catalog | Protocols | Profibus DPV1 | Yes    | PRM_Master_0001 | General Settings | 182.179.244.99 | OK      | Close   | Physical Connections | PRM_Device_Network | Tools | Hardware Catalog | Configure Editor (Completed) |


@TC_EPE_TE_0004b
@test004
Scenario Outline: Map PRM to control project
When I Click '<tabname2>' on service mapping edittor window
And I Drag and drop the EPE Managed Device from devices to channels as '<server>'
And I Click on '<button1>' in the dialog box

Examples: 
  | SlNo. | tabname2              | server | button1 |
  | 1     | Communication Mapping | PRM_1  | OK      |
  
@TC_EPE_TE_0004c
@test003
Scenario Outline: Map PRM to Physical Connections
When I Right Click on nodes System Explorer Node in system explorer as '<Topology Explorer Tree1>'
And I Select context menu item EC project browser in project explorer as '<Topology Explorer Tree2>'
And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
When I click modal dialog window project browser in project explorer as '<Button>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3   | Button |
  | 1     | PRM_1                   | Physical Connections    | PRM_1$$PRM_Device_Network | OK     |