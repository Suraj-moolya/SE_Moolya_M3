"""Engineeringclientutility"""

# Imports
import datetime
import Engineeringclientutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from CurrentScreen import CurrentScreen
from MessageBox import MessageBox
import Systemserverutility

# Object Initialization
eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
cs_obj = CurrentScreen()
lm_obj = MessageBox()

###############################################################################
# Function: verify_warning_popup
# Description: Verifies if the warning popup contains the expected message.
# Parameter: verify_message (str) - The message to verify in the popup.
# Example: verify_warning_popup("Warning: Action not allowed")
###############################################################################
def verify_warning_popup(verify_message):
  caption = war_obj.warningpopuptextbox.get_win_caption
  if verify_message in caption:
    Log.Checkpoint(caption)
  else:
    Log.Warning(caption)
  Applicationutility.take_screenshot()
  
###############################################################################
# Function: warning_popup_close
# Description: Closes the warning popup.
# Parameter: None
###############################################################################
def warning_popup_close():
  war_obj.ecwarningpopupclosebutton.object.Close()
  
###############################################################################
# Function: explorer_popup_close
# Description: Closes the explorer popup.
# Parameter: None
###############################################################################
def explorer_popup_close():
  lm_obj.modaldialogwindowtextbox.close()

###############################################################################
# Function: verify_ec_warning_popup
# Description: Verifies if the Engineering Client warning popup contains the expected message.
# Parameter: verify_message (str) - The message to verify in the popup.
# Example: verify_ec_warning_popup("Error: Invalid operation")
###############################################################################
def verify_ec_warning_popup(verify_message):
  message = ec_obj.warningpopupectextbox.get_win_caption
  if verify_message in message:
    Log.Checkpoint(message)
  else:
    Log.Warning(message)
  Applicationutility.take_screenshot()

###############################################################################
# Function: create_new_system_SE
# Description: Creates a new system in the System Explorer under the specified node.
# Parameter: node_name (str) - The name of the node under which the system is created.
# Example: create_new_system_SE("RootNode")
###############################################################################
def create_new_system_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].ClickR()
      break
  else:
    Log.Error(f"Node with name {node_name} not found in System Explorer")
  SE_Context_Menu = ses_obj.createsystembutton.object
  SE_Context_Menu.Click()
  aqUtils.Delay(5000)
  SE_node.Click()
  
###############################################################################
# Function: clickR_node_SE
# Description: Performs a right-click action on the specified node in the System Explorer.
# Parameter: node_name (str) - The name of the node to right-click.
# Example: clickR_node_SE("Node1")
###############################################################################
def clickR_node_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].ClickR()
      break
  else:
    Log.Error(f"Node with name {node_name} not found in System Explorer")
  
###############################################################################
# Function: click_node_SE
# Description: Clicks on the specified node in the System Explorer.
# Parameter: node_name (str) - The name of the node to click.
# Example: click_node_SE("Node1")
###############################################################################
def click_node_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].Click()
      break
  else:
    Log.Error(f"Node with name {node_name} not found in System Explorer")
  
###############################################################################
# Function: create_new_folder_SE
# Description: Creates a new folder in the System Explorer under the specified node.
# Parameter: node_name (str) - The name of the node under which the folder is created.
# Example: create_new_folder_SE("RootNode")
###############################################################################
def create_new_folder_SE(node_name):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str(node_name):
      SE_node_list[i].ClickR()
      break
  else:
    Log.Error(f"Node with name {node_name} not found in System Explorer")
  SE_Context_Menu = ses_obj.createfolderbutton.object
  SE_Context_Menu.Click()
  aqUtils.Delay(1000)
  SE_node.Click()
  
###############################################################################
# Function: verify_system_folder
# Description: Verifies if a new system or folder is created in the System Explorer.
# Parameter: None
###############################################################################
def verify_system_folder():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
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

