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

def expand_templates_browser(lst):
  identifiers_list = lst.split(',')
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  Applicationutility.wait_in_seconds(500, 'wait')
  for j in identifiers_list:
    for i in range(len(template_list)):
      if template_list[i].Visible:
        if str(template_list[i].DataContext.Identifier) == str(j):
          if not template_list[i].IsExpanded:
            template_list[i].DblClick(50,(template_list[i].Height/2))
  Log.Message(identifiers_list[-1])
            
def collapse_templates_browser(lst):
  identifiers_list = lst.split(',')
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  Applicationutility.wait_in_seconds(500, 'wait')
  for j in identifiers_list:
    for i in range(len(template_list)):
      if template_list[i].Visible:
        if str(template_list[i].DataContext.Identifier) == str(j):
          if template_list[i].IsExpanded:
            template_list[i].DblClick(50,(template_list[i].Height/2))

def check_composite_templates_temp_browser():
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  Applicationutility.wait_in_seconds(500, 'wait')
  for i in range(len(template_list)):
      if template_list[i].Visible: 
        if not template_list[i].Item.ViewModel.Version.OleValue == '':
          Log.Checkpoint(str(template_list[i].Item.Identifier.OleValue) + '  -  ' + str(template_list[i].Item.ViewModel.Version.OleValue) + '  -  ' + str(template_list[i].Item.ViewModel.Description.OleValue))
  
def click_on_scroll_down_temp_browser(count):
  temp_browser = aet_obj.templatesbrowsertextbox
  for _ in range(int(count)):
    temp_browser.click_at((temp_browser.width-15), (temp_browser.height-35))
  
def click_on_scroll_up_temp_browser(count=0):
  temp_browser = aet_obj.templatesbrowsertextbox
  for _ in range(int(count)):
    temp_browser.click_at((temp_browser.width-15), (100))    
    
def check_temp_browser_list():
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  Applicationutility.wait_in_seconds(500, 'wait')
  for i in range(len(template_list)):
      if template_list[i].Visible:
        Log.Checkpoint(str(template_list[i].Item.Identifier.OleValue))

def search_template_browser_AE(search_text):
  App_browser = aet_obj.applicationbrowsertextbox.object
  temp_browser = aet_obj.templatesbrowsertextbox.object
  search = temp_browser.FindAllChildren('ClrClassName', 'SearchComboBoxControl', 50)
  search[0].Click()
  #search.Click()
  #temp_browser.Click((temp_browser.width/2), 50)
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys(search_text)
  Applicationutility.wait_in_seconds(2500, 'wait')
  aet_obj.workspacebutton.object.Click()
  
def sgsgs():
  search_template_browser_AE("Motor")
  
  
   
def drag_composite_template_drop_app_browser_system1_AE(param):
  template, version = param.split('$$')
  Applicationutility.wait_in_seconds(2500, 'wait')
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
      if template_list[i].Visible:
        if str(template) in str(template_list[i].Item.Identifier.OleValue):
          if str(version) == str(template_list[i].Item.ViewModel.Version.OleValue):
            fromx = template_list[i].ScreenLeft
            fromy = template_list[i].ScreenTop
            Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
            break
  App_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if "System" in str(App_list[j].Item.Identifier.OleValue):
        tox = App_list[j].ScreenLeft
        toy = App_list[j].ScreenTop
        Log.Message('The object selected to drop to is : ' + str(App_list[j].Item.Identifier.OleValue))
        break
  main_screen = eng_obj.mainscreenbutton    
  main_screen.drag((fromx+15), (fromy+15), (fromx+tox+115), -(fromy-toy))
  Applicationutility.wait_in_seconds(1000, 'wait')
  
  
  
