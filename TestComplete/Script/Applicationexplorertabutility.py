"""Application Explorer Tab Utility"""

import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from ApplicationExplorerTab import ApplicationExplorerTab
from WindowsExplorer import WindowsExplorer
from MessageBox import MessageBox
import os
import csv
import xml.etree.ElementTree as ET
import datetime
import Actionutility

eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
aet_obj = ApplicationExplorerTab()
win_obj = WindowsExplorer()
msg_obj = MessageBox()

###############################################################################
# Function : expand_templates_browser
# Description: Expands the templates in the browser based on the provided list.
#              Iterates through the identifiers and expands the corresponding 
#              templates if they are not already expanded.
# Parameter : lst (str) - Comma-separated identifiers of templates to expand.
#             Example: "Template1,Template2,Template3"
###############################################################################
def expand_templates_browser(lst):
    identifiers_list = lst.split(',')
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        Applicationutility.wait_in_seconds(500, 'wait')
        for identifier in identifiers_list:
            for template in template_list:
                if template.Visible and str(template.DataContext.Identifier) == str(identifier):
                    if not template.IsExpanded:
                        template.DblClick(50, (template.Height / 2))
        Log.Message(identifiers_list[-1])
    else:
        Log.Warning("No templates found in the template browser.")

###############################################################################
# Function : collapse_templates_browser
# Description: Collapses the templates in the browser based on the provided list.
#              Iterates through the identifiers and collapses the corresponding 
#              templates if they are expanded.
# Parameter : lst (str) - Comma-separated identifiers of templates to collapse.
#             Example: "Template1,Template2,Template3"
###############################################################################
def collapse_templates_browser(lst):
    identifiers_list = lst.split(',')
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        Applicationutility.wait_in_seconds(500, 'wait')
        for identifier in identifiers_list:
            for template in template_list:
                if template.Visible and str(template.DataContext.Identifier) == str(identifier):
                    if template.IsExpanded:
                        template.DblClick(50, (template.Height / 2))
    else:
        Log.Warning("No templates found in the template browser.")

###############################################################################
# Function : check_composite_templates_temp_browser
# Description: Verifies composite templates in the template browser by checking 
#              their version and description. Logs a checkpoint for each valid template.
# Parameter : None
###############################################################################
def check_composite_templates_temp_browser():
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        Applicationutility.wait_in_seconds(500, 'wait')
        for template in template_list:
            if template.Visible and template.Item.ViewModel.Version.OleValue != '':
                Log.Checkpoint(f"{template.Item.Identifier.OleValue} - {template.Item.ViewModel.Version.OleValue} - {template.Item.ViewModel.Description.OleValue}")
    else:
        Log.Warning("No templates found in the template browser.")

###############################################################################
# Function : click_on_scroll_down_temp_browser
# Description: Scrolls down the template browser by clicking on the scroll bar.
# Parameter : count (int) - Number of times to scroll down.
#             Example: 5
###############################################################################
def click_on_scroll_down_temp_browser(count):
    temp_browser = aet_obj.templatesbrowsertextbox
    for _ in range(int(count)):
        temp_browser.click_at((temp_browser.width - 15), (temp_browser.height - 35))

###############################################################################
# Function : click_on_scroll_up_temp_browser
# Description: Scrolls up the template browser by clicking on the scroll bar.
# Parameter : count (int) - Number of times to scroll up.
#             Example: 5
###############################################################################
def click_on_scroll_up_temp_browser(count=0):
    temp_browser = aet_obj.templatesbrowsertextbox
    for _ in range(int(count)):
        temp_browser.click_at((temp_browser.width - 15), 100)

###############################################################################
# Function : check_temp_browser_list
# Description: Logs all visible templates in the template browser.
# Parameter : None
###############################################################################
def check_temp_browser_list():
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        Applicationutility.wait_in_seconds(500, 'wait')
        for template in template_list:
            if template.Visible:
                Log.Checkpoint(str(template.Item.Identifier.OleValue))
    else:
        Log.Warning("No templates found in the template browser.")

###############################################################################
# Function : search_template_browser_AE
# Description: Searches for a template in the template browser using the search text.
# Parameter : search_text (str) - Text to search for in the template browser.
#             Example: "Motor"
###############################################################################
def search_template_browser_AE(search_text):
    temp_browser = aet_obj.templatesbrowsertextbox.object
    search = temp_browser.FindAllChildren('ClrClassName', 'SearchComboBoxControl', 50)
    if search:
        search[0].Click()
        Applicationutility.wait_in_seconds(1000, 'wait')
        Sys.Keys(search_text)
        Applicationutility.wait_in_seconds(2500, 'wait')
        aet_obj.workspacebutton.object.Click()
    else:
        Log.Warning("SearchComboBoxControl not found in template browser.")

