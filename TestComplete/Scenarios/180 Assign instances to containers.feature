Feature: 180 Assign instances to containers

@TC_EPE_SWF_0001
@test0001
Scenario Outline: Assign Instance to Containers in PE
When I Double Click on Containers as '<identifier>'
And I Drag and Drop the Instance in Container Section Under System as '<instance>'
And I click button on the Assignment Viewer window as '<button_name>'
Examples:
  | SlNo. | identifier | instance  | button_name |
  | 1     | Containers | ValveGP_1 | OK          |
  
  
@TC_EPE_SWF_0002
@test0002
Scenario Outline: Creating Multiple folders and Sections
When I Double Click on Containers as '<identifier>'
And I Right click on the ControlProject_1 in Containers window and create FBDSections as '<num_sections>'
And I Drag and Drop the Instance in controlproject_1 under Container Section  as '<controller>' '<section>'
And I drag and Drop the Each instance to Each Sections as '<controllers>' '<sections>'
Examples:
  | SlNo. | identifier | num_sections | controller      | section          | controllers          | sections                   |
  | 1     | Containers | 5            | AnalogInputGP_1 | ControlProject_1 | MotorGP_1$$ValveGP_1 | FBDSection_2$$FBDSection_3 |