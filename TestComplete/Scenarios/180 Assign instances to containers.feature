Feature: 180 Assign instances to containers

@TC_EPE_SWF_0001
@test0001
Scenario Outline: Assign Instance to Containers in PE
When I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock
@Assign_Instance_to_Containers_in_M580_Standalone
Examples:
  | SlNo. | controller      | section         | Button |
  | 1     | ValveGP_1       | M580_Standalone | OK     |
  | 2     | MotorGP_1       | M580_Standalone | OK     |
  | 3     | AnalogInputGP_1 | M580_Standalone | OK     |
#  | 4     | INTERLOCK8OFFGP_UC_1 | M580_Redundant | OK     |

@Assign_Instance_to_Containers_in_M580_Safety
Examples:
  | SlNo. | controller      | section     | Button |
  | 1     | ValveGP_1       | M580_Safety | OK     |
  | 2     | MotorGP_1       | M580_Safety | OK     |
  | 3     | AnalogInputGP_1 | M580_Safety | OK     |
  

@TC_EPE_SWF_0001
@test0001
Scenario Outline: Assign ValveGP_2 to Containers in PE
When I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | controller | section         |
  | 1     | ValveGP_2  | M580_Standalone |

  
@TC_EPE_SWF_0002
@test0002
Scenario Outline: Assign Multiple Instance to different Containers in PE
When I Assign Instances from instance dock to sections in containers dock as '<param>'
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | param                         |
  | 1     | AnalogInputGP_1$$FBDSection_1 |
  | 2     | MotorGP_1$$FBDSection_2       |

  
@TC_EPE_SWF_000
@test0001
Scenario Outline: Assign Instance to Containers FBDSection_1 in PE
When I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | controller           | section      |
  | 1     | ValveGP_1            | FBDSection_1 |
  | 2     | MotorGP_1            | FBDSection_1 |
  | 3     | AnalogInputGP_1      | FBDSection_1 |
  | 4     | INTERLOCK8OFFGP_UC_1 | FBDSection_1 |

  
@TC_EPE_SWF_0001
@test0001
Scenario Outline: Assign Instance to Containers in Supervision in PE
When I drag and Drop the Each instance to Each Sections as '<Instance>' '<section>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock

Examples:
  | SlNo. | Instance  | Button | section          |
  | 1     | ValveGP_1 | OK     | Supervision_Test |
  | 2     | MotorGP_1 | OK     | Supervision_Test |
#  | 3     | AnalogInputGP_1  | OK     | Supervision_Test |
#  | 4     | AnalogOutputGP_1 | OK     | Supervision_Test |

