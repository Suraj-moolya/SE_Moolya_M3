Feature: 60 Check all the devices mapped for controller

@TC_EPE_
@test0011
Scenario Outline: Check all the devices mapped for controller is available in control project
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'


Examples:
  | SlNo. | project browser1 | project browser2   |
  | 1     | Executable_1     | Open Built Project |
  
@Scenario_60
@test001
Scenario Outline: Check all the devices mapped for controller is available in control project
When I selected Tools button in menu bar
And I selected DTM Browser in menu bar
Then Verify Mapped DTM device present CE Project Browser RO in refine offline as '<Project Browser RO1>'

Examples:
  | SlNo. | Project Browser RO1 |
  | 1     | 192.168.0.1         |
