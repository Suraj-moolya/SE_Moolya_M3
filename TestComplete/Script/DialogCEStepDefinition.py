"""DialogCEWorkFlow"""
from DialogCEWorkFlow import DialogCEWorkFlow
import CommonUtil
import Applicationutility

obj=DialogCEWorkFlow()

        
@when("I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as {arg}")
def step_impl(dialogPanelCe3):
    """I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE3>'"""
    CommonUtil.write_text_file("\nWhen I Dblclick dialog panel item CE Dialog Panel CE in dialog ce as \""+dialogPanelCe3+"\"")
    obj.textboxdialogpanelcedblclickdialogpanelitemce(dialogPanelCe3)
  
@when("I Click dialog panel item CE Dialog Panel CE in dialog ce as {arg}")
def step_impl(dialogPanelCe4):
    """I Click dialog panel item CE Dialog Panel CE in dialog ce as '<Dialog Panel CE4>'"""
    CommonUtil.write_text_file("\nWhen I Click dialog panel item CE Dialog Panel CE in dialog ce as \""+dialogPanelCe4+"\"")
    obj.textboxdialogpanelceclickdialogpanelitemce(dialogPanelCe4)
  
@when("I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as {arg}")
def step_impl(dialogListBoxCe5):
    """I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as '<Dialog List box CE5>'"""
    CommonUtil.write_text_file("\nWhen I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as \""+dialogListBoxCe5+"\"")
    obj.textboxdialoglistboxceselectbottomlistitemdialogpanelitemce(dialogListBoxCe5)
  
@when("I selected Dialog OK CE in dialog ce")
def step_impl():
    """I selected Dialog OK CE in dialog ce"""
    CommonUtil.write_text_file("\nWhen I selected Dialog OK CE in dialog ce")
    obj.buttondialogokceselected()

@when("I Select bottom listitem dialog panel item CE Dialog List box CE1 in dialog ce as {arg}")
def step_impl(dialogListBoxCe5):
    """I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as '<Dialog List box CE5>'"""
    CommonUtil.write_text_file("\nWhen I Select bottom listitem dialog panel item CE Dialog List box CE in dialog ce as \""+dialogListBoxCe5+"\"")
    obj.textboxdialoglistboxceselectbottomlistitemdialogpanelitemce1(dialogListBoxCe5)
    
@when("I click on Start button on PLC Simulator")
def step_impl():
    """I click on Start button on PLC Simulator"""
    CommonUtil.write_text_file("\nWhen I click on Start button on PLC Simulator")
    obj.buttondialogstartsimulatorbutton()
    
@when("I change port number of simulator to 503")
def step_impl():
    """I change port number of simulator to 503"""
    CommonUtil.write_text_file("\nWhen I change port number of simulator to 503")
    obj.textboxchangeportnumberplcsimulator()
    
@when("I selected List of modified Yes button CE in dialog ce")
def step_impl():
    """I selected List of modified Yes button CE in dialog ce"""
    CommonUtil.write_text_file("\nWhen I selected List of modified Yes button CE in dialog ce")
    obj.buttonlistofmodifiedyesbuttonceselected()
  