###############################################################################
# Function: Verify_ContextMenu_Items
# Description: Verifies the visibility and enabled status of context menu items.
# Parameter: None
###############################################################################
def Verify_ContextMenu_Items():
  menu = ses_obj.rclickmenuitemsbutton.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 50)
  if not menu_items:
    Log.Error("No context menu items found")
    return
  for item in menu_items:
    if item.Visible and item.Enabled:
      Log.Message(str(item.Header)+" Visible status:"+str(item.Visible))
      Log.Message(str(item.Header)+" Enabled status:"+str(item.Enabled))
    else:
      Log.Message(str(item.Header)+" Visible status:"+str(item.Visible))
      Log.Message(str(item.Header)+" Enabled status:"+str(item.Enabled))
  else:
    Log.Message("Context menu items verification completed")
      
###############################################################################
# Function: Click_on_CreateFolder
# Description: Clicks on the "Create Folder" button in the System Explorer.
# Parameter: None
###############################################################################
def Click_on_CreateFolder():
  createfolder = ses_obj.createfolderbutton.object
  createfolder.Click()
  ses_obj.systemexplorernodebutton.click()
  
###############################################################################
# Function: Click_on_CreateSystem
# Description: Clicks on the "Create System" button in the System Explorer.
# Parameter: None
###############################################################################
def Click_on_CreateSystem():
  createSystem = ses_obj.createsystembutton.object
  createSystem.Click()
  ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  ses_obj.systemexplorernodebutton.click()
  
###############################################################################
# Function: License_management_pop_up_check
# Description: Checks if the license management popup is displayed and logs the license type.
# Parameter: None
###############################################################################
def License_management_pop_up_check():
       License_management_pop_up = lm_obj.licensemanagementpopupbutton.object.VisibleOnScreen
       if License_management_pop_up:
        Log.Message("Trail License used")
       else:
        Log.Message("Commercial License used")

###############################################################################
# Function: Trail_license1_window_validation
# Description: Validates if the trial license popup is displayed and handles it.
# Parameter: None
###############################################################################
def Trail_license1_window_validation():
    Trail_license_pop_up=lm_obj.traillicenseipopupbutton.object.WaitProperty('Exists', True, 1000000)
    if Trail_license_pop_up:
      Log.Message("Trail license pop up visible on screen")
      Applicationutility.wait_in_seconds(2000, 'wait')
      Sys.Keys("[Enter]")
    else:
      Log.Message("Trail license pop up was not visible on the screen")
  
###############################################################################
# Function: Keyboard_action_Enter
# Description: Simulates pressing the "Enter" key on the keyboard.
# Parameter: None
###############################################################################
def Keyboard_action_Enter():
      Sys.Keys("[Enter]")
      
###############################################################################
# Function: verify_explorer_warning_message
# Description: Verifies if the explorer warning message matches the expected message.
# Parameter: MessageBox (str) - The expected warning message.
# Example: verify_explorer_warning_message("Warning: Invalid operation")
###############################################################################
def verify_explorer_warning_message(MessageBox):
  PE_obj = ses_obj.warningpopuptextbox.object
  PE_message = PE_obj.MainText.OleValue
  if MessageBox in PE_message:
    Log.Checkpoint(PE_message)
  else:
    Log.Warning(PE_message)
  Applicationutility.take_screenshot()

###############################################################################
# Function: create_system_1_timestamp
# Description: Creates a new system with a timestamped name in the System Explorer.
# Parameter: None
###############################################################################
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
  
###############################################################################
# Function: select_system_1_application_explorer
# Description: Selects the system with the name stored in the variable 'system_1' and opens the Application Explorer.
# Parameter: None
###############################################################################
def select_system_1_application_explorer():
  clickR_node_SE(Project.Variables.system_1)
  ses_obj.openapplicationbutton.click()
  aqUtils.Delay(3000)
  
