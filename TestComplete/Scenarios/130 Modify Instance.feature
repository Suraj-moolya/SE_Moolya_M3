Feature: Scenario_130

@TC_EPE_AE_0011_New
@test001
Scenario Outline: Modify the properties of Instances - Edit Instance
When I double click on template Identifier in application browser as '<Identifier1>'
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist2>'
And I Enter description AE Instance description in application explorer

Examples:
  | SlNo. | Identifier1 | Instance editor checklist2 |
  | 1     | MotorGP_1   | Running$$1                 |


@TC_EPE_AE_0012_New
@test002
Scenario Outline: Modify the properties of Instances - Save
When I selected Instance editor save in application explorer
Examples:
  | SlNo. | content |
  | 1     | NA      |


@TC_EPE_AE_0013_New
@test003
Scenario Outline: Modify the properties of Instances - Save and No
When I selected Instance editor save in application explorer
And I click modal dialog window Instance editor save in application explorer as 'No'

Examples:
  | SlNo. | content |
  | 1     | NA      |


@TC_EPE_AE_0014_New
@test001
Scenario Outline: Modify the properties of Instances - Close Instance
When I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'

Examples:
  | SlNo. | Instance editor close1 |
  | 1     | MotorGP_1              |


@TC_EPE_AE_0015_New
@test005
Scenario Outline: Modify the properties of Instances and generate the instance in CP - Right Click Control Executables and Generate and build
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I Wait for Execution project browser in project explorer
And I click modal dialog window project browser in project explorer as '<project browser3>'

Examples:
  | SlNo. | project browser1    | project browser2   | project browser3 |
  | 1     | ControlExecutable_1 | Generate and Build | OK               |


@TC_EPE_AE_0016_New
@test002
Scenario Outline: Modify the properties of Instances - Close Instance and click Yes
When I click modal dialog window Instance editor save in application explorer as 'Yes'

Examples:
  | SlNo. | content |
  | 1     | NA      |


@TC_EPE_AE_0017_New
@test003
Scenario Outline: Modify the properties of Instances - Close Instance and click No
When I click modal dialog window Instance editor save in application explorer as 'No'

Examples:
  | SlNo. | content |
  | 1     | NA      |


@TC_EPE_AE_0018_New
@test004
Scenario Outline: Modify the properties of Instances - Close Instance and click Cancel
When I click modal dialog window Instance editor save in application explorer as 'Cancel'

Examples:
  | SlNo. | content |
  | 1     | NA      |


@TC_EPE_AE_0014_New
@test001
Scenario Outline: Modify the properties of Instances - Save and Close Instance
When I selected Instance editor save in application explorer
And I Close instance editor tab Instance editor close in application explorer as '<Instance editor close1>'
 
Examples:
  | SlNo. | Instance editor close1 |
  | 1     | MotorGP_1              |s



