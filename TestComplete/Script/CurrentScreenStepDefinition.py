"""CurrentScreenWorkFlow"""
from CurrentScreenWorkFlow import CurrentScreenWorkFlow
import CommonUtil
import Applicationutility

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
