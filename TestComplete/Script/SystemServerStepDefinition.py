"""SystemServerWorkFlow"""
from SystemServerWorkFlow import SystemServerWorkFlow
import CommonUtil
import Applicationutility
import Applicationexplorertabutility
import Engineeringclientutility

obj=SystemServerWorkFlow()

@then("Verify that the User Login Dialogue window appeared")
def step_impl():
    """Verify that the User Login Dialogue window appeared"""
    CommonUtil.write_text_file("\nVerify that the User Login Dialogue window appeared")
    obj.verifylogindialogue()
    
@then("Verify that the User has no Server Admin rights")
def step_impl():
    """Verify that the User has no Server Admin rights"""
    CommonUtil.write_text_file("\nVerify that the User has no Server Admin rights")
    obj.buttonverifystartstopdisabled()
        
@when("I entered User name in login page as {arg}")
def step_impl(userName1):
    """I entered User name in login page as '<User name1>'"""
    CommonUtil.write_text_file("\nWhen I entered User name in login page as \""+userName1+"\"")
    obj.textboxusernameentered(userName1)
  
@when("I entered Password in login page as {arg}")
def step_impl(password2):
    """I entered Password in login page as '<Password2>'"""
    CommonUtil.write_text_file("\nWhen I entered Password in login page as \""+password2+"\"")
    obj.textboxpasswordentered(password2)
  
@when("I selected Log In in login page")
def step_impl():
    """I selected Log In in login page"""
    CommonUtil.write_text_file("\nWhen I selected Log In in login page")
    obj.buttonloginselected()
  
@when("I selected Action Menu in action")
def step_impl():
    """I selected Action Menu in action"""
    CommonUtil.write_text_file("\nWhen I selected Action Menu in action")
    obj.buttonactionmenuselected()
    
@when("I click on tab and enter")
def step_impl():
    """I click on tab and enter"""
    CommonUtil.write_text_file("\nI click on tab and enter")
    obj.buttonClickonTabEnter()
  
@when("I selected Start server in action")
def step_impl():
    """I selected Start server in action"""
    CommonUtil.write_text_file("\nWhen I selected Start server in action")
    obj.buttonstartserverselected()
    
@when("I selected Stop server in action")
def step_impl():
    """I selected Stop server in action"""
    CommonUtil.write_text_file("\nWhen I selected Stop server in action")
    obj.buttonstopserverselected()
  
@then("verify system server ready Flow document in server console")
def step_impl():
    """verify system server ready Flow document in server console"""
    CommonUtil.write_text_file("\nThen verify system server ready Flow document in server console")
    obj.buttonflowdocumentverifysystemserverready()
    Applicationutility.take_screenshot("Full Screenshot")
    
@then("verify system server stopped from Flow document in server console")
def step_impl():
    """verify system server stopped from Flow document in server console"""
    CommonUtil.write_text_file("\nverify system server stopped from Flow document in server console")
    obj.buttonflowdocumentverifysystemserverstop()
    Applicationutility.take_screenshot("Full Screenshot")
    

  
@then("screen is displayed with {arg}")
def step_impl(content):
    """screen is displayed with '(.*)'"""
    CommonUtil.write_text_file("\nThen screen is displayed with \""+content+"\"")
    obj.labelmessagedisplayed(content)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify content Log On Dialogue in login page as {arg}")
