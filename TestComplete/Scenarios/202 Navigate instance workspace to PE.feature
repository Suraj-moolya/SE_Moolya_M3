Feature: 202 Navigate instance workspace to PE

@TC_EPE_PE_SWF_0039
@test0039
Scenario Outline: Navigating to instance Workspace through Edit Links
When I Click on container section PE container dock in project explorer as '<containerdock>'
And I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then I verify that I have navigated to the '<tabname>'
Examples:
  | SlNo. | containerdock | facet_name        | action         | tabname              |
  | 1     | FBDSection_1  | MotorGP_3_MotorGP | Go To Instance | Application Explorer |