###############################################################################
# Function: select_system_1_topology_explorer
# Description: Selects the system with the name stored in the variable 'system_1' and opens the Topology Explorer.
# Parameter: None
###############################################################################
def select_system_1_topology_explorer():
  clickR_node_SE(Project.Variables.system_1)
  ses_obj.opentopologybutton.click()
  aqUtils.Delay(3000)
  
###############################################################################
# Function: select_system_1_project_explorer
# Description: Selects the system with the name stored in the variable 'system_1' and opens the Project Explorer.
# Parameter: None
###############################################################################
def select_system_1_project_explorer():
  clickR_node_SE(Project.Variables.system_1)
  ses_obj.openprojectexplorerbutton.click()
  aqUtils.Delay(3000)
      
###############################################################################
# Function: clickR_Folder
# Description: Performs a right-click action on the most recently created folder in the System Explorer.
# Parameter: None
###############################################################################
def clickR_Folder():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 1000)
  if not SE_node_list:
    Log.Error("No folders found in System Explorer")
    return
  ordervalue = [SE.WPFControlOrdinalNo for SE in SE_node_list if SE.DataContext.IconResourceKey == "Folder"] 
  if not ordervalue:
    Log.Error("No folders found with the specified icon")
    return
  Latest_Created = max(ordervalue)
  for i in SE_node_list:
    if i.WPFControlOrdinalNo == Latest_Created:
      i.ClickR()
      break     
  else:
    Log.Error("Failed to find the latest created folder")

###############################################################################
# Function: circularprogressbar_Wait
# Description: Waits for the circular progress bar to disappear.
# Parameter: None
###############################################################################
def circularprogressbar_Wait():
  try:
    ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)  
  except:
    Log.Message('No Circular progress bar')
    
###############################################################################
# Function: Rename_Folder
# Description: Renames a folder in the System Explorer.
# Parameter: Foldername (str) - The new name for the folder.
# Example: Rename_Folder("NewFolderName")
###############################################################################
def Rename_Folder(Foldername):
  Applicationutility.wait_in_seconds(1000, 'wait')
  if not Project.Variables.VariableExists('Rename_Folder_HF'):
        Project.Variables.AddVariable('Rename_Folder_HF', "String")
  Project.Variables.Rename_Folder_HF = str(Foldername)
  Sys.Keys(Project.Variables.Rename_Folder_HF)
  ses_obj.systemexplorernodebutton.click()

  
###############################################################################
# Function: Rename_System
# Description: Renames a system in the System Explorer.
# Parameter: SystemName (str) - The new name for the system.
# Example: Rename_System("NewSystemName")
###############################################################################
def Rename_System(SystemName):
  if not Project.Variables.VariableExists('Rename_System_HF'):
        Project.Variables.AddVariable('Rename_System_HF', "String")
  Project.Variables.Rename_System_HF = str(SystemName)
  Sys.Keys(Project.Variables.Rename_System_HF)
  ses_obj.systemexplorernodebutton.click()

###############################################################################
# Function: Verify_Folder_editable
# Description: Verifies if the specified folder is in an editable state.
# Parameter: nodename (str) - The name of the folder to verify.
# Example: Verify_Folder_editable("Folder1")
###############################################################################
def Verify_Folder_editable(nodename):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for node in SE_node_list:
    name = node.DataContext.Identifier.OleValue
    if nodename == str(name) and node.IsEditing:
      Log.Message("Node has entered editing field")
      break
  else:
    Log.Message("Node has not entered editing field")

###############################################################################
# Function: Verify_Folder_Renamed
# Description: Verifies if the folder has been renamed successfully.
# Parameter: None
###############################################################################
def Verify_Folder_Renamed():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for node in SE_node_list:
    name = node.DataContext.Identifier.OleValue
    if Project.Variables.Rename_Folder_HF == str(name):
      Log.Message(f'Folder is renamed as {Project.Variables.Rename_Folder_HF}')
      break
  else:
    Log.Error("Folder is not edited")

