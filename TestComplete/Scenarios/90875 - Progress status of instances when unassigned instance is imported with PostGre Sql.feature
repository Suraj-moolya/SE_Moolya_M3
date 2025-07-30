Feature: 90875 - Progress status of instances when unassigned instance is imported with PostGre Sql


@TC_EPE_AE_PGSQL_90875_1
Scenario Outline: Create New Folder in Application Browser
When I rclick application browser folder AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC ContextMenu in application explorer as '<ContextMenu>'
Then Verify the template is present in Application browser as '<folder>'

@create_new_folder_1_in_Application_browser
Examples:
  | SlNo. | Application browser | ContextMenu   | folder   |
  | 1     | System_1            | Create Folder | Folder_1 |


@TC_EPE_AE_PGSQL_90875_2
Scenario Outline: Drag and drop searched template to folder in Application Browser
When I search text template browser AE Templates browser in application explorer as '<Templates browser>'
And I drag Template from Template browser and drop to the Folders in Application browser with folder name as '<Templates browser2>'
Then Verify the template is present in Application browser as '<Templates browser>'

@Drag_and_drop_GenericDeviceGP_1.0.5_to_folder_1
Examples:
  | SlNo. | Templates browser | Templates browser2               |
  | 1     | GenericDeviceGP   | GenericDeviceGP$$1.0.5$$Folder_1 |


@TC_EPE_AE_PGSQL_90875_3
Scenario Outline: Check Progress status of instances and export
Then Verify the progress status of instance in Application browser when opened as '<template>'
When I rclick application browser folder AE Application browser in application explorer as '<folder>'
And I Select context menu item EC ContextMenu in application explorer as 'Export'
And Export the instance in Application browser when opened as '<filedetails>'
And I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'
Then Verify notification panel message Notification Pannel in message box as '<Message>' 

@check_progress_status_GenericDeviceGP_EXPORT_Folder_1_AE_Instances_Folder1.csv
Examples:
  | SlNo. | template           | folder   | filedetails                | Message            |
  | 1     | GenericDeviceGP$$0 | Folder_1 | AE_Instances_Folder1$$.csv | Export (Completed) |


@TC_EPE_AE_PGSQL_90875_4
Scenario Outline: Rename instance and check progress status of instance
When I rclick application browser template AE Application browser in application explorer as '<Templates browser>'
And I Select context menu item EC ContextMenu in application explorer as '<ContextMenu>'
And I Rename the Insatnce to the requirement '<Name>'
And I clicked Enter in keyboard shortcut
Then Verify notification panel message Notification Pannel in message box as '<Message>' 
Then Verify the progress status of instance in Application browser when opened as '<template>'

@Rename_GenericDeviceGP_$1.0.5_to_GenD_1_check_progress_at_25%
Examples:
  | SlNo. | Templates browser      | ContextMenu | Name   | template   | Message                     |
  | 1     | GenericDeviceGP$$1.0.5 | Rename      | GenD_1 | GenD_1$$25 | Update Instance (Completed) |

  
@TC_EPE_AE_PGSQL_90875_5
Scenario Outline: Import instance and check progress status
When I rclick application browser folder AE Application browser in application explorer as '<folder>'
And I Select context menu item EC ContextMenu in application explorer as 'Import'
And Import the instance in Application browser when opened as '<filedetails>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify notification panel message Notification Pannel in message box as '<Message>' 
Then Verify the progress status of instance in Application browser when opened as '<template>'

@System_1_IMPORT_AE_Instances_Folder1.csv_check_GenericDeviceGP_progress_at_25%
Examples:
  | SlNo. | template            | folder   | filedetails                | Message            |
  | 1     | GenericDeviceGP$$25 | System_1 | AE_Instances_Folder1$$.csv | Import (Completed) |
