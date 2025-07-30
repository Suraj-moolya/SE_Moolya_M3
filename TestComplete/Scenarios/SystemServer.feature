Feature: Eco Struxure Process Expert_Desktop Automation_SRS_TestCases_202407030652351

@TC_EPE_SS_0001
@test001
Scenario Outline: System Server Launch
When I start system server Log In in login page
Then Verify that the User Login Dialogue window appeared
Examples:
  | SlNo. |
  | 1     |


@TC_EPE_SS_0002
@test0002
Scenario Outline: Enter Valid password and Login in SS
When I entered User name in login page as '<User name1>'
And I entered Password in login page as '<Password2>'
And I selected Log In in login page
And I open system server console show hidden icon in windows explorer
Then verify text in system server console Console in server console as '<Console1>'

Examples:
  | SlNo. | User name1     | Password2    | Console1                          |
  | 1     | SE_Moolya_Test | P@ssw0rd1234 | A user was successfully logged on |
  
@TC_EPE_SS_0002
@test0002
Scenario Outline: Enter Valid only password  and Login in SS
When I entered Password in login page as '<Password2>'
And I selected Log In in login page
And I open system server console show hidden icon in windows explorer
Then verify text in system server console Console in server console as '<Console1>'

Examples:
  | SlNo. | Password2    | Console1                    |
  | 1     | P@ssw0rd1234 | A user session was unlocked |


@TC_EPE_SS_0003
@test0003 
Scenario Outline: Open SS from system tray and click on SS start and wair for SS ready 
When I open system server console show hidden icon in windows explorer
And I selected Action Menu in action
And I selected Start server in action
Then verify text in system server console Console in server console as '<Console1>'

Examples:
  | SlNo. | Console1        |
  | 1     | Server is ready |
  
@TC_EPE_SS_0003
@test0003 
Scenario Outline: Open SS from system tray
When I open system server console show hidden icon in windows explorer
Examples:
  | SlNo. |
  | 1     |
  
@TC_EPE_SS_0004
@test0004
Scenario Outline: Open SS from system tray and click on SS stop and wait for SS stop
#When I select from system server icon Console in server console as 'Stop'
When I selected Action Menu in action
And I selected Stop server in action
And I click on tab and enter
Then verify system server stopped from Flow document in server console

Examples:
  | SlNo. |
  | 1     |

  

@TC_EPE_SS_0005
@test0005
Scenario Outline: Enter InValid password and Login in SS
When I entered User name in login page as '<User name1>'
And I entered Password in login page as '<Password2>'
And I selected Log In in login page
Then verify content Log On Dialogue in login page as '<Log On Dialogue3>'
 
Examples:
  | SlNo. | User name1     | Password2     | Log On Dialogue3                                                                                        |
  | 1     | SE_Moolya_Test | WrongPassword | Wrong username or password or the user is disabled in the Security Editor on the system server computer |
 
 
@TC_EPE_SS_0006
@test0006
Scenario Outline: Enter UserName and Password with no user rights and  Login in SS
When I entered User name in login page as '<User name1>'
And I entered Password in login page as '<Password2>'
And I selected Log In in login page
Then verify content Log On Dialogue in login page as '<Log On Dialogue3>'
 
Examples:
  | SlNo. | User name1       | Password2  | Log On Dialogue3                                                                           |
  | 1     | SE_NoRights_Test | Moolya@123 | The user does not belong to a group that has the rights to use EcoStruxure Process Expert. |
  
  

@TC_EPE_SS_0007
@test0007  
Scenario Outline: Open SS from system tray and click on Basic Settings
When I open system server console show hidden icon in windows explorer
And I selected Settings Menu in settings
And I selected Basic settings in settings

Examples:
  | SlNo. |
  | 1     |
  
@TC_EPE_SS_0007
@test0007  
Scenario Outline: click on Basic Settings in SS Console
When I selected Settings Menu in settings
And I selected Basic settings in settings

Examples:
  | SlNo. |
  | 1     |
  
  

@TC_EPE_SS_0008
@test0008
Scenario Outline: Open hosting in basic settings in SS
When I selected next in system server config wizard
And I selected next in system server config wizard
And I selected next in system server config wizard  
Examples:
  | SlNo. |
  | 1     |
  
  

@TC_EPE_SS_0009
@test0009
Scenario Outline: CE tool slot management - Enter 4 Instance of CE and start the system server 
When I entered Control Participant Max Instance in system server config wizard as '<Control Participant Max Instance3>'
And I selected next in system server config wizard
And I selected next in system server config wizard
And I selected save and close in system server config wizard
And I selected Action Menu in action
And I selected Start server in action
Then verify system server ready Console in server console
And verify number of control instances Console in server console as '<Console4>'

Examples:
  | SlNo. | Control Participant Max Instance3 | Console4 |
  | 0001  | 4                                 | 4        |
  

  
@TC_EPE_SS_0010
@test0010
Scenario Outline: CE tool slot management - Enter 20 Instance of CE and start the system server 
When I entered Control Participant Max Instance in system server config wizard as '<Control Participant Max Instance3>'
And I selected next in system server config wizard
And I selected next in system server config wizard
And I selected save and close in system server config wizard
And I selected Action Menu in action
And I selected Start server in action
Then verify system server ready Console in server console
And verify number of control instances Console in server console as '<Console4>'

Examples:
  | SlNo. | Control Participant Max Instance3 | Console4 |
  | 0001  | 20                                | 20       |

  
  
@TC_EPE_SS_0011
@test0011
Scenario Outline: CE tool slot management - Enter 2 Instance of CE and start the system server 
When I entered Control Participant Max Instance in system server config wizard as '<Control Participant Max Instance3>'
And I selected next in system server config wizard
And I selected next in system server config wizard
And I selected save and close in system server config wizard
And I selected Action Menu in action
And I selected Start server in action
Then verify system server ready Console in server console
And verify number of control instances Console in server console as '<Console4>'

Examples:
  | SlNo. | Control Participant Max Instance3 | Console4 |
  | 0001  | 2                                 | 2        |

  
@TC_EPE_SS_0012
@test0012
Scenario Outline: CE tool slot management - Enter 25 Instance of CE and start the system server 
When I entered Control Participant Max Instance in system server config wizard as '<Control Participant Max Instance3>'
And I selected next in system server config wizard
And I selected next in system server config wizard
And I selected save and close in system server config wizard
And I selected Action Menu in action
And I selected Start server in action
Then verify system server ready Console in server console
And verify number of control instances Console in server console as '<Console4>'

Examples:
  | SlNo. | Control Participant Max Instance3 | Console4 |
  | 0001  | 25                                | 25       |

  
@TC_EPE_SS_0005
@test003
@TC_EPE_SS_0005
Scenario Outline: Trial License activated
When I selected Console in server console as '<Console>'
Then verify license in system server Console in server console

Examples:
  | SlNo. | Console | content |
  | 01    | option2 | NA      |

  
    



