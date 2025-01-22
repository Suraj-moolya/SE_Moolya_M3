Feature: Eco Struxure Process Expert_Desktop Automation_SRS_TestCases_202407030652351


@TC_EPE_AE_0001
@test0001
Scenario Outline: Expand all Hirarchy of AE Panes
When I Expand template browser AE Templates browser Application in application explorer as '<Templates browser Application1>'
And I Expand template browser AE Templates browser STAHL in application explorer as '<Templates browser STAHL2>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE STAHL in application explorer as '<STAHL3>'
And I Expand template browser AE Time Stamping in application explorer as '<Time Stamping4>'
And I scroll down template browser AE Templates browser in application explorer as '<Templates browser5>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE Time Stamping in application explorer as '<Time Stamping6>'
And I Expand template browser AE Unity Array Variables in application explorer as '<Unity Array Variables7>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE Unity Array Variables in application explorer as '<Unity Array Variables8>'
And I Expand template browser AE Unity Elementary Time Stamped Variables in application explorer as '<Unity Elementary Time Stamped Variables9>'
And I scroll down template browser AE Templates browser in application explorer as '<Templates browser10>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE Unity Elementary Time Stamped Variables in application explorer as '<Unity Elementary Time Stamped Variables11>'
And I Expand template browser AE Owner_Consumer Templates in application explorer as '<Owner_Consumer Templates12>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE Unity Peer to Peer in application explorer as '<Unity Peer to Peer13>'
And I Expand template browser AE Advantys in application explorer as '<Advantys14>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE Advantys in application explorer as '<Advantys15>'
And I Expand template browser AE M340 in application explorer as '<M34016>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE M340 in application explorer as '<M34017>'
And I Expand template browser AE M580 in application explorer as '<M58018>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE M580 in application explorer as '<M58019>'
And I Expand template browser AE Quantum in application explorer as '<Quantum20>'
Then verify composite template AE Templates browser in application explorer
When I Collapse template browser AE Foundation Library in application explorer as '<Foundation Library21>'
And I Expand template browser AE General Purpose Library in application explorer as '<General Purpose Library22>'
Then verify template browser AE Templates browser in application explorer as '<Templates browser>'

Examples:
  | SlNo. | Templates browser Application1 | Templates browser STAHL2 | STAHL3 | Time Stamping4 | Templates browser5 | Time Stamping6 | Unity Array Variables7      | Unity Array Variables8 | Unity Elementary Time Stamped Variables9 | Templates browser10 | Unity Elementary Time Stamped Variables11 | Owner_Consumer Templates12                  | Unity Peer to Peer13 | Advantys14                           | Advantys15 | M34016 | M34017 | M58018 | M58019 | Quantum20 | Foundation Library21 | General Purpose Library22                                                         | Templates browser |
  | 1     | Foundation Library,Application | Control Modules,STAHL    | STAHL  | Time Stamping  | 3                  | Time Stamping  | Unity,Unity Array Variables | Unity Array Variables  | Unity Elementary Time Stamped Variables  | 6                   | Unity Elementary Time Stamped Variables   | Unity Peer to Peer,Owner_Consumer Templates | Unity Peer to Peer   | Unity Special In Rack Cards,Advantys | Advantys   | M340   | M340   | M580   | M580   | Quantum   | Foundation Library   | General Purpose Library,Communications,Devices SA,Diagnosis SA,Generic,Process SA | _empty_           |


@TC_EPE_AE_0002
@test02
Scenario Outline: Update all instances with latest version(Update Template from one Version to another-postive Complete Flow)
When I create system_1 System Explorer Node in system explorer
And I selected System Explorer Node in system explorer
And I selected Open Global Templates Explorer in engineering client
And I Search text and select GTE global template search in global template explorer as '<global template search1>'
And I right click on the searched template GTE global template core in global template explorer as '<global template core2>'
And I Select context menu item EC global template core in global template explorer as '<global template core3>'
And I selected Ok duuplicate in duplicate
And I right click on the searched template GTE global template core in global template explorer as '<global template core4>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
And I selected toolbox in composite editor
And I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<toolboox table6>'
And I selected save as composite editor in composite editor
And I entered Description in save as window as '<Description7>'
And I selected Save in save as window
And I selected Open System Explorer in engineering client
And I select system 1 application explorer System Explorer Node in system explorer
And I uncheck all filters temp browser AE Templates browser in application explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser8>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser9>'
And I rclick application browser template AE Application browser in application explorer as '<Application browser10>'
And I Select context menu item EC Application browser in application explorer as '<Application browser11>'
Then Verify version in application explorer as '<Application browser>'
When I close all tabs except system explorer in Engineering Client