def drag_composite_template_drop_app_browser_folder_AE(param):
  template, version, folder_name = param.split('$$')
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
      if template_list[i].Visible:
        if str(template) in str(template_list[i].Item.Identifier.OleValue):
          if str(version) == str(template_list[i].Item.ViewModel.Version.OleValue):
            fromx = template_list[i].ScreenLeft
            fromy = template_list[i].ScreenTop
            Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
            break
  App_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if str(folder_name) in str(App_list[j].Item.Identifier.OleValue):
        tox = App_list[j].ScreenLeft
        toy = App_list[j].ScreenTop
        Log.Message('The object selected to drop to is : ' + str(App_list[j].Item.Identifier.OleValue))
        break
  main_screen = eng_obj.mainscreenbutton   
  main_screen.drag((fromx+15), (fromy+15), (fromx+tox), -(fromy-toy))
  Applicationutility.wait_in_seconds(1000, 'wait')
    
  
def right_click_application_browser_template_AE(param):
  identifier,version=param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        if str(version) == str(App_list[j].Item.ViewModel.TemplateVersion):
          App_list[j].ClickR()
          Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
          break
  else:
    Log.Warning("InValid Instance name")
  
  
def right_click_application_browser_folder_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        App_list[j].ClickR()
        Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
        break
  else:
    Log.Warning("InValid Identifier")
  Applicationutility.wait_in_seconds(1000, 'wait')
  
def right_click_asset_workspace_folder_AE(identifier):
  App_browser = aet_obj.assetworkspacetextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        App_list[j].ClickR()
        Log.Message('Right Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
        break
  Applicationutility.wait_in_seconds(1000, 'wait')
  
def verify_folder_and_template_application_browser(identifier):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].DataContext.Identifier.OleValue):
        Log.Checkpoint('The identifier is present : ' + str(template_list[i].DataContext.Identifier.OleValue))
        break
  else:
    Log.Warning('The identifier was not found : ' + str(identifier))
    
def drag_app_browser_drop_asset_workspace_editor_AE(template):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if template in str(template_list[i].DataContext.Identifier.OleValue):
        fromx = template_list[i].ScreenLeft
        fromy = template_list[i].ScreenTop
        Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
        break
  
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

def verify_Template_node_Asset_Workstation_editor_AE(template):
  template_grid = aet_obj.nodeinstancebutton.object
  template_grid_list = aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'Grid', 1000)
  for i in template_grid_list:
    if template in str(i.ToolTip) and i.Visible:
      Log.Message(f'{i.ToolTip.OleValue} is successfully verified')
      break
  else:
      Log.Message(f'{template} no such template exists')
    
    
def double_click_identifier_application_browser(identifier):
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier == str(template_list[i].DataContext.Identifier.OleValue):
        template_list[i].DblClick()
        Applicationutility.wait_in_seconds(2000, 'wait')
        break
    
def verify_inspect_instance_window_name(name):
  try:
    inspect_win = aet_obj.inspectinstancewindowtextbox.object
    if str(name) in str(inspect_win.Title.OleValue):
      Log.Checkpoint('Inspect Instance window is open for : ' + str(inspect_win.Title.OleValue))
  except exception as exe:
    Log.Warning('Inspect Instance window is not open')
    
def close_inspect_instance():
    inspect_win = aet_obj.inspectinstancewindowtextbox
    inspect_win.click_at(inspect_win.width-30, 30)
    Applicationutility.take_screenshot()
    
def verify_save__changes_popup_AE(name):
  window = msg_obj.exportpopupbutton.object.Visible
  if window:
    Log.Message(f'the window {msg_obj.exportpopupbutton.object.Title.OleValue} is Visible')
  else:
    Log.Warning(f'the window doesnt exists in the pop up')
    
def Link_from_ranged_node_to_ranged_node(param):
  from_node, to_node = param.split('$$')
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  
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

def Verify_Link_Status():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for instance in instances:
    if instance.Panel_ZIndex != 0 and instance.DataContext != None:
      submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
      for i in submenuitems:
        if i.WPFControlText == "" and i.WPFControlOrdinalNo != 1:
          Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has Invalid link')
          break
      else:
        Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has valid link')
    
    
