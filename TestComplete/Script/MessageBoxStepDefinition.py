"""MessageBoxWorkFlow"""
from MessageBoxWorkFlow import MessageBoxWorkFlow
import CommonUtil
import Applicationutility
import Applicationexplorertabutility

obj=MessageBoxWorkFlow()

        
@when("I Check for license management window in License Management pop up in message box")
def step_impl():
    """I Check for license management window in License Management pop up in message box"""
    CommonUtil.write_text_file("\nWhen I Check for license management window in License Management pop up in message box")
    obj.buttonlicensemanagementpopupcheckforlicensemanagementwindowin()
  
@when("I Click on OK button from License Management OK in message box")
def step_impl():
    """I Click on OK button from License Management OK in message box"""
    CommonUtil.write_text_file("\nWhen I Click on OK button from License Management OK in message box")
    obj.buttonlicensemanagementokclickonokbuttonfrom()
  
@when("I Check Eco Struxure Control Expert in trail license popup in message box")
def step_impl():
    """I Check Eco Struxure Control Expert in trail license popup in message box"""
    CommonUtil.write_text_file("\nWhen I Check Eco Struxure Control Expert in trail license popup in message box")
    obj.buttontraillicensepopupcheckecostruxurecontrolexpertin()
  
@when("I Click on Enter License Management pop up in message box")
def step_impl():
    """I Click on Enter License Management pop up in message box"""
    CommonUtil.write_text_file("\nWhen I Click on Enter License Management pop up in message box")
    obj.buttonlicensemanagementpopupclickonenter()
  
@then("Verify Rename Warning Message Rename Pop up in message box as {arg}")
def step_impl(renamePopUp2):
    """Verify Rename Warning Message Rename Pop up in message box as '<Rename Pop up2>'"""
    CommonUtil.write_text_file("\nThen Verify Rename Warning Message Rename Pop up in message box as \""+renamePopUp2+"\"")
    obj.textboxrenamepopupverifyrenamewarningmessage(renamePopUp2)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Rename Pop up Ok in message box")
def step_impl():
    """I selected Rename Pop up Ok in message box"""
    CommonUtil.write_text_file("\nWhen I selected Rename Pop up Ok in message box")
    obj.buttonrenamepopupokselected()
  
@then("Verify Rename Warning Pop up Rename Pop up in message box as {arg}")
def step_impl(renamePopUp):
    """Verify Rename Warning Pop up Rename Pop up in message box as '<Rename Pop up>'"""
    CommonUtil.write_text_file("\nThen Verify Rename Warning Pop up Rename Pop up in message box as \""+renamePopUp+"\"")
    obj.textboxrenamepopupverifyrenamewarningpopup(renamePopUp)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Click on Ok from Rename Warning Pop up Rename Pop up in message box as {arg}")
def step_impl(renamePopUp2):
    """I Click on Ok from Rename Warning Pop up Rename Pop up in message box as '<Rename Pop up2>'"""
    CommonUtil.write_text_file("\nWhen I Click on Ok from Rename Warning Pop up Rename Pop up in message box as \""+renamePopUp2+"\"")
    obj.textboxrenamepopupclickonokfromrenamewarningpopup(renamePopUp2)
  
@when("I close ec popup Rename Pop up in message box as {arg}")
def step_impl(renamePopUp2):
    """I close ec popup Rename Pop up in message box as '<Rename Pop up2>'"""
    CommonUtil.write_text_file("\nWhen I close ec popup Rename Pop up in message box as \""+renamePopUp2+"\"")
    obj.textboxrenamepopupcloseecpopup(renamePopUp2)
  
@then("verify delete Popup AE Delete popup in message box as {arg}")
def step_impl(areYouSureYouWantToDelete):
    """verify delete Popup AE Delete popup in message box as 'Are you sure you want to delete'"""
    CommonUtil.write_text_file("\nThen verify delete Popup AE Delete popup in message box as 'Are you sure you want to delete'")
    obj.buttondeletepopupverifydeletepopupae(areYouSureYouWantToDelete)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Click on buttons in popup window Delete popup in message box as {arg}")
def step_impl(yes):
    """I Click on buttons in popup window Delete popup in message box as 'Yes'"""
    CommonUtil.write_text_file("\nWhen I Click on buttons in popup window Delete popup in message box as 'Yes'")
    obj.buttondeletepopupclickonbuttonsinpopupwindow(yes)
  
