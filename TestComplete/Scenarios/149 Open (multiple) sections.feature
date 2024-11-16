Feature: 149 Open (multiple) sections

@TC_EPE_PE_CP_0026
@test006
Scenario Outline: Open (multiple) sections
When I Dclick Control project broswer project browser in project explorer as '<project browser1>'
And I double click container PE container dock in project explorer as '<container dock2>'

Examples:
|SlNo.|project browser1|container dock2|content|
|1|Containers|FBDSection_1|NA|

