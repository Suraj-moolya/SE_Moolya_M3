"""ControlExpertWorkFlow"""
from ControlExpertWorkFlow import ControlExpertWorkFlow
import CommonUtil
import Applicationutility

obj=ControlExpertWorkFlow()

        
@when("I selected Properties of device OK CE in control expert")
def step_impl():
    """I selected Properties of device OK CE in control expert"""
    CommonUtil.write_text_file("\nWhen I selected Properties of device OK CE in control expert")
    obj.buttonpropertiesofdeviceokceselected()
  
@when("I selected Full Screen CE in control expert")
def step_impl():
    """I selected Full Screen CE in control expert"""
    CommonUtil.write_text_file("\nWhen I selected Full Screen CE in control expert")
    obj.buttonfullscreenceselected()
  
@when("I selected Close Full Screen CE in control expert")
def step_impl():
    """I selected Close Full Screen CE in control expert"""
    CommonUtil.write_text_file("\nWhen I selected Close Full Screen CE in control expert")
    obj.buttonclosefullscreenceselected()
  
@when("I selected Unlock Safety Protection CE in control expert")
def step_impl():
    """I selected Unlock Safety Protection CE in control expert"""
    CommonUtil.write_text_file("\nWhen I selected Unlock Safety Protection CE in control expert")
    obj.buttonunlocksafetyprotectionceselected()
    
    
@when("I selected Build and Deploy Changes in control expert")
def step_impl():
    """I selected Build and Deploy Changes in control expert"""
    CommonUtil.write_text_file("\nWhen I selected Build and Deploy Changes in control expert")
    obj.buttonbuildanddeploychangesselected()
    

        
  