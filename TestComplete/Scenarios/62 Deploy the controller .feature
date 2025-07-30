Feature: 62 Deploy the controller 

@TC_EPE_TE_CN_0030
@test001
Scenario Outline: Deploy the controller after disabling the password
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Deploy_the_controller_after_disabling_the_password__192.168.33.4__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 192.168.33.4         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |

@Deploy_the_controller_after_disabling_the_password__182.179.243.21__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.179.243.21       | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |

@Deploy_the_controller_after_disabling_the_password__182.233.65.1__M580_Standalone3
Examples:
  | SlNo. | Controller       | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone3 | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone3 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.233.63.1         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |

@Deploy_the_controller_after_disabling_the_password__182.233.65.1__M580_Standalone4
Examples:
  | SlNo. | Controller       | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone3 | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone4 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.233.63.1         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |
    
@Deploy_the_controller_after_disabling_the_password__182.233.63.8__M580_Standalone3
Examples:
  | SlNo. | Controller       | Topology Explorer Tree1 | project dropdown2                                  | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone3 | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone3 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.233.63.8         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |
  
@Deploy_the_controller_after_disabling_the_password__182.233.63.8__M580_Standalone
Examples:
  | SlNo. | Controller      | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_Standalone | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.233.63.8         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |
@Deploy_the_M580_HSBY_1_controller_after_disabling_the_password
Examples:
  | SlNo. | Controller  | Topology Explorer Tree1 | project dropdown2                             | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5 | Modal Dialog Window 16                    | project browser2                 |
  | 1     | M580_HSBY_1 | Deploy Built Project    | Topology$$projectdropdowntextbox$$M580_HSBY_1 | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | 182.233.63.1         | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) |
  
@TC_EPE_TE_CN_0030
@test001
Scenario Outline: Deploy the controller from workstation after disabling the password
When I Right Click on nodes System Explorer Node in system explorer as '<Controller>'
And I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Select controller in context menu as '<sub_context_menu>'
And I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'
And I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'
And I Click on start engine checkobox in deploy changes refine online window
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window4>'
And I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'
Then Verify Action message in notification pannel project browser in project explorer as '<project browser2>'

@Deploy_the_Workstation_1_after_disabling_the_password__Slot_NIC_1{127.0.0.1:502}_Simulator
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     |
  | 1     | Workstation_1 | Control                 | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:502} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project |
  
  
@Deploy_the_Workstation_2_after_disabling_the_password__NIC_1{127.0.0.1:503}_Standalone
Examples:
  | SlNo. | Controller    | Topology Explorer Tree1 | project dropdown2                                 | Executables dropdown3                                     | Modal dialog window4 | Modal dialog window5       | Modal Dialog Window 16                    | project browser2                 | sub_context_menu     |
  | 1     | Workstation_2 | Control                 | Topology$$projectdropdowntextbox$$M580_Standalone | Topology$$executablesdropdowntextbox$$ControlExecutable_1 | OK                   | Slot NIC_1 {127.0.0.1:503} | MessageBox$$modaldialogwindow1textbox$$OK | Deploy Built Project (Completed) | Deploy Built Project |
  
  
@TC_EPE_TE_CN_0030a
@test001
Scenario Outline: Change service port Settings in configure window 
When I Click tabitem in EIO configaration window in control expert as '<identifiers>'
And I Double click on the Automatic blocking of service port on standby CPU in service port
Examples:
  | SlNo. | identifiers |
  | 1     | ServicePort |