Examples:
  | SlNo. | global template search1   | global template core2 | global template core3 | Duplicate window | global template core4 | global template core5 | toolboox table6 | Description7   | Templates browser8 | Templates browser9 | Application browser10 | Application browser11 | Application browser |
  | 1     | Motorgp$$MotorGP$$1.0.123 | MotorGP$$1.0.123      | Duplicate             | _empty_          | MotorGP$$1.0.0        | Edit                  | Add             | TC_EPE_AE_0002 | motorgp            | MotorGP$$1.0.0     | MotorGP$$1.0.0        | Update Template       | MotorGP             |



@TC_EPE_AE_0003
@test003
Scenario Outline: Update all instances with latest version(Searching an Invalid Template name)
When I selected Open Global Templates Explorer in engineering client
Then verify search text GTE global template search in global template explorer as '<global template search1>'
When I close all tabs except system explorer in Engineering Client

Examples:
  | SlNo. | global template search1 | global template search | content |
  | 1     | Schneider Electric      | _empty_                | NA      |
  
@TC_EPE_AE_0004
@test004
Scenario Outline: Update all instances with latest version(Negative flow of Interupting Inbetween)
When I create system_1 System Explorer Node in system explorer
And I selected System Explorer Node in system explorer
And I selected Open Global Templates Explorer in engineering client
And I Search text and select GTE global template search in global template explorer as '<global template search1>'
And I right click on the searched template GTE global template core in global template explorer as '<global template core2>'
And I Select context menu item EC global template core in global template explorer as '<global template core3>'
And I selected Close duuplicate in duplicate  
Then Verify Duplicate window close
 
  
Examples:
  | SlNo. | global template search1   | global template core2 | global template core3 |
  | 1     | Motorgp$$MotorGP$$1.0.123 | MotorGP$$1.0.123      | Duplicate             |


@TC_EPE_AE_0005
@test005
Scenario Outline: Update all instances with latest version(Without Description User should not able to save)
When I create system_1 System Explorer Node in system explorer
And I selected System Explorer Node in system explorer
And I selected Open Global Templates Explorer in engineering client
And I Search text and select GTE global template search in global template explorer as '<global template search1>'
And I right click on the searched template GTE global template core in global template explorer as '<global template core2>'
And I Select context menu item EC global template core in global template explorer as '<global template core3>'
And I selected Ok duuplicate in duplicate
And I right click on the searched template GTE global template core in global template explorer as '<global template core4>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
And I selected toolbox in composite editor
And I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<toolboox table6>'
And I selected save as composite editor in composite editor
And I selected Save in save as windowo
Then verify popup message in the save as window as '<content>'
When I selected Cancel in save as window
And I close all tabs except system explorer in Engineering Client

Examples:
  | SlNo. | global template search1   | global template core2 | global template core3 | global template core4 | global template core5 | toolboox table6 | Templates browser | content |
  | 1     | Motorgp$$MotorGP$$1.0.123 | MotorGP$$1.0.123      | Duplicate             | MotorGP$$1.0.0        | Edit                  | Add             | _empty_           | Enter a |

 
