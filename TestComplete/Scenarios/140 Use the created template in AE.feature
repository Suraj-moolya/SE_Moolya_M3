Feature: 140 Use the created template in AE

@TC_EPE_AE_0008
Scenario Outline: Use the created template in AE
When I search text template browser AE Templates browser in application explorer as '<Templates browser1>'
And I drag composite template drop application browser system1 AE Templates browser in application explorer as '<Templates browser2>'
Then Verify template added in Application browser AE Application browser in application explorer as '<Template>'

@search_drag_drop_sample_test_template_1.0.130
Examples:
  | SlNo. | Templates browser1 | Templates browser2   | Template    |
  | 1     | Sample_Test        | Sample_Test$$1.0.130 | Sample_Test |