Feature: 54 Map logical network to all communication modules

@TC_EPE_TE_0020a
@test001
Scenario Outline: Map the logical network to all communication modules - edit IP Address 
When I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window4>'

@Map_the_logical_network_-_edit_IP_Address__192.168.33.4
Examples:
  | SlNo. | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4                    |
  | 1     | Main IP address$$192.168.33.4 | Subnetwork mask$$255.255.0.0 | IP address A$$192.168.33.5 | Gateway address$$192.168.0.254 |

@Map_the_logical_network_-_edit_IP_Address__182.179.243.21
Examples:
  | SlNo. | MDI Window1                     | MDI Window2                  | MDI Window3                  | MDI Window4                   |
  | 1     | Main IP address$$182.179.243.21 | Subnetwork mask$$255.255.0.0 | IP address A$$182.179.243.22 | Gateway address$$182.179.10.0 |
  
@Map_the_logical_network_-_edit_IP_Address__10.179.244.99
Examples:
  | SlNo. | MDI Window1                    | MDI Window2                  | MDI Window3                  | MDI Window4                  |
  | 1     | Main IP address$$10.179.244.99 | Subnetwork mask$$255.255.0.0 | IP address A$$10.179.244.100 | Gateway address$$10.179.10.0 |
  
@Map_the_logical_network_-_edit_IP_Address__182.233.63.1
Examples:
  | SlNo. | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4              |
  | 1     | Main IP address$$182.233.63.1 | Subnetwork mask$$255.255.0.0 | IP address A$$182.233.63.3 | Gateway address$$0.0.0.0 |
  
@Map_the_logical_network_-_edit_IP_Address__182.233.63.8
Examples:
  | SlNo. | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4              |
  | 1     | Main IP address$$182.233.63.8 | Subnetwork mask$$255.255.0.0 | IP address A$$182.233.63.9 | Gateway address$$0.0.0.0 |


@TC_EPE_TE_0020b
@test002
Scenario Outline: Map the logical network to all communication modules - click Edit, Validate
When I selected Edit button in menu bar
And I selected Validate in menu bar

Examples:
  | SlNo. |
  | 1     |


@TC_EPE_TE_0020b
@test002
Scenario Outline: Close the logical network window in TM
When I close Logical window in controller configuration window

Examples:
  | SlNo. |
  | 1     |


 
@TC_EPE_TE_CS_0020c
Scenario Outline: Open configure window and click on IPConfig
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I Click tabitem in EIO configaration window in control expert as '<identifiers>'

@Open_configure_window_and_click_on_IPConfig__M580_standalone_P58_6040_3.20
Examples:
  | SlNo. | Project Browser RO1                                                     | identifiers |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME P58 6040$$EIO | IPConfig    |
  
@Open_configure_window_and_click_on_IPConfig__M580_standalone_P58_5040_3.20
Examples:
  | SlNo. | Project Browser RO1                                                     | identifiers |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME P58 5040$$EIO | IPConfig    |
  
@Open_configure_window_and_click_on_IPConfig__M580_standalone_P58_4040_3.20
Examples:
  | SlNo. | Project Browser RO1                                                     | identifiers |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME P58 4040$$EIO | IPConfig    |
  
@Open_configure_window_and_click_on_IPConfig__M580_standalone_H58_6040_3.20
Examples:
  | SlNo. | Project Browser RO1                                                     | identifiers |
  | 1     | Configuration$$0 : PLC bus$$0 : BME XBP 0800$$0 (1) : BME H58 6040$$EIO | IPConfig    |
  

  
  
@TC_EPE_TE_00
@test00
Scenario Outline: Validate using shortcut keys
When I Validate in TE Window using shortcut Keys
Examples:
  | SlNo. |
  | 1     |
  
@TC_EPE_TE_0020aa
Scenario Outline: Map the logical network to all communication modules - edit IP Address HSBY
When I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window4>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window5>'

@Map_the_logical_network_-_edit_IP_Address__182.233.63.1_HSBY
Examples:
  | SlNo. | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4                | MDI Window5              |
  | 1     | Main IP address$$182.233.63.1 | Subnetwork mask$$255.255.0.0 | IP address A$$182.233.63.3 | IP address B$$182.233.63.4 | Gateway address$$0.0.0.0 |


@TC_EPE_TE_CS_0020c
Scenario Outline: Open configure window and click on Service Port
When I Click tabitem in EIO configaration window in control expert as '<identifiers>'
And I select Automatic blocking of service port EIO in control expert

Examples:
  | SlNo. | identifiers |
  | 1     | ServicePort |
  