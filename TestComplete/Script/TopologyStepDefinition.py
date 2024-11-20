"""TopologyWorkFlow"""
from TopologyWorkFlow import TopologyWorkFlow
import CommonUtil
import Applicationutility

obj=TopologyWorkFlow()

        
@when("I Select context menu item EC Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I Select context menu item EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC Topology Explorer Tree in topology as \""+topologyExplorerTree1+"\"")
    obj.textboxtopologyexplorertreeselectcontextmenuitemec(topologyExplorerTree1)
  
@when("I select deploy popup dropdown value TE project dropdown in topology as {arg}")
def step_impl(projectDropdown2):
    """I select deploy popup dropdown value TE project dropdown in topology as '<project dropdown2>'"""
    CommonUtil.write_text_file("\nWhen I select deploy popup dropdown value TE project dropdown in topology as \""+projectDropdown2+"\"")
    obj.textboxprojectdropdownselectdeploypopupdropdownvaluete(projectDropdown2)
  
@when("I select deploy popup dropdown value TE Executables dropdown in topology as {arg}")
def step_impl(executablesDropdown3):
    """I select deploy popup dropdown value TE Executables dropdown in topology as '<Executables dropdown3>'"""
    CommonUtil.write_text_file("\nWhen I select deploy popup dropdown value TE Executables dropdown in topology as \""+executablesDropdown3+"\"")
    obj.textboxprojectdropdownselectdeploypopupdropdownvaluete(executablesDropdown3)

@when("I entered backup data description in topology as {arg}")
def step_impl(backupDataDescription3):
    """I entered backup data description in topology as '<backup data description3>'"""
    CommonUtil.write_text_file("\nWhen I entered backup data description in topology as \""+backupDataDescription3+"\"")
    obj.textboxbackupdatadescriptionentered(backupDataDescription3)
  
@when("I Select deploy data from selection grid TE deploy data selection grid in topology")
def step_impl():
    """I Select deploy data from selection grid TE deploy data selection grid in topology"""
    CommonUtil.write_text_file("\nWhen I Select deploy data from selection grid TE deploy data selection grid in topology")
    obj.textboxdeploydataselectiongridselectdeploydatafromselectiongridte()  
    
@when("I select start engine checkbox in in topology")
def step_impl():
    """I select start engine checkbox in in topology"""
    CommonUtil.write_text_file("\nWhen I select start engine checkbox in in topology")
    obj.checkboxstartenginecheckbox()

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

@when("I search template browser EC Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I search template browser EC Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    CommonUtil.write_text_file("\nWhen I search template browser EC Topology Explorer Tree in topology as \""+topologyExplorerTree1+"\"")
    obj.textboxtopologyexplorertreesearchtemplatebrowserec(topologyExplorerTree1)
    
@when("I Select template EC Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree2):
    """I Select template EC Topology Explorer Tree in topology as '<Topology Explorer Tree2>'"""
    CommonUtil.write_text_file("\nWhen I Select template EC Topology Explorer Tree in topology as \""+topologyExplorerTree2+"\"")
    obj.textboxtopologyexplorertreeselecttemplateec(topologyExplorerTree2)
    
@when("I DblClick template TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I DblClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    CommonUtil.write_text_file("\nWhen I DblClick template TE Topology Explorer Tree in topology as \""+topologyExplorerTree1+"\"")
    obj.textboxtopologyexplorertreedblclicktemplatete(topologyExplorerTree1)
    
@when("I Expand communication tab TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree2):
    """I Expand communication tab TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'"""
    CommonUtil.write_text_file("\nWhen I Expand communication tab TE Topology Explorer Tree in topology as \""+topologyExplorerTree2+"\"")
    obj.textboxtopologyexplorertreeexpandcommunicationtabte(topologyExplorerTree2)
    
@when("I edit IP Address Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree3):
    """I edit IP Address Topology Explorer Tree in topology as '<Topology Explorer Tree3>'"""
    CommonUtil.write_text_file("\nWhen I edit IP Address Topology Explorer Tree in topology as \""+topologyExplorerTree3+"\"")
    obj.textboxtopologyexplorertreeeditipaddress(topologyExplorerTree3)
    
@when("I RClick template TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree1):
    """I RClick template TE Topology Explorer Tree in topology as '<Topology Explorer Tree1>'"""
    CommonUtil.write_text_file("\nWhen I RClick template TE Topology Explorer Tree in topology as \""+topologyExplorerTree1+"\"")
    obj.textboxtopologyexplorertreerclicktemplatete(topologyExplorerTree1)
    
@when("I Click on MenuItem in TE Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree2):
    """I Click on MenuItem in TE Topology Explorer Tree in topology as '<Topology Explorer Tree2>'"""
    CommonUtil.write_text_file("\nWhen I Click on MenuItem in TE Topology Explorer Tree in topology as \""+topologyExplorerTree2+"\"")
    obj.textboxtopologyexplorertreeclickonmenuiteminte(topologyExplorerTree2)
    
@when("I modal dialog window select Item Topology Explorer Tree in topology as {arg}")
def step_impl(topologyExplorerTree3):
    """I modal dialog window select Item Topology Explorer Tree in topology as '<Topology Explorer Tree3>'"""
    CommonUtil.write_text_file("\nWhen I modal dialog window select Item Topology Explorer Tree in topology as \""+topologyExplorerTree3+"\"")
    obj.textboxtopologyexplorertreemodaldialogwindowselectitem(topologyExplorerTree3)
