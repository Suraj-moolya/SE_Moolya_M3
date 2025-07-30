Feature: Configure controllers like standalone & HSBY M580/M580 safety/M340/Quantum

# can use this testcase to create 3 folders use count as 3 
@TC_EPE_EC_000
@test004
Scenario Outline: Creation of Folder
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Create Folder in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then verify system and folder created System Explorer Node in system explorer
Examples:
  | SlNo. | as per requirement1 |
  | 1     | Controllers         |
  | 2     | Networks            |
  | 3     | Devices             |
  | 3     | Workstation         |
  

  
@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Create 2 Ethernet Networks and Rename
When I Right Click on nodes System Explorer Node in system explorer as 'Networks'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I Rename Network as per requirement in system explorer as '<as per requirement1>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | context menu            | as per requirement1       | project browser1        | button          | project browser2        | FolderName |
  | 1     | Create Ethernet Network | SE_Network                | Create Ethernet Network | Networks$$Close | Update Ethernet Network | Networks   |
  | 2     | Create Ethernet Network | Lab_Network               | Create Ethernet Network | Networks$$Close | Update Ethernet Network | Networks   |
  | 3     | Create Ethernet Network | STB_Island_Device_Network | Create Ethernet Network | Networks$$Close | Update Ethernet Network | Networks   |
  | 4     | Create Ethernet Network | PRM_Device_Network        | Create Ethernet Network | Networks$$Close | Update Ethernet Network | Networks   |
  

  
  
@test0002a
Scenario Outline: Close Network Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button          | FolderName |
  | 1     | Networks$$Close | Networks   |
  
@test0002b
Scenario Outline: Close Controllers Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button             | FolderName  |
  | 1     | Controllers$$Close | Controllers |
  
@test0002c
Scenario Outline: Close Workstation Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button             | FolderName  |
  | 1     | Workstation$$Close | Workstation |
  
@test0002d
Scenario Outline: Close Devices Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button         | FolderName |
  | 1     | Devices$$Close | Devices    |
  
@test0002e
Scenario Outline: Open Network Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button         | FolderName |
  | 1     | Networks$$Open | Networks   |
  
@test0002f
Scenario Outline: Open Controllers Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button            | FolderName  |
  | 1     | Controllers$$Open | Controllers |
  
@test0002g
Scenario Outline: Open Workstation Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button            | FolderName  |
  | 1     | Workstation$$Open | Workstation |
  
@test0002h
Scenario Outline: Open Devices Folder in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded
Examples:
  | SlNo. | button        | FolderName |
  | 1     | Devices$$Open | Devices    |
  
  
@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Create a Control Project for M580_Standalone
When I Right Click on nodes System Explorer Node in system explorer as '<Folder Name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I rename the ControlProject as '<controller_name>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
@Create_First_Controller_for_standlone
Examples:
  | SlNo. | Folder Name | context menu      | controller | controller_name | project browser1  | project browser2  |
  | 1     | Controllers | Create Controller | M580       | M580_Standalone | Create Controller | Update Controller |
  
@Create_Second_Controller_for_standlone
Examples:
  | SlNo. | Folder Name | context menu      | controller | controller_name  | project browser1  | project browser2  |
  | 1     | Controllers | Create Controller | M580       | M580_Standalone2 | Create Controller | Update Controller |
  
@Create_Third_Controller_for_standlone
Examples:
  | SlNo. | Folder Name | context menu      | controller | controller_name  | project browser1  | project browser2  |
  | 1     | Controllers | Create Controller | M580       | M580_Standalone3 | Create Controller | Update Controller |
@Create_First_Controller_for_HSBY
Examples:
  | SlNo. | Folder Name | context menu      | controller | controller_name | project browser1  | project browser2  |
  | 1     | Controllers | Create Controller | M580       | M580_HSBY_1     | Create Controller | Update Controller |
    


  
@TC_EPE_TE_CS_0003d
@test0001
Scenario Outline: Create a Devices For PRM Profibus
When I Right Click on nodes System Explorer Node in system explorer as '<Folder Name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<context menu>'   
@Create_PRM_Device
Examples:
  | SlNo. | Folder Name | context menu           |
  | 1     | Controllers | Create PRM Profibus DP |
  
@Create_STB_Device
Examples:
  | SlNo. | Folder Name | context menu      |
  | 1     | Devices     | Create STB Island |
  
  
@TC_EPE_TE_CS_0003a
@test0001
Scenario Outline: Create a Control Project for M580_Safety
When I Right Click on nodes System Explorer Node in system explorer as 'Controllers'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I rename the ControlProject as '<controller_name>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu      | controller  | controller_name | project browser1  | project browser2  |
  | 1     | Create Controller | M580 Safety | M580_Safety     | Create Controller | Update Controller |
  

