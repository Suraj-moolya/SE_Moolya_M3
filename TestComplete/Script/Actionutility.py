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
from Topology import Topology

import os
import csv
import xml.etree.ElementTree as ET
import datetime

Topology1 = Topology()
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
Screen_List = [Topology1, EngineeringClient1, ApplicationExplorerTab1, ECWarningPopup1, GlobalTemplatesTab1, LicenseManagement1, MessageBox1, ProjectExplorerTab1, SystemExplorerScreen1, SystemServer1, TopologyExplorerTab1, WindowsExplorer1]
msg_obj = MessageBox()
win_obj = WindowsExplorer()
server_obj = SystemServer()
eng_obj = EngineeringClient()
aet_obj = ApplicationExplorerTab()

###############################################################################
#Author : Preetham S R
#Function : Launches Engineering Client
#Parameter : No
###############################################################################
def launch_engineering_client():
    TestedApps.EngineeringClient.Run()
    Applicationutility.wait_for_execution(30000, 'Launching Engineering Client')

###############################################################################
#Author : Subhramanya B M
#Function : Launches Engineering Client even if one instance already running.
#Parameter : No
###############################################################################    
def launch_engineering_client_with_secondtime():
    TestedApps.EngineeringClient.Run(-1, True, -1)
    Applicationutility.wait_for_execution(30000, 'Launching Engineering Client')

###############################################################################
#Author : 
#Function :
#Parameter :
###############################################################################
def click_on_more_option(element):
  task_obj = server_obj.consolewindow.object
  task_list = task_obj.FindAllChildren("ClassName", "accessiblebutton", 50)
  for i in range(len(task_list)):
    if task_list[i].ObjectIdentifier == element:
      task_list[i].Click()
      break

###############################################################################
#Author : Preetham S R
#Function : To Open task manager and open details tab
#Parameter : No
###############################################################################
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
      Log.Message('Clicked on Detals tab')
      Applicationutility.wait_in_seconds(2000, 'Wait')
      break
         
###############################################################################
#Author : Suraj R
#Function : Engineering Client Shortcut Key options
#Parameter :R, T, A, P 
###############################################################################
def explorer_shortcut_key(Shortcut):
  Explorer_shortcut = {"Alt+R":"R","Alt+T":"T","Alt+A":"A","Alt+P":"P"}
  if Shortcut in Explorer_shortcut:
    shortcut_key = "~"+ str(Explorer_shortcut[Shortcut])
    Sys.Keys(shortcut_key)
  else:
    Log.Error("No shortcut key assigned for the explorer")
    
###############################################################################
#Author : Suraj R
#Function : Escape keyboard action
#Parameter : No
###############################################################################
def escape_key_action():
    Sys.Keys('[Esc]')
    Applicationutility.take_screenshot()

###############################################################################
#Author : Preetham S R
#Function : Takes screenshot of the screen
#Parameter : Message
###############################################################################    
def take_screenshot(msg="taking screenshot of current screen"):
    """take screenshot"""
    element = Sys.Desktop.Picture()
    Log.Picture(element, msg)

###############################################################################
#Author : Suraj R
#Function : Performs Delete Keboard action
#Parameter : No
###############################################################################    
def delete_key_AE():
  Sys.Keys('[Del]')
  Applicationutility.take_screenshot()
  
###############################################################################
#Author : Preetham S R
#Function : Checks Control exepert instances in Task Manager
#Parameter : No of instances
###############################################################################  
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
  
###############################################################################
#Author : Preetham S R
#Function : Waits for execution completion WRT Engineering Client Notification Panel
#Parameter : No
###############################################################################    
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
  Applicationutility.wait_in_seconds(1500, 'Wait')
  
###############################################################################
#Author : Preetham S R
#Function : Performs click action on Engineering client pop up window
#Parameter : Button Name
###############################################################################
def modal_dialog_window_button(button_name):
  try:
    buttons_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
    take_screenshot('Taking Screenshot of the Message Window.')
    for button in buttons_list:
      if button_name in str(button.WPFControlText) :
        button.click()
        Log.Checkpoint('Clicked ' + str(button.WPFControlText) + ' button.')
        break
    else:
      Log.Message("Button name mentioned doesnt exists")
  except:
    Log.Message('Expected Pop up not present')  
    
###############################################################################
#Author : Preetham S R
#Function : To get the object from the object repository
#Parameter : Screen Name & Object Name
###############################################################################  
def get_obj(param):
  Screen, property = param.split('$$')
  for Screen_item in Screen_List:
    if str(Screen) in str(Screen_item):
        obj = getattr(Screen_item, property)
        return obj
  else:
    Log.Warning(f'The object {property} at {Screen} not found !')

