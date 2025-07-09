Feature: 181 Move instances from Section to other section

@TC_EPE_SWF_0003
@test001
@181
Scenario Outline: Moving the Instance from One section to Another without Generating
When I Click on container section PE container dock in project explorer as '<container dock1>'
And I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as '<assignmentsdock2>'
And I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock3>'
#And I Wait for Execution assignmentsdock in project explorer
When I click modal dialog window project browser in project explorer as '<Button>'
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock4>'

Examples:
  | SlNo. | container dock1 | assignmentsdock2           | assignmentsdock3       | assignmentsdock4        | Button |
  | 1     | System_1        | ValveGP_1_OP$$FBDSection_1 | FBDSection_1$$Generate | ValveGP_1_OP$$Generated | Yes    |



@TC_EPE_SWF_0004
@test002
@181
Scenario Outline: Moving the Instance from One section to Another after Generating
When I Click on container section PE container dock in project explorer as '<container dock2>'
And I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as '<assignmentsdock3>'
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock4>'
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock5>'
And I Wait for Execution assignmentsdock in project explorer
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock6>'

Examples:
  | SlNo. | container dock2 | assignmentsdock3      | assignmentsdock4 | assignmentsdock5       | assignmentsdock6   |
  | 1     | System_1        | LockOn1$$FBDSection_1 | LockOn1$$Moved   | FBDSection_1$$Generate | LockOn1$$Generated |


#Total No. of Test Cases : 2



@TC_EPE_SWF_0004a
@test001
@181
Scenario Outline: Select the section from containers 
When I Click on container section PE container dock in project explorer as '<container dock1>'
Examples:
  | SlNo. | container dock1 |
  | 1     | System_1        |