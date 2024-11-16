"""WindowsExplorerWorkFlow"""
from WindowsExplorerWorkFlow import WindowsExplorerWorkFlow
import CommonUtil
import Applicationutility

obj=WindowsExplorerWorkFlow()

        
@when("I open system server console show hidden icon in windows explorer")
def step_impl():
    """I open system server console show hidden icon in windows explorer"""
    CommonUtil.write_text_file("\nWhen I open system server console show hidden icon in windows explorer")
    obj.buttonshowhiddeniconopensystemserverconsole()
  
@when("I launch Engineering Client Windows in windows explorer")
def step_impl():
    """I launch Engineering Client Windows in windows explorer"""
    CommonUtil.write_text_file("\nWhen I launch Engineering Client Windows in windows explorer")
    obj.parentwindowslaunchengineeringclient()
  
@when("I open details tab in task manager Windows in windows explorer")
def step_impl():
    """I open details tab in task manager Windows in windows explorer"""
    CommonUtil.write_text_file("\nWhen I open details tab in task manager Windows in windows explorer")
    obj.parentwindowsopendetailstabintaskmanager()
  
@then("verify control expert instances in task manager detail list in task manager as {arg}")
def step_impl(detailList4):
    """verify control expert instances in task manager detail list in task manager as '<detail list4>'"""
    CommonUtil.write_text_file("\nThen verify control expert instances in task manager detail list in task manager as \""+detailList4+"\"")
    obj.textboxdetaillistverifycontrolexpertinstancesintaskmanager(detailList4)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I terminate all tested apps tabs in task manager")
def step_impl():
    """I terminate all tested apps tabs in task manager"""
    CommonUtil.write_text_file("\nWhen I terminate all tested apps tabs in task manager")
    obj.buttontabsterminatealltestedapps()

@when("I terminate all tested apps tabs in windows explorer")
def step_impl():
    """I terminate all tested apps tabs in task manager"""
    CommonUtil.write_text_file("\nWhen I terminate all tested apps tabs in task manager")
    obj.buttontabsterminateec()  