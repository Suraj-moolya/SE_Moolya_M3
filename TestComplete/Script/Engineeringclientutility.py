"""Engineeringclientutility"""
import datetime
import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from CurrentScreen import CurrentScreen
from MessageBox import MessageBox
import Systemserverutility


eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
cs_obj = CurrentScreen()
lm_obj = MessageBox()

def verify_warning_popup(verify_message):
  caption = war_obj.warningpopuptextbox.get_win_caption
  if verify_message in caption:
    Log.Checkpoint(caption)
  else:
    Log.Warning(caption)
  Applicationutility.take_screenshot()
  
def warning_popup_close():
  war_obj.ecwarningpopupclosebutton.object.Close()
  
def explorer_popup_close():
  lm_obj.modaldialogwindowtextbox.close()

def verify_ec_warning_popup(verify_message):
  message = ec_obj.warningpopupectextbox.get_win_caption
  if verify_message in message:
    Log.Checkpoint(message)
  else:
    Log.Warning(message)
  Applicationutility.take_screenshot()

def create_new_system_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].ClickR()
      break
  SE_Context_Menu = ses_obj.createsystembutton.object
  SE_Context_Menu.Click()
  aqUtils.Delay(5000)
  SE_node.Click()
  
def clickR_node_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].ClickR()
      break
  
def click_node_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].Click()
      break
      

  
def create_new_folder_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].ClickR()
      break
  SE_Context_Menu = ses_obj.createfolderbutton.object
  SE_Context_Menu.Click()
  aqUtils.Delay(1000)
  SE_node.Click()
  
def verify_system_folder():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  result = [item.DataContext.IconResourceKey for item in SE_node_list ]
  ResultName = [item.DataContext.Identifier for item in SE_node_list]
  if result[-1] == 'System' and len(result)>1:
    Log.Message(f'System named {ResultName[-1]}  is created')
    if not Project.Variables.VariableExists('system_1'):
        Project.Variables.AddVariable('system_1', "String")
    Project.Variables.system_1 = str(ResultName[-1])
  elif result[-1] == 'Folder' and len(result)>1 :
    Log.Message(f'Folder named {ResultName[-1]}  is created')
  else:
    Log.Error("Nothing new is created")
    
def Verify_ContextMenu_Items():
  menu = ses_obj.rclickmenuitemsbutton.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 50)
  for item in menu_items:
    if item.Visible and item.Enabled:
      Log.Message(str(item.Header)+" Visible status:"+str(item.Visible))
      Log.Message(str(item.Header)+" Enabled status:"+str(item.Enabled))
    else:
      Log.Message(str(item.Header)+" Visible status:"+str(item.Visible))
      Log.Message(str(item.Header)+" Enabled status:"+str(item.Enabled))
      
def Click_on_CreateFolder():
  createfolder = ses_obj.createfolderbutton.object
  createfolder.Click()
  ses_obj.systemexplorernodebutton.click()
  
def Click_on_CreateSystem():
  createSystem = ses_obj.createsystembutton.object
  createSystem.Click()
  ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  ses_obj.systemexplorernodebutton.click()
  
def License_management_pop_up_check():
       License_management_pop_up = lm_obj.licensemanagementpopupbutton.object.VisibleOnScreen
       if License_management_pop_up:
        Log.Message("Trail License used")
       else:
        Log.Message("Commercial License used")

def Trail_license1_window_validation():
    Trail_license_pop_up=lm_obj.traillicenseipopupbutton.object.WaitProperty('Exists', True, 1000000)
    if Trail_license_pop_up:
      Log.Message("Trail license pop up visible on screen")
      Applicationutility.wait_in_seconds(2000, 'wait')
      Sys.Keys("[Enter]")
    else:
      Log.Message("Trail license pop up was not visible on the screen")
  
def Keyboard_action_Enter():
      Sys.Keys("[Enter]")
      
def verify_explorer_warning_message(MessageBox):
  PE_obj = ses_obj.warningpopuptextbox.object
  PE_message = PE_obj.MainText.OleValue
  if MessageBox in PE_message:
    Log.Checkpoint(PE_message)
  else:
    Log.Warning(PE_message)
  Applicationutility.take_screenshot()

