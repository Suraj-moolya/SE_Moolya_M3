Feature: Map associated control project to the tag container in properties

@TC_EPE_PE_AS1
Scenario Outline: Map associated control project to the tag container in properties
When I Dclick Control project broswer project browser in project explorer as '<project browser1>'
And I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock3>'
And I change controller properties with drop down options as '<options>'
And I Close tab items EC main screen in engineering client as 'TagContainer_1'

Examples:
  | SlNo. | project browser1 | assignmentsdock3           | options                                     |
  | 1     | Containers       | TagContainer_1$$Properties | Associated Control Project$$M580_Standalone |
  
  
