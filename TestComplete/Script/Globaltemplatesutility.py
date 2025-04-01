"""Global templates Explorer Tab Utility"""

import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from ApplicationExplorerTab import ApplicationExplorerTab
from GlobalTemplatesTab import GlobalTemplatesTab
from MessageBox import MessageBox
import os

eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
aet_obj = ApplicationExplorerTab()
gte_obj = GlobalTemplatesTab()
msg_obj = MessageBox()

###############################################################################
# Function : search_and_double_click_search_text_GTE
# Description : Searches for a specific template in the Global Templates Explorer 
#               tab and double-clicks on the matching item.
# Parameter : param (str) - A string in the format "search_text$$identifier$$version".
#             Example: "TemplateName$$12345$$1.0"
###############################################################################
def search_and_double_click_search_text_GTE(param):
  search_text, identifier, version = param.split('$$')
  search_box = gte_obj.globaltemplatesearchtextbox
  search_box.click()
  Applicationutility.wait_in_seconds(1000, 'wait')
  search_box.sys_keys(search_text)
  Applicationutility.wait_in_seconds(3000, 'wait')
  search_box.sys_keys('[Enter]')
  search_list = search_box.find_children_for_grid_view_row()
  if not search_list:
    Log.Warning("No items found in the search results.")
  else:
    for item in search_list:
      if str(identifier) in str(item.DataContext.Identifier.OleValue):
        if str(version) in str(item.DataContext.Version.OleValue):
          item.DblClick()
          break
  Applicationutility.wait_in_seconds(3000, 'wait')

###############################################################################
# Function : search_and_right_click_search_text_GTE
# Description : Searches for a specific template in the Global Templates Explorer 
#               tab and performs a right-click on the matching item.
# Parameter : param (str) - A string in the format "search_text$$identifier$$version".
#             Example: "TemplateName$$12345$$1.0"
###############################################################################
def search_and_right_click_search_text_GTE(param):
  search_text, identifier, version = param.split('$$')
  search_box = gte_obj.globaltemplatesearchtextbox
  search_box.click()
  Applicationutility.wait_in_seconds(1000, 'wait')
  search_box.sys_keys(search_text)
  Applicationutility.wait_in_seconds(3000, 'wait')
  search_box.sys_keys('[Enter]')
  search_list = search_box.find_children_for_grid_view_row()
  if not search_list:
    Log.Warning("No items found in the search results.")
  else:
    for item in search_list:
      if str(identifier) in str(item.DataContext.Identifier.OleValue):
        if str(version) in str(item.DataContext.Version.OleValue):
          item.ClickR()
          break
  Applicationutility.wait_in_seconds(3000, 'wait')  

###############################################################################
# Function : rclick_idedntifier_explorer_GTE
# Description : Expands the explorer tree in the Global Templates Explorer tab 
#               and performs a right-click on the matching identifier and version.
# Parameter : param (str) - A string in the format "identifier$$version".
#             Example: "12345$$1.0"
###############################################################################
def rclick_idedntifier_explorer_GTE(param):
  identifier, version = param.split('$$')
  explorer_list = gte_obj.globaltemplatecoretextbox.find_children_for_explorer_node()
  if not explorer_list:
    Log.Warning("No explorer nodes found.")
  else:
    for item in explorer_list:
      if item.ChildCount > 1:
        expanded_list = item.FindAllChildren("ClrClassName", 'GridViewRow', 1500, True)
        if len(expanded_list) > 0:
          break
    if not expanded_list:
      Log.Warning("No expanded items found.")
    else:
      for item in expanded_list:
        if str(identifier) in str(item.DataContext.Identifier.OleValue):
          if str(version) in str(item.DataContext.Version.OleValue):
            Applicationutility.wait_in_seconds(1000, 'wait')
            item.ClickR()
            break
  Applicationutility.wait_in_seconds(1000, 'wait')

###############################################################################
# Function : drag_toolbox_item_drop_composite_editor_GTE
# Description : Drags an item from the toolbox and drops it into the composite editor.
# Parameter : name (str) - The name of the toolbox item to drag.
#             Example: "ToolboxItemName"
###############################################################################
def drag_toolbox_item_drop_composite_editor_GTE(name):
  toolbox_item = gte_obj.toolbooxtabletextbox.find_children_for_treeviewrow()
  if not toolbox_item:
    Log.Warning("No toolbox items found.")
  else:
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

###############################################################################
# Function : verify_search_box_message_GTE
# Description : Verifies if the search box displays results for the given text.
# Parameter : search_text (str) - The text to search in the search box.
#             Example: "SearchText"
###############################################################################
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

###############################################################################
# Function : verify_title_bar
# Description : Verifies if the title bar matches the expected tab name.
# Parameter : tabname (str) - The expected name of the tab.
#             Example: "Global Templates"
###############################################################################
def verify_title_bar(tabname):
  titlebar = gte_obj.titlebartab.object
  if titlebar.DataContext.HeaderText == tabname:
    Log.Checkpoint(f"Successfully navigated to '{tabname}'.")
  else:
    Log.Warning(f"Navigation error: Expected '{tabname}', but currently on '{titlebar.DataContext.HeaderText}'.")

