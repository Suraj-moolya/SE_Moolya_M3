Feature: 214 Check all the executable mapping is present

@TC_EPE_SP_005
@test008
Scenario Outline: Check all the executable mapping is present
When I Dclick Control project broswer project browser in project explorer as '<project browser1>'
Then verify supervision mapping PE service maping editor in project explorer

Examples:
|SlNo.|project browser1|content|
|1|Executable_1|NA|