def create_system_1_timestamp():
  clickR_node_SE('Systems Explorer')
  SE_Context_Menu = ses_obj.createsystembutton.object
  SE_Context_Menu.Click()
  ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  if not Project.Variables.VariableExists('system_1'):
        Project.Variables.AddVariable('system_1', "String")
  Project.Variables.system_1 = str('System1_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Applicationutility.wait_in_seconds(2000, 'wait')
  Sys.Keys(Project.Variables.system_1)
  ses_obj.systemexplorernodebutton.click()
  Log.Message(Project.Variables.system_1)
  
def select_system_1_application_explorer():
  clickR_node_SE(Project.Variables.system_1)
  ses_obj.openapplicationbutton.click()
  aqUtils.Delay(3000)
  
def select_system_1_topology_explorer():
  clickR_node_SE(Project.Variables.system_1)
  ses_obj.opentopologybutton.click()
  aqUtils.Delay(3000)
  
def select_system_1_project_explorer():
  clickR_node_SE(Project.Variables.system_1)
  ses_obj.openprojectexplorerbutton.click()
  aqUtils.Delay(3000)
      
      
def clickR_Folder():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 1000)
  ordervalue = [SE.WPFControlOrdinalNo for SE in SE_node_list if SE.DataContext.IconResourceKey == "Folder"] 
  Latest_Created = max(ordervalue)
  for i in SE_node_list:
    if i.WPFControlOrdinalNo == Latest_Created:
      i.ClickR()
      break     

def circularprogressbar_Wait():
  try:
    ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)  
  except:
    Log.Message('No Circular progress bar')
    
def Rename_Folder(Foldername):
  Applicationutility.wait_in_seconds(1000, 'wait')
  if not Project.Variables.VariableExists('Rename_Folder_HF'):
        Project.Variables.AddVariable('Rename_Folder_HF', "String")
  Project.Variables.Rename_Folder_HF = str(Foldername)
  Sys.Keys(Project.Variables.Rename_Folder_HF)
  ses_obj.systemexplorernodebutton.click()

  
def Rename_System(SystemName):
  if not Project.Variables.VariableExists('Rename_System_HF'):
        Project.Variables.AddVariable('Rename_System_HF', "String")
  Project.Variables.Rename_System_HF = str(SystemName)
  Sys.Keys(Project.Variables.Rename_System_HF)
  ses_obj.systemexplorernodebutton.click()

def Verify_Folder_editable(nodename):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for node in SE_node_list:
    name = node.DataContext.Identifier.OleValue
    if nodename == str(name) and node.IsEditing:
      Log.Message("Node has entered editing field")
      break
  else:
    Log.Message("Node has not entered editing field")

def Verify_Folder_Renamed():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for node in SE_node_list:
    name = node.DataContext.Identifier.OleValue
    if Project.Variables.Rename_Folder_HF == str(name):
      Log.Message(f'Folder is renamed as {Project.Variables.Rename_Folder_HF}')
      break
  else:
    Log.Error("Folder is not edited")


def verify_Rename_Popup_Message_SES(Popup_Message):
  Rename_error_pop_up = lm_obj.renamepopupbutton.find_children_for_result_viewer()
  for i in Rename_error_pop_up:
    if Popup_Message in str(i.Text):
      Log.Message(f'Message displayed is {i.Text}')
      break
  else:
    Log.Error("No message was displayed")
    
def Rename_error_pop_up_check_SES():
       Rename_error_pop_up = lm_obj.renamepopupbutton.object.VisibleOnScreen
       if License_management_pop_up:
        Log.Message("Rename Error pop up is visible on screen")
       else:
        Log.Message("Rename Error pop up is not visible on screen")
    
def Rename_error_pop_up_ok(): 
  try:
    lm_obj.renamepopupbutton.object.WaitProperty("Enabled",True,10000)
    if lm_obj.licensemanagementpopupbutton.object.Enabled:
      lm_obj.licensemanagementokbutton.object.Click()
    else:
      Log.Message("No pop up related to License was visible on screen")
  except exception as exe:
    Log.Error(exe)
 
def select_ContextMenu_Items_EC(menu_item):
  menu = eng_obj.rclickmenutextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "*MenuItem", 50)
  for item in menu_items:
    if item.Visible and item.Enabled:
      if item.Header != None and str(item.Header.OleValue) == str(menu_item):
        item.Click()
        Log.Checkpoint('The Context Menu Item clicked is : ' + str(menu_item))
        break
  else:
    Log.Warning(f'The Context menu item {menu_item} not found !')
  Applicationutility.wait_in_seconds(3000, 'wait')
  
def close_tab_EC(tab_name):
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if str(tab_name) in str(tab.WPFControlText):
      tab.Click((tab.Width-15), (tab.Height/2))
      break
      
      
def terminate_engineering_client():
  TestedApps.EngineeringClient.Terminate()
  Applicationutility.wait_in_seconds(1000, 'wait')
  
