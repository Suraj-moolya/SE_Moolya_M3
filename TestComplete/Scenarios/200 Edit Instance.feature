Feature: 200 Edit Instance

@TC_EPE_SWF_0032
@test002
Scenario Outline: Edit Instance from PE by Context menu
When I Right click facet from assignment dock PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I select context submenu EC assignmentsdock in project explorer as '<assignmentsdock2>'
And I Wait for Execution project browser in project explorer
And I Check instance editor Instance editor checklist in application explorer as '<Instance editor checklist2>'
And I selected Instance editor save in application explorer
And I click modal dialog window Instance editor save in application explorer as 'Yes'
And I Close tab items EC main screen in engineering client as 'CompactHWGP_1'
And I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
#And I click modal dialog window Instance editor save in application explorer as 'Yes'
And I Wait for Execution project browser in project explorer
Then Verify Facets Added or Removed context menu PE assignmentsdock in project explorer as '<assignmentsdock3>'


Examples:
  | SlNo. | assignmentsdock1 | assignmentsdock2 | Instance editor checklist2 | assignmentsdock3 | Yes | container dock1    |
  | 1     | CompactHWGP_1_OF | Edit Instance    | MXSignal$$0                | CompactHWGP_1_MX | Yes | System_1$$Generate |


#Total No. of Test Cases :1

@TC_EPE_SWF_0034
@test002
Scenario Outline: Create instance from PE
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
And I Wait for Execution project browser in project explorer

Examples:
  | SlNo. | container dock1           |
  | 1     | System_1$$Create Instance |


