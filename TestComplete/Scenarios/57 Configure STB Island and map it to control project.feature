Feature: 57 Configure STB Island and map it to control project

@TC_EPE_TE_0003
@test003
Scenario Outline: Configure STB Island and map it to control project
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I selected System Explorer Node in system explorer
And I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action2>'
And I double-click on "<main_folder>" "<subfolder1>" and "<final_item1>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder2>" and "<final_item2>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder3>" and "<final_item3>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder4>" and "<final_item4>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder5>" and "<final_item5>" in the catalog browser
And I selected Close Configuration window in Topology Explorer
And I click modal dialog window '<button>' in Topology Explorer
And I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action3>'
And I set the IP address to '<ip_address>' and subnet mask to '<subnet_mask>' in STBIsland properties
And I Perform action on the Folder by Clicking on '<close_button>' in Topology Explorer
And I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action4>'
And I Select particular '<network>' for each  Controller in physical connection
And I Select button in the modal dialoge window as '<buttonname>'

########################## End Test case here #############
# V no need to create control project, has to be done through execution order #####

And I navigate to explorers MainToolBar in system explorer as '<MainToolBar>'
And I RClick control project browser project browser in project explorer as '<node_name>'
And I Select context menu item EC project browser in project explorer as '<contextmenu>'
And I Select controller in context menu as '<controller>'
And I rename the ControlProject as '<controller_name>'
And I Dclick Control project broswer project browser in project explorer as '<projectbrowser2>'
And I Dclick Control project broswer project browser in project explorer as '<projectbrowser3>'
And I Control executable dropdown PE project browser in project explorer as '<network2>'

############################## separate test case to add STB island in service editor #################
And I Click '<tabname>' on service mapping edittor window
And I Drag and drop the EPE Managed Device from devices to channels as '<node_name2>'
And I Click on '<buttonname>' in the dialog box

############ End 2nd test here ##############
#  V build All test case already present nad has to be used through execution order ###### 
And I RClick control project browser project browser in project explorer as '<projectbrowser3>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item1>'
And I click modal dialog window project browser in project explorer as '<buttonname>'

Examples:
  | SlNo. | node_name | action            | node_name2  | action2   | button | action3    | main_folder   | subfolder1 | final_item1        | subfolder2 | final_item2        | subfolder3    | final_item3        | subfolder4     | final_item4        | subfolder5  | final_item5        | ip_address   | subnet_mask | node_name3   | action4              | network           | buttonname | MainToolBar           | contextmenu            | controller | controller_name | projectbrowser2 | projectbrowser3     | network2                         | tabname               | close_button       | contextmenu_item1 |
  | 1     | System_1  | Create STB Island | STBIsland_1 | Configure | Yes    | Properties | STB - Catalog | Networking | STBNIP2311 - V5.xx | Power      | STBPDT2100 - V1.xx | Digital Input | STBDAI5230 - V1.xx | Digital Output | STBDAO5260 - V1.xx | Accessories | STBXBE1100 - V1.xx | 192.168.10.2 | 255.255.0.0 | Controller_1 | Physical Connections | EthernetNetwork_1 | OK         | Open Project Explorer | Create Control Project | M580       | M580_Standalone | Executables     | ControlExecutable_1 | ControlExecutive_1$$Controller_1 | Communication Mapping | STBIsland_1$$Close | Build All         |

  
@TC_EPE_TE_0003a
@test003
Scenario Outline: Configure STB Island
When I right-click on '<node_name>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action>'
And I selected System Explorer Node in system explorer
And I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action2>'
And I double-click on "<main_folder>" "<subfolder1>" and "<final_item1>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder2>" and "<final_item2>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder3>" and "<final_item3>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder4>" and "<final_item4>" in the catalog browser
And I double-click on "<main_folder>" "<subfolder5>" and "<final_item5>" in the catalog browser
And I selected Close Configuration window in Topology Explorer
And I click modal dialog window '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<notification pannel>'
When I right-click on '<node_name2>' in the Topology Explorer
And I Select context menu item EC in Topology Explorer as '<action3>'
And I set the IP address to '<ip_address>' and subnet mask to '<subnet_mask>' in STBIsland properties
And I Perform action on the Folder by Clicking on '<close_button>' in Topology Explorer

Examples:
  | SlNo. | node_name | action            | node_name2  | action2   | button | action3    | main_folder   | subfolder1 | final_item1        | subfolder2 | final_item2        | subfolder3    | final_item3        | subfolder4     | final_item4        | subfolder5  | final_item5        | ip_address     | subnet_mask | action4              | network | buttonname | close_button       | notification pannel                 |
  | 1     | Devices   | Create STB Island | STBIsland_1 | Configure | Yes    | Properties | STB - Catalog | Networking | STBNIP2311 - V5.xx | Power      | STBPDT2100 - V1.xx | Digital Input | STBDAI5230 - V1.xx | Digital Output | STBDAO5260 - V1.xx | Accessories | STBXBE1100 - V1.xx | 182.179.243.26 | 255.255.0.0 | Physical Connections |         | OK         | STBIsland_1$$Close | Close STB Island Editor (Completed) |

  
@TC_EPE_TE_0003b
@test003
Scenario Outline: Map STB Island to control project
When I Click '<tabname>' on service mapping edittor window
And I Drag and drop the EPE Managed Device from devices to channels as '<node_name2>'
And I Click on '<buttonname>' in the dialog box

Examples: 
  | SlNo. | tabname               | node_name2  | buttonname |
  | 1     | Communication Mapping | STBIsland_1 | OK         |
 
@TC_EPE_TE_0003c
@test003
Scenario Outline: Map STB_Island to Physical Connections
When I Right Click on nodes System Explorer Node in system explorer as '<Topology Explorer Tree1>'
And I Select context menu item EC project browser in project explorer as '<Topology Explorer Tree2>'
And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
When I click modal dialog window project browser in project explorer as '<Button>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Button |
  | 1     | STBIsland_1             | Physical Connections    | STBIsland_1$$SE_Network | OK     |
