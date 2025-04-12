from SystemServer import SystemServer
from WindowsExplorer import WindowsExplorer
from EngineeringClient import EngineeringClient
import Applicationutility
from SystemExplorerScreen import SystemExplorerScreen
import Engineeringclientutility
from ProjectExplorerTab import ProjectExplorerTab
from MessageBox import MessageBox

server_obj = SystemServer()
win_obj = WindowsExplorer()
eng_obj = EngineeringClient()
ses_obj = SystemExplorerScreen()
proj_obj = ProjectExplorerTab()
msg_obj = MessageBox()

###############################################################################
# Function : system_server_icon_rclick_on
# Description : Right-clicks on the system server icon in the notification area and selects an option.
# Parameter : element (str) - Name of the context menu option to select. Example: "Exit"
###############################################################################
def system_server_icon_rclick_on(element): 
  Applicationutility.wait_in_seconds(1000, 'wait')
  win_obj.showhiddeniconbutton.object.Click()
  aqUtils.Delay(1500)
  notification_area = win_obj.notificationareawindow.object
  if not notification_area:
    Log.Message("Notification area not found.")
    return
  for i in range(notification_area.wButtonCount):
    if 'EcoStruxure Process Expert - System Server' in str(notification_area.wButtonText[i]):
      notification_area.ClickItemR(i)
      break
  else:
    Log.Message("System Server icon not found in notification area.")
    return
  aqUtils.Delay(1500)
  context_menu = server_obj.contextmenubutton.object
  menu_item_count = context_menu.wItems.Count
  if menu_item_count == 0:
    Log.Message("No context menu items found.")
    return
  for j in range(menu_item_count):
    if element == context_menu.wItems.Item[j].Text:
      context_menu.ClickItem(j)
      break
  else:
    Log.Message(f"Context menu option '{element}' not found.")
  aqUtils.Delay(1500)
  
###############################################################################
# Function : verify_SS_LoginDialogue
# Description : Verifies if the login dialogue box is visible on the screen.
# Parameter : None
###############################################################################
def verify_SS_LoginDialogue():
    Username = server_obj.usernametextbox.object
    if Username.VisibleOnScreen:
      Log.Message("Login Dialogue box successfully appeared")
    else:
      Log.Message("Login Dialogue box did not appear")
    
###############################################################################
# Function : check_server_console_flowdocument
# Description : Verifies a specific message in the server console's flow document.
# Parameter : verify_message (str) - Message to verify in the console. Example: "Server is ready"
###############################################################################
def check_server_console_flowdocument(verify_message):
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 100)
  if not console_list:
    Log.Message("No flow documents found in the console.")
    return
  for _ in range(100):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if str(verify_message) in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    elif 'Processing command metadata overrides...' in check_text:
      Log.Checkpoint(verify_message)
      Applicationutility.take_screenshot()
      break
    else:
      Applicationutility.wait_in_seconds(12000, 'Wait for server ready!')
      console_obj.Refresh()
  else:
    Log.Message(f"Message '{verify_message}' not found in the console.")
      
###############################################################################
# Function : verify_start_stop_disabled
# Description : Verifies if the start and stop server buttons are disabled.
# Parameter : None
###############################################################################
def verify_start_stop_disabled():
  Action_Start = server_obj.startserverbutton.object
  Action_Stop  = server_obj.stopserverbutton.object 
  if Action_Start.Enabled and Action_Stop.Enabled:
    Log.Warning("User has server admin rights Enabled")
  else:
    Log.Message("User has no server admin rights")
    
###############################################################################
# Function : rclick_system_server_show_server_console
# Description : Right-clicks on the system server icon and selects "Show Server Console".
# Parameter : None
###############################################################################
def rclick_system_server_show_server_console(): 
  win_obj.showhiddeniconbutton.object.Click()
  Applicationutility.wait_in_seconds(2500, "Wait")
  notification_area = win_obj.notificationareawindow.object
  for i in range(notification_area.wButtonCount):
    if 'EcoStruxure Process Expert - System Server' in str(notification_area.wButtonText[i]):
      notification_area.ClickItemR(i)
      break
  else:
    Log.Message("System Server icon not found in notification area.")
    return
  aqUtils.Delay(500)
  context_menu = server_obj.contextmenubutton.object
  menu_item_count = context_menu.wItems.Count
  if menu_item_count == 0:
    Log.Message("No context menu items found.")
    return
  for j in range(menu_item_count):
    if 'Show Server Console' == context_menu.wItems.Item[j].Text:
      context_menu.ClickItem(j)
      break
  else:
    Log.Message("'Show Server Console' option not found in context menu.")
  aqUtils.Delay(500)
    