def login_terminate_ec():
  eng_obj.usernametextbox.enter_text(Project.Variables.username)
  eng_obj.passwordtextbox.enter_text(Project.Variables.password)
  eng_obj.loginbutton.click()
  Applicationutility.wait_in_seconds(2000, 'wait')
  #Trail_license1_window_validation()
  verify_Topology_Initiated()
  Applicationutility.wait_in_seconds(5000, 'Wait !!!')
  Systemserverutility.close_x_EC()
  Applicationutility.wait_in_seconds(5000, 'Wait !!!')

def login_password_terminate_ec():
  eng_obj.passwordtextbox.enter_text(Project.Variables.password)
  eng_obj.loginbutton.click()
  Applicationutility.wait_in_seconds(2000, 'wait')
  #Trail_license1_window_validation()
  #verify_Topology_Initiated()
  Applicationutility.wait_in_seconds(5000, 'Wait !!!')
  Systemserverutility.close_x_EC()
  Applicationutility.wait_in_seconds(5000, 'Wait !!!')  
  
def verify_Popup_Message_OK(Popup_Message):
  try:
    Rename_error_pop_up = lm_obj.renamepopupbutton.find_children_for_result_viewer()
    for i in Rename_error_pop_up:
      if Popup_Message in str(i.WPFControlText):
        Log.Checkpoint(f'Message displayed is {i.WPFControlText}')
        lm_obj.renamepopupokbutton.click()
        break
    else:
      Log.Message("No message was displayed")
  except:
    Log.Message('')
    
    
def Verify_logged_in_EC():
  try:
    element = eng_obj.loginbutton
    if element.exists:
      Log.Message('The user is unable to login to Engineering Client')
  except:
    Log.Message('The user is able to login to Engineering Client')
    
def create_system_1_timestamp_and_verify_context_menu_items_():
  clickR_node_SE('Systems Explorer')
  Verify_ContextMenu_Items()
  SE_Context_Menu = ses_obj.createsystembutton.object
  SE_Context_Menu.Click()
  ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  if not Project.Variables.VariableExists('system_1'):
        Project.Variables.AddVariable('system_1', "String")
  Project.Variables.system_1 = str('System1_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Sys.Keys(Project.Variables.system_1)
  ses_obj.systemexplorernodebutton.click()
  Log.Message(Project.Variables.system_1)
  
  
def checks_system_create_system():
  Systemserverutility.Pre_Condition_Navigation_SE()
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 500)
  
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str('System_1'):
      SE_node_list[i].Click()
      break
  else:
    clickR_node_SE('Systems Explorer')
    SE_Context_Menu = ses_obj.createsystembutton.object
    SE_Context_Menu.Click()
    ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
    ses_obj.systemexplorernodebutton.click()
    click_node_SE('System_1')
 
    
# if in sys exp tab it has to check if sys 1 is present or not, if not create and click

def checks_folder_create_folder():
  Systemserverutility.Pre_Condition_Navigation_SE()
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 500)
  
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str('Folder_1'):
      Log.Message("Folder_1 Exists")
      break
  else:
    clickR_node_SE('Systems Explorer')
    SE_Context_Menu = ses_obj.createfolderbutton.object
    SE_Context_Menu.Click()
    ses_obj.systemexplorernodebutton.click()

def License_management_pop_up_ok(): 
  try:
    lm_obj.licensemanagementpopupbutton.object.WaitProperty("Enabled",True,10000)
    if lm_obj.licensemanagementpopupbutton.object.Enabled:
      lm_obj.licensemanagementokbutton.object.Click()
  except:
    Log.Message('No Trial License days remainder popup')
    
    
def Trail_license_window_validation():
  try:
    Trail_license_pop_up=lm_obj.traillicensepopupbutton.object.WaitProperty('Visible', True, 10000)
    if Trail_license_pop_up:
      Log.Message("Trail license pop up visible on screen")
      Sys.Keys("[Enter]")
  except:
    Log.Message('No Trail license pop up')
    
    
def verify_Topology_Initiated():
  try:
    progressbar = ses_obj.progressbarbutton.object.Visible
    ses_obj.progressbarbutton.object.WaitProperty("Visible",False,150000)
  except:
    Log.Message('Circular Progress not Visible')

  
def clickR_node_ordno_SE(ord_num):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)):
    if SE_node_list[i].WPFControlOrdinalNo == ord_num:
      SE_node_list[i].ClickR()
      break

def close_all_tab_except_Systems_explorer_EC():
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if not str('Systems Explorer') in str(tab.WPFControlText):
      if not str('*') in str(tab.WPFControlText):
        tab.Click((tab.Width-15), (tab.Height/2))        
      else:
        tab.Click((tab.Width-15), (tab.Height/2))  
        Applicationutility.modal_dialog_window_button('No')
        
