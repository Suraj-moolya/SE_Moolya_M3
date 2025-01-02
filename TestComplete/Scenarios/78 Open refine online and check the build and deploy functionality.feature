Feature: 78 Open refine online and check the build and deploy functionality

@TC_EPE_WS_0011
@test001
Scenario Outline: Open refine online and check the build and deploy functionality
When I selected Build and Deploy Changes in control expert
And I selected List of modified Yes button CE in dialog ce
And I click modal dialog window Modal dialog window in message box as '<Modal dialog window1>'
Then Verify notification panel message Notification Pannel in message box as '<Notification Pannel2>'

Examples:
|SlNo.|Modal dialog window1|Notification Pannel2|content|
|1|OK|Build and Deploy Changes (Completed)|NA|


#Total No. of Test Cases :1

