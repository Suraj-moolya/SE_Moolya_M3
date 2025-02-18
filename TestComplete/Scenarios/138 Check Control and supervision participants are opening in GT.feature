Feature: 138 Check Control and supervision participants are opening in GT

@TC_EPE_GT_0001
Scenario Outline: Check Control Participants are opening in GT
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Right Click on control template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on fit to content button in global template explorer
And I Right Click on motor template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Right Click on logic template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on templatizer button in global template explorer
And I Click on open control participant button in global template explorer

Examples:
  | SlNo. | Templates browser         | menu item |
  | 1     | Motorgp$$MotorGP$$1.0.123 | Edit      |
  
  
@TC_EPE_GT_0002
Scenario Outline: Check Supervision Participants are opening in GT
When I Search text and Right-Click GTE global template search in global template explorer as '<Templates browser>'
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Right Click on supervision template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Right Click on genie template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Right Click on pump right genie template header in global template explorer
And I Select context menu item EC global template core in global template explorer as '<menu item>'
And I Click on templatizer button in global template explorer
And I Click on open participant button in global template explorer
Then Verify Action message in notification pannel project browser in project explorer as '<Message>'

Examples:
  | SlNo. | Templates browser         | menu item | Message                                           |
  | 1     | Motorgp$$MotorGP$$1.0.123 | Edit      | Open Supervision Include Genie Editor (Completed) |

  
@TC_EPE_GT_0002A
Scenario Outline: Close Supervision Participants without saving and close all tabs
When I click close tool bar button in project explorer
And I click modal dialog window Modal dialog window in message box as '<Button>'
Then Verify Action message in notification pannel project browser in project explorer as '<Message>'
When I selected Close Refine Offline in refine offline
And I close all tabs except system explorer in Engineering Client

Examples:
  | SlNo. | Button | Message                                            |
  | 1     | No     | Close Supervision Include Genie Editor (Completed) |
  
