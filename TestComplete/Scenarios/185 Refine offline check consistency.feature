Feature: 185 Refine offline check consistency

@TC_EPE_SWF_0011
@test0011
Scenario Outline: Open Refine Offline of M580 Control Project through context menu
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | M580_Standalone  | Refine           |
  
  
  
@TC_EPE_SWF_0012
@test0012
Scenario Outline: Creating a Safety M580 Control Project
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'

Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | ControlProject_1 | Refine           |
  

  
