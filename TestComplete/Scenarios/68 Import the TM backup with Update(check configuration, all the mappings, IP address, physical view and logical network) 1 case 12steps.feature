Feature: 68 Import the TM backup with Update(check configuration, all the mappings, IP address, physical view and logical network) 1 case 12steps

@TC_EPE_EC_000
@test004
Scenario Outline: Import Topology Devices
When I Right Click on nodes System Explorer Node in system explorer as '<Supervision>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
When I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
And I Click on Open button from Import TE window
When I click modal dialog window project browser in project explorer as '<Button1>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser8>'
Examples:
  | SlNo. | Supervision | sub_context_menu | context menu | Button1 | Import3             | project browser4                          | project browser8            |
  | 1     | System_2    | Topology         | Import       | OK      | Deploy_ReDeploy.sbk | MessageBox$$modaldialogwindow1textbox$$OK | Import Topology (Completed) |