###############################################################################
# Function: verify_Rename_Popup_Message_SES
# Description: Verifies if the rename popup displays the expected message.
# Parameter: Popup_Message (str) - The expected message in the popup.
# Example: verify_Rename_Popup_Message_SES("Rename operation failed")
###############################################################################
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
 
###############################################################################
# Function: select_ContextMenu_Items_EC
# Description: Selects the specified context menu item in the Engineering Client.
# Parameter: menu_item (str) - The name of the context menu item to select.
# Example: select_ContextMenu_Items_EC("Open")
###############################################################################
def select_ContextMenu_Items_EC(menu_item):
  menu = eng_obj.rclickmenutextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "*MenuItem", 50)
  if menu_items:
    for item in menu_items:
      if item.Visible and item.Enabled:
        if item.Header != None and str(item.Header.OleValue) == str(menu_item):
          item.Click()
          Log.Checkpoint('The Context Menu Item clicked is : ' + str(menu_item))
          #Sys.Keys('[Tab]')
          break
    else:
      Log.Warning(f'The Context menu item {menu_item} not found !')
  else:
    Log.Warning('No Context Menu Found !')
  Applicationutility.wait_in_seconds(3000, 'wait')
  
###############################################################################
# Function: close_tab_EC
# Description: Closes the specified tab in the Engineering Client.
# Parameter: tab_name (str) - The name of the tab to close.
# Example: close_tab_EC("System Explorer")
###############################################################################
def close_tab_EC(tab_name):
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if str(tab_name) in str(tab.WPFControlText):
      tab.Click((tab.Width-15), (tab.Height/2))
      break
      
###############################################################################
# Function: terminate_engineering_client
# Description: Terminates the Engineering Client application.
# Parameter: None
###############################################################################
def terminate_engineering_client():
  TestedApps.EngineeringClient.Terminate()
  Applicationutility.wait_in_seconds(1000, 'wait')
  
###############################################################################
# Function: login_terminate_ec
# Description: Logs in to the Engineering Client and then terminates it.
# Parameter: None
###############################################################################
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

###############################################################################
# Function: login_password_terminate_ec
# Description: Logs in to the Engineering Client using the password and then terminates it.
# Parameter: None
###############################################################################
def login_password_terminate_ec():
  eng_obj.passwordtextbox.enter_text(Project.Variables.password)
  eng_obj.loginbutton.click()
  Applicationutility.wait_in_seconds(2000, 'wait')
  #Trail_license1_window_validation()
  #verify_Topology_Initiated()
  Applicationutility.wait_in_seconds(5000, 'Wait !!!')
  Systemserverutility.close_x_EC()
  Applicationutility.wait_in_seconds(5000, 'Wait !!!')  
  
###############################################################################
# Function: verify_Popup_Message_OK
# Description: Verifies if the popup message matches the expected message and clicks OK.
# Parameter: Popup_Message (str) - The expected message in the popup.
# Example: verify_Popup_Message_OK("Operation successful")
###############################################################################
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
    
###############################################################################
# Function: Verify_logged_in_EC
# Description: Verifies if the user is logged in to the Engineering Client.
# Parameter: None
###############################################################################
def Verify_logged_in_EC():
  try:
    element = eng_obj.loginbutton
    if element.exists:
      Log.Message('The user is unable to login to Engineering Client')
  except:
    Log.Message('The user is able to login to Engineering Client')
    
###############################################################################
# Function: create_system_1_timestamp_and_verify_context_menu_items_
# Description: Creates a new system with a timestamped name in the System Explorer and verifies context menu items.
# Parameter: None
###############################################################################
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
  
