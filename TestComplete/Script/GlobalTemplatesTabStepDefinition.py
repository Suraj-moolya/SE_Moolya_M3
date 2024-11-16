"""GlobalTemplatesTabWorkFlow"""
from GlobalTemplatesTabWorkFlow import GlobalTemplatesTabWorkFlow
import CommonUtil
import Applicationutility
import Globaltemplatesutility
import Engineeringclientutility
obj=GlobalTemplatesTabWorkFlow()

        
@when("I Search text and select GTE global template search in global template explorer as {arg}")
def step_impl(globalTemplateSearch1):
    """I Search text and select GTE global template search in global template explorer as '<global template search1>'"""
    CommonUtil.write_text_file("\nWhen I Search text and select GTE global template search in global template explorer as \""+globalTemplateSearch1+"\"")
    obj.textboxglobaltemplatesearchsearchtextandselectgte(globalTemplateSearch1)
  
@when("I right click on the searched template GTE global template core in global template explorer as {arg}")
def step_impl(globalTemplateCore2):
    """I right click on the searched template GTE global template core in global template explorer as '<global template core2>'"""
    CommonUtil.write_text_file("\nWhen I right click on the searched template GTE global template core in global template explorer as \""+globalTemplateCore2+"\"")
    obj.textboxglobaltemplatecorerightclickonthesearchedtemplategte(globalTemplateCore2)
  
@when("I Select context menu item EC global template core in global template explorer as {arg}")
def step_impl(globalTemplateCore3):
    """I Select context menu item EC global template core in global template explorer as '<global template core3>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC global template core in global template explorer as \""+globalTemplateCore3+"\"")
    obj.textboxglobaltemplatecoreselectcontextmenuitemec(globalTemplateCore3)
  
@when("I selected Ok duuplicate in duplicate")
def step_impl():
    """I selected Ok duuplicate in duplicate"""
    CommonUtil.write_text_file("\nWhen I selected Ok duuplicate in duplicate")
    obj.buttonokduuplicateselected()
  
@when("I wait_for_object_disapear Duplicate window in duplicate as {arg}")
def step_impl(duplicateWindow):
    """I wait_for_object_disapear Duplicate window in duplicate as '<Duplicate window>'"""
    CommonUtil.write_text_file("\nWhen I wait_for_object_disapear Duplicate window in duplicate as \""+duplicateWindow+"\"")
    obj.textboxduplicatewindowwaitforobjectdisapear(duplicateWindow)
  
@when("I Wait for Circular Progress Bar global template core in global template explorer")
def step_impl():
    """I Wait for Circular Progress Bar global template core in global template explorer"""
    CommonUtil.write_text_file("\nWhen I Wait for Circular Progress Bar global template core in global template explorer")
    obj.textboxglobaltemplatecorewaitforcircularprogressbar()
  
@when("I selected toolbox in composite editor")
def step_impl():
    """I selected toolbox in composite editor"""
    CommonUtil.write_text_file("\nWhen I selected toolbox in composite editor")
    obj.buttontoolboxselected()
  
@when("I drag and drop toolbox item composite editor GTE toolboox table in composite editor as {arg}")
def step_impl(toolbooxTable6):
    """I drag and drop toolbox item composite editor GTE toolboox table in composite editor as '<toolboox table6>'"""
    CommonUtil.write_text_file("\nWhen I drag and drop toolbox item composite editor GTE toolboox table in composite editor as \""+toolbooxTable6+"\"")
    obj.textboxtoolbooxtabledraganddroptoolboxitemcompositeeditorgte(toolbooxTable6)
  
@when("I selected save as composite editor in composite editor")
def step_impl():
    """I selected save as composite editor in composite editor"""
    CommonUtil.write_text_file("\nWhen I selected save as composite editor in composite editor")
    obj.buttonsaveascompositeeditorselected()
  
@when("I entered Description in save as window as {arg}")
def step_impl(description7):
    """I entered Description in save as window as '<Description7>'"""
    CommonUtil.write_text_file("\nWhen I entered Description in save as window as \""+description7+"\"")
    obj.textboxdescriptionentered(description7)
  
@when("I selected Save in save as window")
def step_impl():
    """I selected Save in save as window"""
    CommonUtil.write_text_file("\nWhen I selected Save in save as window")
    obj.buttonsaveselected()

@then("verify popup message in the save as window as {arg}")
def step_impl(content):
    Engineeringclientutility.verify_Popup_Message_OK(content)
    
@when("I selected Cancel in save as window")
def step_impl():
    """I selected Cancel in save as window"""
    CommonUtil.write_text_file("\nWhen I selected Cancel in save as window")
    obj.buttoncancelselected()
    

@then("verify search text GTE global template search in global template explorer as {arg}")
def step_impl(globaltemplatesearch1):
    """I selected Cancel in save as window"""
    Globaltemplatesutility.verify_search_box_message_GTE(globaltemplatesearch1)
    
@when("I selected Save in save as windowo")
def step_impl():
    """I selected Save in save as window"""
    CommonUtil.write_text_file("\nWhen I selected Save in save as window")
    obj.buttonsaveselected1()
    
@when("I selected Close duuplicate in duplicate")
def step_impl():
    """I selected Close duuplicate in duplicate"""
    CommonUtil.write_text_file("\nWhen I selected Close duuplicate in duplicate")
    Applicationutility.take_screenshot('Full screenshot')
    obj.closeduuplicateselected()
@then("Verify Duplicate window close")
def step_impl():
    """Verify Duplicate window close"""
    CommonUtil.write_text_file("\nWhen Verify Duplicate window close")
    obj.verify_dup_win()
    Applicationutility.take_screenshot('Full screenshot')
        
@then("I verify that I have navigated to the {arg}")
def step_impl(tabname):
    """I verify that I have navigated to the '<tabname>'"""
    CommonUtil.write_text_file("\nWhen Verify Duplicate window close")
    obj.verifytittlebar(tabname)
    Applicationutility.take_screenshot('Full screenshot')    
    