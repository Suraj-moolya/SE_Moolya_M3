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

  
def system_server_icon_rclick_on(element): 
  Applicationutility.wait_in_seconds(1000, 'wait')
  win_obj.showhiddeniconbutton.object.Click()
  aqUtils.Delay(1500)
  notification_area = win_obj.notificationareawindow.object
  for i in range(notification_area.wButtonCount):
    if 'EcoStruxure Process Expert - System Server' in str(notification_area.wButtonText[i]):
      notification_area.ClickItemR(i)
      break
  aqUtils.Delay(1500)
  context_menu = server_obj.contextmenubutton.object
  menu_item_count = context_menu.wItems.Count
  Applicationutility.wait_in_seconds(1000, 'wait')
  for j in range(menu_item_count):
    if element == context_menu.wItems.Item[j].Text:
      context_menu.ClickItem(j)
      break
  aqUtils.Delay(1500)
  
def verify_SS_LoginDialogue():
    Username = server_obj.usernametextbox.object
    if Username.VisibleOnScreen:
      Log.Message("Login Dialogue box successfully appeared")
    else:
      Log.Message("Login Dialogue box did not appear")
    
    
def check_server_console_flowdocument(verify_message):
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 100)
  for _ in range(100):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if str(verify_message) in str(console_list[0].Blocks.LastBlock.WPFControlText):
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    elif 'Processing command metadata overrides...' in str(console_list[0].Blocks.LastBlock.WPFControlText):
      Log.Checkpoint(verify_message)
      Applicationutility.take_screenshot()
      break
    else:
      #Log.Message(check_text)
      Applicationutility.wait_in_seconds(12000, 'Wait for server ready !')
      console_obj.Refresh()
      
def verify_start_stop_disabled():

  Action_Start = server_obj.startserverbutton.object
  Action_Stop  = server_obj.stopserverbutton.object 
  if Action_Start.Enabled and Action_Stop.Enabled:
    Log.Warning("User has server admin rights Enabled")
  else:
    Log.Message("User has no server admin rights")
    
      
          
def rclick_system_server_show_server_console(): 
  win_obj.showhiddeniconbutton.object.Click()
  Applicationutility.wait_in_seconds(2500, "Wait")
  notification_area = win_obj.notificationareawindow.object
  for i in range(notification_area.wButtonCount):
    if 'EcoStruxure Process Expert - System Server' in str(notification_area.wButtonText[i]):
      notification_area.ClickItemR(i)
      break
  aqUtils.Delay(500)
  context_menu = server_obj.contextmenubutton.object
  menu_item_count = context_menu.wItems.Count
  for j in range(menu_item_count):
    if 'Show Server Console' == context_menu.wItems.Item[j].Text:
      context_menu.ClickItem(j)
      break
  aqUtils.Delay(500)
    
      
def check_server_stopped():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 50)
  for _ in range(60):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
    if 'Server is stopped' in check_text:
      Log.Message(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      aqUtils.Delay(5000)
      console_obj.Refresh()
      
def check_flowdocument_license():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "Paragraph", 1000)
  for i in range(len(console_list)):
    check_text = str(console_list[i].WPFControlText)
    if "Trial License" in check_text:
      Log.Checkpoint(check_text)
      break
  else:
    Log.Checkpoint('Trial license not used')
      
def check_flowdocument_control_instances(instances):
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "Paragraph", 1000)
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
    
def verify_invalid_hosting_control_instances():
  instance = server_obj.controlparticipantmaxinstancetextbox.object
  instance.HoverMouse(100,15)
  aqUtils.Delay(1000)
  msg = instance.ToolTip.OleValue
  if str(msg) == 'Minimum is 4 and maximum is 20 instances':
    Log.Checkpoint(str(msg))

def navigate_to_explorers(Explorername):
  Applicationutility.wait_in_seconds(3000, 'Wait')
  menu_items_obj = ses_obj.maintoolbartextbox.object
  menu_items_list = menu_items_obj.FindAllChildren("ClrClassName", "ContentPresenter", 50)
  for i in range(len(menu_items_list)):
    if Explorername in str(menu_items_list[i].DataContext.ToolTip) :
      menu_items_list[i].click()
      
def verify_explorer_tab(TabName):
  tab_obj = eng_obj.mainscreenbutton.object
  colesable_items = tab_obj.FindAllChildren("ClrClassName", "CloseableTabItem", 50)
  for item in colesable_items:
    if TabName in item.DataContext.TitleToolTip.OleValue   and item.IsActive :
      Log.Message("Tab is sucesfully verified")
      break
  else:
    Log.Message("Tab is not open")

    
    
def terminate_tested_apps():
    aqUtils.Delay(500)
    TestedApps.TerminateAll()
    
def terminate_system_server():
    Applicationutility.wait_in_seconds(1000, 'wait')
    TestedApps.SystemServer.Terminate()
    
    
def start_system_server():
    TestedApps.SystemServer.Run()
    Applicationutility.wait_in_seconds(1000, 'wait')
    
def terminate_ec_app():
    Applicationutility.wait_in_seconds(1000, 'wait')
    TestedApps.EngineeringClient.Terminate()
    
def close_x_EC():
    Applicationutility.wait_in_seconds(1000, 'wait')
    eng_obj.closeecbutton.click()
    
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
      
  
def Pre_Condition_Navigation_SE():
  tabs = eng_obj.workspacetextbox.find_children_for_closeable_tab_item()
  for tab in tabs:
    if tab.IsActive:
      if str('Systems Explorer') in str(tab.WPFControlText):
        Log.Message("Already in Systems Explorer") 
      else:
        navigate_to_explorers("System Explorer")
        break   
        
        
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

    
def check_server_ready():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 100)
  for _ in range(600):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
