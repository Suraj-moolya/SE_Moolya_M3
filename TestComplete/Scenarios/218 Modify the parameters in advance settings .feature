Feature: 218 Modify the parameters in advance settings 

@TC_EPE_SP_007
@test001
Scenario Outline: modify the parameters in advance settings and save it - edit, save and close
When I select Adv Settings properties SVP Project Browser RO in refine offline as '<Project Browser RO1>'
And I Edit Parameter Value AdvSettings SVP Project Browser RO in refine offline as '<Project Browser RO2>'
And I selected Save Refine Offline in refine offline
And I selected Close Refine Offline in refine offline

Examples:
  | SlNo. | Project Browser RO1                        | Project Browser RO2 |
  | 1     | supervision project$$General$$Multiprocess | 5                   |


#Total No. of Test Cases : 1

@TC_EPE_SP_007a
@test002
Scenario Outline: modify the parameters in advance settings and save it - verify 
When I select Adv Settings properties SVP Project Browser RO in refine offline as '<Project Browser RO1>'
Then Verify Parameter Value Adv Settings SVP Project Browser RO in refine offline as '<Project Browser RO2>'

Examples:
  | SlNo. | Project Browser RO1          | Project Browser RO2 |
  | 1     | Aveva$$General$$Multiprocess | 5                   |


#Total No. of Test Cases : 2