@TC_EPE_AE_0006
@test06
Scenario Outline: Update all instances with latest version(Update Template Cancellation at last step)
When I create system_1 System Explorer Node in system explorer
And I selected System Explorer Node in system explorer
And I selected Open Global Templates Explorer in engineering client
And I Search text and select GTE global template search in global template explorer as '<global template search1>'
And I right click on the searched template GTE global template core in global template explorer as '<global template core2>'
And I Select context menu item EC global template core in global template explorer as '<global template core3>'
And I selected Ok duuplicate in duplicate
And I right click on the searched template GTE global template core in global template explorer as '<global template core4>'
And I Select context menu item EC global template core in global template explorer as '<global template core5>'
And I selected toolbox in composite editor
And I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<toolboox table6>'
And I selected save as composite editor in composite editor
And I entered Description in save as window as '<Description7>'
And I selected Save in save as window
And I selected Open System Explorer in engineering client
And I select system 1 application explorer System Explorer Node in system explorer
And I uncheck all filters temp browser AE Templates browser in application explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser8>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser9>'
And I rclick application browser template AE Application browser in application explorer as '<Application browser10>'
And I Select context menu item EC Application browser in application explorer as '<Application browser11>'
Then Verify version in application explorer as '<Application browser>'
When I close all tabs except system explorer in Engineering Client
 
Examples:
  | SlNo. | global template search1   | global template core2 | global template core3 | Duplicate window | global template core4 | global template core5 | toolboox table6 | Description7   | Templates browser8 | Templates browser9 | Application browser10 | Application browser11 | Application browser |
  | 1     | Motorgp$$MotorGP$$1.0.123 | MotorGP$$1.0.123      | Duplicate             | _empty_          | MotorGP$$1.0.0        | Edit                  | Add             | TC_EPE_AE_0002 | motorgp            | MotorGP$$1.0.0     | MotorGP$$1.0.0        | Update Template       | MotorGP             |
  
  
  
   
@TC_EPE_AE_0007
@test007
Scenario Outline: Expand system and Expand Folder and Double click on Template ( Open instance properties )
When I double click on template Identifier in application browser as '<Identifier5>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'

Examples:
  | SlNo. | Identifier5 | Instance Editor6 |
  | 1     | MotorGP_1   | MotorGP_1        |

    
@TC_EPE_AE_0008
@test008
Scenario Outline: Modify the Instance properties - Modify instance property
When I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist7>'
And I Enter description AE Instance description in application explorer

Examples:
  | SlNo. | Instance editor checklist7 |
  | 1     | Running$$1                 |
  
  
@TC_EPE_AE_0008A
@test008A
Scenario Outline: Modify the Instance properties - Save button 
When I selected Instance editor save in application explorer
And I take evidence Instance Editor in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'

Examples:
  | SlNo. | Instance editor close8 |
  | 1     | MotorGP_1              |

  
@TC_EPE_AE_0009
@test009
Scenario Outline: Modify the Instance properties - Close ( X )
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'

Examples:
  | SlNo. | Instance editor close8 |
  | 1     | MotorGP_1              |

    
@TC_EPE_AE_0010
@test010
Scenario Outline: Modify the Instance properties - Close ( X ) and No in Popup
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox9>'
When I selected Save changes dialogbox no in application explorer

Examples:
  | SlNo. | Instance editor close8 | Save changes dialogbox9    |
  | 1     | MotorGP_1              | MotorGP_1: Save Changes(s) |
  
  
@TC_EPE_AE_0011
@test011
Scenario Outline: Modify the Instance properties - Close ( X ) and Cancel in Popup
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox9>'
When I selected Save changes dialogbox cancel in application explorer

Examples:
  | SlNo. | Instance editor close8 | Save changes dialogbox9    |
  | 1     | MotorGP_1              | MotorGP_1: Save Changes(s) |
  
  
@TC_EPE_AE_0012
@test012
Scenario Outline: Modify the Instance properties - Close ( X ) and Yes in Popup
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close8>'
Then verify popup AE Save changes dialogbox in application explorer as '<Save changes dialogbox9>'
When I selected Save changes dialogbox yes in application explorer

Examples:
  | SlNo. | Instance editor close8 | Save changes dialogbox9    |
  | 1     | MotorGP_1              | MotorGP_1: Save Changes(s) |
  
  
@TC_EPE_AE_0013
@test013
Scenario Outline: Copy and paste the Instance - copy instance from context menu and paste
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template5>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as 'Copy'
And I rclick application browser folder AE Folder_2 in application explorer as '<Folder_26>'
And I Select context menu item EC ContextMenu in application explorer as '<ContextMenu7>'
Then Verify template created Application browser template in application explorer as '<Application browser template8>'

