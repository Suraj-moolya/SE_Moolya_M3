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