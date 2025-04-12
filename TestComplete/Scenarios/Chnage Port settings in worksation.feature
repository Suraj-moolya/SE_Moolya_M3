Feature: Chnage Port settings in worksation

@TC_EPE_TE_CS_0002
@test0002
Scenario Outline: Change port settings in Workstation_2
When I Double Click on propeties as '<property>' available when window is open
And I Expand on propeties header as '<property2>' available when window is open
When I Change the port number of workstation as '<port_number>'
And I click modal dialog window Instance editor save in application explorer as 'Yes'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser1>'

Examples:
  | SlNo. | property        | property2     | port_number             | project browser1                   |
  | 1     | ControlExpert_1 | Configuration | Configuration$$502$$503 | Update Control Service (Completed) |
  
  
