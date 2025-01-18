"""Global templates Explorer Tab Utility"""

import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from ApplicationExplorerTab import ApplicationExplorerTab
from GlobalTemplatesTab import GlobalTemplatesTab
from MessageBox import MessageBox

eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
aet_obj = ApplicationExplorerTab()
gte_obj = GlobalTemplatesTab()
msg_obj = MessageBox()

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
  
def search_and_right_click_search_text_GTE(param):
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
        item.ClickR()
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
    
    
def select_tab_in_gtw(prop):
  for i in gte_obj.compositeeditorworkspacebutton.object.FindAllChildren("ClrClassName", 'RadPane', 100):
    if i.WPFControlText == prop:
      i.click()
      Log.Checkpoint(i.WPFControlText +' clicked on Global Templates Window.')
      return
  Log.Warning('Toolbox tab not found.')

def drag_and_drop_toolbox_to_window(func):
  tools = gte_obj.compositeeditorworkspacebutton.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  for tool in tools:
    if getattr(tool.DataContext, 'NameToShow', None) and getattr(tool.DataContext.NameToShow, 'OleValue', None) == func:
      from_x, from_y = tool.ScreenLeft + tool.Width / 2, tool.ScreenTop + tool.Height / 2
      location = gte_obj.compositeeditorworkspacebutton.object
      to_x, to_y = location.ScreenLeft + location.Width / 2, location.ScreenTop + location.Height / 2
      tool.Drag(from_x - tool.ScreenLeft, from_y - tool.ScreenTop, to_x - from_x, to_y - from_y)
      Log.Checkpoint(f"Dragged '{func}' tool to the edit page.")
      return
  Log.Warning("Could not find the tool or destination to perform drag-and-drop.")
  
  
def click_item_in_save_as_window(btn):
  for item in gte_obj.saveaswindow.object.FindAllChildren('ClrClassName', 'RadioButton', 100):
    if btn in item.WPFControlText:
      item.click()
      Log.Checkpoint(f"Clicked on '{btn}' item in the Save As window.")
      return
  Log.Warning(f"Item '{btn}' not found in the Save As window.")

def change_template_name_and_version(name, version):
  for item in gte_obj.saveaswindow.object.FindAllChildren('ClrClassName', 'TextBox', 100):
    item.DataContext.Identifier = name
    item.DataContext.Version = version
    Log.Checkpoint(f"Updated Identifier to '{name}' and Version to '{version}'")
    return
  Log.Warning("No TextBox found in the Save As window to update the Identifier and Version.")
  
def description_for_save_as_window(text):
  for item in gte_obj.saveaswindow.object.FindAllChildren('ClrClassName', 'TextBox', 100):
    if item.WPFControlName == "ChangeDescriptionInput":
      item.click()
      item.Text = text
      Log.Checkpoint(f"Entered '{text}' in the DescriptionInput field.")
      return
  Log.Warning("DescriptionInput TextBox not found.")
  
def select_tag_gtw(tag_name):
  for tag in gte_obj.addtagswindow.object.FindAllChildren('ClrClassName', 'GridViewRow', 100):
    if tag.DataContext == tag_name:
      tag.click()
      Log.checkpoint(f"Clicked on the tag: {tag_name}")
      return
  Log.warning(f"Tag '{tag_name}' not found.")

def click_add_icon_gtw(prop):
  buttons = gte_obj.supervisiondataelement.object.FindAllChildren('ClrClassName', 'Button', 100)
  for button in buttons:
    element_name = getattr(getattr(button, 'DataContext', None), 'ElementName', None)
    if element_name == prop and button.WPFControlName == "BtnAdd":
      button.Click()
      Log.Checkpoint(f"Clicked the 'Add' icon for {element}.")
      return
  Log.Warning(f"'{element}' Button not found.")

def expand_librarys_in_gtw(element):
  for elem in gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100):
    if getattr(getattr(elem, 'DataContext', None), 'Identifier', None) == element:
      if not getattr(elem, 'IsExpanded', False):
        elem.IsExpanded = True
        Log.Checkpoint(f"{element} is now expanded.")
      else:
        Log.Message("GeneralPurposeLibrary is already expanded.")
      return
  Log.Warning(f"'{element}' not found.")
  
def click_library_in_gtw(lib):
  for elem in gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100):
    if getattr(getattr(elem, 'DataContext', None), 'Identifier', None) == lib:
      elem.click()
      Log.Checkpoint(f"{lib} Clicked.")
      return
  Log.Warning(f"{lib} Not Found.")
  
def drag_and_drop_genie_to_genie_facet_in_gtw(prop):
  genie = gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'ListViewItem', 100)
  genie_facet = gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for gen in genie:
    if gen.DataContext.Identifier == prop:
      from_x = gen.ScreenLeft + (gen.Width / 2)
      from_y = gen.ScreenTop + (gen.Height / 2)
      break
  for gen_facet in genie_facet:
    if gen_facet.WPFControlText == "Template_1_CG":
      to_x = gen_facet.ScreenLeft + (gen_facet.Width / 2)
      to_y = gen_facet.ScreenTop + (gen_facet.Height / 2)
      break
  gen.Drag(from_x - gen.ScreenLeft, from_y - gen.ScreenTop, to_x - from_x, to_y - from_y)
  Log.Message(f"Dragging from {prop} to 'Template_1_CG' completed.")
  
def panel_button_gtw(button):
  for btn in gte_obj.panelbutton.object.FindAllChildren('ClrClassName', 'Button', 100):
    if btn.WPFControlText == button:
      btn.click()
      Log.Checkpoint(f"{button} Button Clicked.")
      return
  Log.Warning(f"{button} Button Not Found.")
  
def right_click_created_template_gtw(prop):
  for i in ses_obj.systemexplorermenubutton.object.FindAllChildren('ClrClassName', 'GridViewCell', 100):
    if getattr(getattr(i, 'DataContext', None), 'Identifier', None) == prop:
      i.ClickR()
      Log.Checkpoint(f"{prop} Clicked.")
      return
  Log.Warning(f"{prop} Not Found.")