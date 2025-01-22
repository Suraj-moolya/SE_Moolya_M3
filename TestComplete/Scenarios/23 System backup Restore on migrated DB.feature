Feature: 23 System backup Restore on migrated DB

@TC_EPE_SS_0019
@test0001
Scenario Outline: System Back Up
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Click on Browse Button in System backup Window
And I Enter FileLocation and FileName to be Imported Import in import dialog as 'demo1'
And I Click CheckBox in System backup Window as '<prop>'
And I Click on Button in Back up  window as '<button>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'
Examples:
  | SlNo. | context menu | prop              | button | message |
  | 1     | Back Up      | Back up templates | Save   | Backup System |
  

@TC_EPE_SS_0019
@test0001
Scenario Outline: System Restore
When I Right Click on nodes System Explorer Node in system explorer as 'Systems Explorer'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import>'
And I Click on Button in Back up  window as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'
Examples:
  | SlNo. | context menu | Import  | message |
  | 1     | Restore      | backup  | Restore System |