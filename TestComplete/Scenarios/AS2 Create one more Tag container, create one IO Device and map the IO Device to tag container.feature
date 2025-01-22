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
When I Expand control project browser PE project browser in project explorer as '<project browser1>'
And I Expand control project browser PE project browser in project explorer as '<project browser2>'
And I Expand control project browser PE project browser in project explorer as '<project browser3>'
And I Expand control project browser PE project browser in project explorer as '<project browser4>'
When I RClick control project browser project browser in project explorer as '<project browser5>'
And I Select context menu item EC project browser in project explorer as '<context menu>'
When I Expand IO Device section project browser in project explorer as '<project browser7>'
And I Edit IO Device Properties project browser in project explorer as '<project browser8>'


Examples:
  | SlNo. | project browser1 | project browser2 | project browser3 | project browser4 | project browser5 | context menu     | project browser7 | project browser8              |
  | 1     | Supervision_Test | Cluster_1        | Services         | IOServer_1       | IODevices        | Create IO Device | IODevice_2       | TagContainers$$TagContainer_1 |

 
@TC_EPE_PE_AS2
Scenario Outline: Generate from Supervision Project Browser pane
When I RClick control project browser project browser in project explorer as '<containerinstance>'
And I Select context menu item EC project browser in project explorer as '<contextmenu_item>'
Then Verify Message from notification panel AE Notification Pannel in message box
And I Verify the facet generation status of all facets in Assignments Dock  

Examples:
  | SlNo. | containerinstance | contextmenu_item |
  | 1     | Supervision_Test  | Generate         |