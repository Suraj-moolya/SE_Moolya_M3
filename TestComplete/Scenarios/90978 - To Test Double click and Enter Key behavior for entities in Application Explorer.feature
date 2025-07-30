Feature: 90978 - To Test Double click and Enter Key behavior for entities in Application Explorer

@TC_EPE_AE_PGSQL_90978
@90978_1
Scenario Outline: Creating multiple nested folders under a root folder in Application Explorer
  When I rclick application browser folder AE Application browser in application explorer as '<RootFolder>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel1>'
  And I rclick application browser folder AE Application browser in application explorer as '<FolderLevel1>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel2>'
  And I rclick application browser folder AE Application browser in application explorer as '<FolderLevel2>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel3>'
  And I rclick application browser folder AE Application browser in application explorer as '<FolderLevel3>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel4>'
  And I rclick application browser folder AE Application browser in application explorer as '<FolderLevel4>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel5>'
  And I rclick application browser folder AE Application browser in application explorer as '<FolderLevel5>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel6>'
  And I rclick application browser folder AE Application browser in application explorer as '<FolderLevel6>'
  And I selected Create Folder in context menu
  And I Rename the Folder as '<FolderLevel7>'

  @Creating_7_Nested_Folders
  Examples:
    | SlNo | RootFolder | FolderLevel1 | FolderLevel2 | FolderLevel3 | FolderLevel4 | FolderLevel5 | FolderLevel6 | FolderLevel7 |
    | 1    | System     | Folder_1     | Folder_2     | Folder_3     | Folder_4     | Folder_5     | Folder_6     | Folder_7     |

@90978_2
Scenario Outline: Search Template in Template browser and Drag and drop Multiple Instance from template browser to application browser
  When I search text template browser AE Templates browser in application explorer as '<TemplateToSearch>'
  And I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<TargetFolderPath>'
  Then Verify the template is present in Application browser as '<TemplateToSearch>'

  @drag_and_drop_multiple_Instance
  Examples:
    | SlNo | TemplateToSearch | TargetFolderPath                 |
    | 1    | MotorGP          | MotorGP$$1.0.123$$Folder_7       |
    | 2    | ValveGP          | ValveGP$$1.0.100$$Folder_7       |
    | 3    | HandValveGP      | HandValveGP$$1.0.58$$Folder_7    |
    | 4    | PIDGP            | PIDGP$$1.0.153$$Folder_7         |
    | 5    | AnalogInputGP    | AnalogInputGP$$1.0.138$$Folder_7 |
    
    
# ----------------------------------------------------------------
# NOTE: The following scenarios collectively verify the behavior of
# folder expansion and navigation in the Application Browser using:
# - Double Click or Enter key on collapsed root node
# - Double Click or Enter key on folders with only instances
# - Double Click or Enter key on folders with subfolders & instances
# - Repeated actions on same folder to toggle expansion/collapse
# - Keyboard navigation (up/down arrows) for subfolder traversal
# - Expand/collapse using left/right arrow keys
# These are handled via tags @90978_3, @90978_4, @double_click_instance_and_verify,
# and @press_keys_in_foldername
# ----------------------------------------------------------------

@90978_3
Scenario Outline: Expand root node in Application Browser
  When I double click on template Identifier in application browser as '<NodeIdentifier>'
  Then I verify all folders are expanded in the Application Browser

  @double_click_instance_and_verify
  Examples:
    | SlNo | NodeIdentifier |
    | 1    | System_1       |

@90978_4
Scenario Outline: Navigate and control node expansion using keyboard in Application Browser
  When I press '<ArrowDirection>' arrow key on identifier '<NodeIdentifier>' in the Application Browser
  Then I verify all folders are expanded in the Application Browser

  @press_keys_in_foldername
  Examples:
    | SlNo | NodeIdentifier | ArrowDirection |
    | 1    | Folder_1       | right          |
    
# ----------------------------------------------------------------
# NOTE: The following scenario covers:
# - Click on Expand from root/folder with subfolders using context menu
# - Click on Collapse from root/folder with subfolders using context menu
# - Click on Collapse All from root/folder with subfolders using context menu
# These are handled using the tag @90978_5
# ----------------------------------------------------------------

@90978_5
Scenario Outline: Expand and Collapse folders using context menu in Application Browser
  When I rclick application browser template AE Application browser in application explorer as '<ContextMenuFolder>'
  And I Select context menu item EC Application browser in application explorer as '<ContextMenuAction>'

  @expand_collapse_context_menu
  Examples:
    | SlNo | ContextMenuFolder | ContextMenuAction |
    | 1    | Root_Node         | Expand            |
    
# ----------------------------------------------------------------
# NOTE: The following scenario covers:\
# Again Double click/click Enter key on same element inside the instance editor
# These are handled using the tag @90978_6
# ----------------------------------------------------------------

@90978_6
Scenario Outline: Double Click on Instance and Instance Editor
  When I double click on template Identifier in application browser as '<InstanceIdentifier>'
  And I double click on the instance '<InstanceIdentifier>' in the Instance Editor
  
  @double_click_instance_and_instance_edittor
  Examples:
    | SlNo | InstanceIdentifier |
    | 1    | MotorGP_5          |

@90978_7
Scenario Outline: Create Asset workspace - 4
  When I rclick asset workspace folder AE Asset workspace in application explorer as '<AssetRoot>'
  And I Select context menu item EC Asset workspace in application explorer as '<AssetAction>'

  Examples:
    | SlNo | AssetRoot | AssetAction      |
    | 1    | System_1  | Create Workspace |
    | 2    | System_1  | Create Workspace |
    | 3    | System_1  | Create Workspace |
    | 4    | System_1  | Create Workspace |
    
# ----------------------------------------------------------------
# NOTE: The following scenario covers:\
# Double click/click on Enter key on any asset workspace root node
# These are handled using the tag @90978_8
# ----------------------------------------------------------------

@90978_8
Scenario Outline: Double Click and Using Keys(left,right,up,down) in AssetWorkspace
  When I double click on the '<AssetIdentifier>' folder in the Asset Workspace
  And I press the '<ArrowKey>' arrow key on the '<AssetIdentifier>' folder in the Asset Workspace

  Examples:
    | SlNo | AssetIdentifier  | ArrowKey |
    | 1    | AssetWorkspace_1 | down     |
    
# ----------------------------------------------------------------
# Before this Testcase run this @TC_EPE_AE_0001 - Expand all Hirarchy of AE Panes
# NOTE: The following scenario covers:\
# Again Double click/click on Enter key on any folder/subfolder in template browser pane
# Double click/click on Enter key on any folder with templates but no sub folders in template browser pane
# Expand & collapse the folders using left & right arrow keys
# These are handled using the tag @90978_8
# ----------------------------------------------------------------

@90978_9
Scenario Outline: Double Click and Using Keys(left,right,up,down) in Template Browser
  When I double click on the '<TemplateIdentifier>' folder in the Template browser
  And I press the '<ArrowKey>' arrow key on the '<TemplateIdentifier>' folder in Template browser

  Examples:
    | SlNo | TemplateIdentifier | ArrowKey |
    | 1    | AssetWorkspace_1   | down     |
