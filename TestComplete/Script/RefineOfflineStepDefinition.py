"""RefineOfflineWorkFlow"""
from RefineOfflineWorkFlow import RefineOfflineWorkFlow
import CommonUtil
import Applicationutility
import Engineeringclientutility

obj=RefineOfflineWorkFlow()

        
@when("I selected Unlock in refine offline")
def step_impl():
    """I selected Unlock in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Unlock in refine offline")
    obj.buttonunlockselected()
  
@when("I Unlock Dialog popup Unlock in refine offline as {arg}")
def step_impl(yes):
    """I Unlock Dialog popup Unlock in refine offline as 'Yes'"""
    CommonUtil.write_text_file("\nWhen I Unlock Dialog popup Unlock in refine offline as 'Yes'")
    obj.buttonunlockunlockdialogpopup(yes)
  
@when("I Delete link Refine Offline Unlock in refine offline as {arg}")
def step_impl(chout):
    """I Delete link Refine Offline Unlock in refine offline as 'ChOut'"""
    CommonUtil.write_text_file("\nWhen I Delete link Refine Offline Unlock in refine offline as 'ChOut'")
    obj.buttonunlockdeletelinkrefineoffline(chout)
  
  
@when("I selected Save Refine Offline in refine offline")
def step_impl():
    """I selected Save Refine Offline in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Save Refine Offline in refine offline")
    obj.buttonsaverefineofflineselected()
    Applicationutility.wait_in_seconds(2000, 'Wait')
  
@when("I selected Consistency Check in refine offline")
def step_impl():
    """I selected Consistency Check in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Consistency Check in refine offline")
    obj.buttonconsistencycheckselected()
  
@when("I Consistency Check Select All Consistency Check in refine offline")
def step_impl():
    """I Consistency Check Select All Consistency Check in refine offline"""
    CommonUtil.write_text_file("\nWhen I Consistency Check Select All Consistency Check in refine offline")
    obj.buttonconsistencycheckconsistencycheckselectall()
  
@when("I Click on export System1 Export Popup AE buttons Consistency Check in refine offline as {arg}")
def step_impl(unlink):
    """I Click on export System1 Export Popup AE buttons Consistency Check in refine offline as 'Unlink'"""
    CommonUtil.write_text_file("\nWhen I Click on export System1 Export Popup AE buttons Consistency Check in refine offline as 'Unlink'")
    obj.buttonconsistencycheckclickonexportsystem1exportpopupaebuttons(unlink)
  
@then("Verify Message from notification panel AE Consistency Check in refine offline as {arg}")
def step_impl(checkConsistencycompleted):
    """Verify Message from notification panel AE Consistency Check in refine offline as 'Check Consistency (Completed)'"""
    CommonUtil.write_text_file("\nThen Verify Message from notification panel AE Consistency Check in refine offline as 'Check Consistency (Completed)'")
    obj.buttonconsistencycheckverifymessagefromnotificationpanelae(checkConsistencycompleted)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify modifications available in Refine Offline Consistency Check in refine offline as {arg}")
def step_impl(xor):
    """Verify modifications available in Refine Offline Consistency Check in refine offline as 'XOR'"""
    CommonUtil.write_text_file("\nThen Verify modifications available in Refine Offline Consistency Check in refine offline as 'XOR'")
    obj.buttonconsistencycheckverifymodificationsavailableinrefineoffline(xor)
    Applicationutility.take_screenshot("Full Screenshot")

    
@when("I RClick on filter Refine Offline MDI Window in refine offline")
def step_impl():
    """I RClick on filter Refine Offline MDI Window in refine offline"""
    CommonUtil.write_text_file("\nWhen I RClick on filter Refine Offline MDI Window in refine offline")
    obj.textboxmdiwindowrclickonfilterrefineoffline()
  
@when("I selected Customize Columns in refine offline")
def step_impl():
    """I selected Customize Columns in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Customize Columns in refine offline")
    obj.buttoncustomizecolumnsselected()
  
@when("I Select Column Configuration Customize Columns in refine offline as {arg}")
def step_impl(constant):
    """I Select Column Configuration Customize Columns in refine offline as 'Constant'"""
    CommonUtil.write_text_file("\nWhen I Select Column Configuration Customize Columns in refine offline as 'Constant'")
    obj.buttoncustomizecolumnsselectcolumnconfiguration(constant)
  