###############################################################################
# Function : drag_composite_template_drop_app_browser_system1_AE
# Description: Drags a composite template from the template browser and drops it 
#              onto a system in the application browser.
# Parameter : param (str) - Template and version in the format 'template$$version'.
#             Example: "Template1$$1.0.0"
###############################################################################
def drag_composite_template_drop_app_browser_system1_AE(param):
    template, version = param.split('$$')
    Applicationutility.wait_in_seconds(2500, 'wait')
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        for template_item in template_list:
            if template_item.Visible and str(template) in str(template_item.Item.Identifier.OleValue) and str(version) == str(template_item.Item.ViewModel.Version.OleValue):
                fromx = template_item.ScreenLeft
                fromy = template_item.ScreenTop
                Log.Message(f"The object selected to drag is: {template_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Warning(f"Template '{template}' with version '{version}' not found in template browser.")
    else:
        Log.Warning("No templates found in the template browser.")

    app_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if app_list:
        for app_item in app_list:
            if app_item.Visible and "System" in str(app_item.Item.Identifier.OleValue):
                tox = app_item.ScreenLeft
                toy = app_item.ScreenTop
                Log.Message(f"The object selected to drop to is: {app_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Warning("No 'System' found in application browser.")
    else:
        Log.Warning("No items found in the application browser.")

    main_screen = eng_obj.mainscreenbutton
    main_screen.drag((fromx + 100), (fromy + 15), (fromx + tox + 115), -(fromy - toy))
    Applicationutility.wait_in_seconds(1000, 'wait')

###############################################################################
# Function : drag_composite_template_drop_app_browser_folder_AE
# Description: Drags a composite template and drops it into a folder in the app browser.
# Parameter : param (str) - Template, version, and folder name in the format 'template$$version$$folder_name'.
###############################################################################
def drag_composite_template_drop_app_browser_folder_AE(param):
    template, version, folder_name = param.split('$$')
    template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if template_list:
        for template_item in template_list:
            if template_item.Visible and str(template) in str(template_item.Item.Identifier.OleValue) and str(version) == str(template_item.Item.ViewModel.Version.OleValue):
                fromx = template_item.ScreenLeft
                fromy = template_item.ScreenTop
                Log.Message(f"The object selected to drag is: {template_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Warning(f"Template '{template}' with version '{version}' not found in template browser.")
    else:
        Log.Warning("No templates found in the template browser.")

    app_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if app_list:
        for app_item in app_list:
            if app_item.Visible and str(folder_name) in str(app_item.Item.Identifier.OleValue):
                tox = app_item.ScreenLeft
                toy = app_item.ScreenTop
                Log.Message(f"The object selected to drop to is: {app_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Warning(f"Folder '{folder_name}' not found in application browser.")
    else:
        Log.Warning("No items found in the application browser.")

    main_screen = eng_obj.mainscreenbutton
    main_screen.drag((fromx + 15), (fromy + 15), (fromx + tox), -(fromy - toy))
    Applicationutility.wait_in_seconds(1000, 'wait')
    
###############################################################################
# Function : right_click_application_browser_template_AE
# Description: Right-clicks on a template in the application browser.
# Parameter : param (str) - Template identifier and version in the format 'identifier$$version'.
###############################################################################
def right_click_application_browser_template_AE(param):
    identifier, version = param.split('$$')
    app_list = aet_obj.applicationbrowsertextbox.find_children_for_treeviewrow()
    if app_list:
        for app_item in app_list:
            if app_item.Visible and str(identifier) in str(app_item.Item.Identifier.OleValue) and str(version) == str(app_item.Item.ViewModel.TemplateVersion):
                app_item.ClickR()
                Log.Message(f"Right-clicked object is: {app_item.Item.Identifier.OleValue}")
                break
        else:
            Log.Warning(f"Template '{identifier}' with version '{version}' not found.")
    else:
        Log.Warning("No templates found in the application browser.")
  
###############################################################################
# Function : right_click_application_browser_folder_AE
# Description: Right-clicks on a folder in the application browser.
# Parameter : identifier (str) - Identifier of the folder to right-click.
###############################################################################
def right_click_application_browser_folder_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          App_list[j].ClickR()
          Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
          break
    else:
      Log.Warning("InValid Identifier")
  else:
    Log.Warning("No folders found in the application browser.")
  Applicationutility.wait_in_seconds(1000, 'wait')
  
###############################################################################
# Function : right_click_asset_workspace_folder_AE
# Description: Right-clicks on a folder in the asset workspace.
# Parameter : identifier (str) - Identifier of the folder to right-click.
###############################################################################
def right_click_asset_workspace_folder_AE(identifier):
  App_browser = aet_obj.assetworkspacetextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          App_list[j].ClickR()
          Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
          break
  else:
    Log.Warning("No folders found in the asset workspace.")
  Applicationutility.wait_in_seconds(1000, 'wait')
  
###############################################################################
# Function : verify_folder_and_template_application_browser
# Description: Verifies the presence of a folder or template in the application browser.
# Parameter : identifier (str) - Identifier of the folder or template to verify.
###############################################################################
def verify_folder_and_template_application_browser(identifier):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].DataContext.Identifier.OleValue):
          Log.Checkpoint('The identifier is present : ' + str(template_list[i].DataContext.Identifier.OleValue))
          break
    else:
      Log.Warning('The identifier was not found : ' + str(identifier))
  else:
    Log.Warning("No folders or templates found in the application browser.")
    
###############################################################################
# Function : drag_app_browser_drop_asset_workspace_editor_AE
# Description: Drags an item from the app browser and drops it into the asset workspace editor.
# Parameter : template (str) - Identifier of the template to drag.
###############################################################################
def drag_app_browser_drop_asset_workspace_editor_AE(template):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if template in str(template_list[i].DataContext.Identifier.OleValue):
          fromx = template_list[i].ScreenLeft
          fromy = template_list[i].ScreenTop
          Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
          break
  else:
    Log.Warning("No templates found in the application browser.")
  
  Workspace_editor = aet_obj.assertworkspaceeditortextbox.object
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_presence = node_element_parent.FindAllChildren('ClrClassName', 'LinkNodeControl', 1000)
  n = len(node_element_presence)
  
  if n >= 1:
    tox = node_element_presence[n-1].ScreenLeft
    tox = tox/2
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
  else:
    tox = Workspace_editor.ScreenLeft
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+100), (fromy+15), tox, 0)

###############################################################################
# Function : verify_Template_node_Asset_Workstation_editor_AE
# Description: Verifies a template node in the asset workstation editor.
# Parameter : template (str) - Identifier of the template to verify.
###############################################################################
def verify_Template_node_Asset_Workstation_editor_AE(template):
  template_grid = aet_obj.nodeinstancebutton.object
  template_grid_list = aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'Grid', 1000)
  if template_grid_list:
    for i in template_grid_list:
      if template in str(i.ToolTip) and i.Visible:
        Log.Message(f'{i.ToolTip.OleValue} is successfully verified')
        break
    else:
      Log.Message(f'{template} no such template exists')
  else:
    Log.Warning("No templates found in the asset workstation editor.")
    
###############################################################################
# Function : double_click_identifier_application_browser
# Description: Double-clicks an identifier in the application browser.
# Parameter : identifier (str) - Identifier to double-click.
###############################################################################
def double_click_identifier_application_browser(identifier):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier == str(template_list[i].DataContext.Identifier.OleValue):
          template_list[i].DblClick()
          Applicationutility.wait_in_seconds(2000, 'wait')
          break
  else:
    Log.Warning("No identifiers found in the application browser.")
    
