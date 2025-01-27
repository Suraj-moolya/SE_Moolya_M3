Feature: Clearing Database

@TC_EPE_AS_0007
@test001
Scenario Outline: Clearing Database
When I press Ctrl+M '<mode>'
And I enter the Maintenance mode Password '<password>' and press Enter key '<key>'
And I enter '<command>' and press Enter key '<key>'
#Then verify text in system server console Console in server console as '<Console1>'
Then verify text in system server console Console in server console as '<Console2>'
When I press Ctrl+M '<mode>'

Examples:
  | SlNo. | mode | key     | password          | command            | Console1                   | Console2 |
  | 1     | ^M   | [Enter] | admin@Pes4.2#2016 | Database DeleteAll | Deleting database Global.. | Done     |