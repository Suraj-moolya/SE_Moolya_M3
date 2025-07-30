Feature: Description of the new feature1

@TC_EPE_PE_CP_0002
@test001
Scenario Outline: Open Service Mapping Editor of M580_Standalone and map to Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'
@Map_M580_Controller_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                    |
  | 1     | M580_Standalone  | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Standalone |
  
@Map_M580_Controller3_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                     |
  | 1     | M580_Standalone3 | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Standalone3 |
  
@Map_M580_Controller4_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                     |
  | 1     | M580_Standalone4 | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Standalone3 |
  
@Map_Workstation_1_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                  |
  | 1     | M580_Standalone  | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 |
  
@Map_Workstation_1_in_M580_Standalone2
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                  |
  | 1     | M580_Standalone2 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_1 |
  
@Map_Workstation_2_in_ControlExecutable
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                  |
  | 1     | M580_Standalone2 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_2 |
  
@Map_Workstation_2_in_M580_Standalone3
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                  |
  | 1     | M580_Standalone3 | Executable       | ControlExecutable_1 | ControlExecutive_1$$Workstation_2 |
@Map_M580_HSBY_1_in_M580_HSBY_1_Control_Project
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                |
  | 1     | M580_HSBY_1      | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_HSBY_1 |



@TC_EPE_PE_CP_0004
@test001
Scenario Outline: Open Service Mapping Editor of M580_Redundant and map to Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                    |
  | 1     | M580_Redundant   | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Standalone |


@TC_EPE_PE_CP_0006
@test001
Scenario Outline: Open Service Mapping Editor of M580_Safety_Standalone and map the Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'
@Map_Controller_1
Examples:
  | SlNo. | project browser1       | project browser2 | project browser3    | project browser4                 |
  | 1     | M580_Safety_Standalone | Executable       | ControlExecutable_1 | ControlExecutive_1$$Controller_1 |
@Map_M580_Safety
Examples:s
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4                |
  | 1     | M580_Safety      | Executable       | ControlExecutable_1 | ControlExecutive_1$$M580_Safety |


@TC_EPE_PE_CP_0008
@test001
Scenario Outline: Open Service Mapping Editor of M580_Safety_Redundant and map the Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1      | project browser2 | project browser3    | project browser4                           |
  | 1     | M580_Safety_Redundant | Executable       | ControlExecutable_1 | ControlExecutive_1$$Redundant_Controller_1 |


@TC_EPE_PE_CP_0010
@test001
Scenario Outline: Open Service Mapping Editor of M340_Controller and map the Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4           |
  | 1     | M340             | Executable       | ControlExecutable_1 | ControlExecutive_1$$M340_1 |


@TC_EPE_PE_CP_0012
@test001
Scenario Outline: Open Service Mapping Editor of Quantum_Controller and map the Controller
When I Collapse control project browser PE project browser in project explorer
And I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Dclick Control project broswer project browser in project explorer as '<project browser3>'
And I Control executable dropdown PE project browser in project explorer as '<project browser4>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3    | project browser4              |
  | 1     | Quantum          | Executable       | ControlExecutable_1 | ControlExecutive_1$$Quantum_1 |


