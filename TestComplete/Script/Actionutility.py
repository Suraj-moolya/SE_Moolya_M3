from WindowsExplorer import WindowsExplorer
from SystemServer import SystemServer
import Applicationutility
from MessageBox import MessageBox
from EngineeringClient import EngineeringClient
from ApplicationExplorerTab import ApplicationExplorerTab
from ECWarningPopup import ECWarningPopup
from GlobalTemplatesTab import GlobalTemplatesTab
from LicenseManagement import LicenseManagement
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
from TopologyExplorerTab import TopologyExplorerTab


EngineeringClient1 = EngineeringClient()    
ApplicationExplorerTab1 = ApplicationExplorerTab()
ECWarningPopup1 = ECWarningPopup()
GlobalTemplatesTab1 = GlobalTemplatesTab()
LicenseManagement1 = LicenseManagement()
MessageBox1 = MessageBox()
ProjectExplorerTab1 = ProjectExplorerTab()
SystemExplorerScreen1 = SystemExplorerScreen()
SystemServer1 = SystemServer()
TopologyExplorerTab1 = TopologyExplorerTab()
WindowsExplorer1 = WindowsExplorer()
Screen_List = [EngineeringClient1, ApplicationExplorerTab1, ECWarningPopup1, GlobalTemplatesTab1, LicenseManagement1, MessageBox1, ProjectExplorerTab1, SystemExplorerScreen1, SystemServer1, TopologyExplorerTab1, WindowsExplorer1]
msg_obj = MessageBox()
win_obj = WindowsExplorer()
server_obj = SystemServer()
eng_obj = EngineeringClient()


def launch_engineering_client():
    TestedApps.EngineeringClient.Run()
    aqUtils.Delay(30000)
    
def launch_engineering_client_with_secondtime():
    TestedApps.EngineeringClient.Run(-1, True, -1)
    aqUtils.Delay(30000)

def click_on_more_option(element):
  task_obj = server_obj.consolewindow.object
  task_list = task_obj.FindAllChildren("ClassName", "accessiblebutton", 50)
  for i in range(len(task_list)):
    if task_list[i].ObjectIdentifier == element:
      task_list[i].Click()
      break
  
def open_select_details_tab_TM():
  Sys.Keys('^![Esc]')
  task_obj = win_obj.commandbarbutton.object
  task_list = task_obj.FindAllChildren("ClassName", "accessiblebutton", 50)
  for i in range(len(task_list)):
    if task_list[i].ObjectIdentifier == 'More_details':
      task_list[i].Click()
      break
  tab = win_obj.tabsbutton.object
  for j in range(tab.wTabCount):
    if tab.wTabCaption[j] == 'Details':
      tab.ClickTab(j)
      aqUtils.Delay(2000)
      break
         

def explorer_shortcut_key(Shortcut):
  Explorer_shortcut = {"Alt+R":"R","Alt+T":"T","Alt+A":"A","Alt+P":"P"}
  if Shortcut in Explorer_shortcut:
    shortcut_key = "~"+ str(Explorer_shortcut[Shortcut])
    Sys.Keys(shortcut_key)
  else:
    Log.Error("No shortcut key assigned for the explorer")

def escape_key_action():
    Sys.Keys('[Esc]')
    Applicationutility.take_screenshot()
    
def take_screenshot(msg="taking screenshot of current screen"):
    """take screenshot"""
    element = Sys.Desktop.Picture()
    Log.Picture(element, msg)
    
def delete_key_AE():
  Sys.Keys('[Del]')
  Applicationutility.take_screenshot()
  
  
def check_CE_instances_TM(instances):
  Applicationutility.wait_in_seconds(2000, 'wait')
  details_list = win_obj.detaillisttextbox.object
  count = 0
  Log.Enabled = False
  for i in range(details_list.wItemCount-2):
    if details_list.wItem[i] == 'ControlExpert.exe':
      #count += 1
#      Log.Message(str(details_list.wItem[i]) + ' - ' +str(count))
      details_list.FocusItem(i)
      Applicationutility.wait_in_seconds(1000, 'wait')
  Log.Enabled = True
  for i in range(details_list.wItemCount-2):
    if details_list.wItem[i] == 'ControlExpert.exe':
      count += 1  
      if count == instances:
        break    
  if str(count) == str(instances):
    Log.Checkpoint(str(count) + ' instances of CE is running in Task Manager')
    Applicationutility.take_screenshot()
  else:
    Log.Warning(str(count) + ' instances of CE is running in Task Manager')
    Applicationutility.take_screenshot()
  
    
def wait_for_execution():
  Applicationutility.wait_in_seconds(500, 'Wait')
  Abort_list = msg_obj.notificationpanneltextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for item in Abort_list:
    if item.Panel_ZIndex == 0:
      for _ in range(100):
        if item.DataContext.Status.OleValue != "Executing":
          break
        else:
          Applicationutility.wait_in_seconds(1000, 'Loading !!!')

def modal_dialog_window_button(button_name):
  buttons_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  take_screenshot('Taking Screenshot of the Message Window.')
  for button in buttons_list:
    if button_name in str(button.WPFControlText) :
      button.click()
      Log.Checkpoint('Clicked ' + str(button.WPFControlText) + ' button.')
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    
def ffdfdfdfd():
  modal_dialog_window_button("OK")  
  
def get_obj(param):
  Screen, property = param.split('$$')
  for Screen_item in Screen_List:
    if str(Screen) in str(Screen_item):
        obj = getattr(Screen_item, property)
        return obj
  else:
    Log.Warning(f'The object {property} at {Screen} not found !')
  
def Click_popup_button(param):
  window_class, parent_object, button_name = param.split('$$') 
  parm = window_class + '$$' + parent_object
  obj = get_obj(parm)
  buttons_list = obj.object.FindAllChildren('ClrClassName', 'Button', 1000)
  take_screenshot('Taking Screenshot of the Popup Window.')
  for button in buttons_list:
    Applicationutility.wait_in_seconds(1000, 'Wait')
    if button_name in str(button.WPFControlText) :
      button.click()
      Log.Message('Clicked ' + str(button.WPFControlText) + ' button.')
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    
def close_tab_items_EC(identifier):
  template = eng_obj.mainscreenbutton.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].Header.OleValue):
        template_list[i].Click((template_list[i].Width-15), (template_list[i].Height/2)) 
  else:
     Log.Warning("Tab Item mentioned is not Valid")
     
     
def ProjectSample():
    # Obtains the path to the folder that stores the project configuration files
    ConfigPath = Project.ConfigPath
    # Searches for the .tcLS files in the folder
    ConfigFiles = aqFileSystem.FindFiles(ConfigPath, "*.tcLS")
    if ConfigFiles.Count > 0:
      while ConfigFiles.HasNext():
        aFile = ConfigFiles.Next();
        Log.Message(aFile.Name + " file is located in " + ConfigPath)
    else:
      Log.Message("No .tcLS files were found")