###############################################################################
# Function : verify_inspect_instance_window_name
# Description: Verifies the name of the inspect instance window.
# Parameter : name (str) - Expected name of the inspect instance window.
###############################################################################
def verify_inspect_instance_window_name(name):
  try:
    inspect_win = aet_obj.inspectinstancewindowtextbox.object
    if str(name) in str(inspect_win.Title.OleValue):
      Log.Checkpoint('Inspect Instance window is open for : ' + str(inspect_win.Title.OleValue))
  except exception as exe:
    Log.Warning('Inspect Instance window is not open')
    
###############################################################################
# Function : close_inspect_instance
# Description: Closes the inspect instance window.
# Parameter : None
###############################################################################
def close_inspect_instance():
    inspect_win = aet_obj.inspectinstancewindowtextbox
    inspect_win.click_at(inspect_win.width-30, 30)
    Applicationutility.take_screenshot()
    
###############################################################################
# Function : verify_save__changes_popup_AE
# Description: Verifies the presence of the save changes popup.
# Parameter : name (str) - Expected name of the popup.
###############################################################################
def verify_save__changes_popup_AE(name):
  window = msg_obj.exportpopupbutton.object.Visible
  if window:
    Log.Message(f'the window {msg_obj.exportpopupbutton.object.Title.OleValue} is Visible')
  else:
    Log.Warning(f'the window doesnt exists in the pop up')
    
###############################################################################
# Function : Link_from_ranged_node_to_ranged_node
# Description: Links one ranged node to another in the editor.
# Parameter : param (str) - From and to node identifiers in the format 'from_node$$to_node'.
###############################################################################
def Link_from_ranged_node_to_ranged_node(param):
  from_node, to_node = param.split('$$')
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  if node_element_list:
    for node_element in node_element_list:
      if from_node == str(node_element.DataContext.Identifier) :
            tox = node_element.ScreenLeft
            toy = node_element.ScreenTop

    for node_element in node_element_list:
      if to_node == str(node_element.DataContext.Identifier) :
        fromx = node_element.Width
        regulator1 = node_element.ScreenLeft
        regulator2 = node_element.ScreenTop
        fromy = node_element.Height
        node_element.Drag(fromx-15, fromy/2, tox-regulator1, toy-regulator2)
  else:
    Log.Warning("No nodes found in the editor.")

###############################################################################
# Function : Verify_Link_Status
# Description: Verifies the link status of instances in the application browser.
# Parameter : None
###############################################################################
def Verify_Link_Status():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for instance in instances:
      if instance.Panel_ZIndex != 0 and instance.DataContext != None:
        submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
        for i in submenuitems:
          if i.WPFControlText == "" and i.WPFControlOrdinalNo != 1:
            Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has Invalid link')
            break
        else:
          Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has valid link')
  else:
    Log.Warning("No instances found in the application browser.")
    
###############################################################################
# Function : verify_application_explorer_instance_editor_tab
# Description: Verifies the presence of an instance editor tab in the application explorer.
# Parameter : identifier (str) - Identifier of the instance editor tab to verify.
###############################################################################
def verify_application_explorer_instance_editor_tab(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].Header.OleValue):
          Log.Checkpoint('The instance editor tab is open : ' + str(template_list[i].Header.OleValue))
          break
    else:
      Log.Warning('The instance editor tab was not found : ' + str(identifier))
  else:
    Log.Warning("No instance editor tabs found in the application explorer.")
    
###############################################################################
# Function : application_explorer_instance_editor_tab_close
# Description: Closes an instance editor tab in the application explorer.
# Parameter : identifier (str) - Identifier of the instance editor tab to close.
###############################################################################
def application_explorer_instance_editor_tab_close(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].Header.OleValue):
          template_list[i].Click((template_list[i].Width-15), (template_list[i].Height/2))
  else:
    Log.Warning("No instance editor tabs found in the application explorer.")

def asvfg():
  application_explorer_instance_editor_tab_close('Manage')
        
###############################################################################
# Function : enter_instance_description_AE_instance_editor
# Description: Enters a description for an instance in the instance editor.
# Parameter : None
###############################################################################
def enter_instance_description_AE_instance_editor():
  des = aet_obj.instancedescriptionbutton.object
  des_list = des.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  if des_list:
    for item in des_list:
      cells = item.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
      for cell in cells:
        if 'Instance Description' == str(cell.WPFControlText):
          item.Click((item.Width-25), (item.height/2) )
          Sys.Keys('Added Description !!')
          break
  else:
    Log.Warning("No descriptions found in the instance editor.")
                              
###############################################################################
# Function : expand_uncheck_all_filters_temp_browser_AE
# Description: Expands and unchecks all filters in the template browser.
# Parameter : None
###############################################################################
def expand_uncheck_all_filters_temp_browser_AE():
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'Expander', 1000) 
  if template_list:
    Applicationutility.wait_in_seconds(500, 'wait')
    expander = template_list[0]
    if not expander.IsExpanded:
      expander.Click()
    list = expander.FindAllChildren('ClrClassName', 'ListBoxItem', 1000) 
    for item in list:
      if item.Visible:
        if item.DataContext.IsSelected:
          Log.Message(item.DataContext.IsSelected)
          item.DataContext.IsSelected = False    
  else:
    Log.Warning("No filters found in the template browser.")

