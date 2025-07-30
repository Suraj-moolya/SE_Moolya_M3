Feature: Eco Struxure Process Expert1

@TC_EPE_PE_CP_0001_1_1
@repeatedtestcase
@test001
Scenario Outline: Check existing Executable Status - right click control project and generate
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
@Generate_general_controlproject
Examples:
  | SlNo. | container dock1            | container dock3 |
  | 1     | ControlProject_1$$Generate | Generate        |
  
@Generate_M580_Standalone_controlproject
Examples:
  | SlNo. | container dock1           | container dock3 |
  | 1     | M580_Standalone$$Generate | Generate        |
  
@Generate_M580_Safety_controlproject
Examples:
  | SlNo. | container dock1       | container dock3 |
  | 1     | M580_Safety$$Generate | Generate        |

  
@Generate_general_Supervision_Test
Examples:
  | SlNo. | container dock1            | container dock3 |
  | 1     | Supervision_Test$$Generate | Generate        |
  
@Generate_FBDSection2
Examples:
  | SlNo. | container dock1        | container dock3 |
  | 1     | FBDSection_2$$Generate | Generate        |


@TC_open_refine_online
@test002
Scenario Outline: Open Refine offline and Close
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I entered Refine online window in refine offline
And I selected Close in refine offline
Then Verify Action message in notification pannel project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                         |
  | 1     | M580_Standalone  | Refine           | Close Control Project Editor (Completed) |



@TC_header
@test006
Scenario Outline: Turn on State header in CP browser
When I RClick CPB in project explorer as '<project browser2>'
And I customize CPB header checkbox PE project browser in project explorer as '<project browser3>'
And I Click popup button object project browser in project explorer as '<project browser4>'
Then Verify header control project browser PE project browser in project explorer as '<project browser5>'

Examples:
  | SlNo. | project browser2 | project browser3 | project browser4                            | project browser5 |
  | 1     | Customize        | State$$1         | EngineeringClient$$rclickmenutextbox$$Apply | State            |



@TC_verify_notbuilt
@test008
Scenario Outline: To verify not built state
When I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
Then Verify build state of control executable PE project browser in project explorer as '<project browser3>'

@verify_notbuilt_for_m580_standalone
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                                | content |
  | 1     | M580_Standalone  | Executables      | M580_Standalone$$ControlExecutable_1$$NotBuilt | NA      |



@TC_verify_built
@test009
Scenario Outline: To verify built state
When I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
Then Verify build state of control executable PE project browser in project explorer as '<project browser3>'

@verify_built_for_m580_standalone
Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                            | content |
  | 1     | M580_Standalone | Executables       | M580_Standalone$$ControlExecutable_1$$Built | NA      |



@TC_verify_outofdate
@test010
Scenario Outline: To verify out of date
When I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
Then Verify build state of control executable PE project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1 | project browser2 | project browser3                                 | content |
  | 1     | ControlProject_1 | Executables      | ControlProject_1$$ControlExecutable_1$$OutOfDate | NA      |




