"""CurrentScreenWorkFlow"""
from CurrentScreenWorkFlow import CurrentScreenWorkFlow
import CommonUtil
import Applicationutility
import Topologyexplorerutility

obj=CurrentScreenWorkFlow()

        
@given("I have access to application")
def step_impl():
    """I have access to application"""
    CommonUtil.write_text_file("\nGiven I have access to application")
    obj.windowloginpageaccesstoapplication()
  
@when("I selected Close in login page")
def step_impl():
    """I selected Close in login page"""
    CommonUtil.write_text_file("\nWhen I selected Close in login page")
    obj.buttoncloseselected()

@when("I launch Engineering Client second time Engineering client two in engineering client")
def step_impl():
    """I launch Engineering Client second time Engineering client two in engineering client"""
    CommonUtil.write_text_file("\nWhen I launch Engineering Client second time Engineering client two in engineering client")
    obj.buttonengineeringclienttwolaunchengineeringclientsecondtime()
  
@when("I selected AE Post Condition in conditions")
def step_impl():
    """I selected AE Post Condition in conditions"""
    CommonUtil.write_text_file("\nWhen I selected AE Post Condition in conditions")
    obj.buttonaepostconditionselected()
  
@when("I Close all tab Deletes system AE Post Condition in conditions")
def step_impl():
    """I Close all tab Deletes system AE Post Condition in conditions"""
    CommonUtil.write_text_file("\nWhen I Close all tab Deletes system AE Post Condition in conditions")
    obj.buttonaepostconditionclosealltabdeletessystem()
    
    
##################################################################################################################
@when("I Enter pssword in {arg} field in Controller password grid popup")
def step_impl(password):
    """I Enter pssword in '<password>' field in Controller password grid popup"""
    Topologyexplorerutility.Enter_Controller_Password_TE(password)
    
@when("I close Logical window in controller configuration window")
def step_impl():
    """I Enter pssword in '<password>' field in Controller password grid popup"""
    obj.closebuttontm()
    
    
@when("I change the controller protection to disable")
def step_impl():
    """I change the controller protection to disable"""
    Topologyexplorerutility.Controller_property()
    
@when("I Select {arg} From deploy Project window and Click on Start Engine Checkbox")
def step_impl(IP_address):
    """I Select '<IP_address>' From deploy Project window and Click on Start Engine Checkbox"""
    Topologyexplorerutility.Select_IP_from_ControlProjectDeployment(IP_address)
    
@when("I Validate in TE Window using shortcut Keys")
def step_impl():
    """I change the controller protection to disable"""
    Topologyexplorerutility.Validate_TE_Window_Keyboard_Action()
    
@when("I Enter Password as Schneider0! in Password PopUp available for Controller")
def step_impl():
    """I change the controller protection to disable"""
    Topologyexplorerutility.Enter_password_controller_popup()

@when("I Click on OK in Password popup window")
def step_impl():
    """I change the controller protection to disable"""
    obj.clickokfromdbppopupwindow() 
    
@when("I Click on start engine checkobox in deploy changes refine online window")
def step_impl():
    """I change the controller protection to disable"""
    Applicationutility.wait_in_seconds(2000, "wait")
    obj.clickstartenginecheckbox()
    
    
@when("I close PLC Bus window in controller configuration window")
def step_impl():
    """I close PLC Bus window in controller configuration window"""
    obj.closebuttonplcbus()
    
    
@when("I Click on Yes in Modification Window")
def step_impl():
    """I close PLC Bus window in controller configuration window"""
    obj.clickyesmodificationwindow()