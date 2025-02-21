Feature: 129.Import the instances which is exported in above step

@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: Import - RightClick on the system_1 and select Import from the context menu
When I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
Examples:
  | SlNo. | Application browser1 | Application browser2 |
  | 1     | System_1             | Import               |
  

  
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the one instances file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
#And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 
@import_Enter_the_filelocation_and_file_name_as_csv
Examples: 
  | SlNo. | Import3                  | Import4 |
  | 1     | Import_instance_test.csv | Open    |
@import_Enter_the_filelocation_and_file_name_as_sbk
Examples: 
  | SlNo. | Import3             | Import4 |
  | 1     | Deploy_ReDeploy.sbk | Open    |
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the faulty name file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                | Import4 |
  | 1     | Import_Faulty_name.csv | Open    |
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the faulty Parameter file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                          | Import4 |
  | 1     | Import_Faulty_Parameter_Test.csv | Open    |
  

@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the faulty Version file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                   | Import4 |
  | 1     | Import_Faulty_Version.csv | Open    |
  
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the Invalid Folder file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                           | Import4 |
  | 1     | Import_InvalidFolder_template.csv | Open    |
  

@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the Motor Instance file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                                 | Import4 |
  | 1     | Import_Motor_instance_template_Test.csv | Open    |
  
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the Motor Instance with pendinginterfaces file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                                                   | Import4 |
  | 1     | Import_Motor_instance_template_Test_PendingInterfaces.csv | Open    |
  
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the Bulk Instances file to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3     | Import4 |
  | 1     | Bulk_AE.csv | Open    |
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the File created manually to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                           | Import4 |
  | 1     | Import_Created_instance_Excel.csv | Open    |
  
  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Enter the filelocation and select the File created manually xml format to be imported click on OK in popup 
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box 

Examples: 
  | SlNo. | Import3                     | Import4 |
  | 1     | Import_Addinstance_Test.xml | Open    |
  
  
  
  
@TC_EPE_AE_00
@test00
Scenario Outline: import - Click on Create all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify Message from notification panel AE Notification Pannel in message box

Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 | Application browser9 |
  | 1     | Create All              | OK                      | MotorGP_1_1          |

  
@TC_EPE_AE_00
@test00
Scenario Outline: import - Verify Template added in AE  
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'

Examples:
  | SlNo. | Application browser9 |
  | 1     | MotorGP_1_1          |


  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Click on Update all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify Message from notification panel AE Notification Pannel in message box

Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 |
  | 1     | Update All              | OK                      |

  
@TC_EPE_AE_00
@test00
@TC_EPE_AE_00
Scenario Outline: import - Click on Skip all button from resolve conflict pop up and ok
When I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify Message from notification panel AE Notification Pannel in message box

Examples:
  | SlNo. | Import Conflict Dialog7 | Import Conflict Dialog8 |
  | 1     | Skip All                | OK                      |

  
  
@TC_EPE_AE_00
@test00
Scenario Outline: import - Click on Cancel button from resolve conflict pop up
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import5>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import6>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'
Then Verify Message from notification panel AE Notification Pannel in message box

Examples:
  | SlNo. | Import5                                 | Import6 | Import Conflict Dialog7 | Application browser9 |
  | 1     | Import_Motor_instance_template_Test.csv | Open    | Cancel                  | MotorGP_1_1          |





