Feature: Description of the new feature2


@TC_EPE_TE_CS_0016A
@test004
Scenario Outline: Open Full Screen CE
When I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'
And I selected View button in menu bar
And I selected Full Screen CE in control expert

Examples:
|SlNo.|Project Browser RO1|content|
|1|Configuration$$0 : PLC bus|NA|



@TC_EPE_TE_CS_0016B
@test005
Scenario Outline: Close Full Screen CE
When I selected Close Full Screen CE in control expert
And I selected Full Screen CE in control expert

Examples:
|SlNo.|content|
|1|NA|
