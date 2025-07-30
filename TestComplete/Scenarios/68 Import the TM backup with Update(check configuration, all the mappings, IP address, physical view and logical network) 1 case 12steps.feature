Feature: 68 Import the TM backup with Update(check configuration, all the mappings, IP address, physical view and logical network) 1 case 12steps

@TC_EPE_EC_000
@test004
Scenario Outline: Import Topology Devices
When I Right Click on nodes System Explorer Node in system explorer as '<Supervision>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
And I Enter FileLocation and FileName to be Imported Import in import dialog as '<Import3>'
#And I Click on Open button from Import TE window
#And I click modal dialog window project browser in project explorer as '<Button>'
#And I click modal dialog window project browser in project explorer as '<Button1>'
And I click modal dialog window project browser in project explorer as '<Button2>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser8>'

@Import_Topology_System_1
Examples:
  | SlNo. | Supervision | sub_context_menu | context menu | Button2 | Import3  | project browser4                          | project browser8            | Button  | Button1    |
  | 1     | System_1    | Topology         | Import       | OK      | demo.sbk | MessageBox$$modaldialogwindow1textbox$$OK | Import Topology (Completed) | Resolve | Create All |
  
@Import_Topology_System_2
Examples:
  | SlNo. | Supervision | sub_context_menu | context menu | Button2 | Import3  | project browser4                          | project browser8            | Button  | Button1    |
  | 1     | System_2    | Topology         | Import       | OK      | demo.sbk | MessageBox$$modaldialogwindow1textbox$$OK | Import Topology (Completed) | Resolve | Create All |
 
@Import_Topology_System_3
Examples:
  | SlNo. | Supervision | sub_context_menu | context menu | Button2 | Import3  | project browser4                          | project browser8            | Button  | Button1    |
  | 1     | System_3    | Topology         | Import       | OK      | demo.sbk | MessageBox$$modaldialogwindow1textbox$$OK | Import Topology (Completed) | Resolve | Create All |
 