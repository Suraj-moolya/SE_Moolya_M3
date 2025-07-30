"""SupervisionProjectWorkFlow"""
from SupervisionProjectWorkFlow import SupervisionProjectWorkFlow
import CommonUtil
import Applicationutility
import Projectexplorertabutility

obj=SupervisionProjectWorkFlow()

        
@then("verify displayed advance settings window SP in supervision project")
def step_impl():
    """verify displayed advance settings window SP in supervision project"""
    CommonUtil.write_text_file("\nThen verify displayed advance settings window SP in supervision project")
    obj.buttonadvancesettingswindowspverifydisplayed()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I change SettingsHeader as {arg}")
def step_impl(options):
    """I change SettingsHeader as '<Setting_Header>'"""
    CommonUtil.write_text_file("\nWhen I change SettingsHeader as '<Setting_Header>'")
    obj.selectSPsettingheader(options)

@when("I verify the Page Templates selected")
def step_impl():
    """I verify the Page Templates selected"""
    CommonUtil.write_text_file("\nThen I verify the Page Templates selected")
    obj.verifypagetemplate()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I click on {arg} in Refine window")
def step_impl(button):
    """I click on '<verticalbar button>' in Refine window"""
    CommonUtil.write_text_file("\nWhen I click on '<verticalbar button>' in Refine window")
    obj.clickonsystemmodel(button)
    
@when("I click on {arg} in equipments tab")
def step_impl(button1):
    """I click on '<horizontalbar button>' in equipments tab"""
    CommonUtil.write_text_file("\nWhen I click on '<horizontalbar button>' in equipments tab")
    obj.clickonequipmentexportall(button1)
    

@when("I enter the filename {arg} and file location in the Export Data window")
def step_impl(name):
    """I enter the filename '<name>' and file location in the Export Data window"""
    CommonUtil.write_text_file("\nAnd I enter the filename '<name>' and file location in the Export Data window")
    obj.exportequipment(name)
    
@when("I Click on {arg} button in the Export Data window")
def step_impl(btn):
    """I Click on '<btn>' button in the Export Data window"""
    CommonUtil.write_text_file("\nAnd I Click on '<btn>' button in the Export Data window")
    obj.exportdatasavebutton(btn)
    
@when("I Click on {arg} menu in the Refine window System Model")
def step_impl(menu):
    """I Click on '<menu>' menu in the Refine window System Model"""
    CommonUtil.write_text_file("\nAnd I Click on '<menu>' menu in the Refine window System Model")
    obj.systemmodelmenu(menu)