###############################################################################
#Author : Preetham S R
#Function : To click on pop ups
#Parameter : window_class, parent_object, Button Name
###############################################################################  
def Click_popup_button(param):
  window_class, parent_object, button_name = param.split('$$') 
  parm = window_class + '$$' + parent_object
  obj = get_obj(parm)
  buttons_list = obj.object.FindAllChildren('ClrClassName', 'Button', 1000)
  Applicationutility.wait_in_seconds(500, 'Wait')
  if buttons_list:
    take_screenshot('Taking Screenshot of the Popup Window.')
    for button in buttons_list:
      Applicationutility.wait_in_seconds(1000, 'Wait')
      if button_name in str(button.WPFControlText) and button.Enabled == True:
        button.click()
        Log.Message('Clicked ' + str(button.WPFControlText) + ' button.')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        break
  else:
    Log.Warning("Button name mentioned doesnt exists")

###############################################################################
#Author : Preetham S R
#Function : Close tab in Engineering Client 
#Parameter : tab Name
###############################################################################    
def close_tab_items_EC(identifier):
  template = eng_obj.mainscreenbutton.object
  template_list = template.FindAllChildren('ClrClassName', 'CloseableTabItem', 1000)
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if identifier in str(template_list[i].Header.OleValue):
        template_list[i].Click((template_list[i].Width-15), (template_list[i].Height/2)) 
        break
  else:
     Log.Warning("Tab Item mentioned is not Valid")
 
###############################################################################
#Author : 
#Function :
#Parameter :
###############################################################################    
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

###############################################################################
#Author : Preetham S R
#Function : Verify Dialog Window Text 
#Parameter : Text
###############################################################################
def modal_dialog_window_dialog(param):
  obj = msg_obj.modaldialogwindowtextbox
  headder_list = obj.object.FindAllChildren('WPFControlName', 'HeaderGrid', 1000)
  dialog = headder_list[0].FindAllChildren('ClrClassName', 'TextBlock', 10)
  if dialog:
    for text in dialog:
      if param in str(text.WPFControlText):
        Log.Checkpoint('Dialog box message : ' + str(text.WPFControlText))
        take_screenshot('Taking Screenshot of the Message Window.')
        break
      else:
        Log.Warning(f'{param} : not found!')
  else:
    Log.Warning('{Dialog Window not found!')
      
###############################################################################
#Author : Preetham S R
#Function : To select dropdown value in PopUp Dialog Window
#Parameter : Dependant Dropdown text, Dropdown Value
###############################################################################  
def modal_dialog_windo_selectItem(param):
  controller, val = param.split("$$")
  network_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'ComboBox', 1000)
  if network_list:
    for network in network_list:
      if controller in network.DataContext.DeviceIdentifier.OleValue:
        Log.Message(network.DataContext.DeviceIdentifier.OleValue)
        network.SelectedItem = val
        Log.Message(str(network.SelectedItem) + " is selected")
        take_screenshot('Taking Screenshot')
        break
    else:
      Log.Warning(f'{val} does not exist in the drop down')
  else:
    Log.Warning(f'{controller}, {val} : not found !')
      
###############################################################################
# Function : Enter_filename_fileformat_Export_Window
# Description: Enters the file name and location in the export window.
# Parameter : file_name, file_format (str) - File format for the export.
###############################################################################

def Enter_filename_fileformat_Export_Window(file_details):
  file_name, file_format = file_details.split('$$')
  if not Project.Variables.VariableExists(file_name):
        Project.Variables.AddVariable(file_name, "String")     
  Project.Variables.VariableByName[file_name] = str(file_name + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Log.Message(Project.Variables.VariableByName[file_name])
  Applicationutility.wait_in_seconds(2000,"Wait")
  Export_window = msg_obj.exportfilenametextbox.object
  if Export_window.Exists:
    filename_textbox = msg_obj.exportfilenametextbox.object
    filename_textbox.Keys(Project.Variables.VariableByName[file_name]+file_format)
  else:
    Log.Warning("Export Windows doesnt exists") 
  filelocation = msg_obj.exportfilelocationtextbox
  tox = (filelocation.object.Height)/2
  toy = 10
  filelocation.click_at(tox,toy)
  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name) 
  Sys.Keys(full_path)
  Applicationutility.take_screenshot('taking Screenshot')
  Sys.Keys("[Enter]")    

###############################################################################
# Function : Enter_fileName_fileformat_Import_Window
# Description: Enters the system name and location in the import window.
# Parameter : file_format (str) - File format for the import.
###############################################################################
 
def Enter_fileName_fileformat_Import_Window(file_details):
  filename, fileformat = file_details.split('$$')
  filelocation = aet_obj.addressbandtextbox
  tox = ((filelocation.object.Height)/2) + 5
  toy = 5+5
  filelocation.click_at(toy,tox)
  base_path = os.getcwd()
  folder_name = "Test_Import_Files"
  full_path = os.path.join(base_path, folder_name)
  os.chdir(full_path) 
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]") 
  filename_textbox = aet_obj.comboboxtextbox.object
  filename_textbox.Click()
  filename_textbox.Keys(Project.Variables.VariableByName[filename] + fileformat)
  Applicationutility.take_screenshot('taking Screenshot')
  Applicationutility.wait_in_seconds(1500,"Wait")
  Sys.Keys("[Enter]")   

