Feature: Replace Template


@TC_EPE_AE_0042
@test0042
@TC_EPE_AE_0042
Scenario Outline: Replace template - Select template to replace template from Application browser 
When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC Application browser in application explorer as '<Application browser1>' 
Then verify window open as '<Window>'
When I select the template to replace in replace template as '<Replace_Template>'
And I take evidence Instance Editor in application explorer

Examples:
  | SlNo. | Application browser    | Application browser1 | Window           | Replace_Template          |
  | 1     | INTERLOCK8OFFGP$$1.0.5 | Replace Template     | Replace Template | INTERLOCK4ONGP_UC$$1.0.14 |


@TC_EPE_AE_0043
@test0043
@TC_EPE_AE_0043
Scenario Outline: Replace template - Click on OK in replace template window
When I Select button in the modal dialoge window as '<Button name>'
Then verify template and version in application browser as '<Template>'

Examples:
  | SlNo. | Button name | Template                  |
  | 1     | OK          | INTERLOCK4ONGP_UC$$1.0.14 |


@TC_EPE_AE_0044
@test0044
@TC_EPE_AE_0044
Scenario Outline: Replace template - Click on Close (X) in replace template window
When I Close modal dialog window
Then verify template and version in application browser as '<Template>'

Examples:
  | SlNo. | Button name | Template               |
  | 1     | Close       | INTERLOCK8OFFGP$$1.0.5 |


@TC_EPE_AE_0045
@test0045
@TC_EPE_AE_0045
Scenario Outline: Replace template - Click on Cancel in replace template window
When I Select button in the modal dialoge window as '<Button name>'
Then verify template and version in application browser as '<Template>'

Examples:
  | SlNo. | Button name | Template               |
  | 1     | Cancel      | INTERLOCK8OFFGP$$1.0.5 |