Examples:
  | SlNo. | MotorGP template5  | Folder_26 | ContextMenu7 | Application browser template8 |
  | 1     | MotorGP_1$$1.0.123 | Folder_2  | Paste        | MotorGP_1_1                   |

  
@TC_EPE_AE_0014
@test014
Scenario Outline: Copy and paste the Instance - Copy Paste using Shortcut Keys
When I Copy and paste using shortcut keys Specific template in application browser
Then Verify template created Application browser template in application explorer as '<Application browser template5>'

Examples:
  | SlNo. | Application browser template5 |
  | 1     | MotorGP_1_1                   |

  
@TC_EPE_AE_0015
@test015
Scenario Outline: Copy and paste the Instance - open instance editor, copy and paste, OK on locked poup
When I double click on template Identifier ValveGP_1 in application browser as '<Identifier ValveGP_15>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template7>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu8>'
And I rclick application browser folder AE Folder_2 in application explorer as '<Folder_29>'
And I Select context menu item EC ContextMenu in application explorer as '<ContextMenu10>'
Then Verify instance lock popup Warning popup window in application explorer as '<Warning popup window11>'
When I selected AE warning popup ok in application explorer

Examples:
  | SlNo. | Identifier ValveGP_15 | Instance Editor6 | MotorGP template7  | ContextMenu8 | Folder_29 | ContextMenu10 | Warning popup window11 |
  | 1     | ValveGP_1             | ValveGP_1        | ValveGP_1$$1.0.100 | Copy         | Folder_2  | Paste         | locked                 |

  
@TC_EPE_AE_0016
@test016
Scenario Outline: Copy and paste the Instance - open instance editor, copy and paste ( Shortcut Keys ), OK on locked poup
When I double click on template Identifier ValveGP_1 in application browser as '<Identifier ValveGP_15>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor6>'
When I Copy and paste using shortcut keys value template in application browser
Then Verify instance lock popup Warning popup window in application explorer as '<Warning popup window7>'
When I selected AE warning popup ok in application explorer

Examples:
  | SlNo. | Identifier ValveGP_15 | Instance Editor6 | Warning popup window11 |
  | 1     | ValveGP_1             | ValveGP_1        | locked                 |


@TC_EPE_AE_0017
@test017
Scenario Outline: Copy and paste the Instance, use it in Control Project(Creating multiple Folders and Instance)
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template5>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu6>'
And I rclick application browser folder AE Folder_2 in application explorer as '<Folder_27>'
And I Select context menu item EC ContextMenu in application explorer as '<ContextMenu8>'
Then Verify template created Application browser template in application explorer as '<Application browser template9>'

Examples:
  | SlNo. | MotorGP template5  | ContextMenu6 | Folder_27 | ContextMenu8 | Application browser template9 |
  | 1     | MotorGP_3$$1.0.123 | Copy         | Folder_2  | Paste        | MotorGP_                      |


@TC_EPE_AE_0018
@test0018
@TC_EPE_AE_0018
Scenario Outline: Search Template in Template browser and Drag and drop from template browser to application browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser1>'
Examples:
  | SlNo. | Templates browser1 | Templates browser2     |
  | 1     | INTERLOCK8OFFGP    | INTERLOCK8OFFGP$$1.0.5 |
  | 2     | Analog             | AnalogOutputGP$$1.0.93 |
  | 3     | Analog             | AnalogInputGP$$1.0.138 |
  | 4     | MotorGP            | MotorGP$$1.0.123       |
  | 5     | ValveGP            | ValveGP$$1.0.100       |
  
  
@TC_EPE_AE_0018
@test0018
@TC_EPE_AE_0018
Scenario Outline: Search Valve_Gp in Template browser and Drag and drop from template browser to application browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify the template is present in Application browser

@search_drag_drop_Valve_GP_template
Examples:
  | SlNo. | Templates browser1 | Templates browser2 |
  | 1     | ValveGP            | ValveGP$$1.0.100   |

