from OperationClient import OperationClient

opc_obj = OperationClient()

def double_click_on_editor(identifier):
  for item in opc_obj.instanceedittorpage.object.FindAllChildren('ClrClassName', 'TreeViewItem', 100):
    if item.DataContext.Identifier.OleValue == identifier:
      if not item.IsExpanded:
        item.DblClick()
        Log.Checkpoint(identifier + ' is Double Clicked.')
        Delay(2000, "Wait")
      else:
        Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is already expanded.')


