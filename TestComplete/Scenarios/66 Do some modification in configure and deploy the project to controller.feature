Feature: 66 Do some modification in configure and deploy the project to controller

@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller M580 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu         |
  | 1     | Deploy Built Project |
  

@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller M580 Safety
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Safety'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu         |
  | 1     | Deploy Built Project |
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller M340 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M340_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu         |
  | 1     | Deploy Built Project |
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller Quantum
When I Right Click on nodes System Explorer Node in system explorer as 'Quantum'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu         |
  | 1     | Deploy Built Project |
  
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Controller M580 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu                        |
  | 1     | Deploy Changes/ Undo Online changes |
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Controller M580 Safety
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Safety'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu                        |
  | 1     | Deploy Changes/ Undo Online changes |
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Controller M340 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M340_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu                        |
  | 1     | Deploy Changes/ Undo Online changes |
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Quantum Controller
When I Right Click on nodes System Explorer Node in system explorer as 'Quantum'
And I Select context menu item EC project browser in project explorer as '<context menu>'

Examples:
  | SlNo. | context menu                        |
  | 1     | Deploy Changes/ Undo Online changes |
  
   
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy M580_Controller
When I Select '<IP_address>' From deploy Project window and Click on Start Engine Checkbox
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I Click on OK button from Reconfirm Deploy Built Project Popup window

Examples:
  | SlNo. | IP_address    |
  | 1     | 192.168.33.21 |
