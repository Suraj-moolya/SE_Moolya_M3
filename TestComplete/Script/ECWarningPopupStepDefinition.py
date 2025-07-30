"""ECWarningPopupWorkFlow"""
from ECWarningPopupWorkFlow import ECWarningPopupWorkFlow
import CommonUtil
import Applicationutility

obj=ECWarningPopupWorkFlow()

        
@then("verify windows message Warning popup in ec warning popups as {arg}")
def step_impl(warningPopup1):
    """verify windows message Warning popup in ec warning popups as '<Warning popup1>'"""
    CommonUtil.write_text_file("\nThen verify windows message Warning popup in ec warning popups as \""+warningPopup1+"\"")
    obj.textboxwarningpopupverifywindowsmessage(warningPopup1)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected EC warning popup Ok in ec warning popups")
def step_impl():
    """I selected EC warning popup Ok in ec warning popups"""
    CommonUtil.write_text_file("\nWhen I selected EC warning popup Ok in ec warning popups")
    obj.buttonecwarningpopupokselected()
  
@when("I selected EC warning popup Ok in ec warning popup")
def step_impl():
    """I selected EC warning popup Ok in ec warning popups"""
    CommonUtil.write_text_file("\nWhen I selected EC warning popup Ok in ec warning popups")
    obj.buttonecwarningpopupokselected1()
    
@when("I close ec popup EC warning popup Close in ec warning popups")
def step_impl():
    """I close ec popup EC warning popup Close in ec warning popups"""
    CommonUtil.write_text_file("\nWhen I close ec popup EC warning popup Close in ec warning popups")
    obj.buttonecwarningpopupclosecloseecpopup()
  
@then("verify EC popup message Warning popup EC in ec warning popups as {arg}")
def step_impl(warningPopupEc1):
    """verify EC popup message Warning popup EC in ec warning popups as '<Warning popup EC1>'"""
    CommonUtil.write_text_file("\nThen verify EC popup message Warning popup EC in ec warning popups as \""+warningPopupEc1+"\"")
    obj.textboxwarningpopupecverifyecpopupmessage(warningPopupEc1)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I close ec popup EC popup Close in ec warning popups")
def step_impl():
    """I close ec popup EC popup Close in ec warning popups"""
    CommonUtil.write_text_file("\nWhen I close ec popup EC popup Close in ec warning popups")
    obj.buttonecwarningpopupclosecloseecpopup()
  