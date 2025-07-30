Feature: Import the latest templates

@TC_EPE_GT_0003
@test001
Scenario Outline: Import the latest templates
When I Right Click on nodes System Explorer Node in system explorer as 'Global Templates'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I Enter FileLocation '<path>', '<folder>' and FileName '<file>' import window
And I Click on Open button from Import TE window
And I click modal dialog window project browser in project explorer as '<Button>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'

Examples:
  | SlNo. | context menu | path                                                   | folder            | file        | Button | message |
  | 1     | Import       | C:\ProgramData\Schneider Electric\Process Expert 2025\ | Templates Classic | Devices.sbk | Cancel | Import  |