@when("I Add variable name in name column MDI Window in refine offline as {arg}")
def step_impl(mdiWindow1):
    """I Add variable name in name column MDI Window in refine offline as '<MDI Window1>'"""
    CommonUtil.write_text_file("\nWhen I Add variable name in name column MDI Window in refine offline as \""+mdiWindow1+"\"")
    obj.textboxmdiwindowaddvariablenameinnamecolumn(mdiWindow1)
  
@when("I click on ellipsis MDI Window in refine offline")
def step_impl():
    """I click on ellipsis MDI Window in refine offline"""
    CommonUtil.write_text_file("\nWhen I click on ellipsis MDI Window in refine offline")
    obj.textboxmdiwindowclickonellipsis()
  
@when("I selected Type column ellipsis in refine offline")
def step_impl():
    """I selected Type column ellipsis in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Type column ellipsis in refine offline")
    obj.buttontypecolumnellipsisselected()
  
@when("I select variable type Dialog popup CE Type column ellipsis in refine offline")
def step_impl():
    """I select variable type Dialog popup CE Type column ellipsis in refine offline"""
    CommonUtil.write_text_file("\nWhen I select variable type Dialog popup CE Type column ellipsis in refine offline")
    obj.buttontypecolumnellipsisselectvariabletypedialogpopupce()
  
@when("I select Constant check box Type column ellipsis in refine offline")
def step_impl():
    """I select Constant check box Type column ellipsis in refine offline"""
    CommonUtil.write_text_file("\nWhen I select Constant check box Type column ellipsis in refine offline")
    obj.buttontypecolumnellipsisselectconstantcheckbox()
  
@when("I Enter P2P in Custom box MDI Window in refine offline")
def step_impl():
    """I Enter P2P in Custom box MDI Window in refine offline"""
    CommonUtil.write_text_file("\nWhen I Enter P2P in Custom box MDI Window in refine offline")
    obj.textboxmdiwindowenterp2pincustombox()
  
@when("I select variable type MDI Window in refine offline as {arg}")
def step_impl(mdiWindow2):
    """I select variable type MDI Window in refine offline as '<MDI Window2>'"""
    CommonUtil.write_text_file("\nWhen I select variable type MDI Window in refine offline as \""+mdiWindow2+"\"")
    obj.textboxmdiwindowselectvariabletype(mdiWindow2)
  
@when("I selected Manage Network Variables in refine offline")
def step_impl():
    """I selected Manage Network Variables in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Manage Network Variables in refine offline")
    obj.buttonmanagenetworkvariablesselected()
  
@then("Verify variable is removed Refine Offline MDI Window in refine offline as {arg}")
def step_impl(mdiWindow1):
    """Verify variable is removed Refine Offline MDI Window in refine offline as '<MDI Window1>'"""
    CommonUtil.write_text_file("\nThen Verify variable is removed Refine Offline MDI Window in refine offline as \""+mdiWindow1+"\"")
    obj.textboxmdiwindowverifyvariableisremovedrefineoffline(mdiWindow1)
    Applicationutility.take_screenshot("Full Screenshot")  
    
@when("I select Adv Settings properties SVP Project Browser RO in refine offline as {arg}")
def step_impl(projectBrowserRo1):
    """I select Adv Settings properties SVP Project Browser RO in refine offline as '<Project Browser RO1>'"""
    CommonUtil.write_text_file("\nWhen I select Adv Settings properties SVP Project Browser RO in refine offline as \""+projectBrowserRo1+"\"")
    obj.textboxprojectbrowserroselectadvsettingspropertiessvp(projectBrowserRo1)

@when("I Edit Parameter Value AdvSettings SVP Project Browser RO in refine offline as {arg}")
def step_impl(projectBrowserRo2):
    """I Edit Parameter Value AdvSettings SVP Project Browser RO in refine offline as '<Project Browser RO2>'"""
    CommonUtil.write_text_file("\nWhen I Edit Parameter Value AdvSettings SVP Project Browser RO in refine offline as \""+projectBrowserRo2+"\"")
    obj.textboxprojectbrowserroeditparametervalueadvsettingssvp(projectBrowserRo2)
  

    