@search_drag_drop_sample_test_template_1.0.126
Examples:
  | SlNo. | Templates browser1 | Templates browser2   |
  | 1     | Sample_Test        | Sample_Test$$1.0.126 |
  

  
  
@TC_EPE_AE_0019
@test0019
Scenario Outline: Inspect instance - Rclick on the inspect instance and verify the tab and click on ok  
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
Then verify inspect instance window open Inspect instance tree in inspect instance as '<Inspect instance tree6>'
When I selected Inspect instance ok in inspect instance 
Examples: 
  | SlNo. | Application browser4 | Application browser5 | Inspect instance tree6 |
  | 1     | MotorGP$$1.0.123     | Inspect Instance     | MotorGP_1              |
  
  
  
@TC_EPE_AE_0020
@test0020
Scenario Outline: Inspect instance - Rclick on the inspect instance and verify the tab and click on Close  
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
Then verify inspect instance window open Inspect instance tree in inspect instance as '<Inspect instance tree6>'
When I Close inspect instance window AE Inspect instance window in inspect instance
Examples: 
  | SlNo. | Application browser4 | Application browser5 | Inspect instance tree6 |
  | 1     | MotorGP$$1.0.123     | Inspect Instance     | MotorGP_1              |
  
       
  
@TC_EPE_AE_0021
@test0021
Scenario Outline: Rename instance - invalid 1234 
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I clicked Enter in keyboard shortcut
Then verify the status of the instance
 
Examples: 
  | SlNo. | Application browser4 | Application browser5 | Name1 |
  | 1     | MotorGP$$1.0.123     | Rename               | 1234  |
  

  
@TC_EPE_AE_0022
@test0022
Scenario Outline: Rename instance - invalid 1234a 
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
Then verify the status of the instance
 
Examples: 
  | SlNo. | Application browser4 | Application browser5 | Name1 |
  | 1     | MotorGP$$1.0.123     | Rename               | 1234a |
  
  
  
@TC_EPE_AE_0023
@test0023
Scenario Outline: Rename instance - invalid abc@ 
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I clicked Enter in keyboard shortcut
Then verify the status of the instance
 
Examples: 

  | SlNo. | Application browser4 | Application browser5 | Name1 |
  | 1     | MotorGP$$1.0.123     | Rename               | abc@  |
  
@TC_EPE_AE_0024
@test0024
Scenario Outline: Rename instance - same name abc@
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I clicked Enter in keyboard shortcut
Then I Verify the Instance ToolTip is diaplayed with Identifier Not unique Message
 
Examples: 

  | SlNo. | Application browser4 | Application browser5 | Name1 |
  | 1     | MotorGP$$1.0.123     | Rename               | abc@  |
  
  
@TC_EPE_AE_0025
@test0025
Scenario Outline: Rename instance - invalid _abc 
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I Click on buttons as '<button>'
And I clicked Enter in keyboard shortcut
Then verify the status of the instance
 
Examples: 

  | SlNo. | Application browser4 | Application browser5 | Name1 | button |
  | 1     | MotorGP$$1.0.123     | Rename               | _abc  | Yes    |
  
  
@TC_EPE_AE_0026
@test0026
Scenario Outline: Rename instance - _abc to check lock popup
When I double click on template Identifier ValveGP_1 in application browser as '<Identifier ValveGP_15>'
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I Click on buttons as '<button>'
Then Verify instance lock popup Warning popup window in application explorer as '<Warning popup window6>'
When I clicked Enter in keyboard shortcut
Then verify the status of the instance
 
Examples: 

  | SlNo. | Identifier ValveGP_15 | Application browser4 | Application browser5 | Name1 | button | Warning popup window6            |
  | 1     | MotorGP_1             | MotorGP$$1.0.123     | Rename               | _abc  | Yes    | locked for instance modification |
  

@TC_EPE_AE_0027
@test0027
Scenario Outline: Rename instance - _abc to check lock popup Close(X)
When I double click on template Identifier ValveGP_1 in application browser as '<Identifier ValveGP_15>'
When I rclick application browser template AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>' 
And I Rename the Insatnce to the requirement '<Name1>'
And I Click on buttons as '<button>'
Then Verify instance lock popup Warning popup window in application explorer as '<Warning popup window6>'
When I Close Lockup pop up window
Then verify the status of the instance
 