###############################################################################
# Function: checks_system_create_system
# Description: Checks if the system "System_1" exists in the System Explorer, and creates it if it doesn't.
# Parameter: None
###############################################################################
def checks_system_create_system():
  Systemserverutility.Pre_Condition_Navigation_SE()
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 500)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str('System_1'):
      SE_node_list[i].Click()
      break
  else:
    Log.Message("System_1 not found, creating a new system")
    clickR_node_SE('Systems Explorer')
    SE_Context_Menu = ses_obj.createsystembutton.object
    SE_Context_Menu.Click()
    ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
    ses_obj.systemexplorernodebutton.click()
    click_node_SE('System_1')
 
###############################################################################
# Function: checks_folder_create_folder
# Description: Checks if the folder "Folder_1" exists in the System Explorer, and creates it if it doesn't.
# Parameter: None
###############################################################################
def checks_folder_create_folder():
  Systemserverutility.Pre_Condition_Navigation_SE()
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 500)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str('Folder_1'):
      Log.Message("Folder_1 Exists")
      break
  else:
    Log.Message("Folder_1 not found, creating a new folder")
    clickR_node_SE('Systems Explorer')
    SE_Context_Menu = ses_obj.createfolderbutton.object
    SE_Context_Menu.Click()
    ses_obj.systemexplorernodebutton.click()

###############################################################################
# Function: License_management_pop_up_ok
# Description: Clicks OK on the license management popup if it is displayed.
# Parameter: None
###############################################################################
def License_management_pop_up_ok(): 
  try:
    lm_obj.licensemanagementpopupbutton.object.WaitProperty("Enabled",True,10000)
    if lm_obj.licensemanagementpopupbutton.object.Enabled:
      lm_obj.licensemanagementokbutton.object.Click()
  except:
    Log.Message('No Trial License days remainder popup')
    
###############################################################################
# Function: Trail_license_window_validation
# Description: Validates if the trial license popup is displayed and handles it.
# Parameter: None
###############################################################################
def Trail_license_window_validation():
  try:
    Trail_license_pop_up=lm_obj.traillicensepopupbutton.object.WaitProperty('Visible', True, 10000)
    if Trail_license_pop_up:
      Log.Message("Trail license pop up visible on screen")
      Sys.Keys("[Enter]")
  except:
    Log.Message('No Trail license pop up')
    
###############################################################################
# Function: verify_Topology_Initiated
# Description: Verifies if the topology is initiated by checking the visibility of the progress bar.
# Parameter: None
###############################################################################
def verify_Topology_Initiated():
  try:
    progressbar = ses_obj.progressbarbutton.object.Visible
    ses_obj.progressbarbutton.object.WaitProperty("Visible",False,150000)
  except:
    Log.Message('Circular Progress not Visible')

###############################################################################
# Function: clickR_node_ordno_SE
# Description: Performs a right-click action on the node with the specified ordinal number in the System Explorer.
# Parameter: ord_num (int) - The ordinal number of the node to right-click.
# Example: clickR_node_ordno_SE(1)
###############################################################################
def clickR_node_ordno_SE(ord_num):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)):
    if SE_node_list[i].WPFControlOrdinalNo == ord_num:
      SE_node_list[i].ClickR()
      break
  else:
    Log.Error(f"Node with ordinal number {ord_num} not found in System Explorer")

###############################################################################
# Function: close_all_tab_except_Systems_explorer_EC
# Description: Closes all tabs in the Engineering Client except the "Systems Explorer" tab.
# Parameter: None
###############################################################################
def close_all_tab_except_Systems_explorer_EC():
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if not str('Systems Explorer') in str(tab.WPFControlText):
      if not str('*') in str(tab.WPFControlText):
        tab.Click((tab.Width-15), (tab.Height/2))        
      else:
        tab.Click((tab.Width-15), (tab.Height/2))  
        Applicationutility.modal_dialog_window_button('No')
        
