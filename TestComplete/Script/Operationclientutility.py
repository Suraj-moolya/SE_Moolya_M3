from OperationClient import OperationClient

opc_obj = OperationClient()

###############################################################################
# Function   : double_click_on_editor
# Description: This function locates a specific item in the editor tree view 
#              based on the provided identifier. If the item is not expanded, 
#              it performs a double-click action to expand it. If already 
#              expanded, it logs a checkpoint message.
# Parameter  : identifier (str) - The unique identifier of the tree view item.
#              Example: "Node123"
# Test Data  : Ensure the identifier corresponds to an existing tree view item.
###############################################################################
def double_click_on_editor(identifier):
  for item in opc_obj.instanceedittorpage.object.FindAllChildren('ClrClassName', 'TreeViewItem', 100):
    if item.DataContext.Identifier.OleValue == identifier:
      if not item.IsExpanded:
        item.DblClick()
        Log.Checkpoint(identifier + ' is Double Clicked.')
        Delay(2000, "Wait")
      else:
        Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is already expanded.')


