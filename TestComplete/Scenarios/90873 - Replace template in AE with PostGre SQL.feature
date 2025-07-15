Feature: 90873 - Replace template in AE with PostGre SQL


@TC_EPE_AE_PGSQL_90873_1
Scenario Outline: Select template to replace template in Application browser 
When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC Application browser in application explorer as '<Application browser1>' 
Then verify window open as '<Window>'
When I select the template to replace in replace template as '<Replace_Template>'
And I take evidence Instance Editor in application explorer

@Select_INTERLOCK8OFFGP_1.0.5_to_replace_with_INTERLOCK4ONGP_UC_1.0.14_template_in_Application_browser
Examples:
  | SlNo. | Application browser    | Application browser1 | Window           | Replace_Template          |
  | 1     | INTERLOCK8OFFGP$$1.0.5 | Replace Template     | Replace Template | INTERLOCK4ONGP_UC$$1.0.14 |

  
@TC_EPE_AE_PGSQL_90873_2
Scenario Outline: Select Folder to replace templates in Application browser 
When I rclick application browser folder AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC Application browser in application explorer as '<Application browser1>' 
Then verify window open as '<Window>'
When I select the template to replace in replace template as '<Replace_Template>'
And I take evidence Instance Editor in application explorer

@Select_System_1_Folder_to_replace_with_INTERLOCK4ONGP_UC_1.0.14_template_in_Application_browser
Examples:
  | SlNo. | Application browser | Application browser1 | Window           | Replace_Template          |
  | 1     | System_1            | Replace Template     | Replace Template | INTERLOCK4ONGP_UC$$1.0.14 |

  
@TC_EPE_AE_PGSQL_90873_3
Scenario Outline: Click on OK in replace template window and verify
When I Select button in the modal dialoge window as '<Button name>'
Then verify template and version in application browser as '<Template>'
Then Verify notification panel message Notification Pannel in message box as '<Message>' 

@Click_OK_in_Replace_Template_and_verify_INTERLOCK4ONGP_UC_1.0.14
Examples:
  | SlNo. | Button name | Template                  | Message                               |
  | 1     | OK          | INTERLOCK4ONGP_UC$$1.0.14 | Replace Instance Template (Completed) |


@TC_EPE_AE_PGSQL_90873_4
Scenario Outline: Click on Close (X) in replace template window and verify
When I Close modal dialog window
Then verify template and version in application browser as '<Template>'

@Click_CLOSE_in_Replace_Template_and_verify_INTERLOCK4ONGP_UC_1.0.14
Examples:
  | SlNo. | Button name | Template               |
  | 1     | Close       | INTERLOCK8OFFGP$$1.0.5 |


@TC_EPE_AE_PGSQL_90873_5
Scenario Outline: Click on Cancel in replace template window and verify
When I Select button in the modal dialoge window as '<Button name>'
Then verify template and version in application browser as '<Template>'

@Click_CANCEL_in_Replace_Template_and_verify_INTERLOCK4ONGP_UC_1.0.14
Examples:
  | SlNo. | Button name | Template               |
  | 1     | Cancel      | INTERLOCK8OFFGP$$1.0.5 |