@when("I selected Close Refine Offline in refine offline")
def step_impl():
    """I selected Close Refine Offline in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Close Refine Offline in refine offline")
    Applicationutility.wait_in_seconds(5000,"Wait")
    obj.buttoncloserefineofflineselected()
    Applicationutility.wait_for_execution()
    Applicationutility.wait_in_seconds(15000, 'Wait')
    
@then("Verify Parameter Value Adv Settings SVP Project Browser RO in refine offline as {arg}")
def step_impl(projectBrowserRo2):
    """Verify Parameter Value Adv Settings SVP Project Browser RO in refine offline as '<Project Browser RO2>'"""
    CommonUtil.write_text_file("\nThen Verify Parameter Value Adv Settings SVP Project Browser RO in refine offline as \""+projectBrowserRo2+"\"")
    obj.textboxprojectbrowserroverifyparametervalueadvsettingssvp(projectBrowserRo2)
    Applicationutility.take_screenshot("Full Screenshot")
    obj.buttoncloserefineofflineselected() 
    Applicationutility.take_screenshot("Full Screenshot")  
    
@when("I edit IP Address in configure MDI Window in refine offline as {arg}")
def step_impl(mdiWindow1):
    """I edit IP Address in configure MDI Window in refine offline as '<MDI Window1>'"""
    CommonUtil.write_text_file("\nWhen I edit IP Address in configure MDI Window in refine offline as \""+mdiWindow1+"\"")
    obj.textboxmdiwindoweditipaddressinconfigure(mdiWindow1)
  
@when("I selected Edit button in menu bar")
def step_impl():
    """I selected Edit button in menu bar"""
    CommonUtil.write_text_file("\nWhen I selected Edit button in menu bar")
    obj.buttoneditbuttonselected()
  
@when("I selected Validate in menu bar")
def step_impl():
    """I selected Validate in menu bar"""
    CommonUtil.write_text_file("\nWhen I selected Validate in menu bar")
    obj.buttonvalidateselected()

@when("I selected Tools button in menu bar")
def step_impl():
    """I selected Tools button in menu bar"""
    CommonUtil.write_text_file("\nWhen I selected Tools button in menu bar")
    obj.buttontoolsbuttonselected()
  
@when("I selected DTM Browser in menu bar")
def step_impl():
    """I selected DTM Browser in menu bar"""
    CommonUtil.write_text_file("\nWhen I selected DTM Browser in menu bar")
    obj.buttondtmbrowserselected()
  
@then("Verify Mapped DTM device present CE Project Browser RO in refine offline as {arg}")
def step_impl(projectBrowserRo1):
    """Verify Mapped DTM device present CE Project Browser RO in refine offline as '<Project Browser RO1>'"""
    CommonUtil.write_text_file("\nThen Verify Mapped DTM device present CE Project Browser RO in refine offline as \""+projectBrowserRo1+"\"")
    obj.textboxprojectbrowserroverifymappeddtmdevicepresentce(projectBrowserRo1)
    Applicationutility.take_screenshot("Full Screenshot")
        
@when("I Navigate through project browser CE Project Browser RO in refine offline as {arg}")
def step_impl(projectBrowserRo1):
    """I Navigate through project browser CE Project Browser RO in refine offline as '<Project Browser RO1>'"""
    CommonUtil.write_text_file("\nWhen I Navigate through project browser CE Project Browser RO in refine offline as \""+projectBrowserRo1+"\"")
    obj.textboxprojectbrowserronavigatethroughprojectbrowserce(projectBrowserRo1)
  
@when("I enterkey Project Browser RO in refine offline")
def step_impl():
    """I enterkey Project Browser RO in refine offline"""
    CommonUtil.write_text_file("When I enterkey Project Browser RO in refine offline")
    obj.textboxprojectbrowserroenterkey()
  
@when("I selected View button in menu bar")
def step_impl():
    """I selected View button in menu bar"""
    CommonUtil.write_text_file("\nWhen I selected View button in menu bar")
    obj.buttonviewbuttonselected()
  
@when("I Rclick Drops EIO add new device CE FBD SectionWindow in refine offline")
def step_impl():
    """I Rclick Drops EIO add new device CE FBD SectionWindow in refine offline"""
    CommonUtil.write_text_file("\nWhen I Rclick Drops EIO add new device CE FBD SectionWindow in refine offline")
    obj.textboxfbdsectionwindowrclickdropseioaddnewdevicece()

@then("verify displayed Project Browser RO in refine offline")
def step_impl():
    """verify displayed Project Browser RO in refine offline"""
    CommonUtil.write_text_file("\nThen verify displayed Project Browser RO in refine offline")
    obj.textboxprojectbrowserroverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify displayed Refine online window in refine offline")
def step_impl():
    """verify displayed Refine online window in refine offline"""
    CommonUtil.write_text_file("\nThen verify displayed Refine online window in refine offline")
    obj.textboxrefineonlinewindowverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Modifications of sections CE FBD SectionWindow in refine offline")
def step_impl():
    """I Modifications of sections CE FBD SectionWindow in refine offline"""
    CommonUtil.write_text_file("\nWhen I Modifications of sections CE FBD SectionWindow in refine offline")
    obj.textboxfbdsectionwindowmodificationsofsectionsce()
  
@then("Verify modifications available in Refine Offline FBD SectionWindow in refine offline")
def step_impl():
    """Verify modifications available in Refine Offline FBD SectionWindow in refine offline"""
    CommonUtil.write_text_file("\nThen Verify modifications available in Refine Offline FBD SectionWindow in refine offline")
    obj.textboxfbdsectionwindowverifymodificationsavailableinrefineoffline()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I wait in seconds Refine online window in refine offline")
def step_impl():
    """I wait in seconds Refine online window in refine offline as '<Refine online window1>'"""
    CommonUtil.write_text_file("\nWhen I wait in seconds Refine online window in refine offline")
    obj.textboxrefineonlinewindowwaitinseconds()
    
@when("I selected Save Refine Offline in refine offline1")
def step_impl():
    """I selected Save Refine Offline in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Save Refine Offline in refine offline")
    obj.buttonsaverefineofflineselected1()
    
