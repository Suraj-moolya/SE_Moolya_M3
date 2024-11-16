Feature: 181 Move instances from Section to other section

@TC_EPE_SWF_0003
@test001
@181
Scenario Outline: Moving the Instance from One section to Another without Generating
When I Click on container section PE container dock in project explorer as '<container dock1>'
And I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as '<assignmentsdock2>'
And I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock3>'
And I Wait for Execution assignmentsdock in project explorer
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock4>'

Examples:
  | SlNo. | container dock1 | assignmentsdock2     | assignmentsdock3       | assignmentsdock4  |
  | 1     | FBDSection_1    | LockOn$$FBDSection_2 | FBDSection_2$$Generate | LockOn$$Generated |



@TC_EPE_SWF_0004
@test002
@181
Scenario Outline: Moving the Instance from One section to Another after Generating
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock1>'
And I Wait for Execution assignmentsdock in project explorer
And I Click on container section PE container dock in project explorer as '<container dock2>'
And I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as '<assignmentsdock3>'
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock4>'
When I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock5>'
And I Wait for Execution assignmentsdock in project explorer
Then Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock6>'

Examples:
  | SlNo. | assignmentsdock1       | container dock2 | assignmentsdock3     | assignmentsdock4 | assignmentsdock5       | assignmentsdock6  |
  | 1     | FBDSection_1$$Generate | FBDSection_1    | LockOn$$FBDSection_2 | LockOn$$Moved    | FBDSection_2$$Generate | LockOn$$Generated |


#Total No. of Test Cases : 2