###############################################################################
# Function : select_tab_in_gtw
# Description : Selects a specific tab in the Global Templates Window.
# Parameter : prop (str) - The name of the tab to select.
#             Example: "Properties"
###############################################################################
def select_tab_in_gtw(prop):
  for i in gte_obj.compositeeditorworkspacebutton.object.FindAllChildren("ClrClassName", 'RadPane', 100):
    if i.WPFControlText == prop:
      i.click()
      Log.Checkpoint(i.WPFControlText + ' clicked on Global Templates Window.')
      return
  Log.Warning('Toolbox tab not found.')

###############################################################################
# Function : drag_and_drop_toolbox_to_window
# Description : Drags a toolbox item and drops it into the specified window.
# Parameter : func (str) - The name of the toolbox item to drag.
#             Example: "ToolboxFunctionName"
###############################################################################
def drag_and_drop_toolbox_to_window(func):
  tools = gte_obj.compositeeditorworkspacebutton.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  if not tools:
    Log.Warning("No tools found in the toolbox.")
  else:
    for tool in tools:
      if getattr(tool.DataContext, 'NameToShow', None) and getattr(tool.DataContext.NameToShow, 'OleValue', None) == func:
        from_x, from_y = tool.ScreenLeft + tool.Width / 2, tool.ScreenTop + tool.Height / 2
        location = gte_obj.compositeeditorworkspacebutton.object
        to_x, to_y = location.ScreenLeft + location.Width / 2, location.ScreenTop + location.Height / 2
        tool.Drag(from_x - tool.ScreenLeft, from_y - tool.ScreenTop, to_x - from_x, to_y - from_y)
        Log.Checkpoint(f"Dragged '{func}' tool to the edit page.")
        Applicationutility.wait_in_seconds(1500, 'Wait')
        return
  Log.Warning("Could not find the tool or destination to perform drag-and-drop.")

###############################################################################
# Function : click_item_in_save_as_window
# Description : Clicks on a specific item (radio button) in the Save As window.
# Parameter : btn (str) - The name of the button to click.
#             Example: "SaveAsOption"
###############################################################################
def click_item_in_save_as_window(btn):
  items = gte_obj.saveaswindow.object.FindAllChildren('ClrClassName', 'RadioButton', 100)
  if not items:
    Log.Warning("No radio buttons found in the Save As window.")
  else:
    for item in items:
      if btn in item.WPFControlText:
        item.click()
        Log.Checkpoint(f"Clicked on '{btn}' item in the Save As window.")
        return
  Log.Warning(f"Item '{btn}' not found in the Save As window.")

###############################################################################
# Function : change_template_name_and_version
# Description : Updates the template name and version in the Save As window.
# Parameter : name (str) - The new template name.
#             version (str) - The new version number.
#             Example: name="NewTemplateName", version="2.0"
###############################################################################
def change_template_name_and_version(name, version):
  items = gte_obj.saveaswindow.object.FindAllChildren('ClrClassName', 'TextBox', 100)
  if not items:
    Log.Warning("No text boxes found in the Save As window.")
  else:
    for item in items:
      item.DataContext.Identifier = name
      item.DataContext.Version = version
      Log.Checkpoint(f"Updated Identifier to '{name}' and Version to '{version}'")
      return
  Log.Warning("No TextBox found in the Save As window to update the Identifier and Version.")

###############################################################################
# Function : description_for_save_as_window
# Description : Adds a description in the Save As window.
# Parameter : text (str) - The description text to add.
#             Example: "This is a new template description."
###############################################################################
def description_for_save_as_window(text):
  items = gte_obj.saveaswindow.object.FindAllChildren('ClrClassName', 'TextBox', 100)
  if not items:
    Log.Warning("No text boxes found in the Save As window.")
  else:
    for item in items:
      if item.WPFControlName == "ChangeDescriptionInput":
        item.click()
        item.Text = text
        Log.Checkpoint(f"Entered '{text}' in the DescriptionInput field.")
        return
  Log.Warning("DescriptionInput TextBox not found.")

###############################################################################
# Function : select_tag_gtw
# Description : Selects a specific tag in the Global Templates Window.
# Parameter : tag_name (str) - The name of the tag to select.
#             Example: "TagName"
###############################################################################
def select_tag_gtw(tag_name):
  tags = gte_obj.addtagswindow.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  if not tags:
    Log.Warning("No tags found in the Add Tags window.")
  else:
    for tag in tags:
      if tag.DataContext == tag_name:
        tag.click()
        Log.Checkpoint(f"Clicked on the tag: {tag_name}")
        return
  Log.Warning(f"Tag '{tag_name}' not found.")

