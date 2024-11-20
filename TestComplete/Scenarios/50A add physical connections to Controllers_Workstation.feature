Feature: 50A add physical connections to Controllers_Workstation

@TC_EPE_TE_CS_0003
@test0001
Scenario Outline: Map Networks to the respective controllers 
When I Right Click on nodes System Explorer Node in system explorer as '<Controllers>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And 
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'
Examples:
  | SlNo. | Controllers     | context menu         | project browser1   |
  | 1     | M580_Standalone | Physical Coneections | Create Workstation |