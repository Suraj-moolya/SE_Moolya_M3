Feature: 91 Configure EPE device to M340 Controller



@TC_EPE_TE_M340
Scenario Outline: Configure EPE device to M340 Controller - Create new network
When I Right_click_selected_project_browser_item_CE System Project in topology explorer as '<System Project1>'
And I click_MenuItem_Toolbar_CE System Project in topology explorer as '<System Project2>'
And I Select_network_CE System Project in topology explorer as '<System Project3>'
And I selected Dialog OK CE in dialog ce

Examples:
  | SlNo. | System Project1         | System Project2 | System Project3 |
  | 1     | Communication$$Networks | New Network     | Ethernet        |

  
@TC_EPE_TE_M340a
@test001
Scenario Outline: Configure EPE device to M340 Controller - edit IP Address 
When I Click tabitem in EIO configaration window in control expert as '<identifiers>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>'
When I close PLC Bus window in controller configuration window
And I selected List of modified Yes button CE in dialog ce

Examples:
  | SlNo. | identifiers      | MDI Window2                  | MDI Window1             | MDI Window3                  |
  | 1     | IP Configuration | Subnetwork mask$$255.255.0.0 | IP address$$192.168.0.1 | Gateway address$$192.168.0.3 |

  
@TC_EPE_TE_M340b
Scenario Outline: Configure EPE device to M340 Controller - Channel 
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
When I Click tabitem in EIO configaration window in control expert as '<identifiers>'
When I select_item_mdi_window_CE MDI Window in refine offline as '<MDI Window1>'
And I select_item_mdi_window_CE MDI Window in refine offline as '<MDI Window2>'
When I close PLC Bus window in controller configuration window
And I selected List of modified Yes button CE in dialog ce

Examples:
  | SlNo. | MDI Window1 | MDI Window2 | Project Browser RO1                             | identifiers |
  | 1     | ETH TCP IP  | Ethernet_2  | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$1 | Channel 0   |



@TC_EPE_TE_M340c
@test001
Scenario Outline: Map the logical network to all communication modules - edit IP Address 
When I close PLC Bus window in controller configuration window
And I selected List of modified Yes button CE in dialog ce

Examples:
  | SlNo. |
  | 1     |
  
  
@TC_EPE_TE_M340c
@test002
Scenario Outline: Configure EPE device to M340 Controller - Edit communication tab
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree4>'
When I Close the Tab by Clicking on Close as '<identifier>'

@Edit_CPU_Device_Editor_in_Communication_section
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Topology Explorer Tree4 | identifier |
  | 1     | M340CPU                 | Communication           | ServerMemoryStart$$1    | ServerLengthMem$$100    | M340       |
@Edit_NOE_Device_Editor_in_Communication_section
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Topology Explorer Tree4 | identifier |
  | 1     | MNOEIOSClient           | Communication           | ClientMemoryStart$$1    | ClientLengthMem$$600    | M340       |
  
  
@TC_EPE_TE_CN_0022d
@test003
Scenario Outline: Configure EPE device to M340 Controller - Map M340 to Ethernet Network
When I Right Click on nodes System Explorer Node in system explorer as '<Topology Explorer Tree1>'
And I Select context menu item EC project browser in project explorer as '<Topology Explorer Tree2>'
And I Select particular '<network>' for each  Controller in physical connection
When I click modal dialog window project browser in project explorer as '<Button>'

Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | network    | Button |
  | 1     | M340                    | Physical Connections    | SE_Network | OK     |
  