"""Global templates Explorer Tab Utility"""

import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from ApplicationExplorerTab import ApplicationExplorerTab
from GlobalTemplatesTab import GlobalTemplatesTab

eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
aet_obj = ApplicationExplorerTab()
gte_obj = GlobalTemplatesTab()

def search_and_double_click_search_text_GTE(param):
  search_text, identifier, version = param.split('$$')
  search_box = gte_obj.globaltemplatesearchtextbox
  search_box.click()
  Applicationutility.wait_in_seconds(1000, 'wait')
  search_box.sys_keys(search_text)
  Applicationutility.wait_in_seconds(3000, 'wait')
  search_box.sys_keys('[Enter]')
  search_list = search_box.find_children_for_grid_view_row()
  #search_list = search_box.FindAllChildren("ClrClassName", 'GridViewRow', 1500, True)
  for item in search_list:
    if str(identifier) in str(item.DataContext.Identifier.OleValue):
      if str(version) in str(item.DataContext.Version.OleValue):
        item.DblClick()
        break
  Applicationutility.wait_in_seconds(3000, 'wait')
    
  
def rclick_idedntifier_explorer_GTE(param):
  identifier, version = param.split('$$')
  explorer_list = gte_obj.globaltemplatecoretextbox.find_children_for_explorer_node()
  for item in explorer_list:
    if item.ChildCount > 1:
      expanded_list = item.FindAllChildren("ClrClassName", 'GridViewRow', 1500, True)
      if len(expanded_list) > 0:
        break
  for item in expanded_list:
    if str(identifier) in str(item.DataContext.Identifier.OleValue):
      if str(version) in str(item.DataContext.Version.OleValue):
        Applicationutility.wait_in_seconds(1000, 'wait')
        item.ClickR()
        break
  Applicationutility.wait_in_seconds(1000, 'wait')
  
  
def drag_toolbox_item_drop_composite_editor_GTE(name):
  toolbox_item = gte_obj.toolbooxtabletextbox.find_children_for_treeviewrow()
  for i in range(len(toolbox_item)):
      if toolbox_item[i].Visible:
        if str(name) in str(toolbox_item[i].DataContext.NameToShow):
          fromx = toolbox_item[i].ScreenLeft
          fromy = toolbox_item[i].ScreenTop
          Log.Message('The object selected to drag is : ' + str(toolbox_item[i].DataContext.NameToShow))
          break
  
  App_list = gte_obj.compositeeditorworkspacebutton.object
  tox = App_list.ScreenLeft + 300
  toy = App_list.ScreenTop + 50

  main_screen = eng_obj.mainscreenbutton   
  main_screen.drag((fromx+15), (fromy+15), (fromx+tox), -(fromy-toy))
  Applicationutility.wait_in_seconds(1000, 'wait')
 
 
def verify_search_box_message_GTE(search_text):
  search_box = gte_obj.globaltemplatesearchtextbox.object
  search_box.Click()
  Applicationutility.wait_in_seconds(1000, 'wait')
  search_box.Keys(search_text)
  Applicationutility.wait_in_seconds(2000, 'wait')
  if not search_box.DataContext.HasResults:
    Log.Checkpoint('The specified text was not found')
  else:
    Log.Warning('Result was found for the text')
    
  Applicationutility.take_screenshot()
  
  
def verify_title_bar(tabname):
  titlebar = gte_obj.titlebartab.object
  if titlebar.DataContext.HeaderText == tabname:
    Log.Checkpoint(f"Successfully navigated to '{tabname}'.")
  else:
    Log.Warning(f"Navigation error: Expected '{tabname}', but currently on '{titlebar.DataContext.HeaderText}'.")