Feature: Eco Struxure Process Expert_Desktop Automation_SRS_TestCases_202407030652351

@TC_EPE_EC_0001
@test0001
Scenario Outline: Launch Engineering Client
When I launch Engineering Client Engineering client in engineering client
#Then verify Tabs Explorer tab in system explorer as '<Explorer tab1>'
Examples:
  | SlNo. | System explorer window1 | Explorer tab1    |
  | 1     | Systems Explorer        | Systems Explorer |
  


@TC_EPE_EC_0002
@test0002
Scenario Outline:  Launch Engineering Client - Without Launching System Server,Open Engineering Client and Click on "OK" button in Popup window
When I launch Engineering Client Engineering client in engineering client
Then verify displayed Launch Engineering Client in engineering client
And verify windows message Warning popup in ec warning popups as '<Warning popup1>'
When I selected EC warning popup Ok in ec warning popups

Examples:
  | SlNo. | Warning popup1                 |
  | 1     | Unable to connect to Host name |

  
@TC_EPE_EC_0003
@test0003
Scenario Outline:  Launch Engineering Client - Without Launching System Server,Open Engineering Client and Click on Close(X) button in Popup window
When I launch Engineering Client Engineering client in engineering client
Then verify displayed Launch Engineering Client in engineering client
And verify windows message Warning popup in ec warning popups as '<Warning popup1>'
When I close ec popup EC warning popup Close in ec warning popups
Examples:
  | SlNo. | Warning popup1                 |
  | 1     | Unable to connect to Host name |
  
  
@TC_EPE_EC_0004
@test004
Scenario Outline: Launch Engineering Client Trial License 2 Instance and Click on OK button in Popup window
When I launch Engineering Client second time Engineering client two in engineering client
Then verify EC popup message Warning popup EC in ec warning popups as '<Warning popup EC1>'
When I selected EC warning popup Ok in ec warning popup

Examples:
  | SlNo. | Warning popup EC1                                                      |
  | 1     | Only one instance of Engineering Client can be open with Trial License |


@TC_EPE_EC_0005
@test005
Scenario Outline: Launch Engineering Client Trial License 2 Instance and Click on close button in Popup window
When I launch Engineering Client second time Engineering client two in engineering client
Then verify EC popup message Warning popup EC in ec warning popups as '<Warning popup EC1>'
When I close ec popup EC popup Close in ec warning popups

Examples:
  | SlNo. | Warning popup EC1                                                      |
  | 1     | Only one instance of Engineering Client can be open with Trial License |

@TC_EPE_EC_0006
@test004
Scenario Outline: Creation of Folder
When I Right Click on nodes System Explorer Node in system explorer as 'Systems Explorer'
Then verify context menu items from Rclick menu items in system explorer
When I selected Create Folder in context menu
Then verify system and folder created System Explorer Node in system explorer

Examples:
  | SlNo. |
  | 1     |
  
@TC_EPE_EC_0006a
@test004
Scenario Outline: Creation of Folder within Folder
When I Right Click on nodes System Explorer Node in system explorer as '<Folder>'
Then verify context menu items from Rclick menu items in system explorer
When I selected Create Folder in context menu
Then verify system and folder created System Explorer Node in system explorer

Examples:
  | SlNo. | Folder   |
  | 1     | Folder_1 |
 
  
@TC_EPE_EC_0007
@test0007
Scenario Outline: Creation of System - By Right clicking on System Explorer
When I Right Click on nodes System Explorer Node in system explorer as 'Systems Explorer'
Then verify context menu items System Explorer Node in system explorer
When I selected Create System in context menu
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | project browser2 |
  | 1     | Create System    |

     
@TC_EPE_EC_0008 
@test001
Scenario Outline: Creation of System within Folder
When I Right Click on nodes System Explorer Node in system explorer as 'Folder_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Create System in context menu
Then verify system and folder created System Explorer Node in system explorer

Examples:
  | SlNo. | node_name1 | node_name2 |
  | 1     | System_1   | Folder_1   |
  
  
@TC_EPE_EC_0009
@test006
Scenario Outline: Rename of Folder as Test_1
When I Right Click on nodes System Explorer Node in system explorer as 'Folder_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify_Folder_Renamed as per requirement in system explorer

Examples:
  | SlNo. | as per requirement1 |
  | 1     | Test_1              |
 
   
@TC_EPE_EC_0010
@test007
Scenario Outline: Rename of Folder as 12345 and close
When I Right Click on nodes System Explorer Node in system explorer as 'Folder_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
And I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up2>'
Then I Close the message window

Examples:
  | SlNo. | as per requirement1 | Rename Pop up2             |
  | 01    | 12345               | Identifier must start with |
  

