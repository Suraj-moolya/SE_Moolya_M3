Feature: 90880 - Performance Validation for Bulk Instance Operations in Different Systems with Multiple Template Types
@TC_EPE_AE_PGSQL_90880

@90880_0
Scenario Outline: Creating Multiple instances with specific template in Application Explorer
  When I search text template browser AE Templates browser in application explorer as '<TemplatesBrowser1>'
  And I drag Template from Template browser and drop to Application browser '<Count>' times with template as '<TemplatesBrowser2>'
  Then Verify the template is present in Application browser as '<TemplatesBrowser1>'

  @Create_Instances_5000
  Examples:
    | SlNo | TemplatesBrowser1 | TemplatesBrowser2   | Count |
    | 1    | MotorGP           | MotorGP_1$$1.0.123  | 5000  |


@90880_1
Scenario Outline: Verify loading time of Application Explorer after initial navigation
  When I Click on Nodes System Explorer Node in system explorer as '<TabName1>'
  And I navigate to explorers MainToolBar in system explorer as '<TabName2>'
  Then I Verifies time taken to load the Application Tree Pane

  @Initial_Load_ApplicationExplorer
  Examples:
    | SlNo | TabName1  | TabName2             |
    | 1    | System_1  | Application Explorer |

    
@90880_2
Scenario Outline: Verify Application Explorer load time after closing and reopening tab
  When I Close tab items EC main screen in engineering client as '<TabName1>'
  And I navigate to explorers MainToolBar in system explorer as '<TabName2>'
  Then I Verifies time taken to load the Application Tree Pane

  @Close_And_Reopen_AppExplorer
  Examples:
    | SlNo | TabName1  | TabName2             |
    | 1    | System_1  | Application Explorer |


@90880_3
Scenario Outline: Verify Application Explorer loading time after navigating from Topology Explorer
  When I Close tab items EC main screen in engineering client as '<TabName1>'
  And I navigate to explorers MainToolBar in system explorer as '<TabName3>'
  And I navigate to explorers MainToolBar in system explorer as '<TabName2>'
  Then I Verifies time taken to load the Application Tree Pane

  @Topology_And_ApplicationExplorer_Load
  Examples:
    | SlNo | TabName1  | TabName2             | TabName3          |
    | 1    | System_1  | Application Explorer | Topology Explorer |


@90880_4
Scenario Outline: Verify Application Explorer load time via Project Explorer and Facet navigation
  When I navigate to explorers MainToolBar in system explorer as '<TabName3>'
  And I Dclick Control project broswer project browser in project explorer as '<ProjectBrowser1>'
  And I Dclick Control project broswer project browser in project explorer as '<ProjectBrowser2>'
  And I Right Click on the Facet in Assignments Section as "<FacetName1>" "<Action>"
  Then I Verifies time taken to load the Application Tree Pane

  @From_ProjectExplorer_To_ApplicationExplorer_Load
  Examples:
    | SlNo | ProjectBrowser1  | ProjectBrowser2 | TabName2             | TabName3         | FacetName1           | Action          |
    | 1    | ControlProject_1 | Containers      | Application Explorer | Project Explorer | MotorGP_0001_MotorGP | Go To Instance  |


@90880_5
Scenario Outline: Verify Application Explorer load time in Multi(second) Engineering Client 
  When I launch Engineering Client Engineering client in engineering client
  And I Click on Nodes System Explorer Node in system explorer as '<TabName1>'
  And I navigate to explorers MainToolBar in system explorer as '<TabName2>'
  Then I Verifies time taken to load the Application Tree Pane

  @Second_Client_ApplicationExplorer_Load
  Examples:
    | SlNo | TabName1  | TabName2             |
    | 1    | System_1  | Application Explorer |
    
    
@90880_6
Scenario Outline: Verify Application Explorer load time while switching to Grid view
  When I Switch Application Explorer view to '<view>'
  Then I Verifies time taken to load the Application Tree Pane
  
  @Change_To_Grid_View
  Examples:
    | SlNo | view |
    |  1   | Grid |