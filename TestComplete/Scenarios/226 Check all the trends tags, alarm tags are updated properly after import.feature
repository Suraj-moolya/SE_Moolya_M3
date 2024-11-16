Feature: 226 Check all the trends tags, alarm tags are updated properly after import

  
@TC_EPE_SWF_0000
@test0030
Scenario Outline: Reassign Folder After Generating
When I Right Click on the Facet in Assignments Section as "<facet_name1>", "<action>"
Then Verify Action message in notification pannel container dock in project explorer as '<container dock3>'
Examples:
  | SlNo. | facet_name1       | action   | container dock3 |
  | 1     | MotorGP_1_MotorGP | Reassign | Reassign        |