def verify_application_explorer_instance_editor_tab(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].Header.OleValue):
        Log.Checkpoint('The instance editor tab is open : ' + str(template_list[i].Header.OleValue))
        break
  else:
    Log.Warning('The instance editor tab was not found : ' + str(identifier))
    
    

def application_explorer_instance_editor_tab_close(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].Header.OleValue):
        template_list[i].Click((template_list[i].Width-15), (template_list[i].Height/2))

def asvfg():
  application_explorer_instance_editor_tab_close('Manage')
        
def enter_instance_description_AE_instance_editor():
  des = aet_obj.instancedescriptionbutton.object
  des_list = des.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for item in des_list:
    cells = item.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
    for cell in cells:
      if 'Instance Description' == str(cell.WPFControlText):
        item.Click((item.Width-25), (item.height/2) )
        Sys.Keys('Added Description !!')
        break
                              
                              
def expand_uncheck_all_filters_temp_browser_AE():
  template_list = aet_obj.templatesbrowsertextbox.object.FindAllChildren('ClrClassName', 'Expander', 1000) 
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
  
  
def Explorer_buttons_AE(button_name):
  buttons_list = msg_obj.exportwpopupbutton.object.FindAllChildren('WndClass', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WndCaption) :
      button.click()
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    
def Explorer_buttons_TE(button_name):
  buttons_list = msg_obj.exportbutton.object.FindAllChildren('WndClass', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WndCaption) :
      button.click()
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")

def Verify_already_exists_Popup_message_AE():
  Message_AE = msg_obj.exportwpopuptextbox.object
  Message_list_AE = Message_AE.FindAllChildren('WndClass', 'Static', 1000)
  for item in Message_list_AE:
    if "Do you want to replace it?" in str(item.WndCaption) and item.WndCaption != "" :
      Log.Message(f'{item.WndCaption} sucessfully verified')
      break
  else:
    Log.Warning("message:already exists.Do you want to replace it? doesnt exists")  
    
    
def export_System1_Export_Popup_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  for item in windowlist:
    if message in str(item.Text):
      Log.Message(f'message is verified as: {item.Text}')
      break
  else:
    Log.Message("{message} doesnt exists in the pop up")
    
def export_System1_Export_Popup_AE_buttons(button_name):
  buttons_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
#  Log.Warning(len(buttons_list))
  for button in buttons_list  :
#    Log.Message(button.WPFControlText)
    if button_name in str(button.WPFControlText) :
      button.click()
      Log.Message(button.WPFControlText)
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    

                   
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
    for detail in template_details:
        if detail.WPFControlText in str(data) and detail.WPFControlText not in ["Valid", "","InValid"]:
            Log.Message(f'XML data is verified with {detail.WPFControlText} in Application')
            
def verify_modification_popup(message):
  popupmsg = msg_obj.exportpopupbutton.object.MainText.OleValue
  if message in popupmsg:
    Log.Message(f'{popupmsg} has been verified')
  else:
    Log.Message(f'{message} does not exits in popup')
    
def verify_files_existance_Project_Variable_AE(filetype):
  exported_xml = Project.Variables.system_1 + filetype
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
  if not os.path.exists(d_path):
    Log.Error(f"File not found: {d_path}")
  else:
    Log.Message(f"File found: {d_path}")
    
def verify_files_existance_AE(filename_with_extension):
  d_path = os.path.abspath(os.path.join(os.getcwd(), filename_with_extension))
  if not os.path.exists(d_path):
    Log.Error(f"File not found: {d_path}")
  else:
    Log.Message(f"File found: {d_path}")
    

  
def delete_all_files_Post_Condition():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
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
      
def delete_created_system1_Project_Variable():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  for node in SE_node_list:
    if node.DataContext.Identifier.OleValue == Project.Variables.system_1:
      Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
      Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
      Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
      ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)