Examples: 

  | SlNo. | Identifier ValveGP_15 | Application browser4 | Application browser5 | Name1 | button | Warning popup window6            |
  | 1     | MotorGP_1             | MotorGP$$1.0.123     | Rename               | _abc  | Yes    | locked for instance modification |


@TC_EPE_AE_0028
@test028
Scenario Outline: R-Click on RootNode ( System_1) from Application browser pane
When I rclick application browser folder AE Application browser in application explorer as '<Application browser4>'
Then Verify application browser folder AE
Examples:
  | SlNo. | Application browser4 |
  | 1     | System               |



@TC_EPE_AE_0029
@test029
Scenario Outline: Export instance - Click Export, Save and Open CSV
When I Select context menu item EC Application browser in application explorer as '<Application browser5>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.csv'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Are you sure you want to continue'
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Extracted Template CSV Data and Template Details Export in ec windows explorer

Examples:
  | SlNo. | Application browser5 |
  | 1     | Export               |

  

@TC_EPE_AE_0030
@test030
Scenario Outline: Export instance - Rclick root node ( folder ), Export as XML, open XML file
When I rclick application browser folder AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.xml'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify Extracted Template XML Data and Template Details Export in ec windows explorer

Examples:
  | SlNo. | Application browser4 | Application browser5 |
  | 1     | System               | Export               |

  
@TC_EPE_AE_0031
@test031
Scenario Outline: Export instance - Rclick instance, Export, save and cancel in export window
When I rclick application browser folder AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.xml'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Cancel'
Then I verify the file existance

Examples:
  | SlNo. | Application browser4 | Application browser5 |
  | 1     | System               | Export               |
  

@TC_EPE_AE_0032
@test032
Scenario Outline: Export instance - Export to csv, and open csv file ( over-write )
When I rclick application browser folder AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.csv'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then I Click on  button from popup window as '<ButtonName>'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Are you sure you want to continue'
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Extracted Template CSV Data and Template Details Export in ec windows explorer

Examples:

  | SlNo. | Application browser4 | Application browser5 | ButtonName |
  | 1     | AnalogOutputGP       | Export               | No         |

  
@TC_EPE_AE_0033
@test033
Scenario Outline: Export instance - Rclick instance, Export, save and cancel in export window
When I rclick application browser folder AE Application browser in application explorer as '<Application browser4>'
And I Select context menu item EC Application browser in application explorer as '<Application browser5>'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.xml'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Cancel'
Then I verify the file existance

Examples:
  | SlNo. | Application browser4 | Application browser5 |
  | 1     | System               | Export               |
  


@TC_EPE_AE_0035
@test035
Scenario Outline: Delete instance - from context Menu
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template1>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu2>'
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template3>'
When I Click on buttons in popup window Delete popup in message box as 'Yes'
Then Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'


Examples:
  | SlNo. | MotorGP template1  | ContextMenu2 | MotorGP template3                             |
  | 1     | MotorGP_1$$1.0.123 | Delete       | Are you sure you want to delete this Instance |



@TC_EPE_AE_0036
@test036
Scenario Outline: Delete instance - Rclick instance, select Delete from Menu and No on Popup
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template1>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu2>'
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template3>'
When I Click on buttons in popup window Delete popup in message box as 'No'
And I take evidence Identifier MotorGP_1 in application browser

Examples:
  | SlNo. | MotorGP template1  | ContextMenu2 | MotorGP template3                             |
  | 1     | MotorGP_1$$1.0.123 | Delete       | Are you sure you want to delete this Instance |



@TC_EPE_AE_0037
@test037
Scenario Outline: Delete instance - from Delete Key
When I Click template AE MotorGP template in application explorer as '<MotorGP template1>'
And I Press short keys MotorGP template in application explorer
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template2>'
When I Click on buttons in popup window Delete popup in message box as 'Yes'
Then Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'