def step_impl(logOnDialogue3):
    """verify content Log On Dialogue in login page as '<Log On Dialogue3>'"""
    CommonUtil.write_text_file("\nThen verify content Log On Dialogue in login page as \""+logOnDialogue3+"\"")
    obj.textboxlogondialogueverifycontent(logOnDialogue3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify text in system server console Console in server console as {arg}")
def step_impl(console4):
    """verify text in system server console Console in server console as '<Console4>'"""
    CommonUtil.write_text_file("\nThen verify text in system server console Console in server console as \""+console4+"\"")
    obj.windowconsoleverifytextinsystemserverconsole(console4)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I select from system server icon Console in server console as {arg}")
def step_impl(console5):
    """I select from system server icon Console in server console as '<Console5>'"""
    CommonUtil.write_text_file("\nWhen I select from system server icon Console in server console as \""+console5+"\"")
    obj.windowconsoleselectfromsystemservericon(console5)
  
@when("I selected Console in server console as {arg}")
def step_impl(console):
    """I selected Console in server console as '<Console>'"""
    CommonUtil.write_text_file("\nWhen I selected Console in server console as \""+console+"\"")
    obj.windowconsoleselected(console)
  
@then("verify license in system server Console in server console")
def step_impl():
    """verify license in system server Console in server console"""
    CommonUtil.write_text_file("\nThen verify license in system server Console in server console")
    obj.windowconsoleverifylicenseinsystemserver()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I start system server Log In in login page")
def step_impl():
    """I start system server Log In in login page"""
    CommonUtil.write_text_file("\nWhen I start system server Log In in login page")
    obj.buttonloginstartsystemserver()
  
@when("I selected Settings Menu in settings")
def step_impl():
    """I selected Settings Menu in settings"""
    CommonUtil.write_text_file("\nWhen I selected Settings Menu in settings")
    obj.buttonsettingsmenuselected()
  
@when("I selected Basic settings in settings")
def step_impl():
    """I selected Basic settings in settings"""
    CommonUtil.write_text_file("\nWhen I selected Basic settings in settings")
    obj.buttonbasicsettingsselected()
  
@when("I selected next in system server config wizard")
def step_impl():
    """I selected next in system server config wizard"""
    CommonUtil.write_text_file("\nWhen I selected next in system server config wizard")
    obj.buttonnextselected()
  
@when("I entered Control Participant Max Instance in system server config wizard as {arg}")
def step_impl(controlParticipantMaxInstance3):
    """I entered Control Participant Max Instance in system server config wizard as '<Control Participant Max Instance3>'"""
    CommonUtil.write_text_file("\nWhen I entered Control Participant Max Instance in system server config wizard as \""+controlParticipantMaxInstance3+"\"")
    obj.textboxcontrolparticipantmaxinstanceentered(controlParticipantMaxInstance3)
  
@when("I selected save and close in system server config wizard")
def step_impl():
    """I selected save and close in system server config wizard"""
    CommonUtil.write_text_file("\nWhen I selected save and close in system server config wizard")
    obj.buttonsaveandcloseselected()
  
@then("verify system server ready Console in server console")
def step_impl():
    """verify system server ready Console in server console"""
    CommonUtil.write_text_file("\nThen verify system server ready Console in server console")
    obj.buttonflowdocumentverifysystemserverready()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify number of control instances Console in server console as {arg}")
def step_impl(console4):
    """verify number of control instances Console in server console as '<Console4>'"""
    CommonUtil.write_text_file("\nThen verify number of control instances Console in server console as \""+console4+"\"")
    obj.windowconsoleverifynumberofcontrolinstances(console4)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I start system server User name in login page as {arg}")
def step_impl(userName1):
    """I start system server User name in login page as '<User name1>'"""
    CommonUtil.write_text_file("\nWhen I start system server User name in login page as \""+userName1+"\"")
    obj.buttonloginstartsystemserver(userName1)
  
@when("I selected hosting in system server config wizard")
def step_impl():
    """I selected hosting in system server config wizard"""
    CommonUtil.write_text_file("\nWhen I selected hosting in system server config wizard")
    obj.buttonhostingselected()
  
@then("verify invalid control instance in hosting Control Participant Max Instance in system server config wizard")
def step_impl():
    """verify invalid control instance in hosting Control Participant Max Instance in system server config wizard"""
    CommonUtil.write_text_file("\nThen verify invalid control instance in hosting Control Participant Max Instance in system server config wizard")
    obj.textboxcontrolparticipantmaxinstanceverifyinvalidcontrolinstanceinhosting()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected cancel in system server config wizard")
def step_impl():
    """I selected cancel in system server config wizard"""
    CommonUtil.write_text_file("\nWhen I selected cancel in system server config wizard")
    obj.buttoncancelselected()
  
@when("I terminate all tested apps hosting in system server config wizard")
def step_impl():
    """I terminate all tested apps hosting in system server config wizard"""
    CommonUtil.write_text_file("\nWhen I terminate all tested apps hosting in system server config wizard")
    obj.buttonhostingterminatealltestedapps()
  
@then("verify disabled Start server in action")
def step_impl():
    """verify disabled Start server in action"""
    CommonUtil.write_text_file("\nThen verify disabled Start server in action")
    obj.buttonstartserververifydisabled()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Delete The folder/System Created in systems explorer")
def step_impl():
  CommonUtil.write_text_file("\nDelete The folder/System Created in systems explorer")
  Applicationexplorertabutility.delete_all_files_Post_Condition()
  Applicationutility.take_screenshot("Full Screenshot")

  
@when("Checks for system and creates if absent")
def step_impl():
  Engineeringclientutility.checks_system_create_system()
  
  
@when("Checks for folder and creates if absent")
def step_impl(): 
  Engineeringclientutility.checks_folder_create_folder()
  
@when("I click on Username dropdown")
def step_impl():
    """I click on Username dropdown"""
    CommonUtil.write_text_file("\nWhen I click on Username dropdown")
    obj.usernamedropdown()
    
@when("I click on menuItem option from usericon as {arg}")
def step_impl(param):
    """I click on menuItem option from usericon as '<param>'"""
    CommonUtil.write_text_file("\nAnd I click on menuItem option from usericon")
    obj.SSlogout(param)
    
@when("I click on Login option")
def step_impl():
    """I click on Login option"""
    CommonUtil.write_text_file("\nAnd I click on Login option")
    obj.SSlogin()
    
@when("I press Ctrl+M {arg}")
def step_impl(mode):
    """I press Ctrl+M '<mode>'"""
    CommonUtil.write_text_file("\nWhen I press Ctrl+M")
    obj.maintenancemode(mode)
    
@when("I enter the Maintenance mode Password {arg} and press Enter key {arg}")
def step_impl(password, key):
    """And I enter the Maintenance mode Password '<password>'and press Enter key '<key>'"""
    CommonUtil.write_text_file("\nAnd I enter the Maintenance mode Password and press Enter key")
    obj.entermaintenancepassword(password, key)
    
@when("I enter {arg} and press Enter key {arg}")
def step_impl(command, key):
    """And I enter '<command>' and press Enter key '<key>'"""
    CommonUtil.write_text_file("\nAnd I enter command and press Enter key")
    obj.databasedeleteall(command, key)
    
@when("I selected {arg} in settings")
def step_impl(option):
  CommonUtil.write_text_file(f'I selected {option} in settings')
  obj.selectoptioninserversettings(option)
  Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected {arg} in System Backup Sheduler window")
def step_impl(system):
  CommonUtil.write_text_file(f'I Selected {system} in System Backup Sheduler window')
  obj.selectoptioninsystembackupshedulerdropdown(system)
  Applicationutility.take_screenshot("Full Screenshot")
  
@when("I click {arg} Checkbox in System Backup Sheduler window")
def step_impl(prop):
  CommonUtil.write_text_file(f'I Click {prop} Checkbox in System Backup Sheduler window')
  obj.checkboxsystembackupsheduler(prop)
  Applicationutility.take_screenshot("Full Screenshot")
  
@when("I select {arg} from the Frequency dropdown in the System Backup Scheduler window")
def step_impl(freq):
  CommonUtil.write_text_file(f'I select {freq} from the Frequency dropdown in the System Backup Scheduler window')
  obj.selectfreqbackupsheduler(freq)
  Applicationutility.take_screenshot("Full Screenshot")
  
@when("I click on Save button in System Backup Scheduler window")
def step_impl():
  CommonUtil.write_text_file(f'I click on Save button in System Backup Scheduler window')
  obj.systembackupsavebuttonselected()
  Applicationutility.take_screenshot("Full Screenshot")
  
@when("I click on {arg} in Confirmation popup window")
def step_impl(button):
  CommonUtil.write_text_file(f'I click on {button} in Confirmation popup window')
  obj.confiramtionpopup(button)
  Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Click on Button in Save as windows explorer as {arg}")
def step_impl(button):
    """I Click on Button in Save as windows explorer as '<button>'"""
    CommonUtil.write_text_file(f"\nWhen I Click on Button in Save as windows explorer as {button}")
    obj.saveaswindowbutton(button)
    
@when("I Click CheckBox in System backup Window as {arg}")
def step_impl(prop):
    """I Click CheckBox in System backup Window as '<prop>'"""
    CommonUtil.write_text_file(f"\nWhen I Click CheckBox in System backup Window as {prop}")
    obj.backupwindowcheckbox(prop)
    
@when("I Click on Button in Back up  window as {arg}")
def step_impl(button):
    """I Click on Button in Back up  window as '<button>'"""
    CommonUtil.write_text_file(f"\nWhen I Click on Button in Back up  window as {button}")
    obj.backupwindowbutton(button)