def select_Context_SubMenu_Items_EC(menu_item):
  menu = eng_obj.rclicksubmenutextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 50)
  for item in menu_items:
    if item.Visible and item.Enabled:
      if str(item.Header.OleValue) == str(menu_item):
        item.Click()
        Log.Checkpoint('The Context Menu Item clicked is : ' + str(menu_item))
        break
  Applicationutility.wait_in_seconds(3000, 'wait')

   

def open_EC_ok_on_trial_pop_up():
  Log.Enabled = False
  Engineering_client = Sys.Process("EngineeringClient")
  if Engineering_client.Exists:
    Log.Enabled = True
    Log.Checkpoint('Engineering Client Application already running !')
  else:
    Log.Enabled = True
    TestedApps.EngineeringClient.Run()
    Applicationutility.wait_in_seconds(1000, 'wait')
    License_management_pop_up_ok()
    Applicationutility.wait_in_seconds(1000, 'wait')
    Trail_license_window_validation()
    Applicationutility.wait_in_seconds(1000, 'wait')
    verify_Topology_Initiated()
  Log.Enabled = True
  
  
def close_EC_ok_on_trial_pop_up():
  Log.Enabled = False
  Engineering_client = Sys.Process("EngineeringClient")
  if Engineering_client.Exists:
    Log.Enabled = True
    close_all_tab_except_Systems_explorer_EC()
    Systemserverutility.close_x_EC()
    Applicationutility.wait_in_seconds(5000, 'wait')
    Log.Message('Engineering Client Application is Closing !')
  else:
    Log.Enabled = True
    Applicationutility.wait_in_seconds(1000, 'wait')
    Log.Message('Engineering Client Application is already closed !')
  Log.Enabled = True
  
  

def Verify_Dropdown_options():
  aqUtils.Delay(100)
  MenuItem = eng_obj.userdropdownmenuitemtextbox.object
  
  if MenuItem.Visible :
    Log.Message(f'Dropdown options successfully verified ')
  else:
    Log.Warning("User drown not verified")
    

def Verify_Logout():
  aqUtils.Delay(100)
  MenuItem = eng_obj.logouttextbox.object
  
  if MenuItem.WPFControlText == "Log in to use the client" :
    Log.Message(f'Logout successfully verified ')
  else:
    Log.Warning("Logout not verified")

def Rename_Insatnce(Name):
  Sys.Keys(Name)
  

def verify_imported_file_Popup_Message_AES(Popup_Message):
  Invalid_import_error_pop_up = lm_obj.renamepopupbutton.object.DetailsText.OleValue
  if Popup_Message in str(Invalid_import_error_pop_up):
    Log.Message(f'Message displayed is {Invalid_import_error_pop_up}')
  else:
    Log.Error("No message was displayed")


def open_application_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open Application Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
  
def open_system_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open System Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
      
def open_topology_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open Topology Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
        
def open_project_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open Project Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
  
def Verify_ContextMenu_Item(param):
  menuitem, state = param.split('$$')
  menu = ses_obj.rclickmenuitemsbutton.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 50)
  for item in menu_items:
    if item.Visible:
      if menuitem in item.WPFControlText:
        if state in str(item.Enabled):
          Log.Checkpoint(str(item.Header)+" Visible status:"+str(item.Visible))
          Log.Checkpoint(str(item.Header)+" Enabled status:"+str(item.Enabled))
        else:
          Log.Warning(str(item.Header)+" Visible status:"+str(item.Visible))
          Log.Warning(str(item.Header)+" Enabled status:"+str(item.Enabled))
          
def Open_Close_folder_TE(param):
  FolderName,ButtonName = param.split("$$")
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)): 
    if SE_node_list[i].DataContext.Identifier.OleValue == FolderName:
      for i in SE_node_list[i].FindAllChildren("ClrClassName", "Button", 50):
        if i.ToolTip.OleValue == ButtonName and i.Visible:
          i.Click()
          clicked = True
          break

def Verify_folder_Content_Status_TE(FolderName):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  
  for i in range(len(SE_node_list)): 
    if SE_node_list[i].DataContext.Identifier.OleValue == FolderName and SE_node_list[i].IsInnerContentExpanded:
       Log.Message(f'{SE_node_list[i].DataContext.Identifier.OleValue} folder is expanded')
       break
  else:
    Log.Message(f'{SE_node_list[i].DataContext.Identifier.OleValue} folder is not expanded')
          

def no_password_system(btn):
  buttons = lm_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName','Button', 10)
  checkbox = lm_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName','CheckBox', 10)
  if checkbox[0].wState == 0:
    checkbox[0].wState = 1
  Applicationutility.wait_in_seconds(2000, 'Wait')
  for button in buttons:
    if btn in button.WPFControlText:
      button.Click()
  Applicationutility.wait_in_seconds(2000, 'Wait')
  

