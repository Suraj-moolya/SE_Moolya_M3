Feature: 95 Open DTM Browser

@TC_EPE_DTM_0002
Scenario Outline: Open DTM Browser
When I click '<menu>' in Tool Bar
And I click '<menu_item>' in Tool Bar popup window

Examples:
  | SlNo. | menu  | menu_item   |
  | 1     | Tools | DTM Browser |