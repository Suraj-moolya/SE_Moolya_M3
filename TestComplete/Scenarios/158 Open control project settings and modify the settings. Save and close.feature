﻿Feature: 158 Open control project settings and modify the settings. Save and close(change expression, enable auto generate)

@TC_EPE_SP_006
@test009
Scenario Outline: Open  Settings
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'


Examples:
  | SlNo. | project browser1 | project browser2 |
  | 1     | M580_Standalone  | Settings         |
  
  
@TC_EPE_SP_006
@test009
Scenario Outline: Select settings Tab : Generation
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<project browser2>'
And I change SettingsHeader  in settings window as '<Setting_Header>'
And I change Settings option with drop down options as '<options>'
And I click on Yes button in Message Box
And I click modal dialog window project browser in project explorer as '<Button1>'
And I click on Yes button in Message Box

Examples:
  | SlNo. | project browser1 | project browser2 | options | Button1 | Setting_Header |
  | 1     | M580_Standalone  | Settings         | True    | OK      | Generation     |