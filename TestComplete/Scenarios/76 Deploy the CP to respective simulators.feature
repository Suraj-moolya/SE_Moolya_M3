Feature: 76 Deploy the CP to respective simulators

@TC_EPE_WS_0006
@test001
Scenario Outline: Deploy the CP after starting the simulator - Positive flow
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | Workstation_1 | Control      | Deploy Built Project    | OK                   | 127.0.0.1:502    | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |


@TC_EPE_WS_0007a
@test001
Scenario Outline: Deploy the CP to respective simulators - Stop Simulator
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window4 | Modal Dialog Window 16                    | project browser2 |
  | 1     | Workstation_1 | Control      | Stop                    | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Stop (Completed) |

  
@TC_EPE_WS_0007b
@test001
Scenario Outline: Deploy the CP after starting the simulator - Deploy CP
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Deploy_the_controller_after_disabling_the_password__192.168.33.4__M580_Standalone_Simulator
Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window4 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | Workstation_1 | Control      | Deploy Built Project    | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |

  
@TC_EPE_WS_0007c
@test001
Scenario Outline: Deploy the CP to respective simulators - Start Simulator
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<Topology Explorer Tree1>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | Controller    | context menu | Topology Explorer Tree1 | Modal dialog window4 | Modal Dialog Window 16                    | project browser2 |
  | 1     | Workstation_1 | Control      | Start                    | OK                   | MessageBox$$modaldialogwindow1textbox$$OK | Start (Completed) |