###############################################################################
# Function : check_server_stopped
# Description : Verifies if the server has stopped by checking the console messages.
# Parameter : None
###############################################################################
def check_server_stopped():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 50)
  if not console_list:
    Log.Message("No flow documents found in the console.")
    return
  for _ in range(60):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if 'Server is stopped' in check_text:
      Log.Message(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      aqUtils.Delay(5000)
      console_obj.Refresh()
  else:
    Log.Message("Server stop message not found in the console.")
      
###############################################################################
# Function : check_flowdocument_license
# Description : Checks if the server is using a trial license by analyzing the console messages.
# Parameter : None
###############################################################################
def check_flowdocument_license():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "Paragraph", 1000)
  if not console_list:
    Log.Message("No paragraphs found in the console.")
    return
  for i in range(len(console_list)):
    check_text = str(console_list[i].WPFControlText)
    if "Trial License" in check_text:
      Log.Checkpoint(check_text)
      break
  else:
    Log.Checkpoint('Trial license not used')
      
###############################################################################
# Function : check_flowdocument_control_instances
# Description : Verifies the number of control instances created in the server console.
# Parameter : instances (int) - Expected number of control instances. Example: 5
###############################################################################
def check_flowdocument_control_instances(instances):
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "Paragraph", 1000)
  if not console_list:
    Log.Message("No paragraphs found in the console.")
    return
  count = 0
  for i in range(len(console_list)):
    check_text = str(console_list[i].WPFControlText)
    if "Created ToolConnector for ControlExpert." in check_text:
      count+=1
      Log.Message(check_text)
  if int(instances) == int(count):
    Log.Checkpoint('The total number of control instances is ' + str(instances))   
  else:
    Log.Warning('The total number of control instances is not ' + str(instances))
    Log.Message(int(count))
    
###############################################################################
# Function : verify_invalid_hosting_control_instances
# Description : Verifies the tooltip message for invalid hosting control instances.
# Parameter : None
###############################################################################
def verify_invalid_hosting_control_instances():
  instance = server_obj.controlparticipantmaxinstancetextbox.object
  instance.HoverMouse(100,15)
  aqUtils.Delay(1000)
  msg = instance.ToolTip.OleValue
  if str(msg) == 'Minimum is 4 and maximum is 20 instances':
    Log.Checkpoint(str(msg))

###############################################################################
# Function : navigate_to_explorers
# Description : Navigates to a specific explorer tab in the application.
# Parameter : Explorername (str) - Name of the explorer to navigate to. Example: "System Explorer"
###############################################################################
def navigate_to_explorers(Explorername):
  Applicationutility.wait_in_seconds(3000, 'Wait')
  menu_items_obj = ses_obj.maintoolbartextbox.object
  menu_items_list = menu_items_obj.FindAllChildren("ClrClassName", "ContentPresenter", 50)
  if not menu_items_list:
    Log.Message("No menu items found in the toolbar.")
    return
  for i in range(len(menu_items_list)):
    if Explorername in str(menu_items_list[i].DataContext.ToolTip) :
      menu_items_list[i].click()
      break
  else:
    Log.Message(f"Explorer '{Explorername}' not found in the toolbar.")
      
###############################################################################
# Function : verify_explorer_tab
# Description : Verifies if a specific tab is active in the application.
# Parameter : TabName (str) - Name of the tab to verify. Example: "System Explorer"
###############################################################################
def verify_explorer_tab(TabName):
  tab_obj = eng_obj.mainscreenbutton.object
  colesable_items = tab_obj.FindAllChildren("ClrClassName", "CloseableTabItem", 50)
  for item in colesable_items:
    if TabName in item.DataContext.TitleToolTip.OleValue   and item.IsActive :
      Log.Message(f"{TabName} Tab is sucesfully verified")
      break
  else:
    Log.Message(f"Tab '{TabName}' is not open")

###############################################################################
# Function : terminate_tested_apps
# Description : Terminates all tested applications.
# Parameter : None
###############################################################################
def terminate_tested_apps():
  aqUtils.Delay(500)
  TestedApps.TerminateAll()
    
###############################################################################
# Function : terminate_system_server
# Description : Terminates the system server application.
# Parameter : None
###############################################################################
def terminate_system_server():
  Applicationutility.wait_in_seconds(1000, 'wait')
  TestedApps.SystemServer.Terminate()
    
###############################################################################
# Function : start_system_server
# Description : Starts the system server application.
# Parameter : None
###############################################################################
def start_system_server():
  TestedApps.SystemServer.Run()
  Applicationutility.wait_in_seconds(1000, 'wait')
    
