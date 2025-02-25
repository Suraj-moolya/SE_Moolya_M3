Feature: 155 Navigate to Hardware mapping Tab and check the mapping is available
@TC_EPE_PE_CP_0040
@test0040
Scenario Outline: click on control project and Navigate to Hardware mapping Tab, check the mapping is available and map
When I Dclick Control project broswer project browser in project explorer as '<projectBrowser7>'
And I Dclick Control project broswer project browser in project explorer as '<projectBrowser8>'
And I Dclick Control project broswer project browser in project explorer as '<projectBrowser9>'
And I Click '<tabname>' on service mapping edittor window
And I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<appfacet>'
And I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
Then I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance
Examples:
  | SlNo. | projectBrowser7  | projectBrowser8 | projectBrowser9     | tabname          | appfacet     |
  | 1     | M580_Standalone  | Executables     | ControlExecutable_1 | Hardware Mapping | ValveGP_1_OP |
@TC_EPE_PE_CP_0040a
@test0040a
Scenario Outline: Navigate to Hardware mapping Tab, check the mapping is available and map
When I Click '<tabname>' on service mapping edittor window
And I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<appfacet>'
And I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
Then I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance
Examples:
  | SlNo. | tabname          | appfacet           |
  | 1     | Hardware Mapping | ValveGP_1_OP       |
@TC_EPE_PE_CP_0040b
@test0040a
Scenario Outline: Navigate to Service mapping Tab
When I Click '<tabname>' on service mapping edittor window
Examples:
  | SlNo. | tabname         |
  | 2     | Service Mapping |
@TC_EPE_PE_CP_0040a
@test0040a
Scenario Outline: hghghghghghghg
When I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'
Examples:
  | SlNo. | appfacet |
  | 1     | P2P2     |