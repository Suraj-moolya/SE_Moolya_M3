Feature: 217 Open Advanced Settings


@TC_EPE_SP_006
@test009
Scenario Outline: Open Advanced Settings
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
Then verify displayed advance settings window SP in supervision project

Examples:
  | SlNo. | project browser1 | project browser2  |
  | 1     | Supervision_Test | Advanced Settings |


@TC_EPE_SP_006A
@test005
Scenario Outline: Save and Close Advance Settings
When I selected Save Refine Offline in refine offline
And I wait in seconds Refine online window in refine offline
And I selected Close Refine Offline in refine offline

Examples:
  | SlNo. |
  | 1     |