###############################################################################
# Function : extract_template_csvdata_AE
# Description: Extracts template data from a CSV file and verifies it with the application.
# Parameter : None
###############################################################################
def extract_template_csvdata_AE():
  # combines system name and file format
  exported_csv = Project.Variables.system_1 + ".csv"
  Applicationutility.wait_in_seconds(10000, 'wait')
  
  # collect all the template in Application Browser
  template_details = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  
  # extract csv file
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_csv))
  with open(d_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        # all rows are stored in data list
        data = [str(row) for row in reader if len(row) >=1]
        # log Export version
        for j in data:
          if "Export Version" in str(j):
            Log.Message(str(j)) 
            break
        else:
          Log.Message("Export Version not found in excel")
        
        #checks for Template Details in data list
        for i in template_details:
          if i.WPFControlText in str(data) and i.WPFControlText not in ["Valid", "","InValid"] :
            Log.Message(f'Excel data is verified with {i.WPFControlText} in Application' )                             

###############################################################################
# Function : Enter_systemName_systemlocation_ExportWindow_AE
# Description: Enters the system name and location in the export window.
# Parameter : file_format (str) - File format for the export.
###############################################################################
def Enter_systemName_systemlocation_ExportWindow_AE(file_format):
  if not Project.Variables.VariableExists('system_1'):
        Project.Variables.AddVariable('system_1', "String")
  Project.Variables.system_1 = str('System1_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Log.Message(Project.Variables.system_1)
  Applicationutility.wait_in_seconds(2000,"Wait")
  Export_window = msg_obj.exportfilenametextbox.object
  
  if Export_window.Exists:
    filename_textbox = msg_obj.exportfilenametextbox.object
    filename_textbox.Keys(Project.Variables.system_1+file_format)
  else:
    Log.Warning("Export Windows doesnt exists")
  filelocation = msg_obj.exportfilelocationtextbox
  tox = (filelocation.object.Height)/2
  toy = 10
  filelocation.click_at(tox,toy)
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")

###############################################################################
# Function : import_TE
# Description: Imports a file into the application.
# Parameter : None
###############################################################################
def import_TE():
  Export_window = aet_obj.comboboxtextbox.object
  
  if Export_window.Exists:
    filename_textbox = aet_obj.comboboxtextbox.object
    filename_textbox.Keys(Project.Variables.system_1+".sbk")
  else:
    Log.Warning("Export Windows doesnt exists")
  filelocation = msg_obj.exportfilelocationtextbox
  tox = (filelocation.object.Height)/2
  toy = 5
  filelocation.click_at(tox,toy)
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")

###############################################################################
# Function : Explorer_buttons_AE
# Description: Clicks a button in the explorer window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Explorer_buttons_AE(button_name):
  buttons_list = msg_obj.exportwpopupbutton.object.FindAllChildren('WndClass', 'Button', 1000)
  if buttons_list:
    for button in buttons_list:
      if button_name in str(button.WndCaption) :
        button.click()
        break
    else:
      Log.Warning("Button name mentioned doesnt exists")
  else:
    Log.Warning("No buttons found in the explorer window.")
    
###############################################################################
# Function : Explorer_buttons_TE
# Description: Clicks a button in the explorer window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Explorer_buttons_TE(button_name):
  buttons_list = msg_obj.exportbutton.object.FindAllChildren('WndClass', 'Button', 1000)
  if buttons_list:
    for button in buttons_list:
      if button_name in str(button.WndCaption) :
        button.click()
        break
    else:
      Log.Warning("Button name mentioned doesnt exists")
  else:
    Log.Warning("No buttons found in the explorer window.")

###############################################################################
# Function : Verify_already_exists_Popup_message_AE
# Description: Verifies the presence of a popup message indicating a file already exists.
# Parameter : None
###############################################################################
def Verify_already_exists_Popup_message_AE():
  Message_AE = msg_obj.exportwpopuptextbox.object
  Message_list_AE = Message_AE.FindAllChildren('WndClass', 'Static', 1000)
  if Message_list_AE:
    for item in Message_list_AE:
      if "Do you want to replace it?" in str(item.WndCaption) and item.WndCaption != "" :
        Log.Message(f'{item.WndCaption} sucessfully verified')
        break
    else:
      Log.Warning("message:already exists.Do you want to replace it? doesnt exists")  
  else:
    Log.Warning("No messages found in the popup.")
    
###############################################################################
# Function : export_System1_Export_Popup_AE
# Description: Verifies the presence of a popup message during export.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def export_System1_Export_Popup_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  if windowlist:
    for item in windowlist:
      if message in str(item.Text):
        Log.Message(f'message is verified as: {item.Text}')
        break
    else:
      Log.Message("{message} doesnt exists in the pop up")
  else:
    Log.Warning("No messages found in the export popup.")
    
###############################################################################
# Function : export_System1_Export_Popup_AE_buttons
# Description: Clicks a button in the export popup.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def export_System1_Export_Popup_AE_buttons(button_name):
    buttons_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                Log.Message(button.WPFControlText)
                break
        else:
            Log.Warning("Button name mentioned doesn't exist.")
    else:
        Log.Warning("No buttons found in the export popup.")
    
###############################################################################
# Function : extract_template_xmldata_AE
# Description: Extracts template data from an XML file and verifies it with the application.
# Parameter : None
###############################################################################
def extract_template_xmldata_AE():
    # Combines system name and file format
    exported_xml = Project.Variables.system_1 + ".xml"
  
    # Collect all the template details in the Application Browser
    template_details = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  
    # Extract XML file
    d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
    tree = ET.parse(d_path)
    root = tree.getroot()

    # Convert XML elements to strings for easier searching
    data = [ET.tostring(element, encoding='unicode') for element in root.iter()]
    
    # Log Export Version
    export_version = root.attrib.get("Version")
    Log.Message(f"Export Version: {export_version}")
        
    # Check for Template Details in data list
    if template_details:
      for detail in template_details:
          if detail.WPFControlText in str(data) and detail.WPFControlText not in ["Valid", "","InValid"]:
              Log.Message(f'XML data is verified with {detail.WPFControlText} in Application')
    else:
      Log.Warning("No template details found in the application browser.")
            
###############################################################################
# Function : verify_modification_popup
# Description: Verifies the presence of a modification popup message.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def verify_modification_popup(message):
  popupmsg = msg_obj.exportpopupbutton.object.MainText.OleValue
  if message in popupmsg:
    Log.Message(f'{popupmsg} has been verified')
  else:
    Log.Message(f'{message} does not exits in popup')
    
###############################################################################
# Function : verify_files_existance_Project_Variable_AE
# Description: Verifies the existence of a file based on a project variable.
# Parameter : filetype (str) - File type to verify.
###############################################################################
def verify_files_existance_Project_Variable_AE(filetype):
  exported_xml = Project.Variables.system_1 + filetype
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
  if not os.path.exists(d_path):
    Log.Error(f"File not found: {d_path}")
  else:
    Log.Message(f"File found: {d_path}")
    
###############################################################################
# Function : verify_files_existance_AE
# Description: Verifies the existence of a file.
# Parameter : filename_with_extension (str) - Filename with extension to verify.
###############################################################################
def verify_files_existance_AE(filename_with_extension):
  d_path = os.path.abspath(os.path.join(os.getcwd(), filename_with_extension))
  if not os.path.exists(d_path):
    Log.Error(f"File not found: {d_path}")
  else:
    Log.Message(f"File found: {d_path}")
    
###############################################################################
# Function : delete_all_files_Post_Condition
# Description: Deletes all files in the post condition.
# Parameter : None
###############################################################################
def delete_all_files_Post_Condition():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    for node in SE_node_list:
      if node.DataContext.Identifier.OleValue == "Systems Explorer":
        pass
      else:
        Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
        Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
        Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
        try:
          Engineeringclientutility.circularprogressbar_Wait()
        except:
          Log.Message("Progress bar was not visible")
  else:
    Log.Warning("No files found in the post condition.")
      
###############################################################################
# Function : delete_created_system1_Project_Variable
# Description: Deletes the created system based on a project variable.
# Parameter : None
###############################################################################
def delete_created_system1_Project_Variable():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    for node in SE_node_list:
      if node.DataContext.Identifier.OleValue == Project.Variables.system_1:
        Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
        Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
        Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
        ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  else:
    Log.Warning("No systems found in the project variable.")

###############################################################################
# Function : Verify_Notification_Message
# Description: Verifies the presence of a notification message.
# Parameter : None
###############################################################################
def Verify_Notification_Message():
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_in_seconds(5000, 'wait')  
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  if N_Message_List:
    for i in N_Message_List:
      if i.Visible and i.Panel_ZIndex == 0:
        Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
        break
  else:
    Log.Warning("No messages found in the notification panel.")
          
###############################################################################
# Function : Click_on_Button_Conflict_Dialog
# Description: Clicks a button in the conflict dialog.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Click_on_Button_Conflict_Dialog(button_name):##
  buttons = msg_obj.importconflictdialogtextbox.object.FindAllChildren("ClrClassName", "Button", 50)
  if buttons:
    for button in buttons:
      if button_name in button.WPFControlText:
        button.click()
        break
    else:
      Log.Warning(f'Mentioned {button_name} does not exists in Conflict_Dialog' )
  else:
    Log.Warning("No buttons found in the conflict dialog.")
    
###############################################################################
# Function : Import_File_Directory
# Description: Sets the import file directory.
# Parameter : None
###############################################################################
def Import_File_Directory():##

  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path)
  Log.Message(f"New working directory: {os.getcwd()}")
  if not Project.Variables.VariableExists("ImportTestFile_path"):
          Project.Variables.AddVariable("ImportTestFile_path", "String")
  Project.Variables.ImportTestFile_path = os.getcwd()     
      
###############################################################################
# Function : Enter_systemName_systemlocation_ImportWindow_AE
# Description: Enters the system name and location in the import window.
# Parameter : file_format (str) - File format for the import.
###############################################################################
def Enter_systemName_systemlocation_ImportWindow_AE(file_format):
#  Import_window = aet_obj.importtextbox.object
#  if Import_window.Exists:
  filelocation = aet_obj.addressbandtextbox
  tox = (filelocation.object.Height)/2
  toy = 5
  filelocation.click_at(tox,toy)
  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path) 
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]") 
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(file_format)
  Applicationutility.take_screenshot('taking Screenshot')
  Sys.Keys("[Enter]")
  
