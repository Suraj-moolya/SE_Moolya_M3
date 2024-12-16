Feature: 35 Check consistency with auto generation enable in refine offline

@TC_EPE_TE_0006
Scenario Outline: Check consistency with auto generation enable in refine offline
Then I verify Status updated in Generation Section as '<facet_name>' '<status>'

Examples:
  | SlNo. | facet_name                                       | status   |
  | 1     | AnalogOutputGP_1_AOGP$$AnalogOutputGP_1_AOGP_AOS | Unlinked |