###############################################################################
# Function : terminate_ec_app
# Description : Terminates the Engineering Client application.
# Parameter : None
###############################################################################
def terminate_ec_app():
  Applicationutility.wait_in_seconds(1000, 'wait')
  TestedApps.EngineeringClient.Terminate()
    
###############################################################################
# Function : close_x_EC
# Description : Closes the Engineering Client application using the close button.
# Parameter : None
###############################################################################
def close_x_EC():
  Applicationutility.wait_in_seconds(1000, 'wait')
  eng_obj.closeecbutton.click()
    
###############################################################################
# Function : Pre_Condition1_SE
# Description : Prepares the system by creating a new system in the Systems Explorer.
# Parameter : None
###############################################################################
def Pre_Condition1_SE():
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if str('Systems Explorer') in str(tab.WPFControlText):
      Engineeringclientutility.clickR_node_SE("Systems Explorer")
      createSystem = ses_obj.createsystembutton.object
      createSystem.Click()
      ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
      aqUtils.Delay(1000)
      Sys.Keys("System_Test")
      ses_obj.systemexplorernodebutton.click()
      
###############################################################################
# Function : Pre_Condition_Navigation_SE
# Description : Navigates to the Systems Explorer tab if not already active.
# Parameter : None
###############################################################################
def Pre_Condition_Navigation_SE():
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if tab.IsActive:
      if str('Systems Explorer') in str(tab.WPFControlText):
        Log.Message("Already in Systems Explorer") 
      else:
        navigate_to_explorers("System Explorer")
        break   
        
###############################################################################
# Function : Pre_Condition_check_for_system_Create_System_SE3
# Description : Checks for an existing system in Systems Explorer or creates a new one.
# Parameter : None
###############################################################################
def Pre_Condition_check_for_system_Create_System_SE3():
  SE_node = ses_obj.systemexplorernodebutton.object
  SE_node_list = SE_node.FindAllChildren("ClrClassName", "ExplorerNode", 500)
  for i in range(len(SE_node_list)):
    name = SE_node_list[i].DataContext.Identifier.OleValue
    if str(name) == str('System_1'):
      SE_node_list[i].Click()
      break
  else:
    Engineeringclientutility.clickR_node_SE('Systems Explorer')
    SE_Context_Menu = ses_obj.createsystembutton.object
    SE_Context_Menu.Click()
    ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
    ses_obj.systemexplorernodebutton.click()
    Engineeringclientutility.click_node_SE('System_1')

###############################################################################
# Function : Pre_Condition_Navigation_SE2
# Description : Ensures navigation to Systems Explorer and checks for a specific system.
# Parameter : None
###############################################################################
def Pre_Condition_Navigation_SE2():
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if tab.IsActive:
      if str('Systems Explorer') in str(tab.WPFControlText):
        Log.Message("Already in Systems Explorer")
        Pre_Condition_check_for_system_Create_System_SE3()
      elif str(tab.WPFControlText) == "System_1" :
        break
      else:
        navigate_to_explorers("System Explorer")
        Pre_Condition_check_for_system_Create_System_SE3()
        break   

###############################################################################
# Function : check_whole_flowdocument
# Description : Checks the entire flow document for a specific message.
# Parameter : verify_message (str) - Message to verify. Example: "Server is ready"
###############################################################################
def check_whole_flowdocument(verify_message):
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "Paragraph", 10000)
  for i in range(len(console_list)):
    check_text = str(console_list[i].WPFControlText)
    if verify_message in str(console_list[0].WPFControlText):
      Log.Checkpoint(check_text)
      return True
    elif verify_message in str(console_list[1].WPFControlText):
      Log.Checkpoint(check_text)
      return True
  else:
    return False

###############################################################################
# Function : check_server_ready
# Description : Verifies if the server is ready by checking the console messages.
# Parameter : None
###############################################################################
def check_server_ready():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 100)
  for _ in range(600):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if 'Server is ready' in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    elif 'Processing command metadata overrides...' in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      Applicationutility.wait_in_seconds(8000, 'Wait for server ready !')

###############################################################################
# Function : check_server_stop
# Description : Verifies if the server has stopped by checking the console messages.
# Parameter : None
###############################################################################
def check_server_stop():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 1000)
  for _ in range(600):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if 'Server is stopped' in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      Applicationutility.wait_in_seconds(1000, 'Wait for server Stopped !')
      console_obj.Refresh()
      
###############################################################################
# Function : Click_on_Tab_Enter
# Description : Simulates pressing the Tab and Enter keys.
# Parameter : None
###############################################################################
def Click_on_Tab_Enter():
  Sys.Keys('[Tab]')
  Sys.Keys('[Enter]')
  