Examples:
  | SlNo. | MotorGP template1  | MotorGP template2                             |
  | 1     | MotorGP_1$$1.0.123 | Are you sure you want to delete this Instance |



@TC_EPE_AE_0038
@test038
Scenario Outline: Delete instance - Click instance, click delete key and No on Popup
When I Create system and create instance Create Multiple instance in application explorer
And I Click template AE MotorGP template in application explorer as '<MotorGP template1>'
And I Press short keys MotorGP template in application explorer
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template2>'
When I Click on buttons in popup window Delete popup in message box as 'No'
And I take evidence Identifier MotorGP_1 in application browser

Examples:
  | SlNo. | MotorGP template1  | MotorGP template2                             |
  | 1     | MotorGP_1$$1.0.123 | Are you sure you want to delete this Instance |



@TC_EPE_AE_0039
@test039
Scenario Outline: Delete instance - Double click instance (Open the Instance editor tab), right click and delete Yes and OK on Popup
When I double click on template Identifier MotorGP_1 in application browser as '<Identifier MotorGP_11>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor2>'
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template3>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu4>'
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template5>'
When I Click on buttons in popup window Delete popup in message box as 'Yes'
Then Verify instance lock popup Warning popup window in application explorer as '<Warning popup window6>'
When I Click on buttons in popup window Warning popup window in application explorer as '<Warning popup window7>'
Then Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'

Examples:
  | SlNo. | Identifier MotorGP_11 | Instance Editor2 | MotorGP template3  | ContextMenu4 | MotorGP template5                             | Warning popup window6 | Warning popup window7 |
  | 1     | MotorGP_1             | MotorGP_1        | MotorGP_1$$1.0.123 | Delete       | Are you sure you want to delete this Instance | locked                | OK                    |



@TC_EPE_AE_0040
@test040
Scenario Outline: Delete instance - Double click instance (Open the Instance editor tab), right click and delete Yes and X on Popup
When I double click on template Identifier MotorGP_1 in application browser as '<Identifier MotorGP_11>'
Then Verify template instance editor Instance Editor in application explorer as '<Instance Editor2>'
When I rclick application browser template AE MotorGP template in application explorer as '<MotorGP template3>'
Then verify context menu items ContextMenu in application explorer
When I Select context menu item EC ContextMenu in application explorer as '<ContextMenu4>'
Then Verify delete window AE MotorGP template in application explorer as '<MotorGP template5>'
When I Click on buttons in popup window Delete popup in message box as 'Yes'
Then Verify instance lock popup Warning popup window in application explorer as '<Warning popup window6>'
When I Warning popup close Warning popup window in application explorer
Then Verify Message from notification panel AE Delete popup in message box as 'Delete Instance'

Examples:
  | SlNo. | Identifier MotorGP_11 | Instance Editor2 | MotorGP template3  | ContextMenu4 | MotorGP template5                             | Warning popup window6 |
  | 1     | MotorGP_1             | MotorGP_1        | MotorGP_1$$1.0.123 | Delete       | Are you sure you want to delete this Instance | locked                |


@TC_EPE_AE_0041
@test0041
@TC_EPE_AE_0041
Scenario Outline: Expand Asset workspace
When I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace4>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace5>'
And I Click on Enter Press shortcut keys in system explorer
And I rclick asset workspace folder AE Asset workspace in application explorer as '<Asset workspace6>'
And I Select context menu item EC Asset workspace in application explorer as '<Asset workspace7>'
And I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor8>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'
When I drag template in application browser drop Asset Workspace Editor AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor10>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor11>'
When I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'
Then Verify Link Status Node Instance in application explorer
When I Close instance editor tab Instance editor close in application explorer as '<Asset workspace6>'

Examples:
  | SlNo. | Asset workspace4 | Asset workspace5 | Asset workspace6 | Asset workspace7 | Assert Workspace Editor8 | Assert Workspace Editor9 | Assert Workspace Editor10 | Assert Workspace Editor11 |
  | 1     | System_1         | Create Workspace | AssetWorkspace   | Edit Workspace   | AnalogOutputGP           | AnalogInputGP            | AnalogInputGP             | AnalogOutputGP            |

  