###############################################################################
# Function: select_Context_SubMenu_Items_EC
# Description: Selects the specified sub-menu item in the context menu of the Engineering Client.
# Parameter: menu_item (str) - The name of the sub-menu item to select.
# Example: select_Context_SubMenu_Items_EC("Open")
###############################################################################
def select_Context_SubMenu_Items_EC(menu_item):
  menu = eng_obj.rclicksubmenutextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 50)
  for item in menu_items:
    if item.Visible and item.Enabled:
      if str(item.Header.OleValue) == str(menu_item):
        item.Click()
        Log.Checkpoint('The Context Menu Item clicked is : ' + str(menu_item))
        break
  else:
    Log.Warning(f'The Context sub-menu item {menu_item} not found !')
  Applicationutility.wait_in_seconds(3000, 'wait')

###############################################################################
# Function: open_EC_ok_on_trial_pop_up
# Description: Opens the Engineering Client and handles the trial license popup if displayed.
# Parameter: None
###############################################################################
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
  
###############################################################################
# Function: close_EC_ok_on_trial_pop_up
# Description: Closes the Engineering Client and handles the trial license popup if displayed.
# Parameter: None
###############################################################################
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
  
###############################################################################
# Function: Verify_Dropdown_options
# Description: Verifies if the user dropdown options are visible.
# Parameter: None
###############################################################################
def Verify_Dropdown_options():
  aqUtils.Delay(100)
  MenuItem = eng_obj.userdropdownmenuitemtextbox.object
  
  if MenuItem.Visible :
    Log.Message(f'Dropdown options successfully verified ')
  else:
    Log.Warning("User drown not verified")
    
###############################################################################
# Function: Verify_Logout
# Description: Verifies if the user is logged out of the Engineering Client.
# Parameter: None
###############################################################################
def Verify_Logout():
  aqUtils.Delay(100)
  MenuItem = eng_obj.logouttextbox.object
  
  if MenuItem.WPFControlText == "Log in to use the client" :
    Log.Message(f'Logout successfully verified ')
  else:
    Log.Warning("Logout not verified")

###############################################################################
# Function: Rename_Insatnce
# Description: Renames an instance by simulating typing the new name.
# Parameter: Name (str) - The new name for the instance.
# Example: Rename_Insatnce("NewInstanceName")
###############################################################################
def Rename_Insatnce(Name):
  Sys.Keys(Name)
  
###############################################################################
# Function: verify_imported_file_Popup_Message_AES
# Description: Verifies if the imported file popup displays the expected message.
# Parameter: Popup_Message (str) - The expected message in the popup.
# Example: verify_imported_file_Popup_Message_AES("Import successful")
###############################################################################
def verify_imported_file_Popup_Message_AES(Popup_Message):
  Invalid_import_error_pop_up = lm_obj.renamepopupbutton.object.DetailsText.OleValue
  if Popup_Message in str(Invalid_import_error_pop_up):
    Log.Message(f'Message displayed is {Invalid_import_error_pop_up}')
  else:
    Log.Error("No message was displayed")

###############################################################################
# Function: open_application_explorer
# Description: Opens the Application Explorer in the System Explorer.
# Parameter: None
###############################################################################
def open_application_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open Application Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
  
###############################################################################
# Function: open_system_explorer
# Description: Opens the System Explorer in the System Explorer.
# Parameter: None
###############################################################################
def open_system_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open System Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
      
###############################################################################
# Function: open_topology_explorer
# Description: Opens the Topology Explorer in the System Explorer.
# Parameter: None
###############################################################################
def open_topology_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open Topology Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
        
###############################################################################
# Function: open_project_explorer
# Description: Opens the Project Explorer in the System Explorer.
# Parameter: None
###############################################################################
def open_project_explorer():
  obj = ses_obj.maintoolbartextbox.find_children_for_content_presenter()
  for item in obj:
    if 'Open Project Explorer' in item.ToolTip.OleValue:
      item.click()
      Applicationutility.wait_in_seconds(3000, 'wait')
      break
  
###############################################################################
# Function: Verify_ContextMenu_Item
# Description: Verifies the visibility and enabled status of a specific context menu item.
# Parameter: param (str) - The context menu item and its expected state, separated by "$$".
# Example: Verify_ContextMenu_Item("Open$$True")
###############################################################################
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
  else:
    Log.Message("Context menu item verification completed")
          
