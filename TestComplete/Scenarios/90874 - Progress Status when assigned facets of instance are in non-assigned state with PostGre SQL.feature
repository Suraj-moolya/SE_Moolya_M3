Feature: 90874 - Progress Status when assigned facets of instance are in non-assigned state with PostGre SQL

#WPFObject("TreeListViewRow", "", 2) object
#.DataContext.IsProgressStateVisible = True

#.DataContext.ProgressStateToolTip = "Some facets are not assigned yet"   # 75 %
#.DataContext.ProgressState = "AssignedToBothParticipant"

#.DataContext.ProgressStateToolTip = "Facets have not been assigned to both types of projects/the status of some assigned facets is not 'Assigned'"   # 50 %
#.DataContext.ProgressState = "AssignedToOneParticipant"

#.DataContext.ProgressStateToolTip = "No facet has been assigned" # 25 %

#.DataContext.ProgressStateToolTip = "Instance still has default values/no links exist/no facet has been assigned"  # 0 %
#.DataContext.ProgressState = "Created"