###############################################################################
# Function : Import_System1_Popup_AE_buttons
# Description: Clicks a button in the import popup.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def Import_System1_Popup_AE_buttons(button_name):
    buttons_list = aet_obj.importtextbox.object.FindAllChildren('WndClass', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            Log.Message(button.WndCaption)
            if button_name in str(button.WndCaption):
                button.click()
                break
        else:
            Log.Warning("Button name mentioned doesn't exist.")
    else:
        Log.Warning("No buttons found in the import popup.")
  
###############################################################################
# Function : Wait_for_Import_pop_up_AE
# Description: Waits for the import popup to appear.
# Parameter : None
###############################################################################
def Wait_for_Import_pop_up_AE():
  try:
    windows = aet_obj.importdialogbutton.object
    windows.WaitProperty("Visible", True)
  except:
    Log.Error('Wait for import popup')
  
###############################################################################
# Function : importdialog_popup_button_AE_buttons
# Description: Clicks a button in the import dialog popup.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def importdialog_popup_button_AE_buttons(button_name):
    buttons_list = aet_obj.importdialogbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                break
        else:
            Log.Warning("Button name mentioned doesn't exist.")
    else:
        Log.Warning("No buttons found in the import dialog popup.")     

###############################################################################
# Function : Verify_Warning_Popup_locked_instance_AE
# Description: Verifies the presence of a warning popup for a locked instance.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def Verify_Warning_Popup_locked_instance_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  if windowlist:
    for item in windowlist:
      if message in str(item.Text):
        Log.Message(f'message is verified as: {item.Text}')
        break
    else:
      Log.Message(f'{message} doesnt exists in the pop up')
  else:
    Log.Warning("No messages found in the warning popup.")
    
###############################################################################
# Function : MessageWindow_buttons
# Description: Clicks a button in the message window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def MessageWindow_buttons(button_name):
    buttons_list = aet_obj.savechangesdialogboxtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                break
        else:
            Log.Warning("Button name mentioned doesn't exist.")
    else:
        Log.Warning("No buttons found in the message window.")
    
###############################################################################
# Function : Verify_DeleteMessage_content_AE
# Description: Verifies the content of a delete message popup.
# Parameter : message (str) - Expected message in the popup.
###############################################################################
def Verify_DeleteMessage_content_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  if windowlist:
    for item in windowlist:
      if message in str(item.Text):
        Log.Message(f'message is verified as: {item.Text}')
        break
    else:
      Log.Message(f'{message} doesnt exists in the pop up')
  else:
    Log.Warning("No messages found in the delete message popup.")
  
###############################################################################
# Function : verify_application_browser_template_AE
# Description: Verifies the presence of a template in the application browser.
# Parameter : identifier (str) - Identifier of the template to verify.
###############################################################################
def verify_application_browser_template_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          param = str(App_list[j].Item.ViewModel.TemplateVersion)
  
    Applicationutility.modal_dialog_window_button('OK')
  
    Applicationutility.wait_in_seconds(1500, 'wait')
    App_browser = aet_obj.applicationbrowsertextbox
    App_list = App_browser.find_children_for_treeviewrow()
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          if str(param) != str(App_list[j].Item.ViewModel.TemplateVersion):
            Log.Checkpoint('The ' + str(App_list[j].Item.Identifier.OleValue) + ' template is updated to ' + str(App_list[j].Item.ViewModel.TemplateVersion))
            break
    else:
      Log.Warning('The template is not updated')
    Applicationutility.take_screenshot()
  else:
    Log.Warning("No templates found in the application browser.")
  
###############################################################################
# Function : delete_system_Folder
# Description: Deletes a system folder.
# Parameter : node_name (str) - Name of the node to delete.
###############################################################################
def delete_system_Folder(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    for node in SE_node_list:
      if node.DataContext.Identifier.OleValue == node_name :
        Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
        Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
        Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
        try:
          ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
        except:
          Log.Message("Circular progrss bar doesnt appear for folder deletion")
  else:
    Log.Warning("No folders found in the system.")
  
###############################################################################
# Function : delete_all_folder_system_ord_EC
# Description: Deletes all folders in the system in order.
# Parameter : None
###############################################################################
def delete_all_folder_system_ord_EC():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if SE_node_list:
    h_level = [int(i.HierarchyLevel) for i in SE_node_list]
    n = max(h_level)
    Log.Message(n)
    for i in range(n, 0, -1):
      for ord in SE_node_list:
        if int(ord.HierarchyLevel) == 0:
          pass
        elif ord.HierarchyLevel == i:
          Log.Message(i)
          Engineeringclientutility.clickR_node_ordno_SE(ord.WPFControlOrdinalNo)
          Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
          Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
          try:
            ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
          except:
            Log.Message("Circular progress bar doesnt appear for folder deletion")
  else:
    Log.Warning("No folders found in the system.")
          
###############################################################################
# Function : close_Message_Window
# Description: Closes the message window.
# Parameter : None
###############################################################################
def close_Message_Window():
    inspect_win = msg_obj.renamepopupbutton
    inspect_win.click_at(inspect_win.width-25, 25)
    Applicationutility.take_screenshot()   
 
###############################################################################
# Function : Wait_import_conflict_dialog_AE
# Description: Waits for the import conflict dialog to appear.
# Parameter : None
###############################################################################
def Wait_import_conflict_dialog_AE():
   try:
    Conflict_dialog_box = aet_obj.importconflictdialogtextbox.object
    Conflict_dialog_box.WaitProperty("Visible", True)
   except:
    Log.Message("Conflict Dialog Box did not exists") 
   
###############################################################################
# Function : ConflictWindow_buttons
# Description: Clicks a button in the conflict window.
# Parameter : button_name (str) - Name of the button to click.
###############################################################################
def ConflictWindow_buttons(button_name):
    buttons_list = aet_obj.importconflictdialogtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
    if buttons_list:
        for button in buttons_list:
            if button_name in str(button.WPFControlText):
                button.click()
                break
        else:
            Log.Warning("Button name mentioned doesn't exist.")
    else:
        Log.Warning("No buttons found in the conflict window.")
    
###############################################################################
# Function : Verify_latest_template_added_Application_browser_AE
# Description: Verifies the presence of the latest template added in the application browser.
# Parameter : template_name (str) - Name of the template to verify.
###############################################################################
def Verify_latest_template_added_Application_browser_AE(template_name):
  AB_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if AB_list:
    for template in AB_list:
      if template_name == template.DataContext.Identifier.OleValue:
        Log.Message(f'{template_name} exists in Application browser')
        break
    else:
      Log.Message(f'{template_name} does not exists in Application browser')
  else:
    Log.Warning("No templates found in the application browser.")
    
###############################################################################
# Function : template_checkbox
# Description: Checks or unchecks a template checkbox.
# Parameter : param (str) - Template identifier and state in the format 'identifier$$state'.
###############################################################################
def template_checkbox(param):
  identifier, state = param.split('$$')
  obj = aet_obj.instanceeditorchecklisttextbox.object
  obj_list = obj.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if obj_list:
    for item in obj_list:
      if str(identifier) in str(item.DataContext.ElementFullPath.OleValue):
        checkbox = item.FindAllChildren('ClrClassName', 'CheckBox', 1000)
        break
    if int(state) != 0 :
      checkbox[0].wState = 1
      checkbox[0].WaitProperty('wState', 1, 100000)
      Log.Message('Checked')
    elif int(state) != 1:
      checkbox[0].wState = 0
      Log.Message('Unchecked')
  else:
    Log.Warning("No checkboxes found in the template.")
    
def TC_EPE_AE_00012_and_TC_EPE_AE_00014():
  click_application_browser_template_AE('MotorGP_1$$1.0.123')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^c')
  click_application_browser_folder_AE('Folder_2')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^v')

def TC_EPE_AE_00012_and_TC_EPE_AE_00014_1():
  click_application_browser_template_AE('ValveGP_1$$1.0.100')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^c')
  click_application_browser_folder_AE('Folder_2')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('^v')  
  
###############################################################################
# Function : click_application_browser_template_AE
# Description: Clicks a template in the application browser.
# Parameter : param (str) - Template identifier and version in the format 'identifier$$version'.
###############################################################################
def click_application_browser_template_AE(param):
  identifier,version=param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          if str(version) == str(App_list[j].Item.ViewModel.TemplateVersion):
            App_list[j].Click()
            Log.Message('Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
            break
    Applicationutility.wait_in_seconds(1000, 'wait')
  else:
    Log.Warning("No templates found in the application browser.")
  
###############################################################################
# Function : click_application_browser_folder_AE
# Description: Clicks a folder in the application browser.
# Parameter : identifier (str) - Identifier of the folder to click.
###############################################################################
def click_application_browser_folder_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if App_list[j].Visible:
        if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
          App_list[j].Click()
          Log.Message('Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
  else:
    Log.Warning("No folders found in the application browser.")
       
def instance_locked_close_AE():
  msg_obj.exportpopupbutton.object.close()      
  
def Verify_file_existance():
  exported_xml = Project.Variables.system_1 + ".xml"
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
  if not os.path.exists(d_path):
    Log.Message(f"File does not exist: {d_path}")  

###############################################################################
# Function : verify_instance_validity
# Description: Verifies the validity of instances in the application browser.
# Parameter : None
###############################################################################
def verify_instance_validity():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for instance in instances:
      if instance.Panel_ZIndex != 0 and instance.DataContext != None:
        submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
        for i in submenuitems:
          if i.WPFControlText == "" and i.WPFControlOrdinalNo != 1:
            Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has Invalid link')
            break
        else:
          Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has valid link')
  else:
    Log.Warning("No instances found in the application browser.")
  
###############################################################################
# Function : expand_folder_system
# Description: Expands all folders in the system.
# Parameter : None
###############################################################################
def expand_folder_system():
  ApplicationBroswer = aet_obj.applicationbrowsertextbox.object
  instances = ApplicationBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for i in instances:
      if i.IsExpandable == True:
        i.IsExpanded = True
        continue
  else:
    Log.Warning("No folders found in the system.")
      
###############################################################################
# Function : verify_instance_application_browser
# Description: Verifies the presence of an instance in the application browser.
# Parameter : param (str) - Identifier of the instance to verify.
###############################################################################
def verify_instance_application_browser(param):
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if instances:
    for instance in instances:
      if instance.Panel_ZIndex != 0 and instance.DataContext != None:
  #        Log.Message(str(instance.DataContext.Identifier.OleValue) + ' is  present in the Application browser')
        if param in str(instance.DataContext.Identifier.OleValue):
          Log.Checkpoint(f'{str(instance.DataContext.Identifier.OleValue)} is present in Application Browser')
          break
    else:
      Log.Warning(f'{param} is not present in Application Browser')
  else:
    Log.Warning("No instances found in the application browser.")
        
###############################################################################
# Function : verify_SameName_Errorbox_application_browser
# Description: Verifies the presence of a same name error box in the application browser.
# Parameter : None
###############################################################################
def verify_SameName_Errorbox_application_browser():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TemplatedAdorner', 1000)
  if instances:
    Log.Message(len(instances))
    for instance in instances:
      if instance.IsVisible:
        Log.Message(f'{instance.AdornedElement.ToolTip.OleValue} appeared on the screen as a ToolTip Value')
        break
    else:
      Log.Message(f'{instance.AdornedElement.ToolTip.OleValue} did not appear on the screen as a ToolTip Value')
  else:
    Log.Warning("No error boxes found in the application browser.")
    
###############################################################################
# Function : rename_instance_popup_button
# Description: Clicks a button in the rename instance popup.
# Parameter : button (str) - Name of the button to click.
###############################################################################
def rename_instance_popup_button(button):
  rename_intance_object = aet_obj.renameinstancepopupmessagebutton.object
  buttons = rename_intance_object.FindAllChildren('ClrClassName', 'Button', 1000)
  if buttons:
    for i in buttons:
      if button in i.WPFControlText:
        i.Click()
        break
    else:
      Log.Message("No such button exists")
  else:
    Log.Warning("No buttons found in the rename instance popup.")
    
###############################################################################
# Function : Verify_node_link_line_asset_work_AE
# Description: Verifies the presence of a node link line in the asset workspace.
# Parameter : param (str) - Identifier of the node to verify.
###############################################################################
def Verify_node_link_line_asset_work_AE(param):
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  if node_element_list:
    for node_element in node_element_list:
      if param == str(node_element.DataContext.Identifier):
        tox = node_element.Width
        toy = node_element.Height
        node_element.ClickR(tox-5, toy/2)
        try:
          if eng_obj.rclickmenutextbox.exists:  
            Log.Checkpoint('verified two instances linked between elements')
        except:
          Log.Message('Instances are unlinked')
  else:
    Log.Warning("No nodes found in the asset workspace.")
        
###############################################################################
# Function : Right_click_Assestworkspace_editor_AE
# Description: Right-clicks an instance in the asset workspace editor.
# Parameter : None
###############################################################################
def Right_click_Assestworkspace_editor_AE():
  template_list = aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'InstanceNode', 1000)
  if template_list:
    for node in template_list:
      if 'ValveGP_1' in str(node.DataContext.Identifier.OleValue):
        Log.Message('verified instance name')
        node.ClickR((node.width/2), (25))
        Log.Message('Right clicked on instance name')
  else:
    Log.Warning("No instances found in the asset workspace editor.")
      
###############################################################################
# Function : click_Abort_AE
# Description: Clicks the abort button in the notification panel.
# Parameter : None
###############################################################################
def click_Abort_AE():
   Abort_list = msg_obj.notificationpanneltextbox.object.FindAllChildren('ClrClassName', 'Path', 1000)
   if Abort_list:
    Log.Message(len(Abort_list))
    for i in Abort_list:
      if i.DataContext.ParentStatus.OleValue == "Executing":
        i.Click()
        break
   else:
    Log.Warning("No abort buttons found in the notification panel.")

###############################################################################
# Function : replace_template_combo_AE
# Description: Replaces a template in the combo box.
# Parameter : param (str) - Template identifier and version in the format 'identifier$$version'.
###############################################################################
def replace_template_combo_AE(param):
    identifier, version = param.split('$$')
    comb = aet_obj.replacetemplatecombotextbox.object
    if comb.Items.Count:
      for i in range(comb.Items.Count):
        if identifier in comb.Items.Item[i].TemplateName.OleValue:
          if version in comb.Items.Item[i].TemplateName.OleValue:
            comb.SelectedIndex = i
            Log.Message('The Selected template is ' + str(comb.Items.Item[i].TemplateName.OleValue))
            Applicationutility.wait_in_seconds(1500, 'wait')
            aet_obj.replacetemplatetextbox.click()
            break
      else:
        Log.Warning('No template with ' + str(identifier) + ' and ' + str(version))
    else:
      Log.Warning("No templates found in the combo box.")
      
###############################################################################
# Function : capture_template_application_browser_AE
# Description: Captures a template in the application browser.
# Parameter : identifier (str) - Identifier of the template to capture.
###############################################################################
def capture_template_application_browser_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        return identifier + str('$$')+ str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue)
  else:
    Log.Warning("No templates found in the application browser.")

###############################################################################
# Function : verify_template_replaced_AE
# Description: Verifies that a template has been replaced in the application browser.
# Parameter : param (str) - Template identifier and new template in the format 'identifier$$template'.
###############################################################################
def verify_template_replaced_AE(param):
  identifier, template = param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  if App_list:
    for j in range(len(App_list)):
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        if str(template) != str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue):
          Log.Checkpoint('The Template ' + str(template) + ' is changed to ' + str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue))
          break
        else:
          Log.Message('The Template ' + str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue) + ' is not changed.' )  
  else:
    Log.Warning("No templates found in the application browser.")
        