@TC_EPE_TE_CS_0003b
@test0001
Scenario Outline: Create a Control Project for M340_Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'Controllers'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I rename the ControlProject as '<controller_name>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu      | controller | controller_name | project browser1  | project browser2  |
  | 1     | Create Controller | M340       | M340_Standalone | Create Controller | Update Controller |
  
  
@TC_EPE_TE_CS_0003c
@test0001
Scenario Outline: Create a Control Project for Quantum
When I Right Click on nodes System Explorer Node in system explorer as 'Controllers'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
When I rename the ControlProject as '<controller_name>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu      | controller | controller_name | project browser1  | project browser2  |
  | 1     | Create Controller | Quantum    | Quantum         | Create Controller | Update Controller |
  

@TC_EPE_TE_CS_0004
@test0001
Scenario Outline: Set Safety Password for Safety Controller
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Safety'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
And I Enter pssword in '<password1>' field in Controller password grid popup
And I Enter pssword in '<password2>' field in Controller password grid popup
And I click modal dialog window project browser in project explorer as '<Button>'
And I Wait for Circular Progress Bar To Complete in system explorer
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu    | controller | password1            | password2                    | Button | project browser2  |
  | 1     | Manage Password | Safety     | Password$$Moolya@123 | Confirm Password$$Moolya@123 | OK     | Validate Password |
  

@TC_EPE_TE_CS_0006
@test0001
Scenario Outline: Open Configuration window of Controller
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<Notification>'

@open_Configuration_window_of_Controller_M580_Standalone
Examples:
  | SlNo. | Controller      | context menu | Notification          |
  | 1     | M580_Standalone | Configure    | Open Configure Editor |
  
@open_Configuration_window_of_Controller_M580_Safety
Examples:
  | SlNo. | Controller  | context menu | Notification          |
  | 1     | M580_Safety | Configure    | Open Configure Editor |
  
@open_Configuration_window_of_Controller_M580_Standalone3
Examples:
  | SlNo. | Controller       | context menu | Notification          |
  | 1     | M580_Standalone3 | Configure    | Open Configure Editor |
@open_Configuration_window_of_Controller_M580_HSBY_1
Examples:
  | SlNo. | Controller  | context menu | Notification          |
  | 1     | M580_HSBY_1 | Configure    | Open Configure Editor |
  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Double click on PLC Bus 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'

Examples:
  | SlNo. | Project Browser RO1        |
  | 1     | Configuration$$0 : PLC bus |
  
  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Controller protection to Disable 
When I change the controller protection to disable

Examples:
  | SlNo. |
  | 1     |
  
@test0002b
Scenario Outline: Close Controllers  in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded

@Close_Controllers_in_Topology_Explorer__M580_Standalone
Examples:
  | SlNo. | button                 | FolderName  |
  | 1     | M580_Standalone$$Close | Controllers |
  
@Close_Controllers_in_Topology_Explorer__M580_Safety
Examples:
  | SlNo. | button             | FolderName  |
  | 1     | M580_Safety$$Close | Controllers |

@Close_devices_in_Topology_Explorer__Devices__-50-
Examples:
  | SlNo. | button         | FolderName |
  | 1     | Devices$$Close | Devices    |
  
@Close_Controllers_in_Topology_Explorer__M580_Standalone3
Examples:
  | SlNo. | button                  | FolderName  |
  | 1     | M580_Standalone3$$Close | Controllers |
  
@Close_Controllers_in_Topology_Explorer__M580_HSBY_1
Examples:
  | SlNo. | button             | FolderName  |
  | 1     | M580_HSBY_1$$Close | Controllers |
    
  
@test0002b
Scenario Outline: Open Workstation_2  in Topology Explorer
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded

@Open_Workstation_in_Topology_Explorer_Workstation_2
Examples:
  | SlNo. | button              | FolderName  |
  | 1     | Workstation_2$$Open | Controllers |
  
@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Create a Station Node in Workstation folder
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I enterkey Project Browser RO in refine offline
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
@Create_Workstation_1
Examples:
  | SlNo. | context menu       | project browser1   |
  | 1     | Create Workstation | Create Workstation |
  
@Create_Workstation_2
Examples:
  | SlNo. | context menu       | project browser1   |
  | 1     | Create Workstation | Create Workstation |
  
@Create_Workstation_on_New_Build
Examples:
  | SlNo. | context menu       | project browser1   |
  | 1     | Create Workstation | Create Workstation |
  

  
@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Create NIC in Workstation folder
When I Right Click on nodes System Explorer Node in system explorer as 'Workstation_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I Perform action on the Folder by Clicking on '<button>' in Topology Explorer
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
Examples:
  | SlNo. | context menu | project browser1       | button               |
  | 1     | Create NIC   | Create Service Handler | Workstation_1$$Close |
  
  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Change safety settings of controller to Disable
When I Right Click on nodes System Explorer Node in system explorer as '<Controller name>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
When I Select button in the modal dialoge window as '<Button name>'

