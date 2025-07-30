Feature: 19 Check Report Generation

@TC_EPE_EC_0042
@test0001
Scenario Outline: Check Report Generation
When I Right Click on nodes System Explorer Node in system explorer as 'System_1'
And I Select context menu item EC in Topology Explorer as '<action>'
And I update the report details with '<customer_name>', '<site_name>', '<report_desc>', '<report_author>', '<page_size>', '<orientation>', '<report_footer>', '<report_header>'
And I Select button in the modal dialoge window as '<button1>'
And I Select button in the modal dialoge window as '<button>'
And I Select button in the modal dialoge window as '<button>'
And I Select button in the modal dialoge window as '<button2>'
And I selected Rename Pop up Ok in message box
Then Verify notification panel message Notification Pannel in message box as '<content>'
When I selected Rename Pop up Ok in message box


Examples:
  | SlNo. | action          | customer_name | site_name | report_desc | report_author | page_size | orientation | report_footer | report_header | button1 | button | button2  | content                            |
  | 1     | Generate Report | Moolya        | SE        | Test Desc   | Expert        | A4        | Landscape   | Confidential  | Test Header   | Refresh | Next   | Generate | Close Configure Editor (Completed) |
  