###############################################################################
# Function : verify_button_enabled_disabled_modaldialogue_window
# Description: Verifies whether a button is enabled or disabled in a modal dialogue window.
# Parameter : button_name (str) - Name of the button to verify.
###############################################################################
def verify_button_enabled_disabled_modaldialogue_window(button_name):
  buttons_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
  if buttons_list:
    for button in buttons_list:
      if button_name in str(button.WPFControlText):
        if  not button.Enabled:
          Log.Message( str(button.WPFControlText) + ' button is disabled')
          Applicationutility.take_screenshot()
          break
        else:
             Log.Message(str(button.WPFControlText) +" button is Enabled")
  else:
    Log.Warning("No buttons found in the modal dialogue window.")
           
###############################################################################
# Function : verify_template_application_browser
# Description: Verifies the presence of a template in the application browser.
# Parameter : param (str) - Template identifier and version in the format 'template$$version'.
###############################################################################
def verify_template_application_browser(param):
  template, version = param.split('$$')
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible:
        if template_list[i].DataContext.ViewModel.DisplayTypeName.OleValue != 'Folder':
          if template in template_list[i].DataContext.ViewModel.TemplateIdentifier.OleValue:
            if version in str(template_list[i].DataContext.ViewModel.TemplateVersion.OleValue):
              Log.Checkpoint(str(template_list[i].DataContext.ViewModel.TemplateIdentifier.OleValue) +' '+  str(template_list[i].DataContext.ViewModel.TemplateVersion.OleValue))
              break
    else:
      Log.Warning(f'Template {template} - {version} not in Application Browser')     
  else:
    Log.Warning("No templates found in the application browser.")
      
