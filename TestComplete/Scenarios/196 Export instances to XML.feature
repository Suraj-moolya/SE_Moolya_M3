Feature: Create instance from PE and Export

@TC_EPE_SWF_0000
@test002
Scenario Outline: Create instance from PE
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
And I Wait for Execution project browser in project explorer

Examples:
  | SlNo. | container dock1               |
  | 1     | FBDSection_2$$Create Instance |