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
 # | 4     | INTERLOCK8OFFGP_UC_1 | M580_Redundant | OK     |

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
Scenario Outline: Assign  Instance from system to different Containers in PE
When I Assign Instances from instance dock to sections in containers dock as '<param>'
And I click modal dialog window project browser in project explorer as '<Button>'
Then I Verify the facet generation status of all facets in Assignments Dock

@Assign_Instance_from_system_to_different_Containers_in_PE
Examples:
  | SlNo. | param                     | Button |
  | 1     | System_1$$M580_Standalone | OK     |
  
@Assign_Instance_from_system_to_M580_Standalone2_Containers_in_PE
Examples:
  | SlNo. | param                      | Button |
  | 1     | System_1$$M580_Standalone2 | OK     |
  
@Assign_Instance_from_system_to_M580_Standalone3_Containers_in_PE
Examples:
  | SlNo. | param                      | Button |
  | 1     | System_1$$M580_Standalone3 | OK     |
  
  
@Assign_Instance_from_system_to_different_Containers_in_Supervision_PE
Examples:
  | SlNo. | param               | Button |
  | 1     | System$$Supervision | OK     |
  
@Assign_Instance_from_Folder2_to_different_Containers_in_Supervision_PE
Examples:
  | SlNo. | param                 | Button |
  | 1     | Folder_2$$Supervision | OK     |
  
@Assign_Instance_from_Folder2_to_different_Containers_in_PE
Examples:
  | SlNo. | param                     | Button |
  | 1     | Folder_2$$M580_Standalone | OK     |
  
@Assign_Instance_from_Valvegp_1_to_different_Containers_in_PE
Examples:
  | SlNo. | param                      | Button |
  | 1     | ValveGP_1$$M580_Standalone | OK     |
  
@Assign_Instance_from_GDGP_to_different_Containers_in_PE
Examples:
  | SlNo. | param                 | Button |
  | 1     | GDGP$$M580_Standalone | OK     |
@Assign_Instance_from_system_to_M580_HSBY_1_Containers_in_PE
Examples:
  | SlNo. | param                 | Button |
  | 1     | System_1$$M580_HSBY_1 | OK     |
  



  
@TC_EPE_SWF_000
@test0001
Scenario Outline: Assign Instance to Containers section in PE
When I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'
Then I Verify the facet generation status of all facets in Assignments Dock

@Assign_Instance_to_Containers_FBDSection_1
Examples:
  | SlNo. | controller           | section      |
  | 1     | ValveGP_1            | FBDSection_1 |
  | 2     | MotorGP_1            | FBDSection_1 |
  | 3     | AnalogInputGP_1      | FBDSection_1 |
  | 4     | INTERLOCK8OFFGP_UC_1 | FBDSection_1 |
  

@Assign_Instance_to_Containers_System_1
Examples:
  | SlNo. | controller           | section  |
  | 1     | ValveGP_1            | System_1 |
  | 2     | MotorGP_1            | System_1 |
  | 3     | AnalogInputGP_1      | System_1 |
  | 4     | INTERLOCK8OFFGP_UC_1 | System_1 |

  
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

@TC_EPE_SWF_0001
@test0001
Scenario Outline: Assign Multiple Instance to System_1 Containers in PE
When I Drag and Drop the Instance to in Container as '<controller>'
Then I Verify the facet generation status of all facets in Assignments Dock
Examples:
  | SlNo. | controller           |
  | 1     | ValveGP_1            |
  | 2     | MotorGP_1            |
  | 3     | AnalogInputGP_1      |
  | 4     | INTERLOCK8OFFGP_UC_1 |