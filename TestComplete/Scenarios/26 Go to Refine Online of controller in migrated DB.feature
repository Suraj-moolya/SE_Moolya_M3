Feature: 26 Go to Refine Online of controller in migrated DB

Scenario Outline: Open Refine Online window
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I Click on OK button from Reconfirm Deploy Built Project Popup window

Examples:
  | SlNo. | context menu  | Controller      |
  | 1     | Refine Online | M580_Standalone |