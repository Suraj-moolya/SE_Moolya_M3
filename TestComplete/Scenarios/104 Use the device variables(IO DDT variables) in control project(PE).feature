Feature: 104 Use the device variables(IO DDT variables) in control project(PE)

@TC_EPE_DTM_0014
@test001
Scenario Outline: Use the device variables(IO DDT variables) in control project(PE)
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I checked IODDT CE in elemetary variables
And I checked Device DDT CE in elemetary variables
And I selected Access to unmapped hardware CE in refine offline
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window2>'
And I selected Device DDT popup moveall CE in elemetary variables
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window3>'

Examples:
  | SlNo. | Project Browser RO1                            | Modal dialog window2 | Modal dialog window3 | content |
  | 1     | Variables & FB instances$$Elementary Variables | Next                 | OK                   | NA      |


#Total No. of Test Cases :1