###############################################################################
# Function : check_server_stop_1
# Description : Verifies if the server has stopped or is ready by checking the console messages.
# Parameter : None
###############################################################################
def check_server_stop_1():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 50)
  for _ in range(600):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if Systemserverutility.check_whole_flowdocument('Server is stopped'):
      Applicationutility.take_screenshot()
      break
    elif 'Server is ready' in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      Applicationutility.wait_in_seconds(1000, 'Wait for server ready !')
      console_obj.Refresh()

###############################################################################
# Function : click_on_username_dropdown
# Description : Clicks on the username dropdown menu.
# Parameter : None
###############################################################################
def click_on_username_dropdown():
  dropdown = server_obj.usernamedropdown.object
  if dropdown.ClrClassName == "Menu":
    dropdown.Click()
    Log.Checkpoint("Username dropdown is clicked")
    
###############################################################################
# Function : click_on_menuitem_Usericon
# Description : Clicks on a specific menu item under the user icon dropdown.
# Parameter : param (str) - Name of the menu item to click. Example: "Logout"
###############################################################################
def click_on_menuitem_Usericon(param):
  logout = server_obj.logout.object.FindAllChildren("ClrClassName", "MenuItem", 50)
  for option in logout:
    if option.WPFControlText == param:
      option.Click()
      Log.Checkpoint(f'{param} option is clicked')
      break
  else:
    Log.Warning(f'{param} option is does not exists in menuitem')
      
###############################################################################
# Function : click_on_login
# Description : Clicks on the login menu item.
# Parameter : None
###############################################################################
def click_on_login():
  server_obj.loginmenuitem.object.Click()
  Log.Checkpoint("Login option is clicked")
  
###############################################################################
# Function : enter_maintenance_mode
# Description : Simulates entering maintenance mode by sending keyboard input.
# Parameter : param (str) - Keyboard input to simulate. Example: "Ctrl+M"
###############################################################################
def enter_maintenance_mode(param):
  Sys.Keys(param)
  Log.Checkpoint(f'The keyboard action - {param}, has been performed.')
  Applicationutility.take_screenshot()
  
###############################################################################
# Function : enter_maintenance_password
# Description : Enters the maintenance mode password and confirms it.
# Parameter : password (str) - Password to enter. Example: "admin123"
#             key (str) - Key to confirm the password. Example: "[Enter]"
###############################################################################
def enter_maintenance_password(password, key):
  server_obj.passwordboxtextbox.enter_text(password)
  Log.Checkpoint(f'The maintenance mode password {password}, has been entered.')
  Applicationutility.wait_in_seconds(2000, "wait")
  Sys.Keys(key)
  Log.Checkpoint(f'The keyboard action - {key}, has been performed.')
  
###############################################################################
# Function : database_deleteall
# Description : Enters a database command and executes it.
# Parameter : command (str) - Database command to execute. Example: "DELETE ALL"
#             key (str) - Key to confirm the command. Example: "[Enter]"
###############################################################################
def database_deleteall(command, key):
  server_obj.DBcommand.enter_text("  "+command)
  Log.Checkpoint(f'The command {command}, has been entered.')
  Applicationutility.wait_in_seconds(2000, "wait")
  Sys.Keys(key)
  Log.Checkpoint(f'The keyboard action - {key}, has been performed.')

###############################################################################
# Function : select_settings_submenu_systemserver
# Description : Selects an option from the system server settings submenu.
# Parameter : option (str) - Name of the submenu option to select. Example: "Backup"
###############################################################################
def select_settings_submenu_systemserver(option):
  menu_items = server_obj.settingsbutton.object.FindAllChildren("ClrClassName", "MenuItem", 50)
  menu_item = next((item for item in menu_items if item.WPFControlText == option), None)  
  if menu_item is not None:
    menu_item.click()
    Log.Checkpoint(f"{option} was selected in Server Settings Context Menu.")
  else:
    Log.Warning(f"{option} not found in Server Settings Context Menu.")
  
###############################################################################
# Function : select_system_in_systembackupsheduler
# Description : Selects a system from the system backup scheduler dropdown.
# Parameter : system (str) - Name of the system to select. Example: "System_1"
###############################################################################
def select_system_in_systembackupsheduler(system):
  for box in server_obj.systembackupshedulerbutton.object.FindAllChildren("ClrClassName", "ComboBox", 50):
    if system in box.wText:
      box.click()
      break
  else:
    Log.Warning(f'{system} not found in ComboBox.')
    return
  for item in server_obj.systembackupdropdownbutton.object.FindAllChildren("ClrClassName", "TextBlock", 50):
    if item.DataContext.Identifier == system:
      item.click()
      Log.Checkpoint(f'{system} was selected in DropDown.')
      return
  Log.Warning(f'{system} was not found in DropDown.')