###############################################################################
# Function : wait_import_dialogue_window_appear
# Description: Waits for the import dialogue window to appear.
# Parameter : None
###############################################################################
def wait_import_dialogue_window_appear():
  try:
    Import_window = aet_obj.importtextbox.object
    Import_window.WaitProperty('Visible',True, 1000)
    Log.Message("Import window  appeared")   
  except:
    Log.Message("Import window did not appear")

###############################################################################
# Function : Verify_Notification_pannel_Message
# Description: Verifies the presence of a notification panel message.
# Parameter : Message (str) - Expected message in the notification panel.
###############################################################################
def Verify_Notification_pannel_Message(Message):
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_for_execution()
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  if N_Message_List:
    for i in N_Message_List:
      if i.Visible and i.Panel_ZIndex == 0:
        if Message in i.DataContext.Message.OleValue:
          Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
          break
        else:
          Log.Message(f'{i.DataContext.Message.OleValue} in Notification Pannel')
  else:
    Log.Warning("No messages found in the notification panel.")
        
def jsjsjs():
  Verify_Notification_pannel_Message("Close Refine Online Editor (Completed)")

## this method can be used for drag and drop intances in assetworkspace or linkeditor based on position 
## only 3 position can be defined based on the screen width

###############################################################################
# Function : drag_app_browser_drop_asset_workspace_editor_with_POS_AE
# Description: Drags an item from the app browser and drops it into the asset workspace editor at a specified position.
# Parameter : param (str) - Template identifier and position in the format 'template$$pos'.
###############################################################################
def drag_app_browser_drop_asset_workspace_editor_with_POS_AE(param):
  Log.Message(param)
  template, pos = param.split('$$')
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if template in str(template_list[i].DataContext.Identifier.OleValue):
          fromx = template_list[i].ScreenLeft
          fromy = template_list[i].ScreenTop
          Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
          break
  else:
    Log.Warning("No templates found in the application browser.")
  
  Workspace_editor = aet_obj.assertworkspaceeditortextbox.object
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_presence = node_element_parent.FindAllChildren('ClrClassName', 'LinkNodeControl', 1000)
  n = len(node_element_presence)
  
  if pos == '1':
    tox = node_element_presence[n-1].ScreenLeft
    tox = tox/2
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
  elif pos == '2':
    tox = Workspace_editor.ScreenLeft
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
  else:
    tox = node_element_presence[n-1].ScreenLeft
    tox = tox*1.25
    main_screen = eng_obj.mainscreenbutton   
    main_screen.drag((fromx+15), (fromy+15), tox, 0)
    