def Verify_Notification_Message():
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_in_seconds(5000, 'wait')  
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  for i in N_Message_List:
    if i.Visible and i.Panel_ZIndex == 0:
      Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
      break
  
          
def Click_on_Button_Conflict_Dialog(button_name):##
  buttons = msg_obj.importconflictdialogtextbox.object.FindAllChildren("ClrClassName", "Button", 50)
  for button in buttons:
    if button_name in button.WPFControlText:
      button.click()
      break
  else:
    Log.Warning(f'Mentioned {button_name} does not exists in Conflict_Dialog' )
    
def Import_File_Directory():##

  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path)
  Log.Message(f"New working directory: {os.getcwd()}")
  if not Project.Variables.VariableExists("ImportTestFile_path"):
          Project.Variables.AddVariable("ImportTestFile_path", "String")
  Project.Variables.ImportTestFile_path = os.getcwd()     
      
def Enter_systemName_systemlocation_ImportWindow_AE(file_format):
#  Import_window = aet_obj.importtextbox.object
#  if Import_window.Exists:
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(file_format)
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
  
def Import_System1_Popup_AE_buttons(button_name):
    buttons_list = aet_obj.importtextbox.object.FindAllChildren('WndClass', 'Button', 1000)
    for button in buttons_list:
      Log.Message(button.WndCaption)
      if button_name in str(button.WndCaption) :
        button.click()
        break
    else:
      Log.Warning("Button name mentioned doesnt exists")
  
def Wait_for_Import_pop_up_AE():
  try:
    windows = aet_obj.importdialogbutton.object
    windows.WaitProperty("Visible", True)
  except:
    Log.Error('Wait for import popup')
  
      
def importdialog_popup_button_AE_buttons(button_name):
    buttons_list = aet_obj.importdialogbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
    for button in buttons_list:
      if button_name in str(button.WPFControlText) :
        button.click()
        break
    else:
      Log.Warning("Button name mentioned doesnt exists")     

  
def Verify_Warning_Popup_locked_instance_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  for item in windowlist:
    if message in str(item.Text):
      Log.Message(f'message is verified as: {item.Text}')
      break
  else:
    Log.Message(f'{message} doesnt exists in the pop up')
    
    
def MessageWindow_buttons(button_name):
  buttons_list = aet_obj.savechangesdialogboxtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WPFControlText) :
      button.click()
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    
    
def Verify_DeleteMessage_content_AE(message):
  window = msg_obj.exportpopupbutton.object
  windowlist = window.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  for item in windowlist:
    if message in str(item.Text):
      Log.Message(f'message is verified as: {item.Text}')
      break
  else:
    Log.Message(f'{message} doesnt exists in the pop up')
  
      
def verify_application_browser_template_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
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
  
def delete_system_Folder(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  for node in SE_node_list:
    if node.DataContext.Identifier.OleValue == node_name :
      Engineeringclientutility.clickR_node_SE(node.DataContext.Identifier.OleValue)
      Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
      Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
      try:
        ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
      except:
        Log.Message("Circular progrss bar doesnt appear for folder deletion")
  
def delete_all_folder_system_ord_EC():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
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
          
          
def close_Message_Window():
    inspect_win = msg_obj.renamepopupbutton
    inspect_win.click_at(inspect_win.width-30, 30)
    Applicationutility.take_screenshot()   
 
def Wait_import_conflict_dialog_AE():
   try:
    Conflict_dialog_box = aet_obj.importconflictdialogtextbox.object
    Conflict_dialog_box.WaitProperty("Visible", True)
   except:
    Log.Message("Conflict Dialog Box did not exists") 
   
def ConflictWindow_buttons(button_name):
  buttons_list = aet_obj.importconflictdialogtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WPFControlText) :
      button.click()
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    
    
def Verify_latest_template_added_Application_browser_AE(template_name):
  AB_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for template in AB_list:
    if template_name == template.DataContext.Identifier.OleValue:
      Log.Message(f'{template_name} exists in Application browser')
      break
  else:
    Log.Message(f'{template_name} does not exists in Application browser')
    
