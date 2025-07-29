"""Applicationutility"""
import Systemserverutility
import Engineeringclientutility
from SystemServer import SystemServer
from MessageBox import MessageBox

ss_obj = SystemServer()
msg_obj = MessageBox()

###############################################################################
#Author : Preetham S R
#Function : Stops Server and Closes System Server
#Parameter : No
###############################################################################
def close_system_server():
    """close appliactions"""
    try:
      Log.Enabled = False
      system_server = Sys.Process("SystemServer")
      if system_server.Exists:
        Log.Enabled = True
        Systemserverutility.rclick_system_server_show_server_console()
        if not Systemserverutility.check_whole_flowdocument('Server is stopped'):
          ss_obj.actionmenubutton.click()
          ss_obj.stopserverbutton.click()
          aqUtils.Delay(500)
          Sys.Keys('[Tab]')
          Sys.Keys('[Enter]')
          aqUtils.Delay(500)
          Log.Message("System Server Application is Closing !")
          Systemserverutility.check_server_stopped()
          Applicationutility.wait_in_seconds(2000, 'Wait')
          Systemserverutility.system_server_icon_rclick_on('Exit')
          Applicationutility.wait_in_seconds(5000, 'Wait')
        else:
          Log.Enabled = True
          Log.Message('System Server is not running')
          Systemserverutility.system_server_icon_rclick_on('Exit')
          Applicationutility.wait_in_seconds(5000, 'Wait')
    except:
      Log.Enabled = True
      Log.Message('System Server is not running')
    Log.Enabled = True
    Applicationutility.wait_in_seconds(3000, 'Wait')
  

def login_wait_server_ready():
    ss_obj.usernametextbox.enter_text(Project.Variables.username)
    ss_obj.passwordtextbox.enter_text(Project.Variables.password)
    ss_obj.loginbutton.click()
    Systemserverutility.rclick_system_server_show_server_console()
    ss_obj.actionmenubutton.click()
    ss_obj.startserverbutton.click()
    aqUtils.Delay(1500)
    Systemserverutility.check_server_ready()
    
def take_screenshot(msg="taking screenshot of current screen"):
    """take screenshot"""
    element = Sys.Desktop.Picture()
    Log.Picture(element, msg)
    
def close_system_server_1():
  '''Close system server 1'''
  ###
    
def screen_displayed():
    Engineeringclientutility.close_EC_ok_on_trial_pop_up()
    close_system_server()
#    Systemserverutility.rclick_system_server_show_server_console()
#    ss_obj.actionmenubutton.click()
#    ss_obj.stopserverbutton.click()
#    aqUtils.Delay(500)
#    Sys.Keys('[Tab]')
#    Sys.Keys('[Enter]')
#    aqUtils.Delay(500)
#    Systemserverutility.check_server_stopped()
#    aqUtils.Delay(500)
#    TestedApps.TerminateAll()

def application_access():
    Applicationutility.wait_in_seconds(3000, 'Wait')
    launch_system_server()
    
def wait_in_seconds(count,reson_for_delay):
    """waiting_for_page"""
    aqUtils.Delay(count,reson_for_delay)
    

def wait_for_execution():
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Abort_list = msg_obj.notificationpanneltextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for item in Abort_list:
    if item.Panel_ZIndex == 0:
      for _ in range(100):
        if item.Visible:
          if  item.DataContext.Status.OleValue != "Executing":
            break
          else:
            Applicationutility.wait_in_seconds(2000, 'Loading !!!')

def modal_dialog_window_button(button_name):
  wait_in_seconds(1000, 'wait')
  buttons_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  take_screenshot('Taking Screenshot of the Message Window.')
  for button in buttons_list:
    if button_name in str(button.WPFControlText) :
      button.click()
      Log.Checkpoint('Clicked ' + str(button.WPFControlText) + ' button.')
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
      
    
def launch_system_server_engineering_client():
    """launch appliactions"""
    try:
      Log.Enabled = False
      system_server = Sys.Process("SystemServer")
      if system_server.Exists:
        Log.Enabled = True
        Log.Message("System Server Application already Running !")
        Systemserverutility.rclick_system_server_show_server_console()
        if not Systemserverutility.check_whole_flowdocument('Server is ready'):
          ss_obj.actionmenubutton.click()
          ss_obj.startserverbutton.click()
          aqUtils.Delay(1500)
          Systemserverutility.check_server_ready()
        Sys.Process("SystemServer").WPFObject("HwndSource: MainWindow", "EcoStruxure Process Expert - System Server").Minimize()
      else:
        Log.Enabled = True
        TestedApps.SystemServer.Run()
        login_wait_server_ready()
        Sys.Process("SystemServer").WPFObject("HwndSource: MainWindow", "EcoStruxure Process Expert - System Server").Minimize()
    except:
      Log.Enabled = True
      Log.Message('System Server is not running')
    Log.Enabled = True
    Engineeringclientutility.open_EC_ok_on_trial_pop_up()
 
def launch_system_server():
    """launch appliactions"""
    try:
      Log.Enabled = False
      system_server = Sys.Process("SystemServer")
      if system_server.Exists:
        Log.Enabled = True
        Log.Message("System Server Application already Running !")
        Systemserverutility.rclick_system_server_show_server_console()
        if not Systemserverutility.check_whole_flowdocument('Server is ready'):
          ss_obj.actionmenubutton.click()
          ss_obj.startserverbutton.click()
          aqUtils.Delay(1500)
          Systemserverutility.check_server_ready()
      else:
        Log.Enabled = True
        TestedApps.SystemServer.Run()
        login_wait_server_ready()
    except:
      Log.Enabled = True
      Log.Message('System Server is not running')
    Log.Enabled = True
    Applicationutility.wait_in_seconds(3000, 'Wait')
    
def modal_dialog_window_close():
  wait_in_seconds(1000, 'wait')
  try:
    msg_obj.modaldialogwindowtextbox.object.Close()
  except:
    Log.Warning('No Message window to close !')
  
def modal_dialog_window_textbox(param):
  param = default_text, new_text
  wait_in_seconds(1000, 'wait')
  buttons_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  take_screenshot('Taking Screenshot of the Message Window.')
  for text in buttons_list:
    if default_text in str(button.WPFControlText) :
      text.Text = new_text
      Log.Checkpoint('New text : ' + str(button.WPFControlText) + ' is added.')
      take_screenshot('Taking Screenshot of the Message Window.')
      break
  else:
    Log.Warning("Text name mentioned doesnt exists")
