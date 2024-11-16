Feature: 201 Edit links From PE

@TC_EPE_SWF_0033a
Scenario Outline: Edit Instance from PE by Context menu
When I Right click facet from assignment dock PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I select context submenu EC assignmentsdock in project explorer as '<assignmentsdock2>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor10>

Examples:
|SlNo.|assignmentsdock1|assignmentsdock2|Assert Workspace Editor10|
|1|AnalogInputGP_1_AInputGP|Edit Links|AnalogInputGP_1|


@TC_EPE_AE_00
Scenario Outline: Right Click on the facet and click on Edit Links from Project explorer
When I Right Click on the Facet in Assignments Section as '<facet_name>'
And I Select context menu item as '<action>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor10>'

Examples:
  | SlNo. | facet_name               | action     |Assert Workspace Editor10|
  | 1     | AnalogInputGP_1_AInputGP | Edit Links |AnalogInputGP_1          |
  

@TC_EPE_SWF_0033b
Scenario Outline: Drag and Drop Template from Application Browser to Link Editor wrt Position
When I drag template in application browser Link Editor as '<Assert Workspace Editor8>'
Then Verify Template AE Assert Workspace Editor in application explorer as '<Assert Workspace Editor9>'

Examples:
  | SlNo. | Assert Workspace Editor8 | Assert Workspace Editor9 |
  | 1     | PWMOutputGP_1$$3         | PWMOutputGP_1            |
  
  
@TC_EPE_SWF_0033c
Scenario Outline: Link between facet nodes of respective instances 
When I Link from range node to range node AE Node Instance in application explorer as 'RSPRanged$$PVRanged'
Then Verify Link Status Node Instance in application explorer


Examples:
  | SlNo. |
  | 1     |