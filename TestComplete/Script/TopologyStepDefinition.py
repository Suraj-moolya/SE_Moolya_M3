"""TopologyWorkFlow"""
from TopologyWorkFlow import TopologyWorkFlow
import CommonUtil
import Applicationutility

obj=TopologyWorkFlow()

        
@when("I Enter Controller Password TE New Password box in topology as {arg}")
def step_impl(newPasswordBox1):
    """I Enter Controller Password TE New Password box in topology as '<New Password box1>'"""
    CommonUtil.write_text_file("\nWhen I Enter Controller Password TE New Password box in topology as \""+newPasswordBox1+"\"")
    obj.textboxnewpasswordboxentercontrollerpasswordte(newPasswordBox1)
  
@when("I Enter Controller Password TE Confirm Password box in topology as {arg}")
def step_impl(confirmPasswordBox2):
    """I Enter Controller Password TE Confirm Password box in topology as '<Confirm Password box2>'"""
    CommonUtil.write_text_file("\nWhen I Enter Controller Password TE Confirm Password box in topology as \""+confirmPasswordBox2+"\"")
    obj.textboxnewpasswordboxentercontrollerpasswordte(confirmPasswordBox2)
  
@then("Verify entered Controller Password valid invalid TE New Password box in topology as {arg}")
def step_impl(newPasswordBox4):
    """Verify entered Controller Password valid invalid TE New Password box in topology as '<New Password box4>'"""
    CommonUtil.write_text_file("\nThen Verify entered Controller Password valid invalid TE New Password box in topology as \""+newPasswordBox4+"\"")
    obj.textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte(newPasswordBox4)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify entered Controller Password valid invalid TE Confirm Password box in topology as {arg}")
def step_impl(confirmPasswordBox5):
    """Verify entered Controller Password valid invalid TE Confirm Password box in topology as '<Confirm Password box5>'"""
    CommonUtil.write_text_file("\nThen Verify entered Controller Password valid invalid TE Confirm Password box in topology as \""+confirmPasswordBox5+"\"")
    Delay(5000,"Wait")
    obj.textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte(confirmPasswordBox5)
    Applicationutility.take_screenshot("Full Screenshot")
  

  