###############################################################################
# Function : verify_application_explorer_instance_editor_tab1
# Description: Verifies the presence of an instance editor tab in the application explorer.
# Parameter : identifier (str) - Identifier of the instance editor tab to verify.
###############################################################################
def verify_application_explorer_instance_editor_tab1(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  if template_list:
    for i in range(len(template_list)):
      if template_list[i].Visible: 
        if identifier in str(template_list[i].Header.OleValue):
          Log.Checkpoint('The instance editor tab is open : ' + str(template_list[i].Header.OleValue))
          break
    else:
      Log.Warning('The instance editor tab was not found : ' + str(identifier))
  else:
    Log.Warning("No instance editor tabs found in the application explorer.")

###############################################################################
# Function : remove_PV_ranged_link_AE
# Description: Removes the PV ranged link in the asset workspace.
# Parameter : None
###############################################################################
def remove_PV_ranged_link_AE():
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  if node_element_list:
    for node_element in node_element_list:
      if 'PVRanged' == str(node_element.DataContext.Identifier):
        tox = node_element.Width
        toy = node_element.Height
        node_element.ClickR(tox-5, toy/2)
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Engineeringclientutility.select_ContextMenu_Items_EC('Delete')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        break
    else:
      Log.Warning('PVRanged not found.')
  else:
    Log.Warning("No nodes found in the asset workspace.")
    
###############################################################################
# Function : EmptyPages_ImportWindow_PE
# Description: Enters the system name and location in the import window for empty pages.
# Parameter : file_format (str) - File format for the import.
###############################################################################
def EmptyPages_ImportWindow_PE(file_format):
  filelocation = aet_obj.addressbandtextbox
  tox = (filelocation.object.Height)/2
  toy = 10
  filelocation.click_at(tox,toy)
  base_path = os.getcwd()
  folder_name =  "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path) 
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(file_format)
````