#    if Systemserverutility.check_whole_flowdocument('Server is ready'):
#      Applicationutility.take_screenshot()
#      break
#    el
    if 'Server is ready' in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      Applicationutility.wait_in_seconds(5000, 'Wait for server ready !')
      #console_obj.Refresh()
      
def check_server_stop():
  console_obj = server_obj.consolewindow.object
  console_list = console_obj.FindAllChildren("ClrClassName", "FlowDocument", 1000)
  for _ in range(600):
    check_text = str(console_list[0].Blocks.LastBlock.WPFControlText)
#    if Systemserverutility.check_whole_flowdocument('Server is stopped'):
#      Applicationutility.take_screenshot()
#      break
    if 'Server is stopped' in check_text:
      Log.Checkpoint(check_text)
      Applicationutility.take_screenshot()
      break
    else:
      Applicationutility.wait_in_seconds(1000, 'Wait for server Stopped !')
      console_obj.Refresh()
#  system_server_icon_rclick_on('Exit')
      
      
def Click_on_Tab_Enter():
  Sys.Keys('[Tab]')
  Sys.Keys('[Enter]')
  
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

def click_on_username_dropdown():
  dropdown = server_obj.usernamedropdown.object
  if dropdown.ClrClassName == "Menu":
    dropdown.Click()
    Log.Checkpoint("Username dropdown is clicked")
    
def click_on_menuitem_Usericon(param):
  logout = server_obj.logout.object.FindAllChildren("ClrClassName", "MenuItem", 50)
  for option in logout:
    if option.WPFControlText == param:
      option.Click()
      Log.Checkpoint(f'{param} option is clicked')
      break
  else:
    Log.Warning(f'{param} option is does not exists in menuitem')
      
def click_on_login():
  server_obj.loginmenuitem.object.Click()
  Log.Checkpoint("Login option is clicked")
  
def enter_maintenance_mode(param):
  Sys.Keys(param)
  Log.Checkpoint(f'The keyboard action - {param}, has been performed.')
  
def enter_maintenance_password(password, key):
  server_obj.passwordboxtextbox.enter_text(password)
  Log.Checkpoint(f'The maintenance mode password {password}, has been entered.')
  Applicationutility.wait_in_seconds(2000, "wait")
  Sys.Keys(key)
  Log.Checkpoint(f'The keyboard action - {key}, has been performed.')
  
def database_deleteall(command, key):
  server_obj.DBcommand.enter_text("  "+command)
  Log.Checkpoint(f'The command {command}, has been entered.')
  Applicationutility.wait_in_seconds(2000, "wait")
  Sys.Keys(key)
  Log.Checkpoint(f'The keyboard action - {key}, has been performed.')

def select_settings_submenu_systemserver(option):
  menu_items = server_obj.settingsbutton.object.FindAllChildren("ClrClassName", "MenuItem", 50)
  menu_item = next((item for item in menu_items if item.WPFControlText == option), None)  
  if menu_item is not None:
    menu_item.click()
    Log.Checkpoint(f"{option} was selected in Server Settings Context Menu.")
  else:
    Log.Warning(f"{option} not found in Server Settings Context Menu.")
  
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

  
def checkboxinsystembackup(prop):
  unchecked_checkboxes = [i for i in server_obj.systembackupshedulerbutton.object.FindAllChildren("ClrClassName", "CheckBox", 50) 
                          if i.WPFControlText.strip() in set(prop.split("/")) and not i.IsChecked]
  for checkbox in unchecked_checkboxes:
    checkbox.Click()
    Log.Checkpoint(f"Checkbox for {checkbox.WPFControlText.strip()} is Checked")
  Log.Message("checkbox are already checked." if not unchecked_checkboxes else "")


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
  
  
def system_server_popup(button):
  for btn in server_obj.systemserverconfirmationpopup.object.FindAllChildren("WndClass", "Button", 50):
    if button in btn.WndCaption:
      btn.click()
      Log.Checkpoint(f"{button} Clicked in Popup Window.")
      break
  else:
    Log.Warning("{button} button not found.")
  
  
def ldkjf():
  server_obj.systembackupshedulerbutton.object.Close()
  
def clicksaveaswindowbutton(button):
  for i in server_obj.filesavedlocation.object.FindAllChildren("WndClass", "Button", 50):
    if button in i.WndCaption:
      i.click()
      Log.Checkpoint(f"{button} Clicked in Popup Window.")
      break
  else:
    Log.Warning("{button} button not found.")
    
def backup_window_checkbox(prop):
  for i in msg_obj.modeldialogfeedbacktextbox.object.FindAllChildren("ClrClassName", "CheckBox", 50):
    if prop in i.WPFControlText:
      i.click()
      Log.Checkpoint(f'{prop} check box clicked.')
      break
  else:
    Log.Warning(f'{prop} check box not found.')
    
def backup_window_button(button):
  for i in msg_obj.modeldialogfeedbacktextbox.object.FindAllChildren("ClrClassName", "Button", 50):
    if button in i.WPFControlText:
      i.click()
      Log.Checkpoint(f'{button} Button Clicked in Backup Window.')
      break
  else:
    Log.Warning(f'{button} Button not found in Backup Window.')

def browsebutton_backup():
  for btn in ses_obj.browsebutton.object.FindAllChildren("ClrClassName", "Button", 50):
    if btn.ToolTip == "Select the desired file destination path":
      btn.click()