@when("I selected select PLC bus combobox item CE in refine offline as {arg}")
def step_impl(PLCbuscomboboxitem):
    """I selected select PLC bus combobox item CE in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected select PLC bus combobox item CE in refine offline as <PLC bus combo box item>")
    obj.buttonselectPLCbuscomboboxitemCE(PLCbuscomboboxitem)
    
@when("I selected create logical network in refine offline")
def step_impl():
    """I selected create logical network in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected create logical network in refine offline")
    obj.buttoncreatelogicalnetwork()   
    Applicationutility.wait_in_seconds(1000,"Wait")
    
@when("I Click on Build and Deploy changes Button in refine online window")
def step_impl():
    """I Click on Build and Deploy changes Button in refine online window"""
    CommonUtil.write_text_file("\nWhen I Click on Build and Deploy changes Button in refine online window")
    obj.clickbuilddeploychangesbutton()   
    Applicationutility.wait_in_seconds(1000,"Wait")
    
@when("I select Initialze Animation Table in refine offline")
def step_impl():
    """I select Initialze Animation Table in refine offline"""
    CommonUtil.write_text_file("\nWhen I select Initialze Animation Table in refine offline")
    obj.initializerefineofflinemenuitemRF()
    
@when("I Click on Modification button after initialization of Animation Table")
def step_impl():
    """I select Initialze Animation Table in refine offline"""
    CommonUtil.write_text_file("\nWhen I select Initialze Animation Table in refine offline")
    obj.modificationbuttonrefineofflineRF()
    
@when("I checked IODDT CE in elemetary variables")
def step_impl():
    """I checked IODDT CE in elemetary variables"""
    CommonUtil.write_text_file("\nWhen I checked IODDT CE in elemetary variables")
    obj.checkboxioddtcechecked()
  
@when("I checked Device DDT CE in elemetary variables")
def step_impl():
    """I checked Device DDT CE in elemetary variables"""
    CommonUtil.write_text_file("\nWhen I checked Device DDT CE in elemetary variables")
    obj.checkboxdeviceddtcechecked()
  
@when("I selected Access to unmapped hardware CE in refine offline")
def step_impl():
    """I selected Access to unmapped hardware CE in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Access to unmapped hardware CE in refine offline")
    obj.buttonaccesstounmappedhardwareceselected()
  
@when("I selected Device DDT popup moveall CE in elemetary variables")
def step_impl():
    """I selected Device DDT popup moveall CE in elemetary variables"""
    CommonUtil.write_text_file("\nWhen I selected Device DDT popup moveall CE in elemetary variables")
    obj.buttondeviceddtpopupmoveallceselected()