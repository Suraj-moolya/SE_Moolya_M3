Feature: 67 Do Some modification in configure side in refine online and update the project and check configure(add/delete communication/DIO/AIO modules)

@TC_EPE_EC_000
@test000
Scenario Outline: Refine Online M580 Standalone
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I Click on OK button from Reconfirm Deploy Built Project Popup window

Examples:
  | SlNo. | context menu  | Controller      |
  | 1     | Refine Online | M580_Standalone |
  
@TC_EPE_EC_000
@test000
Scenario Outline: Refine Online M580 Standalone and click on Build and Deploy changes
When I Click on Build and Deploy changes Button in refine online window
And I Click on start engine checkobox in deploy changes refine online window


Examples:
  | SlNo. | context menu  |
  | 1     | Refine Online |
  