###############################################################################
# Function : click_add_icon_gtw
# Description : Clicks the "Add" icon for a specific property in the Global Templates Window.
# Parameter : prop (str) - The name of the property for which the "Add" icon should be clicked.
#             Example: "PropertyName"
###############################################################################
def click_add_icon_gtw(prop):
  buttons = gte_obj.supervisiondataelement.object.FindAllChildren('ClrClassName', 'Button', 100)
  if not buttons:
    Log.Warning("No buttons found in the supervision data element.")
  else:
    for button in buttons:
      element_name = getattr(getattr(button, 'DataContext', None), 'ElementName', None)
      if element_name == prop and button.WPFControlName == "BtnAdd":
        button.Click()
        Log.Checkpoint(f"Clicked the 'Add' icon for {prop}.")
        return
  Log.Warning(f"'{prop}' Button not found.")

###############################################################################
# Function : expand_librarys_in_gtw
# Description : Expands a specific library in the Global Templates Window.
# Parameter : element (str) - The name of the library to expand.
#             Example: "LibraryName"
###############################################################################
def expand_librarys_in_gtw(element):
  elements = gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  if not elements:
    Log.Warning("No libraries found in the supervision genie element.")
  else:
    for elem in elements:
      if getattr(getattr(elem, 'DataContext', None), 'Identifier', None) == element:
        if not getattr(elem, 'IsExpanded', False):
          elem.IsExpanded = True
          Log.Checkpoint(f"{element} is now expanded.")
        else:
          Log.Message("Library is already expanded.")
        return
  Log.Warning(f"'{element}' not found.")

###############################################################################
# Function : click_library_in_gtw
# Description : Clicks on a specific library in the Global Templates Window.
# Parameter : lib (str) - The name of the library to click.
#             Example: "LibraryName"
###############################################################################
def click_library_in_gtw(lib):
  elements = gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  if not elements:
    Log.Warning("No libraries found in the supervision genie element.")
  else:
    for elem in elements:
      if getattr(getattr(elem, 'DataContext', None), 'Identifier', None) == lib:
        elem.click()
        Log.Checkpoint(f"{lib} Clicked.")
        return
  Log.Warning(f"{lib} Not Found.")

###############################################################################
# Function : drag_and_drop_genie_to_genie_facet_in_gtw
# Description : Drags a genie item and drops it onto a genie facet in the Global Templates Window.
# Parameter : prop (str) - The name of the genie item to drag.
#             Example: "GenieName"
###############################################################################
def drag_and_drop_genie_to_genie_facet_in_gtw(prop):
  genie = gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'ListViewItem', 100)
  genie_facet = gte_obj.supervisiongenieelement.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  if not genie:
    Log.Warning("No genie items found.")
  elif not genie_facet:
    Log.Warning("No genie facets found.")
  else:
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

###############################################################################
# Function : panel_button_gtw
# Description : Clicks a specific button in the panel of the Global Templates Window.
# Parameter : button (str) - The name of the button to click.
#             Example: "ButtonName"
###############################################################################
def panel_button_gtw(button):
  buttons = gte_obj.panelbutton.object.FindAllChildren('ClrClassName', 'Button', 100)
  if not buttons:
    Log.Warning("No buttons found in the panel.")
  else:
    for btn in buttons:
      if btn.WPFControlText == button:
        btn.click()
        Log.Checkpoint(f"{button} Button Clicked.")
        return
  Log.Warning(f"{button} Button Not Found.")

###############################################################################
# Function : right_click_created_template_gtw
# Description : Performs a right-click on a created template in the Global Templates Window.
# Parameter : prop (str) - The name of the template to right-click.
#             Example: "TemplateName"
###############################################################################
def right_click_created_template_gtw(prop):
  items = ses_obj.systemexplorermenubutton.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  if not items:
    Log.Warning("No templates found in the system explorer menu.")
  else:
    for i in items:
      if getattr(getattr(i, 'DataContext', None), 'Identifier', None) == prop:
        i.ClickR()
        Log.Checkpoint(f"{prop} Clicked.")
        return
  Log.Warning(f"{prop} Not Found.")

###############################################################################
# Function : GlobalTemplates_Import
# Description : Imports a file into the Global Templates Window.
# Parameter : path (str) - The base path of the file.
#             folder (str) - The folder containing the file.
#             file (str) - The name of the file to import.
#             Example: path="C:/Templates", folder="FolderName", file="FileName.ext"
###############################################################################
def GlobalTemplates_Import(path, folder, file):
    filelocation = aet_obj.addressbandtextbox
    tox = (filelocation.object.Height)/2
    toy = 5
    filelocation.click_at(tox,toy)
    full_path = os.path.join(path, folder)
    os.chdir(full_path) 
    Sys.Keys(os.getcwd())
    Sys.Keys("[Enter]")
    filename_textbox = aet_obj.comboboxtextbox.object
    filename_textbox.Click()
    filename_textbox.Keys(file)