@Change_safety_settings_of_M580_standalone_controller_to_Disable
Examples:
  | SlNo. | context menu | options           | Button name | Controller name |
  | 1     | Properties   | Controller$$False | Yes         | M580_Standalone |
 
@Change_safety_settings_of_M580_HSBY_1_controller_to_Disable 
Examples:
  | SlNo. | context menu | options           | Button name | Controller name |
  | 1     | Properties   | Controller$$False | Yes         | M580_HSBY_1     |
  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Change safety settings of controller to Disable M580_Standalone3
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Standalone3'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
When I Select button in the modal dialoge window as '<Button name>'

Examples:
  | SlNo. | context menu | options           | Button name | Controller name |
  | 1     | Properties   | Controller$$False | Yes         | M580_HSBY_1     |
  

  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Change CPU Version of controller 
When I selected select PLC bus combobox item CE in refine offline as '<Cpu_version>'

@Change_CPU_Version_of_controller__BME_P58_4040_03.20
Examples:
  | SlNo. | Cpu_version          |
  | 1     | BME P58 4040   03.20 |
  

@Change_CPU_Version_of_controller__BME_P58_6040_03.20
Examples:
  | SlNo. | Cpu_version          |
  | 1     | BME P58 6040   03.20 |
  
@Change_CPU_Version_of_controller__BME_P58_5040_03.20
Examples:
  | SlNo. | Cpu_version          |
  | 1     | BME P58 5040   03.20 |

@Change_CPU_Version_of_controller__BME_P58_4040S_03.20
Examples:
  | SlNo. | Cpu_version          |
  | 1     | BME P58 4040   03.20 |
  
@Change_CPU_Version_of_controller__BME_H58_6040S_03.20
Examples:
  | SlNo. | Cpu_version          |
  | 1     | BME H58 6040   03.20 |
  
  

@TC_EPE_TE_CS_000
@test000
Scenario Outline: Double click on PLC Bus - EIO 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
@Double_click_on_PLC_Bus_EIO 
Examples:
  | SlNo. | Project Browser RO1        |
  | 1     | Configuration$$0 : PLC bus |

  

@TC_EPE_TE_CS_000
@test000
Scenario Outline: Close PLC Bus Window in TM 
When I close PLC Bus window in controller configuration window

Examples:
  | SlNo. |
  | 1     |

  
@TC_EPE_TE_CS_000
@test000
Scenario Outline: Change safety settings of safety controller to Disable
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Safety'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I change controller properties with drop down options as '<options>'
And I click modal dialog window project browser in project explorer as '<Button>'
When I change controller properties with drop down options as '<options1>'
When I Select button in the modal dialoge window as '<Button name>'

Examples:
  | SlNo. | context menu | options           | Button name | options1      | Button |
  | 1     | Properties   | Controller$$False | Yes         | Safety$$False | Yes    |
  
  

  
@TC_EPE_TE_CS_0008
@test000
Scenario Outline: Set Firmware and Web Diagnostic/ Data Storage passwords (for 4.xx M580, M580 Safety Controllers) in the Configure Editor window 
When I Right Click on the '<item>' in Project Browser Pane
And I click '<menu_item>' in Tool Bar popup window
And I Select '<tab_item>' Tab in Project Browser Properties Window
And I select '<button1>' in New Device PopUp Window
And I Entered '<oldpassword>' and '<newpassword>' in Modify Password Dialogue window
And I select '<button>' in New Device PopUp Window
And I select '<button2>' in New Device PopUp Window
And I Entered '<oldpassword1>' and '<newpassword>' in Modify Password Dialogue window
And I select '<button>' in New Device PopUp Window
And I select '<button3>' in New Device PopUp Window
And I select '<button>' in New Device PopUp Window

Examples:
  | SlNo. | item    | menu_item  | tab_item                        | oldpassword | newpassword | button | button1              | oldpassword1 | button2              | button3 |
  | 1     | Project | Properties | Project & Controller Protection | fwdownload  | Moolya@1234 | OK     | Chan&ge password ... | webuser      | Change &password ... | &Apply  |

  
    
@TC_EPE_TE_CS_0009
@test000
Scenario Outline: Set the Security and IP (for M580, M580 Safety) 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'

Examples:
  | SlNo. | Project Browser RO1        |
  | 1     | Configuration$$0 : PLC bus |

  
Scenario Outline: Unlock Security of 4th gen M580 controller
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser path>'
And I selected unlock security EIO in control expert
And I close PLC Bus window in controller configuration window
And I selected List of modified Yes button CE in dialog ce

Examples:
  | SlNo. | Project Browser path                                           |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME$$EIO |
 
   
Scenario Outline: Disable HTTPS of controller in CE
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser path>'
And I select HTTPS EIO in control expert as '<Option>'
And I close PLC Bus window in controller configuration window
And I selected List of modified Yes button CE in dialog ce

Examples:
  | SlNo. | Project Browser path                                           | Option   |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME$$EIO | Disabled |
  