def template_checkbox(param):
  identifier, state = param.split('$$')
  obj = aet_obj.instanceeditorchecklisttextbox.object
  obj_list = obj.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
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
  
def click_application_browser_template_AE(param):
  identifier,version=param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        if str(version) == str(App_list[j].Item.ViewModel.TemplateVersion):
          App_list[j].Click()
          Log.Message('Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
          break
  Applicationutility.wait_in_seconds(1000, 'wait')
  
  
def click_application_browser_folder_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if App_list[j].Visible:
      if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
        App_list[j].Click()
        Log.Message('Clicked object is : ' + str(App_list[j].Item.Identifier.OleValue))
       
        
def instance_locked_close_AE():
  msg_obj.exportpopupbutton.object.close()      
  
def Verify_file_existance():
  exported_xml = Project.Variables.system_1 + ".xml"
  d_path = os.path.abspath(os.path.join(os.getcwd(), exported_xml))
  if not os.path.exists(d_path):
    Log.Message(f"File does not exist: {d_path}")  

    
    
def verify_instance_validity():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for instance in instances:
    if instance.Panel_ZIndex != 0 and instance.DataContext != None:
      submenuitems = instance.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
      for i in submenuitems:
        if i.WPFControlText == "" and i.WPFControlOrdinalNo != 1:
          Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has Invalid link')
          break
      else:
        Log.Message(str(instance.DataContext.Identifier.OleValue) + ' has valid link')
  
  
def expand_folder_system():
  ApplicationBroswer = aet_obj.applicationbrowsertextbox.object
  instances = ApplicationBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in instances:
    if i.IsExpandable == True:
      i.IsExpanded = True
      continue
      
def verify_instance_application_browser():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for instance in instances:
    if instance.Panel_ZIndex != 0 and instance.DataContext != None:
        Log.Message(str(instance.DataContext.Identifier.OleValue) + ' is  present in the Application browser')
        
        
def verify_SameName_Errorbox_application_browser():
  instnaceBroswer = aet_obj.applicationbrowsertextbox.object
  instances = instnaceBroswer.FindAllChildren('ClrClassName', 'TemplatedAdorner', 1000)
  Log.Message(len(instances))
  for instance in instances:
    if instance.IsVisible:
      Log.Message(f'{instance.AdornedElement.ToolTip.OleValue} appeared on the screen as a ToolTip Value')
      break
  else:
    Log.Message(f'{instance.AdornedElement.ToolTip.OleValue} did not appear on the screen as a ToolTip Value')
    
def rename_instance_popup_button(button):
  rename_intance_object = aet_obj.renameinstancepopupmessagebutton.object
  buttons = rename_intance_object.FindAllChildren('ClrClassName', 'Button', 1000)
  for i in buttons:
    if button in i.WPFControlText:
      i.Click()
      break
  else:
    Log.Message("No such button exists")
    

def Verify_node_link_line_asset_work_AE(param):
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  
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
        
def Right_click_Assestworkspace_editor_AE():
  template_list = aet_obj.nodeinstancebutton.object.FindAllChildren('ClrClassName', 'InstanceNode', 1000)
  for node in template_list:
    if 'ValveGP_1' in str(node.DataContext.Identifier.OleValue):
      Log.Message('verified instance name')
      node.ClickR((node.width/2), (25))
      Log.Message('Right clicked on instance name')
      
      
def click_Abort_AE():
   Abort_list = msg_obj.notificationpanneltextbox.object.FindAllChildren('ClrClassName', 'Path', 1000)
   Log.Message(len(Abort_list))
   for i in Abort_list:
    if i.DataContext.ParentStatus.OleValue == "Executing":
      i.Click()
      break


def replace_template_combo_AE(param):
    identifier, version = param.split('$$')
    comb = aet_obj.replacetemplatecombotextbox.object
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
      

  
def capture_template_application_browser_AE(identifier):
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
      return identifier + str('$$')+ str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue)

      
