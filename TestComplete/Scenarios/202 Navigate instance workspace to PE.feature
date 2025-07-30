Feature: 202 Navigate instance workspace to PE

@TC_EPE_PE_SWF_0039
@test0039
Scenario Outline: Navigating to instance Workspace through Edit Links
When I Click on container section PE container dock in project explorer as '<containerdock>'
And I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'
Then verify Tabs Explorer tab in system explorer as '<Explorer tab4>'
Examples:
  | SlNo. | containerdock | facet_name        | action         | Explorer tab4        |
  | 1     | System_1      | MotorGP_1_MotorGP | Go To Instance | Application Explorer |