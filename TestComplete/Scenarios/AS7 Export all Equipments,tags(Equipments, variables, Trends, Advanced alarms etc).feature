Feature: Export all Equipments,tags(Equipments, variables, Trends, Advanced alarms etc)

@TC_EPE_AS_0005
@test001
Scenario Outline: Export all Equipments,tags(Equipments, variables, Trends, Advanced alarms etc)
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I click on '<verticalbar button>' in Refine window
And I click on '<horizontalbar button>' in equipments tab
And I enter the filename '<name>' and file location in the Export Data window
And I Click on '<btn>' button in the Export Data window
And I Click on '<menu>' menu in the Refine window System Model
And I click on '<horizontalbar button>' in equipments tab
And I enter the filename '<name1>' and file location in the Export Data window
And I Click on '<btn>' button in the Export Data window
And I Click on '<menu1>' menu in the Refine window System Model
And I click on '<horizontalbar button>' in equipments tab
And I enter the filename '<name2>' and file location in the Export Data window
And I Click on '<btn>' button in the Export Data window
And I Click on '<menu2>' menu in the Refine window System Model
And I click on '<horizontalbar button>' in equipments tab
And I enter the filename '<name3>' and file location in the Export Data window
And I Click on '<btn>' button in the Export Data window

Examples:
  | SlNo. | project browser1 | context menu | verticalbar button     | horizontalbar button | name        | name1      | name2   | name3   | btn  | menu      | menu1  | menu2  |
  | 1     | Supervision_Test | Refine       | AID_System ModelButton | AID_Export AllButton | Equipments_ | Variables_ | Alarms_ | Trends_ | Save | Variables | Alarms | Trends |