###############################################################################
# Function : checkboxinsystembackup
# Description : Checks specific checkboxes in the system backup scheduler.
# Parameter : prop (str) - Names of the checkboxes to check, separated by "/". Example: "Monday/Tuesday"
###############################################################################
def checkboxinsystembackup(prop):
  unchecked_checkboxes = [i for i in server_obj.systembackupshedulerbutton.object.FindAllChildren("ClrClassName", "CheckBox", 50) 
                          if i.WPFControlText.strip() in set(prop.split("/")) and not i.IsChecked]
  for checkbox in unchecked_checkboxes:
    checkbox.Click()
    Log.Checkpoint(f"Checkbox for {checkbox.WPFControlText.strip()} is Checked")
  Log.Message("checkbox are already checked." if not unchecked_checkboxes else "")

###############################################################################
# Function : select_frequency_in_system_backup
# Description : Selects a frequency option in the system backup scheduler.
# Parameter : freq (str) - Frequency to select. Example: "Weekly"
###############################################################################
def select_frequency_in_system_backup(freq):
  for box in server_obj.systembackupshedulerbutton.object.FindAllChildren("ClrClassName", "ComboBox", 50):
    if "Daily|Weekly|Monthly" in box.wItemList:
      box.click()
      break
  else:
    Log.Warning(f'dropdown not found in ComboBox.')
    return
  for item in server_obj.systembackupdropdownbutton.object.FindAllChildren("ClrClassName", "ComboBoxItem", 50):
    if item.WPFControlText == freq:
      item.click()
      Log.Checkpoint(f'{freq} was selected in DropDown.')
      if freq == "Weekly":
        checkboxinsystembackup("Monday/Tuesday/Wednesday/Thursday/Friday")
      return
  Log.Warning(f'{freq} was not found in DropDown.')
  
###############################################################################
# Function : system_server_popup
# Description : Clicks a button in the system server confirmation popup.
# Parameter : button (str) - Name of the button to click. Example: "Yes"
###############################################################################
def system_server_popup(button):
  for btn in server_obj.systemserverconfirmationpopup.object.FindAllChildren("WndClass", "Button", 50):
    if button in btn.WndCaption:
      btn.click()
      Log.Checkpoint(f"{button} Clicked in Popup Window.")
      break
  else:
    Log.Warning("{button} button not found.")
  
###############################################################################
# Function : clicksaveaswindowbutton
# Description : Clicks a button in the "Save As" window.
# Parameter : button (str) - Name of the button to click. Example: "Save"
###############################################################################
def clicksaveaswindowbutton(button):
  for i in server_obj.filesavedlocation.object.FindAllChildren("WndClass", "Button", 50):
    if button in i.WndCaption:
      i.click()
      Log.Checkpoint(f"{button} Clicked in Popup Window.")
      break
  else:
    Log.Warning("{button} button not found.")
    
###############################################################################
# Function : backup_window_checkbox
# Description : Clicks a checkbox in the backup window.
# Parameter : prop (str) - Name of the checkbox to click. Example: "Include Logs"
###############################################################################
def backup_window_checkbox(prop):
  for i in msg_obj.modeldialogfeedbacktextbox.object.FindAllChildren("ClrClassName", "CheckBox", 50):
    if prop in i.WPFControlText:
      i.click()
      Log.Checkpoint(f'{prop} check box clicked.')
      break
  else:
    Log.Warning(f'{prop} check box not found.')
    
###############################################################################
# Function : backup_window_button
# Description : Clicks a button in the backup window.
# Parameter : button (str) - Name of the button to click. Example: "OK"
###############################################################################
def backup_window_button(button):
  for i in msg_obj.modeldialogfeedbacktextbox.object.FindAllChildren("ClrClassName", "Button", 50):
    if button in i.WPFControlText:
      i.click()
      Log.Checkpoint(f'{button} Button Clicked in Backup Window.')
      break
  else:
    Log.Warning(f'{button} Button not found in Backup Window.')

###############################################################################
# Function : browsebutton_backup
# Description : Clicks the browse button to select a file destination path.
# Parameter : None
###############################################################################
def browsebutton_backup():
  for btn in ses_obj.browsebutton.object.FindAllChildren("ClrClassName", "Button", 50):
    if btn.ToolTip == "Select the desired file destination path":
      btn.click()