@TC_EPE_EC_0011
@test007
Scenario Outline: Rename of Folder as Floor@1 and close
When I Right Click on nodes System Explorer Node in system explorer as 'Folder_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
And I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up2>'
Then I Close the message window

Examples:
  | SlNo. | as per requirement1 | Rename Pop up2     |
  | 01    | Floor@1             | Special characters |

  
@TC_EPE_EC_0012
@test009
Scenario Outline: Rename of System as 12345, Click on ok Button
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up3>'
When I selected Rename Pop up Ok in message box

Examples:
  | SlNo. | as per requirement1 | Rename Pop up3             |
  | 1     | 12345               | Identifier must start with |
  
@TC_EPE_EC_0012
@test009
Scenario Outline: Rename of System as 12345, Click on Close
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up3>'
Then I Close the message window

Examples:
  | SlNo. | as per requirement1 | Rename Pop up3             |
  | 1     | 12345               | Identifier must start with |
  
  
@TC_EPE_EC_0013
@test009
Scenario Outline: Rename of System as Control@123 Click on ok Button
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up3>'
When I selected Rename Pop up Ok in message box

Examples:
  | SlNo. | as per requirement1 | Rename Pop up3     |
  | 1     | Control@123         | Special characters |
  
  
@TC_EPE_EC_0013a
@test009
Scenario Outline: Rename of System as Control@123 Click on close
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up3>'
Then I Close the message window

Examples:
  | SlNo. | as per requirement1 | Rename Pop up3     |
  | 1     | Control@123         | Special characters |
  
@TC_EPE_EC_0013
@test009
Scenario Outline: Rename of System as Control_Test
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify_Folder_Renamed as per requirement in system explorer
Examples:
  | SlNo. | as per requirement1 | Rename Pop up3     |
  | 1     | Control_Test        | Special characters |


@TC_EPE_EC_0014
@test012
Scenario Outline: Rename of 2 folder with same name using OK
When I Right Click on nodes System Explorer Node in system explorer as 'Folder_2'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up6>'
When I selected Rename Pop up Ok in message box

Examples:
  | SlNo. | as per requirement1 | Rename Pop up6           |
  | 1     | Folder_1            | Identifier is not unique |
  
  
@TC_EPE_EC_0014
@test012
Scenario Outline: Rename of 2 folder with same name by clicking on close
When I Right Click on nodes System Explorer Node in system explorer as 'Folder_2'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up6>'
Then I Close the message window

Examples:
  | SlNo. | as per requirement1 | Rename Pop up6           |
  | 1     | Folder_1            | Identifier is not unique |

  
@TC_EPE_EC_0015
@test012
Scenario Outline: Rename of 2 system with same name using OK
When I Right Click on nodes System Explorer Node in system explorer as 'System_2'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up6>'
When I selected Rename Pop up Ok in message box

Examples:
  | SlNo. | as per requirement1 | Rename Pop up6           |
  | 1     | System_1            | Identifier is not unique |
  
  
  
@TC_EPE_EC_0015a
@test012
Scenario Outline: Rename of 2 system with same name by clicking on close
When I Right Click on nodes System Explorer Node in system explorer as 'System_2'
Then verify context menu items from Rclick menu items in system explorer
When I selected Rename in context menu
When I Rename Folder as per requirement in system explorer as '<as per requirement1>'
Then Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up6>'
Then I Close the message window

Examples:
  | SlNo. | as per requirement1 | Rename Pop up6           |
  | 1     | System_1            | Identifier is not unique |


@TC_EPE_EC_0016
@test0016
Scenario Outline: Navigation To Project Explorer(PE)- by selecting system
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

Examples:
  | SlNo. | Systems Explorer | MainToolBar1     | Explorer tab2    |
  | 1     | System_1         | Project Explorer | Project Explorer |
  
  
@TC_EPE_EC_0017
@test009
Scenario Outline: Navigate to Project Explorer Without selecting the system and click on OK in popup 
When I selected System Explorer Canvas in system explorer
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I selected Popup Ok in system explorer

Examples:
  | SlNo. | MainToolBar1     | Warning popup2                                             |
  | 1     | Project Explorer | Please select a system to navigate to the Project Explorer |


@TC_EPE_EC_0018
@test010
Scenario Outline: Navigate to Project Explorer Without selecting the system and click on X in popup
When I selected System Explorer Canvas in system explorer
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I PE warning Popup Close in system explorer

Examples:
  | SlNo. | MainToolBar1     | Warning popup2                                             |
  | 1     | Project Explorer | Please select a system to navigate to the Project Explorer |
  
    
@TC_EPE_EC_0019
@test009
Scenario Outline: Navigate to Project Explorer Without creating a Folder and System and click on OK in popup 
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I selected Popup Ok in system explorer