@then("Verify Action message in notification pannel Delete popup in message box as {arg}")
def step_impl(deleteInstance):
    """Verify Action message in notification pannel Delete popup in message box as 'Delete Instance'"""
    CommonUtil.write_text_file("\nThen Verify Action message in notification pannel Delete popup in message box as 'Delete Instance'")
    obj.buttondeletepopupverifyactionmessageinnotificationpannel(deleteInstance)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Enter File Name and File Location in Export Window AE Export in ec windows explorer as {arg}")
def step_impl(csv):
    """I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.csv'"""
    CommonUtil.write_text_file("\nWhen I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.csv'")
    obj.buttonexportenterfilenameandfilelocationinexportwindowae(csv)
  
@when("I Click on Button in AE Explorer Window Export in ec windows explorer as {arg}")
def step_impl(save):
    """I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'"""
    CommonUtil.write_text_file("\nWhen I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'")
    obj.buttonexportclickonbuttoninaeexplorerwindow(save)
   
@when("I Click on Button in TE Explorer Window Export in ec windows explorer as {arg}")
def step_impl(save):
    """I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'"""
    CommonUtil.write_text_file("\nWhen I Click on Button in AE Explorer Window Export in ec windows explorer as 'Save'")
    Applicationexplorertabutility.Explorer_buttons_TE(save) 

  
@then("Verify export_System1_Export_Popup_AE Export in ec windows explorer as {arg}")
def step_impl(areYouSureYouWantToContinue):
    """Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Are you sure you want to continue'"""
    CommonUtil.write_text_file("\nThen Verify export_System1_Export_Popup_AE Export in ec windows explorer as 'Are you sure you want to continue'")
    obj.buttonexportverifyexportsystem1exportpopupae(areYouSureYouWantToContinue)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Click on export System1 Export Popup AE buttons Export in ec windows explorer as {arg}")
def step_impl(ok):
    """I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'"""
    CommonUtil.write_text_file("\nWhen I Click on export System1 Export Popup AE buttons Export in ec windows explorer as 'OK'")
    obj.buttonexportclickonexportsystem1exportpopupaebuttons(ok)
  
@then("Verify Extracted Template CSV Data and Template Details Export in ec windows explorer")
def step_impl():
    """Verify Extracted Template CSV Data and Template Details Export in ec windows explorer"""
    CommonUtil.write_text_file("\nThen Verify Extracted Template CSV Data and Template Details Export in ec windows explorer")
    obj.buttonexportverifyextractedtemplatecsvdataandtemplatedetails()
    Applicationutility.take_screenshot("Full Screenshot")
  
#@when("I Enter File Name and File Location in Export Window AE Export in ec windows explorer as {arg}")
#def step_impl(xml):
#    """I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.xml'"""
#    CommonUtil.write_text_file("\nWhen I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '.xml'")
#    obj.buttonexportenterfilenameandfilelocationinexportwindowae(xml)
  
@then("Verify Extracted Template XML Data and Template Details Export in ec windows explorer")
def step_impl():
    """Verify Extracted Template XML Data and Template Details Export in ec windows explorer"""
    CommonUtil.write_text_file("\nThen Verify Extracted Template XML Data and Template Details Export in ec windows explorer")
    obj.buttonexportverifyextractedtemplatexmldataandtemplatedetails()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify Message from notification panel AE Notification Pannel in message box")
def step_impl():
    obj.textboxnotificationpannelverifymessagefromnotificationpanelae()
    Applicationutility.take_screenshot("Full Screenshot")
    

@when("I Right click on variable Manage Network Variables in message box as {arg}")
def step_impl(manageNetworkVariables1):
    """I Right click on variable Manage Network Variables in message box as '<Manage Network Variables1>'"""
    CommonUtil.write_text_file("\nWhen I Right click on variable Manage Network Variables in message box as \""+manageNetworkVariables1+"\"")
    obj.textboxmanagenetworkvariablesrightclickonvariable(manageNetworkVariables1) 
    
@when("I Add new text modal dialog window Modal dialog window in message box as {arg}")
def step_impl(modalDialogWindow1):
    """I Add new text modal dialog window Modal dialog window in message box as '<Modal dialog window1>'"""
    CommonUtil.write_text_file("\nWhen I Add new text modal dialog window Modal dialog window in message box as \""+modalDialogWindow1+"\"")
    obj.textboxmodaldialogwindowaddnewtextmodaldialogwindow(modalDialogWindow1)
  
@when("I click modal dialog window Modal dialog window in message box as {arg}")
def step_impl(modalDialogWindow2):
    """I click modal dialog window Modal dialog window in message box as '<Modal dialog window2>'"""
    CommonUtil.write_text_file("\nWhen I click modal dialog window Modal dialog window in message box as \""+modalDialogWindow2+"\"")
    obj.textboxmodaldialogwindowclickmodaldialogwindow(modalDialogWindow2)
    
