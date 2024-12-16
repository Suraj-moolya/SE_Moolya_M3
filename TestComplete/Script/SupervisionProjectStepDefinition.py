"""SupervisionProjectWorkFlow"""
from SupervisionProjectWorkFlow import SupervisionProjectWorkFlow
import CommonUtil
import Applicationutility

obj=SupervisionProjectWorkFlow()

        
@then("verify displayed advance settings window SP in supervision project")
def step_impl():
    """verify displayed advance settings window SP in supervision project"""
    CommonUtil.write_text_file("\nThen verify displayed advance settings window SP in supervision project")
    obj.buttonadvancesettingswindowspverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I click on the {arg} in the Refine Online window")
def step_impl(icon):
    """I click on the '<icon>' in the Refine Online window"""
    CommonUtil.write_text_file("\nWhen I click on the '{icon}' in the Refine Online window")
    obj.textboxclickicononrefineonline(icon)