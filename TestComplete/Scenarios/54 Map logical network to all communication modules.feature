Feature: 54 Map logical network to all communication modules

@TC_EPE_TE_0020a
@test001
Scenario Outline: Map the logical network to all communication modules - edit IP Address 
When I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window4>'
Examples:
  | SlNo. | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4                   |
  | 1     | Main IP address$$192.168.33.4 | Subnetwork mask$$255.255.0.0 | IP address A$$192.168.33.4 | Gateway address$$192.168.33.4 |


#Total No. of Test Cases : 1

@TC_EPE_TE_0020b
@test002
Scenario Outline: Map the logical network to all communication modules - click Edit, Validate
When I selected Edit button in menu bar
And I selected Validate in menu bar

Examples:
  | SlNo. | content |
  | 1     | NA      |

#Total No. of Test Cases : 2

@TC_EPE_TE_0020b
@test002
Scenario Outline: Close the logical network window in TM
When I close Logical window in controller configuration window

Examples:
  | SlNo. |
  | 1     |

@TC_EPE_TE_0020a
@test001
Scenario Outline: Map the logical network to all communication modules - edit IP Address (192.168.33.4)
When I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window2>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window3>'
And I edit IP Address in configure MDI Window in refine offline as '<MDI Window4>'
Examples:
  | SlNo. | MDI Window1                   | MDI Window2                  | MDI Window3                | MDI Window4                   |
  | 1     | Main IP address$$192.168.33.4 | Subnetwork mask$$255.255.0.0 | IP address A$$192.168.33.4 | Gateway address$$192.168.33.4 |
