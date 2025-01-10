Feature: 3.System backup Scheduler

@TC_EPE_SS_0019
@test0001
Scenario Outline: System backup Scheduler
When I open system server console show hidden icon in windows explorer
And I selected Settings Menu in settings
And I selected '<option>' in settings
And I selected '<system>' in System Backup Sheduler window
And I click '<option1>' Checkbox in System Backup Sheduler window
And I select '<freq>' from the Frequency dropdown in the System Backup Scheduler window
And I click on Save button in System Backup Scheduler window
And I click on '<button>' in Confirmation popup window
 

Examples:
  | SlNo. | option                  | system   | option1 | freq   | button |
  | 1     | System Backup Scheduler | System_1 | Enabled | Weekly | Yes    |