###############################################################################
# Function: Open_Close_folder_TE
# Description: Opens or closes a folder in the Topology Explorer.
# Parameter: param (str) - The folder name and button name, separated by "$$".
# Example: Open_Close_folder_TE("Folder1$$Open")
###############################################################################
def Open_Close_folder_TE(param):
  FolderName,ButtonName = param.split("$$")
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)): 
    if SE_node_list[i].DataContext.Identifier.OleValue == FolderName:
      for i in SE_node_list[i].FindAllChildren("ClrClassName", "Button", 50):
        if i.ToolTip.OleValue == ButtonName and i.Visible:
          i.Click()
          return
  
###############################################################################
# Function: Verify_folder_Content_Status_TE
# Description: Verifies if the specified folder is expanded in the Topology Explorer.
# Parameter: FolderName (str) - The name of the folder to verify.
# Example: Verify_folder_Content_Status_TE("Folder1")
###############################################################################
def Verify_folder_Content_Status_TE(FolderName):
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 50)
  if not SE_node_list:
    Log.Error("No nodes found in System Explorer")
    return
  for i in range(len(SE_node_list)): 
    if SE_node_list[i].DataContext.Identifier.OleValue == FolderName and SE_node_list[i].IsInnerContentExpanded:
       Log.Message(f'{SE_node_list[i].DataContext.Identifier.OleValue} folder is expanded')
       break
  else:
    Log.Message(f'{FolderName} folder is not expanded')
  
###############################################################################
# Function: no_password_system
# Description: Handles the "No Password" system popup by clicking the specified button.
# Parameter: btn (str) - The name of the button to click.
# Example: no_password_system("OK")
###############################################################################
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
  
###############################################################################
# Function: close_the_tab_EC
# Description: Closes the specified tab in the Engineering Client.
# Parameter: param (str) - The name of the tab to close.
# Example: close_the_tab_EC("System Explorer")
###############################################################################
def close_the_tab_EC(param):
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    Log.Message(tab.WPFControlText)
    if param in str(tab.DataContext.TitleToolTip):
        tab.Click((tab.Width-15), (tab.Height/2)) 
  else:
    Log.Message(f'{param} parameter passed might be wrong')       

###############################################################################
# Function: update_report_details
# Description: Updates the report details with the specified values.
# Parameters:
#   - customer_name (str): The name of the customer.
#   - site_name (str): The name of the site.
#   - report_desc (str): The description of the report.
#   - report_author (str): The author of the report.
#   - page_size (str): The size of the page.
#   - orientation (str): The orientation of the report.
#   - report_footer (str): The footer of the report.
#   - report_header (str): The header of the report.
# Example: update_report_details("Customer1", "Site1", "Report Description", "Author", "A4", "Portrait", "Footer", "Header")
###############################################################################
def update_report_details(customer_name, site_name, report_desc, report_author, page_size, orientation, report_footer, report_header):
  updates = {
    'CustomerName': customer_name,
    'SiteName': site_name,
    'ReportDescription': report_desc,
    'ReportAuthor': report_author,
    'PageSize': page_size,
    'Orientation': orientation,
    'ReportFooter': report_footer,
    'ReportHeader': report_header
  }
  report_details = cs_obj.reportdialogwindow.object.FindAllChildren('ClrClassName', 'TextBlock', 100)
  if not report_details:
    Log.Error("No report details found")
    return
  for det in report_details:
    data_context = getattr(det, 'DataContext', None)
    if data_context is not None:
      for attr, value in updates.items():
        if hasattr(data_context, attr):
          setattr(data_context, attr, value)
          Log.Message(f"{attr} updated to '{value}'")
    else:
      Log.Warning("Data context not found for some report details")
  else:
    Log.Message("Report details updated successfully")