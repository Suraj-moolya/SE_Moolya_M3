Feature: 189 add links in instance workspaces


@TC_EPE_AE_00
Scenario Outline: Link between facet nodes of respective instances 
When I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'
Then Verify Link Status Node Instance in application explorer


Examples:
  | SlNo. |
  | 1     |


@TC_EPE_AE_00
Scenario Outline: Drag and Drop Template from Application Browser to Link Editor wrt Position
When I drag template in application browser Link Editor as '<Assert Workspace Editor8>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'

Examples:
  | SlNo. | Assert Workspace Editor8 | Assert Workspace Editor9 |
  | 1     | PWMOutputGP_1$$1         | PWMOutputGP_1            |
  
  
@TC_EPE_AE_00
Scenario Outline: Right Click on the facet and click on Edit Links from Project explorer
When I Right Click on the Facet in Assignments Section as "<facet_name>" "<action>"
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor10>'

Examples:
  | SlNo. | facet_name               | action     |Assert Workspace Editor10|
  | 1     | AnalogInputGP_1_AInputGP | Edit Links |AnalogInputGP_1          |
  
@TC_EPE_AE_00
Scenario Outline: Right Click on the Instance and click on Edit Links from Apllication explorer
When I rclick application browser template AE Application browser in application explorer as '<facet_name>'
And I Select context menu item as '<action>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor10>'

Examples:
  | SlNo. | facet_name               | action     |Assert Workspace Editor10|
  | 1     | AnalogInputGP_1$$1.0.138 | Edit Links |AnalogInputGP_1          |