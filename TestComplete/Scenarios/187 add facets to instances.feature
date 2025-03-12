Feature: 187 add facets to instances

@TC_EPE_SWF_0013
@test0013
Scenario Outline: Adding Facets from PE
When I Double Click on the Facet in Assingnment section as '<facet_name>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<tabname>'
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
Then I verify the section is generated successfully as '<facet_name>' '<generation_state>'
Examples:
  | SlNo. | facet_name        | instance_names         | button_name | tabname   | container dock1            | generation_state |
  | 1     | MotorGP_1_MotorGP | Running$$Fail$$Stopped | Yes         | MotorGP_1 | M580Standalone_1$$Generate | OutOfDate        |
  
  
@TC_EPE_SWF_0013a
@test0013
Scenario Outline: Adding Facets from PE from with modal dialogue window 
When I Double Click on the Facet in Assingnment section as '<facet_name>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<tabname>'
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
When I click modal dialog window project browser in project explorer as '<Button>'
Then I verify the section is generated successfully as '<facet_name>' '<generation_state>'
Examples:
  | SlNo. | facet_name        | instance_names         | button_name | tabname   | container dock1    | generation_state | Button |
  | 1     | MotorGP_1_MotorGP | Running$$Fail$$Stopped | Yes         | MotorGP_1 | System_1$$Generate | Generated        | Yes    |
  
  
@TC_EPE_SWF_0014
@test0014
Scenario Outline: Adding Facets from AE
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar2>'
And I double click on template Identifier in application browser as '<identifier5>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<identifier5>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
Then I verify the section is generated successfully as '<facet_name>' '<generation_state>'
Examples:
  | SlNo. | identifier5 | instance_names  | button_name | container dock1        | facet_name        | generation_state | MainToolBar2         | MainToolBar3     |
  | 1     | ValveGP_1   | ExternalControl | Yes         | FBDSection_1$$Generate | MotorGP_1_MotorGP | OutOfDate        | Application Explorer | Project Explorer |
  

@TC_EPE_SWF_0015
@test0015  
Scenario Outline: Adding Facets from PE by Context menu
When Right Click on any one of the Facet in Assignments Section of PE-Container and Click Go Into Instance as '<facet_name>' and perform '<action>'
When I double click on template Identifier in application browser as '<identifier5>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<identifier5>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar3>'
And I Right Click on the Particular Section and Click on Generate '<container>'
Then I verify the section is generated successfully as '<facet_name>' '<generation_state>'
Examples:
  | SlNo. | facet_name        | action         | identifier5 | instance_names  | button_name | container    | generation_state | MainToolBar3     |
  | 1     | ValveGP_1_ValveGP | Go To Instance | ValveGP_1   | ExternalControl | Yes         | FBDSection_1 | OutOfDate        | Project Explorer |

  
@TC_EPE_SWF_0016
@test0016  
Scenario Outline: Adding Multiple Facets from AE
When I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'
When I double click on template Identifier in application browser as '<identifier5>'
And I Check Any of the Facet Boxes to be added as '<instance_names>'
And I click button on the Instance editor window as '<button_name>'
And I Close the Tab by Clicking on Close as '<identifier5>'
And I navigate to explorers MainToolBar in system explorer as '<MainToolBar2>'
And I Right Click on the Particular Section and Click on Generate '<container>'
Then I verify the section is generated successfully as '<facet_names>' '<generation_state>'
Examples:
  | SlNo. | identifier5 | instance_names                               | button_name | container    | facet_names                                              | generation_state            | MainToolBar1         | MainToolBar2     |
  | 1     | ValveGP_1   | ExternalControl$$OpenPosition$$ClosePosition | Yes         | FBDSection_1 | ValveGP_1_ValveGP$$ValveGP_1_OpenPos$$ValveGP_1_ClosePos | OutOfDate$$Deleted$$Deleted | Application Explorer | Project Explorer |