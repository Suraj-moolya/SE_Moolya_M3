Feature: 65 Export the controller and devices from TM root folder

@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Export Topology from root folder 
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<sub_context_menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.sbk'
And I Click on Button in TE Explorer Window Export in ec windows explorer as 'Save'

@RClick_System_1
Examples:
  | SlNo. | Controllers | context menu | sub_context_menu |
  | 1     | System_1    | Export       | Topology         |
  
  


