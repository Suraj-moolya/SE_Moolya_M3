Feature: Import the empty pages in supervision project and check the pages are created with the default page which is selected in the project settings

@TC_EPE_AS_0005
@test001
Scenario Outline: Import the empty pages in supervision project and check the pages are created with the default page which is selected in the project settings
When I Right click on the Supervision Project
And I click on Logout button
Then verify text in system server console Console in server console as '<Console1>' 