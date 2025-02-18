"""EngineeringClientWorkFlow"""
from EngineeringClientWorkFlow import EngineeringClientWorkFlow
import CommonUtil
import Applicationutility
import Systemserverutility
import Engineeringclientutility


obj=EngineeringClientWorkFlow()


       
@when("I launch Engineering Client Engineering client in engineering client")
def step_impl():
    """I launch Engineering Client Engineering client in engineering client"""
    CommonUtil.write_text_file("\nWhen I launch Engineering Client Engineering client in engineering client")
    obj.buttonengineeringclientlaunchengineeringclient()
  
@then("verify displayed Launch Engineering Client in engineering client")
def step_impl():
    """verify displayed Launch Engineering Client in engineering client"""
    CommonUtil.write_text_file("\nThen verify displayed Launch Engineering Client in engineering client")
    obj.buttonlaunchengineeringclientverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify content System explorer window in engineering client as {arg}")
def step_impl(systemExplorerWindow1):
    """verify content System explorer window in engineering client as '<System explorer window1>'"""
    CommonUtil.write_text_file("\nThen verify content System explorer window in engineering client as \""+systemExplorerWindow1+"\"")
    obj.textboxsystemexplorerwindowverifycontent(systemExplorerWindow1)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify displayed Engineering Client Dialogue Box in engineering client")
def step_impl():
    """verify displayed Engineering Client Dialogue Box in engineering client"""
    CommonUtil.write_text_file("\nThen verify displayed Engineering Client Dialogue Box in engineering client")
    obj.buttonengineeringclientdialogueboxverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
        
@when("I open Engineering Client Launch Engineering Client in engineering client")
def step_impl():
    """I open Engineering Client Launch Engineering Client in engineering client"""
    CommonUtil.write_text_file("\nWhen I open Engineering Client Launch Engineering Client in engineering client")
    obj.buttonlaunchengineeringclientopenengineeringclient()
          

  
@when("I selected User dropdown in engineering client")
def step_impl():
    """I selected User dropdown in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected User dropdown in engineering client")
    obj.buttonuserdropdownselected()
  
@when("I selected User lock in engineering client")
def step_impl():
    """I selected User lock in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected User lock in engineering client")
    obj.buttonuserlockselected()
  
@when("I entered password in login page ec as {arg}")
def step_impl(password1):
    """I entered password in login page ec as '<password1>'"""
    CommonUtil.write_text_file("\nWhen I entered password in login page ec as \""+password1+"\"")
    obj.textboxpasswordentered(password1)
  
@when("I selected Log in in login page ec")
def step_impl():
    """I selected Log in in login page ec"""
    CommonUtil.write_text_file("\nWhen I selected Log in in login page ec")
    obj.buttonloginselected()
  
@then("verify displayed Open System Explorer in engineering client")
def step_impl():
    """verify displayed Open System Explorer in engineering client"""
    CommonUtil.write_text_file("\nThen verify displayed Open System Explorer in engineering client")
    obj.buttonopensystemexplorerverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify displayed Engineering client in engineering client")
def step_impl():
    """verify displayed Engineering client in engineering client"""
    CommonUtil.write_text_file("\nThen verify displayed Engineering client in engineering client")
    obj.buttonengineeringclientverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected User logout in engineering client")
def step_impl():
    """I selected User logout in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected User logout in engineering client")
    obj.buttonuserlogoutselected()

@then("verify displayed log in to use the client in engineering client")
def step_impl():
    """verify displayed log in to use the client in engineering client"""
    CommonUtil.write_text_file("\nThen verify displayed log in to use the client in engineering client")
    obj.textboxVerifyLogout()
    Applicationutility.take_screenshot("Full Screenshot")
     
@when("I selected User login in engineering client")
def step_impl():
    """I selected User login in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected User login in engineering client")
    obj.buttonuserloginselected()
  
@when("I entered User name in login page ec as {arg}")
def step_impl(userName1):
    """I entered User name in login page ec as '<User name1>'"""
    CommonUtil.write_text_file("\nWhen I entered User name in login page ec as \""+userName1+"\"")
    obj.textboxusernameentered(userName1)
  
@then("verify content Notification panel in engineering client")
def step_impl():
    """verify content Notification panel in engineering client"""
    CommonUtil.write_text_file("\nThen verify content Notification panel in engineering client")
    obj.windownotificationpanelverifycontent()

    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Close EC in engineering client")
