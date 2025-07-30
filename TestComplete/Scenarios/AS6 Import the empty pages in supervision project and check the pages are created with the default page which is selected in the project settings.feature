Feature: Import the empty pages in supervision project and check the pages are created with the default page which is selected in the project settings

@TC_EPE_AS_0005
@test001
Scenario Outline: Import the empty pages in supervision project and check the pages are created with the default page which is selected in the project settings
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Enter FileLocation and FileName in empty pages import dialog as '<Import file>'
And I Click on Open button from Import TE window
And I click modal dialog window project browser in project explorer as '<Button>'
And I click modal dialog window project browser in project explorer as '<dialogbox button>'
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu1>'
And I change SettingsHeader as '<Setting_Header>'
And I verify the Page Templates selected
And I click modal dialog window project browser in project explorer as '<Button>'



Examples:
  | SlNo. | project browser1 | context menu       | Import file       | Button | dialogbox button | context menu1 | Setting_Header |
  | 1     | Supervision_Test | Import Empty Pages | Import_EmptyPages | OK     | OK               | Settings      | Page Templates |
 
