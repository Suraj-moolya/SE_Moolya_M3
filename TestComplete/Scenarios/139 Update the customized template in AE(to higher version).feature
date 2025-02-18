Feature: 139 Update the customized template in AE(to higher version)


@TC_EPE_GT_0007
Scenario Outline: Update the customized template in AE(to higher version)
When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC Application browser in application explorer as '<Menu Item>'
And I click modal dialog window Modal dialog window in message box as '<Button>'
Then Verify Action message in notification pannel project browser in project explorer as '<Message>'

@Update_the_sample_test_template_to_higher_version
Examples:
  | SlNo. | Application browser  | Menu Item       | Message                              | Button |
  | 1     | Sample_Test$$1.0.126 | Update Template | Update Instance Template (Completed) | OK     |