@when("I select ip adress from deploy project build TE Modal dialog window in message box as {arg}")
def step_impl(modalDialogWindow5):
    """I select ip adress from deploy project build TE Modal dialog window in message box as '<Modal dialog window5>'"""
    CommonUtil.write_text_file("\nWhen I select ip adress from deploy project build TE Modal dialog window in message box as \""+modalDialogWindow5+"\"")
    Applicationutility.wait_in_seconds(10000,"Wait")
    obj.textboxmodaldialogwindowselectipadressfromdeployprojectbuildte(modalDialogWindow5)
  
@when("I click modal dialog window Modal Dialog Window 1 in message box as {arg}")
def step_impl(modalDialogWindow16):
    """I click modal dialog window Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'"""
    CommonUtil.write_text_file("\nWhen I click modal dialog window Modal Dialog Window 1 in message box as \""+modalDialogWindow16+"\"")
    obj.textboxmodaldialogwindowclickmodaldialogwindow(modalDialogWindow16)

@when("I Click popup button object Modal Dialog Window 1 in message box as {arg}")
def step_impl(modalDialogWindow16):
    """I Click popup button object Modal Dialog Window 1 in message box as '<Modal Dialog Window 16>'"""
    CommonUtil.write_text_file("\nWhen I Click popup button object Modal Dialog Window 1 in message box as \""+modalDialogWindow16+"\"")
    obj.textboxmodaldialogwindow1clickpopupbuttonobject(modalDialogWindow16)
    
@then("Verify modal dialog window text Modal Dialog Window 1 in message box as {arg}")
def step_impl(modalDialogWindow15):
    """Verify modal dialog window text Modal Dialog Window 1 in message box as '<Modal Dialog Window 15>'"""
    CommonUtil.write_text_file("\nThen Verify modal dialog window text Modal Dialog Window 1 in message box as \""+modalDialogWindow15+"\"")
    obj.textboxmodaldialogwindow1verifymodaldialogwindowtext(modalDialogWindow15)
    Applicationutility.take_screenshot("Full Screenshot")
    
@then("Verify notification panel message Notification Pannel in message box as {arg}")
def step_impl(notificationPannel7):
    """Verify notification panel message Notification Pannel in message box as '<Notification Pannel7>'"""
    CommonUtil.write_text_file("\nThen Verify notification panel message Notification Pannel in message box as \""+notificationPannel7+"\"")
    obj.textboxnotificationpannelverifynotificationpanelmessage(notificationPannel7)
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@when("I Click on OK button from Reconfirm Deploy Built Project Popup window")
def step_impl():
    """I Click on OK button from Reconfirm Deploy Built Project Popup window"""
    CommonUtil.write_text_file("\nWhen I Click on OK button from Reconfirm Deploy Built Project Popup window")
    obj.clickokfromdbppopupwindow()
    
@when("I Click button Message Window Modification popup in message box as {arg}")
def step_impl(modificationPopup3):
    """I Click button Message Window Modification popup in message box as '<Modification popup3>'"""
    CommonUtil.write_text_file("\nWhen I Click button Message Window Modification popup in message box as \""+modificationPopup3+"\"")
    obj.textboxmodificationpopupclickbuttonmessagewindow(modificationPopup3)
  
@then("Verify forgot password Authentication Code Export popup in message box")
def step_impl():
    """Verify forgot password Authentication Code Export popup in message box"""
    CommonUtil.write_text_file("\nThen Verify forgot password Authentication Code Export popup in message box")
    obj.buttonexportpopupverifyforgotpasswordauthenticationcode()
    Applicationutility.take_screenshot("Full Screenshot")
    
    
@when("I Click on Open button from Import TE window")
def step_impl():
    """I Click on Open button from Import TE window"""
    CommonUtil.write_text_file("\nWhen I Click on Open button from Import TE window")
    obj.clickopenimporttewindow()
    
@when("I checked header cb in message box")
def step_impl():
    """I checked header cb in message box"""
    CommonUtil.write_text_file("\nWhen I checked header cb in message box")
    obj.checkboxheadercbchecked()
    
@when("I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '(.*)' with format '(.*)'")
def step_impl(file_name, file_format):
  """I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '<file_name>' with format '<file_format>'"""
  CommonUtil.write_text_file(
    f"\nWhen I Enter File Name and File Location in Export Window AE Export in ec windows explorer as '{file_name}' with format '{file_format}'"
  )
  obj.export_file_from_ae_explorer_window(file_name, file_format)

