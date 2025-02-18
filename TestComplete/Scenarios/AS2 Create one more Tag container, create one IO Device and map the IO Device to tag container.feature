Feature: AS2 Create one more Tag container, create one IO Device and map the IO Device to tag container


@TC_EPE_PE_AS2a
Scenario Outline: Create one more Tag container
When I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'
And I click modal dialog window project browser in project explorer as '<Button>'

Examples:
  | SlNo. | container dock1                        | Button |
  | 1     | Supervision_Test$$Create Tag Container | OK     |
  
  
@TC_EPE_PE_AS2b
Scenario Outline: Create one IO Device and map the IO Device to tag container
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu1>'
When I RClick control project browser project browser in project explorer as '<project browser1>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
And I RClick control project browser project browser in project explorer as '<project browser5>'
And I Select context menu item EC project browser in project explorer as '<create>'
And I Expand IO Device section project browser in project explorer as '<project browser7>'
And I Edit IO Device Properties project browser in project explorer as '<project browser8>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'
When I Close instance editor tab Instance editor close in application explorer as 'IODevices'

Examples:
  | SlNo. | project browser1 | context menu | context menu1 | project browser7 | project browser8              | message                     | project browser5 | create           |
  | 1     | Supervision_Test | Expand All   | Collapse All  | IODevice_1       | TagContainers$$TagContainer_1 | Create IODevice (Completed) | IODevices        | Create IO Device |

  
@TC_EPE_PE_AS2c
Scenario Outline: map the IO Device to tag container
When I Dclick Control project broswer project browser in project explorer as '<project browser5>'
When I Expand IO Device section project browser in project explorer as '<project browser7>'
And I Edit IO Device Properties project browser in project explorer as '<project browser8>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'
When I Close instance editor tab Instance editor close in application explorer as 'IODevices'

@map_the_IODevice_2_to_TagContainer_2
Examples:
  | SlNo. | project browser5 | project browser7 | project browser8              | message                     |
  | 1     | IODevices        | IODevice_2       | TagContainers$$TagContainer_2 | Update IODevice (Completed) |

 
@TC_EPE_PE_AS2
Scenario Outline: Generate from Supervision Project Browser pane
When I RClick control project browser project browser in project explorer as '<containerinstance>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item>'
Then Verify Action message in notification pannel project browser in project explorer as '<message>'
 
Examples:
  | SlNo. | containerinstance | contextmenu_item | message                                  |
  | 1     | Supervision_Test  | Generate         | Generate Supervision Project (Completed) |