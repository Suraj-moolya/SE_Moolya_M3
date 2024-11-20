Feature: 55 Map the EPE devices to controller

@TC_EPE_TE_CS_0021
@test0001
Scenario Outline: Create IO Device - Modbus TCP
When I Right Click on nodes System Explorer Node in system explorer as 'Devices'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Examples:
  | SlNo. | context menu     | controller |
  | 1     | Create Device-IO | Modbus TCP |
  
  
@TC_EPE_TE_CN_0021a
@test001
Scenario Outline: Map Modbus TCP device to Controller - select template
When I search template browser EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Select template EC Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 |
  | 1     | ETesysTHW               | ETesysTHW$$3.1.5        |

  
@TC_EPE_TE_CN_0021b
@test002
Scenario Outline: Map Modbus TCP device to Controller - open template, add IP and SubnetMask, close Editor tab
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree4>'
When I Close the Tab by Clicking on Close as '<identifier>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | Topology Explorer Tree4 | identifier |
  | 1     | ETesysTHW               | Communication           | IPAddress$$192.168.10.2 | SubnetMask$$255.255.0.0 | ETesysTHW  |

  
  
@TC_EPE_TE_CN_0021c
@test003
Scenario Outline: Map Modbus TCP device to Controller - add Ethernet Network
When I RClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Click on MenuItem in TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 |
  | 1     | ETesysTHW               | Physical Connections    | EthernetNetwork_1       |

  
  
@TC_EPE_TE_CS_0022
@test0001
Scenario Outline: Create IO Device - EtherNet/IP
When I Right Click on nodes System Explorer Node in system explorer as 'Devices'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Select controller in context menu as '<controller>'
Examples:
  | SlNo. | context menu     | controller  |
  | 1     | Create Device-IO | EtherNet/IP |
  
  
@TC_EPE_TE_CN_0022a
@test001
Scenario Outline: Map EtherNet IP device to Controller - select template
When I search template browser EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Select template EC Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2   |
  | 1     | EIPGenericDeviceHW      | EIPGenericDeviceHW$$1.0.3 |
  
  
@TC_EPE_TE_CN_0022b
@test002
Scenario Outline: Map EtherNet IP device to Controller - open template, add IP and SubnetMask, close Editor tab
When I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
When I Close the Tab by Clicking on Close as '<identifier>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 | identifier         |
  | 1     | EIPGenericDeviceHW      | Communication           | IPAddress$$192.168.10.2 | EIPGenericDeviceHW |

  
@TC_EPE_TE_CN_0022c
@test003
Scenario Outline: Map EtherNet IP device to Controller - add Ethernet Network
When I RClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'
And I Click on MenuItem in TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'
And I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'
Examples:
  | SlNo. | Topology Explorer Tree1 | Topology Explorer Tree2 | Topology Explorer Tree3 |
  | 1     | EIPGenericDeviceHW      | Physical Connections    | EthernetNetwork_1       |








