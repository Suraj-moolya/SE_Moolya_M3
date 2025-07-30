Feature: 188 remove facets to instances

@TC_EPE_SWF_0017
@test0017
Scenario Outline: Removing Factes from AE
When I double click on template Identifier in application browser as '<identifier5>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<identifier5>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
And I Right Click on the Particular Section and Click on Generate '<container>'
Then I verify the section is generated successfully as '<facet_name>' '<generation_state>'
Examples:
  | SlNo. | identifier5 | instance_names  | button_name | container    | facet_name        | generation_state | MainToolBar3     |
  | 1     | ValveGP_1   | ExternalControl | Yes         | FBDSection_1 | ValveGP_1_ValveGP | OutOfDate        | Project Explorer |
  
  
@TC_EPE_SWF_0018
@test0018
Scenario Outline: Remove facets from PE
When I Double Click on the Facet in Assingnment section as '<facet_name>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<identifier>'
And I Right Click on the Particular Section and Click on Generate '<container>'
Then I verify the section is generated successfully as '<facet_name>' '<generation_state>'
Examples:
  | SlNo. | facet_name        | instance_names                               | button_name | container     | generation_state | identifier |
  | 1     | MotorGP_3_MotorGP | ExternalControl$$OpenPosition$$ClosePosition | Yes         | FBDSection_1  | OutOfDate        | ValveGP_1  |
  
  
@TC_EPE_SWF_0019
@test0019
Scenario Outline: Remove Facets from PE by Context menu
When Right Click on any one of the Facet in Assignments Section of PE-Container and Click Go Into Instance as '<facet_name>' and perform '<action>'
When I double click on template Identifier in application browser as '<identifier>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<identifier>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
And I verify Status updated in Generation Section as '<facet_name>' '<status>'
And I Right Click on the Particular Section and Click on Generate '<container>'
Examples:
  | SlNo. | facet_name        | action         | identifier | instance_names | button_name | container    | facet_names                     | status             | MainToolBar3     |
  | 1     | ValveGP_1_ValveGP | Go To Instance | ValveGP_1  | OP             | Yes         | FBDSection_1 | ValveGP_1_ValveGP$$ValveGP_1_OP | OutOfDate$$Deleted | Project Explorer |