Examples:
  | SlNo. | MainToolBar1     | Warning popup2                                             |
  | 1     | Project Explorer | Please select a system to navigate to the Project Explorer |


@TC_EPE_EC_0020
@test010
Scenario Outline: Navigate to Project Explorer Without creating a Folder and System and click on X in popup 
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I PE warning Popup Close in system explorer

Examples:
  | SlNo. | MainToolBar1     | Warning popup2                                             |
  | 1     | Project Explorer | Please select a system to navigate to the Project Explorer |

  
@TC_EPE_EC_0021
@test021
Scenario Outline: Navigate to Project Explorer by right click on system
When I Right Click on nodes System_1 in system_1 node as '<System_11>'
Then verify context menu items ContextMenu in system explorer
When I selected Open Project in system_1 node
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

Examples:
  | SlNo. | System_11 | Explorer tab2    |
  | 1     | System_1  | Project Explorer |
  
@TC_EPE_EC_0021a
@test0040
Scenario Outline: Navigation To Project Explorer(PE) - Main Tool Bar by selecting system
When I Click on Nodes System Explorer Node in system explorer as '<System_21a>'
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'

Examples:
  | SlNo. | MainToolBar3     | Explorer tab4    | System_21a |
  | 1     | Project Explorer | Project Explorer | System_1   |

    
@TC_EPE_EC_0022
@test007
Scenario Outline: Navigate to Project Explorer by shortcut (ALT+P)
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I Click on shortcut Keys Press shortcut keys in system explorer as '<Press shortcut keys1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

Examples:
  | SlNo. | Systems Explorer | Press shortcut keys1 | Explorer tab2    |
  | 1     | System_1         | Alt+P                | Project Explorer |
 
   
@TC_EPE_EC_0023
@test0023
Scenario Outline: Navigation To Application Explorer(AE)
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

Examples:
  | SlNo. | Systems Explorer | MainToolBar1                      | Explorer tab2 |
  | 1     | System_1         | Open Application Explorer (Alt+A) | Application   |

  
@TC_EPE_EC_0024
@test009
Scenario Outline: Navigate to Application Explorer Without selecting the system and click on OK in popup
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I selected Popup Ok in system explorer

Examples:
  | SlNo. | MainToolBar1         | Warning popup2                                                 |
  | 1     | Application Explorer | Please select a system to navigate to the Application Explorer |


@TC_EPE_EC_0025
@test010
Scenario Outline: Navigate to Application Explorer Without selecting the system and click on X in popup 
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I PE warning Popup Close in system explorer

Examples:
  | SlNo. | MainToolBar1         | Warning popup2                                                 |
  | 1     | Application Explorer | Please select a system to navigate to the Application Explorer |
  
    
@TC_EPE_EC_0026
@test009
Scenario Outline: Navigate to Application Explorer Without creating a Folder and System and click on OK in popup  
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I selected Popup Ok in system explorer

Examples:
  | SlNo. | MainToolBar1         | Warning popup2                                                 |
  | 1     | Application Explorer | Please select a system to navigate to the Application Explorer |


@TC_EPE_EC_0027
@test010
Scenario Outline: Navigate to Application Explorer Without creating a Folder and System and click on X in popup  
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'
When I PE warning Popup Close in system explorer

Examples:
  | SlNo. | MainToolBar1         | Warning popup2                                                 |
  | 1     | Application Explorer | Please select a system to navigate to the Application Explorer |

  
@TC_EPE_EC_0028
@test007
Scenario Outline: Navigate to Application Explorer by shortcut (ALT+A)
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I Click on shortcut Keys Press shortcut keys in system explorer as '<Press shortcut keys1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

Examples:
  | SlNo. | Systems Explorer | Press shortcut keys1 | Explorer tab2        |
  | 1     | System_1         | Alt+A                | Application Explorer |


@TC_EPE_EC_0029
@test0029
Scenario Outline: Navigation to Global template Explorer(GTE)
When I navigate to explorers MainToolBar in system explorer as 'Open Global Templates Explorer'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab1>'

Examples:
  | SlNo. | Explorer tab1    |
  | 1     | Global Templates |
  
  
@TC_EPE_EC_0030
@test0030
Scenario Outline: Navigation to Content Repository(CR)
When I navigate to explorers MainToolBar in system explorer as 'Open Content Repository'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab1>'
Examples:
  | SlNo. | Explorer tab1    |
  | 1     | Global Templates |
  
  
@TC_EPE_EC_0031
@test0031
Scenario Outline: Navigation To Topology Explorer(TE)
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'
@Navigate_TE_selecting_system1
Examples:
  | SlNo. | Systems Explorer | MainToolBar1                   | Explorer tab2 |
  | 1     | System_1         | Open Topology Explorer (Alt+T) | Topology      |