def step_impl():
    """I selected Close EC in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected Close EC in engineering client")
    obj.buttoncloseecselected()
  
@then("verify content dialogue box in login page ec as {arg}")
def step_impl(dialogueBox3):
    """verify content dialogue box in login page ec as '<dialogue box3>'"""
    CommonUtil.write_text_file("\nThen verify content dialogue box in login page ec as \""+dialogueBox3+"\"")
    obj.textboxdialogueboxverifycontent(dialogueBox3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I terminate engineering client Log in in login page ec")
def step_impl():
    """I terminate engineering client Log in in login page ec"""
    CommonUtil.write_text_file("\nWhen I terminate engineering client Log in in login page ec")
    obj.buttonloginterminateengineeringclient()
  
@when("I selected Open Global Templates Explorer in engineering client")
def step_impl():
    """I selected Open Global Templates Explorer in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected Open Global Templates Explorer in engineering client")
    obj.buttonopenglobaltemplatesexplorerselected()
  
@when("I selected Open System Explorer in engineering client")
def step_impl():
    """I selected Open System Explorer in engineering client"""
    CommonUtil.write_text_file("\nWhen I selected Open System Explorer in engineering client")
    obj.buttonopensystemexplorerselected()
    
@when("login and terminate EC")
def step_impl():
    """login and terminate EC"""
    Engineeringclientutility.login_terminate_ec()
  
@when("login with password and terminate EC")
def step_impl():
    """login and terminate EC"""
    Engineeringclientutility.login_password_terminate_ec()

@when("explorer tab is not Systems Explorer then Navigate")
def step_impl():
    Systemserverutility.Pre_Condition_Navigation_SE()
    Applicationutility.take_screenshot("Full Screenshot")
    
@then("I Verify the contents of the drop down")
def step_impl():
    """I Verify the contents of the drop down"""
    CommonUtil.write_text_file("\nThen I Verify the contents of the drop down")
    obj.textboxVerifyDropdownoptions()
    Applicationutility.take_screenshot("Full Screenshot")   
    
@when("I clicked Enter in keyboard shortcut")
def step_impl():
    """I Verify the contents of the drop down"""
    CommonUtil.write_text_file("\nThen I Verify the contents of the drop down")
    obj.keyboardactionenter()
    
@when("I Close tab items EC main screen in engineering client as {arg}")
def step_impl(compacthwgp1):
    """I Close tab items EC main screen in engineering client as 'CompactHWGP_1'"""
    CommonUtil.write_text_file("\nWhen I Close tab items EC main screen in engineering client as 'CompactHWGP_1'")
    obj.buttonmainscreenclosetabitemsec(compacthwgp1)    

    
@when("I Close the Tab by Clicking on Close as {arg}")
def step_impl(tabname):
    """I Close the Tab by Clicking on Close as '<tabname>''"""
    CommonUtil.write_text_file("\nWhen I Close the Tab by Clicking on Close as \""+tabname+"\"")
    obj.closetabitemec(tabname)
    
@when("I Perform action on the Folder by Clicking on {arg} in Topology Explorer")
def step_impl(button):
    """I Close the Folder by Clicking on '<button>' in Topology Explorer"""
    obj.OpenClosefolderTE(button)
    
@then("I Verify Folder Renamed as {arg} in Topology Explorer is Expanded")
def step_impl(FolderName):
    """I Verify Folder Renamed as '<FolderName>' in Topology Explorer is Expanded"""
    obj.VerifyFolderExpansionstatusTE(FolderName)
    
@when("I Close the Tab by Clicking on Close in EC as {arg}")
def step_impl(tabname):
    """I Close the Tab by Clicking on Close in EC as '<tabname>''"""
    CommonUtil.write_text_file("\nWhen I Close the Tab by Clicking on Close in EC as \""+tabname+"\"")
    obj.closetabec(tabname)
    
@when("I update the report details with {arg}, {arg}, {arg}, {arg}, {arg}, {arg}, {arg}, {arg}")
def step_impl(customer_name, site_name, report_desc, report_author, page_size, orientation, report_footer, report_header):
    """I update the report details with '<customer_name>', '<site_name>', '<report_desc>', '<report_author>', '<page_size>', '<orientation>', '<report_footer>', '<report_header>'"""
    CommonUtil.write_text_file(f"\nWhen I update the report details with '{customer_name}', '{site_name}', '{report_desc}', '{report_author}', '{page_size}', '{orientation}', '{report_footer}', '{report_header}'")
    obj.updatereport(customer_name, site_name, report_desc, report_author, page_size, orientation, report_footer, report_header)