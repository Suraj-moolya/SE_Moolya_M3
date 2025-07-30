Feature: Import the instances which is exported in above step

  
@TC_EPE_AE_00
@test00
Scenario Outline: Import - RightClick on the system and select Import from the context menu
When I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel5>'

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3                  | Import4 | Notification Pannel5 |
  | 1     | System_1             | Import               | Import_instance_test.csv | Open    | Import(Completed)    |
  
@TC_EPE_AE_0043
@uida1696791200
@set21
@test001
@TC_EPE_AE_0027
Scenario Outline: Importing by Create All option
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
And I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'
And I Select context menu item EC Application browser in application explorer as '<Application browser4>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import5>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import6>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'
And Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel10>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Application browser3 | Application browser4 | Import5                                 | Import6 | Import Conflict Dialog7 | Import Conflict Dialog8 | Application browser9 | Notification Pannel10 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | System1_             | Import               | Import_Motor_instance_template_Test.csv | Open    | Create All              | OK                      | MotorGP_1_1          | Import(Completed)     |

  
@TC_EPE_AE_0044
@uida1696791200
@set21
@test001
@TC_EPE_AE_0027
Scenario Outline: Importing by adding one more instance and Updating
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
And I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'
And I Select context menu item EC Application browser in application explorer as '<Application browser4>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import5>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import6>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'
And Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel10>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Application browser3 | Application browser4 | Import5                                 | Import6 | Import Conflict Dialog7 | Import Conflict Dialog8 | Application browser9 | Notification Pannel10 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | System1_             | Import               | Import_Motor_instance_template_Test.csv | Open    | Update All              | OK                      | MotorGP_1            | Import(Completed)     |

  
@TC_EPE_AE_0044
@uida1696791200
@set21
@test001
@TC_EPE_AE_0027
Scenario Outline: Import Cancelled
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
And I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'
And I Select context menu item EC Application browser in application explorer as '<Application browser4>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import5>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import6>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'
And Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel10>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Application browser3 | Application browser4 | Import5                                 | Import6 | Import Conflict Dialog7 | Application browser9 | Notification Pannel10 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | System1_             | Import               | Import_Motor_instance_template_Test.csv | Open    | Cancel                  | MotorGP_1_1          | Import(Completed)     |

  
@TC_EPE_AE_0043
@uida1696791200
@set21
@test001
@TC_EPE_AE_0027
Scenario Outline: Import Skipped
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
And I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'
And I Select context menu item EC Application browser in application explorer as '<Application browser4>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import5>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import6>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'
And Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel10>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Application browser3 | Application browser4 | Import5                                 | Import6 | Import Conflict Dialog7 | Import Conflict Dialog8 | Application browser9 | Notification Pannel10 |
  | 1     | MotorGP            | MotorGP$$1.0.123   | System1_             | Import               | Import_Motor_instance_template_Test.csv | Open    | Skip All                | OK                      | MotorGP_1_1          | Import(Completed)     |

  
  
@TC_EPE_AE_0047
@uid267882473
@set21
@test002
@TC_EPE_AE_0047
Scenario Outline: Import by Selecting Relative Path
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I selected Relative Radio in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify instance lock popup Application browser in application explorer as '<Application browser5>'
When I Click on buttons in popup window Application browser in application explorer as '<Application browser6>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser7>'
And Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel8>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3                  | Import4 | Application browser5 | Application browser6 | Application browser7 | Notification Pannel8 |
  | 1     | System1_             | Import               | Import_instance_test.csv | Open    | Are you sure         | Yes                  | MotorGP_1            | Import(Completed)    |

  
@TC_EPE_AE_0054
@uid1951464184
@set21
@test004
@TC_EPE_AE_0054
Scenario Outline: Changing the Parameter Value of Exported file to Invalid
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel5>'

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3                          | Import4 | Notification Pannel5 |
  | 1     | System1_             | Import               | Import_Faulty_Parameter_Test.csv | Open    | Import(Completed)    |
  
  

@TC_EPE_AE_0050
@uida1696791200
@set21
@test001
@TC_EPE_AE_0050
Scenario Outline: Create a new Instance in the exported csv file and Import
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
And I rclick application browser folder AE Application browser in application explorer as '<Application browser3>'
And I Select context menu item EC Application browser in application explorer as '<Application browser4>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import5>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import6>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog7>'
And I Click on Buttons in Conflict Dialog popup Import Conflict Dialog in import dialog as '<Import Conflict Dialog8>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Application browser9>'
And Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel10>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Templates browser1 | Templates browser2 | Application browser3 | Application browser4 | Import5                           | Import6 | Import Conflict Dialog7 | Import Conflict Dialog8 | Application browser9 | Notification Pannel10 |
  | 1     | Motor              | MotorGP$$1.0.123   | System1_             | Import               | Import_Created_instance_Excel.csv | Open    | Update All              | OK                      | MotorGP_1            | Import(Completed)     |
  
  
  
  
@TC_EPE_AE_0051
@uid1951464184
@set21
@test004
@TC_EPE_AE_0051
Scenario Outline: Creating a Invalid folder and Importing
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify Invalid import mesaage Import Dialog in import dialog as 'must be greater than or equal to zero and less'
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel5>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3                           | Import4 | Notification Pannel5 |
  | 1     | System1_             | Import               | Import_InvalidFolder_template.csv | Open    | Import               |

  
  
@TC_EPE_AE_0052
@uid1951464184
@set21
@test004
@TC_EPE_AE_0052
Scenario Outline: Changing the Template name to Invalid name
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Import not successful'
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel5>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3                | Import4 | Notification Pannel5 |
  | 1     | System1_             | Import               | Import_Faulty_name.csv | Open    | Import               |
  

@TC_EPE_AE_0053
@uid1951464184
@set21
@test004
@TC_EPE_AE_0053
Scenario Outline: Changing Template version to Invalid
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
Then Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Import not successful'
When I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'
Then Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel5>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3                   | Import4 | Notification Pannel5 |
  | 1     | System1_             | Import               | Import_Faulty_Version.csv | Open    | Import               |
  
  
@TC_EPE_AE_0053*
@uid1951464184
@set21
@test004
@TC_EPE_AE_0053*
Scenario Outline:Abort while Import is in progress
When I create system_1 System Explorer Node in system explorer
And I select system 1 application explorer Open Application in system explorer
And I rclick application browser folder AE Application browser in application explorer as '<Application browser1>'
And I Select context menu item EC Application browser in application explorer as '<Application browser2>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Buttons in Import System1 Popup_AE Import in import dialog as '<Import4>'
And I Wait for Import popup Import in import dialog
And I Click on Buttons in Import Dialog popup AE Import Dialog in import dialog as 'OK'
And I Click on Abort AE Import Dialog in import dialog
Then Verify Message from notification panel AE Notification Pannel in message box as '<Notification Pannel5>'
When I Close all tab Deletes system AE Post Condition in conditions

Examples:
  | SlNo. | Application browser1 | Application browser2 | Import3     | Import4 | Notification Pannel5 |
  | 1     | System1_             | Import               | Bulk_AE.csv | Open    | Import               |