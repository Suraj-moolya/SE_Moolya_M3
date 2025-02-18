Feature: 66 Do some modification in configure and deploy the project to controller

@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller M580 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu         | project browser2                 |
  | 1     | Deploy Built Project | Deploy Built Project (Completed) |
  

@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller M580 Safety
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Safety'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu         | project browser2                 |
  | 1     | Deploy Built Project | Deploy Built Project (Completed) |

  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller M340 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M340_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu         | project browser2                 |
  | 1     | Deploy Built Project | Deploy Built Project (Completed) |
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Controller Quantum
When I Right Click on nodes System Explorer Node in system explorer as 'Quantum'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu         | project browser2                 |
  | 1     | Deploy Built Project | Deploy Built Project (Completed) |
  
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Controller M580 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
When I selected Rename Pop up Ok in message box
And I Click on OK button from Reconfirm Deploy Built Project Popup window
Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'
Examples:
  | SlNo. | context menu                         | project browser3                                 |
  | 1     | Deploy Changes / Undo Online Changes | Deploy Changes / Undo Online Changes (Completed) |
      

  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Controller M580 Safety
When I Right Click on nodes System Explorer Node in system explorer as 'M580_Safety'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu                        | project browser2                 |
  | 1     | Deploy Changes/ Undo Online changes | Deploy Built Project (Completed) |
  
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Controller M340 Standalone
When I Right Click on nodes System Explorer Node in system explorer as 'M340_Standalone'
And I Select context menu item EC project browser in project explorer as '<context menu>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | context menu                        | project browser2                 |
  | 1     | Deploy Changes/ Undo Online changes | Deploy Built Project (Completed) |
  
@TC_EPE_EC_000
@test000
Scenario Outline: Deploy Changes for Quantum Controller
When I Right Click on nodes System Explorer Node in system explorer as 'Quantum'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I click modal dialog window Instance editor save in application explorer as 'OK'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
When I click modal dialog window Instance editor save in application explorer as 'OK'
And I Click on OK button from Reconfirm Deploy Built Project Popup window
Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'
Examples:
  | SlNo. | context menu                        | project browser2                                                            | project browser3                                 |
  | 1     | Deploy Changes/ Undo Online changes | Obtaining Candidates for *Deploy Changes / Undo Online Changes* (Completed) | Deploy Changes / Undo Online Changes (Completed) |

  
   
@TC_EPE_EC_000
@test000
Scenario Outline: Select IP and Click on Start Engine 
When I Select '<IP_address>' From deploy Project window and Click on Start Engine Checkbox
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I Click on OK button from Reconfirm Deploy Built Project Popup window
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | IP_address    | project browser2                 |
  | 1     | 192.168.33.21 | Deploy Built Project (Completed) |

  
@TC_EPE_PE_CP_00
@test00
Scenario Outline: Save and Close configuration with configuration pop up
When I wait in seconds Refine online window in refine offline
And I selected Save Refine Offline in refine offline
And I wait in seconds Refine online window in refine offline
And I click modal dialog window Instance editor save in application explorer as 'OK'
And I selected Close Refine Offline in refine offline
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | project browser2                   |
  | 1     | Close Configure Editor (Completed) |

  
@TC_EPE_PE_CP_00
@test00
Scenario Outline: Save and Close configuration without configuration pop up
When I wait in seconds Refine online window in refine offline
And I selected Save Refine Offline in refine offline
And I wait in seconds Refine online window in refine offline
And I selected Close Refine Offline in refine offline
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'
Examples:
  | SlNo. | project browser2              |
  | 1     | Close Page Editor (Completed) |

  
  
@TC_EPE_TE_00
@test00
Scenario Outline: Enter Controller password as Schneider0!
When I Enter Password as Schneider0! in Password PopUp available for Controller
And I Click on OK in Password popup window
Examples:
  | SlNo. |
  | 1     |