@Navigate_TE_selecting_system2
Examples:
  | SlNo. | Systems Explorer | MainToolBar1                   | Explorer tab2 |
  | 1     | System_2         | Open Topology Explorer (Alt+T) | Topology      |
  
  
@TC_EPE_EC_0032
@test0032
Scenario Outline: Navigate to Topology Explorer ( TE ) - Without selecting system and click on Ok popup
When explorer tab is not Systems Explorer then Navigate
And I selected System Explorer Canvas in system explorer
And I navigate to explorers MainToolBar in system explorer as 'Topology Explorer'
Then verify Explorer warning message Warning popup in system explorer as 'navigate to the Topology Explorer'
When I selected Popup Ok in system explorer

Examples:
  | SlNo. |
  | 1     |
  
  
@TC_EPE_EC_0033
@test0033
Scenario Outline: Navigate to Topology Explorer ( TE ) - from shortcut ( ALT + T )
When I Click on Nodes System Explorer Node in system explorer as '<Systems Explorer>'
And I Click on shortcut Keys Press shortcut keys in system explorer as '<Press shortcut keys1>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab2>'

Examples:
  | SlNo. | Systems Explorer | Press shortcut keys1 | <Explorer tab2> |
  | 1     | System_1         | Alt+T                | Topology        |
      

@TC_EPE_EC_034
@test0034
Scenario Outline: Click - User dropdown - next to user details in EC  
When I selected User dropdown in engineering client
Then I Verify the contents of the drop down
Examples:
  | SlNo. |
  | 1     |


@TC_EPE_EC_035
@test0035
Scenario Outline: Click - Lock - option under dropdown in EC   
When I selected User dropdown in engineering client
And I selected User lock in engineering client
And I entered password in login page ec as '<password2>'
And I selected Log in in login page ec
Then Verify Action message in notification pannel project browser in project explorer as '<notification>'

Examples:
  | SlNo. | password2    | notification        |
  | 1     | P@ssw0rd1234 | A user was unlocked |

  
  
  
@TC_EPE_EC_0036
@test0036
Scenario Outline: Click - Login - from dropdown and enter valid username, password and click login
When I selected User dropdown in engineering client
And I selected User login in engineering client
And I entered password in login page ec as '<password1>'
And I selected Log in in login page ec
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | password1    | project browser2 |
  | 1     | P@ssw0rd1234 | A user was successfully logged on |



@TC_EPE_EC_0037    
@test0037
Scenario Outline: Click - Lock - option under dropdown and enter invalid password and click login
When I selected User dropdown in engineering client
And I selected User lock in engineering client
And I entered password in login page ec as '<password1>'
And I selected Log in in login page ec
Then verify displayed Engineering client in engineering client

Examples:
  | SlNo. | password1 |
  | 1     | Invalid   |

    
@TC_EPE_EC_0038
@test0038
Scenario Outline: Logout - click under dropdown in EC 
When I selected User dropdown in engineering client
And I selected User logout in engineering client
Then verify displayed log in to use the client in engineering client
Examples:
  | SlNo. |
  | 1     |

  
@TC_EPE_EC_0039
@test0039
Scenario Outline: Navigate to System Explorer ( SE )
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'

Examples:
  | SlNo. | MainToolBar3         | Explorer tab4    |
  | 1     | Open System Explorer | Systems Explorer |
  

@TC_EPE_EC_0040
@test0040
Scenario Outline: Navigation To Project Explorer(PE) - Main Tool Bar
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'

Examples:
  | SlNo. | MainToolBar3     | Explorer tab4    |
  | 1     | Project Explorer | Project Explorer |
  
@TC_EPE_EC_0041
@test0041
Scenario Outline: Navigation To Topology Explorer(TE) - Main Tool Bar
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'

Examples:
  | SlNo. | MainToolBar3      | Explorer tab4     |
  | 1     | Topology Explorer | Topology Explorer |
  
@TC_EPE_EC_0042
@test0042
Scenario Outline: Navigation To Application Explorer(AE) - Main Tool Bar
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'

Examples:
  | SlNo. | MainToolBar3         | Explorer tab4        |
  | 1     | Application Explorer | Application Explorer |
  
  
@TC_EPE_EC_0043
@test0043
Scenario Outline: Release Supervision Participant - Main Tool Bar 
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples:
  | SlNo. | MainToolBar3                    |
  | 1     | Release Supervision Participant |
  
  
@TC_EPE_EC_44
Scenario Outline: Check the tool slots are created
When I open details tab in task manager Windows in windows explorer
Then verify control expert instances in task manager detail list in task manager as '<Control Participant Max Instance>'

@Check_the_tool_slots_created_are_4
Examples:
  | SlNo. | Control Participant Max Instance |
  | 02    | 4                                |