def verify_template_replaced_AE(param):
  identifier, template = param.split('$$')
  App_browser = aet_obj.applicationbrowsertextbox
  App_list = App_browser.find_children_for_treeviewrow()
  for j in range(len(App_list)):
    if str(identifier) in str(App_list[j].Item.Identifier.OleValue):
      if str(template) != str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue):
        Log.Checkpoint('The Template ' + str(template) + ' is changed to ' + str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue))
        break
      else:
        Log.Message('The Template ' + str(App_list[j].DataContext.ViewModel.TemplateIdentifier.OleValue) + ' is not changed.' )  
        


def verify_button_enabled_disabled_modaldialogue_window(button_name):
  buttons_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WPFControlText):
      if  not button.Enabled:
        Log.Message( str(button.WPFControlText) + ' button is disabled')
        Applicationutility.take_screenshot()
        break
      else:
           Log.Message(str(button.WPFControlText) +" button is Enabled")
           
def verify_template_application_browser(param):
  template, version = param.split('$$')
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible:
      if template_list[i].DataContext.ViewModel.DisplayTypeName.OleValue != 'Folder':
        if template in template_list[i].DataContext.ViewModel.TemplateIdentifier.OleValue:
          if version in str(template_list[i].DataContext.ViewModel.TemplateVersion.OleValue):
            Log.Checkpoint(str(template_list[i].DataContext.ViewModel.TemplateIdentifier.OleValue) +' '+  str(template_list[i].DataContext.ViewModel.TemplateVersion.OleValue))
            break
  else:
    Log.Warning(f'Template {template} - {version} not in Application Browser')     
      
def wait_import_dialogue_window_appear():
  try:
    Import_window = aet_obj.importtextbox.object
    Import_window.WaitProperty('Visible',True, 1000)
    Log.Message("Import window  appeared")   
  except:
    Log.Message("Import window did not appear")

def Verify_Notification_pannel_Message(Message):
  Applicationutility.wait_in_seconds(1000, 'wait')
  msg_obj.notificationpanneltextbox.object.Refresh()
  Applicationutility.wait_for_execution()
  N_Message_List = msg_obj.notificationpanneltextbox.object.FindAllChildren("ClrClassName", "TreeListViewRow", 50)
  for i in N_Message_List:
    if i.Visible and i.Panel_ZIndex == 0:
      if Message in i.DataContext.Message.OleValue:
        Log.Checkpoint(f'{i.DataContext.Message.OleValue} in Notification Pannel')
        break
      else:
        Log.Warning(f'{i.DataContext.Message.OleValue} in Notification Pannel')
        
def jsjsjs():
  Verify_Notification_pannel_Message("Update")

## this method can be used for drag and drop intances in assetworkspace or linkeditor based on position 
## only 3 position can be defined based on the screen width

def drag_app_browser_drop_asset_workspace_editor_with_POS_AE(param):
  Log.Message(param)
  template, pos = param.split('$$')
  template_list = aet_obj.applicationbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if template in str(template_list[i].DataContext.Identifier.OleValue):
        fromx = template_list[i].ScreenLeft
        fromy = template_list[i].ScreenTop
        Log.Message('The object selected to drag is : ' + str(template_list[i].Item.Identifier.OleValue))
        break
  
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
    
def verify_application_explorer_instance_editor_tab1(identifier):
  template = aet_obj.instanceeditortextbox.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].Header.OleValue):
        Log.Checkpoint('The instance editor tab is open : ' + str(template_list[i].Header.OleValue))
        break
  else:
    Log.Warning('The instance editor tab was not found : ' + str(identifier))

def remove_PV_ranged_link_AE():
  node_element_parent = aet_obj.nodeinstancebutton.object
  node_element_list = node_element_parent.FindAllChildren('ClrClassName', 'TreeViewItem', 1000) 
  
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