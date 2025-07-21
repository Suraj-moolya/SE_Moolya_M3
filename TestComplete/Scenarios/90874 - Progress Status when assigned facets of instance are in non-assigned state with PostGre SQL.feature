Feature: 90874 - Progress Status when assigned facets of instance are in non-assigned state with PostGre SQL


@TC_EPE_AE_PGSQL_90874_1
Scenario Outline: Check Progress Status of instance in Application or instance browser 
When I rclick application browser template AE Application browser in application explorer as '<Application browser>'
And I Select context menu item EC Application browser in application explorer as '<Application browser1>' 
Then verify window open as '<Window>'
When I select the template to replace in replace template as '<Replace_Template>'
And I take evidence Instance Editor in application explorer
# Verify the progress status of instance in Application browser when opened as

@Select_INTERLOCK8OFFGP_1.0.5_to_replace_with_INTERLOCK4ONGP_UC_1.0.14_template_in_Application_browser
Examples:
  | SlNo. | Application browser    | Application browser1 | Window           | Replace_Template          |
  | 1     | INTERLOCK8OFFGP$$1.0.5 | Replace Template     | Replace Template | INTERLOCK4ONGP_UC$$1.0.14 |

#WPFObject("TreeListViewRow", "", 2) object
#.DataContext.IsProgressStateVisible = True

#.DataContext.ProgressStateToolTip = "Some facets are not assigned yet"   # 75 %
#.DataContext.ProgressState = "AssignedToBothParticipant"

#.DataContext.ProgressStateToolTip = "Facets have not been assigned to both types of projects/the status of some assigned facets is not 'Assigned'"   # 50 %
#.DataContext.ProgressState = "AssignedToOneParticipant"

#.DataContext.ProgressStateToolTip = "No facet has been assigned" # 25 %

#.DataContext.ProgressStateToolTip = "Instance still has default values/no links exist/no facet has been assigned"  # 0 %
#.DataContext.ProgressState = "Created"
