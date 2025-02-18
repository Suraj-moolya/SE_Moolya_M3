"""SystemExplorerScreenWorkFlow"""
from SystemExplorerScreenWorkFlow import SystemExplorerScreenWorkFlow
import CommonUtil
import Applicationutility
import Systemserverutility
import Applicationexplorertabutility

obj=SystemExplorerScreenWorkFlow()

        
@then("Verify Topology Initialized Progress Bar in system explorer")
def step_impl():
    """Verify Topology Initialized Progress Bar in system explorer"""
    CommonUtil.write_text_file("\nThen Verify Topology Initialized Progress Bar in system explorer")
    obj.buttonprogressbarverifytopologyinitialized()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Right Click on nodes System Explorer Node in system explorer as {arg}")
def step_impl(systemsExplorer):
    """I Right Click on nodes System Explorer Node in system explorer as 'Systems Explorer'"""
    CommonUtil.write_text_file("\nWhen I Right Click on nodes System Explorer Node in system explorer as 'Systems Explorer'")
    obj.buttonsystemexplorernoderightclickonnodes(systemsExplorer)
  
@then("verify context menu items from Rclick menu items in system explorer")
def step_impl():
    """verify context menu items from Rclick menu items in system explorer"""
    CommonUtil.write_text_file("\nThen verify context menu items from Rclick menu items in system explorer")
    obj.buttonfromrclickmenuitemsverifycontextmenuitems()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Create Folder in context menu")
def step_impl():
    """I selected Create Folder in context menu"""
    CommonUtil.write_text_file("\nWhen I selected Create Folder in context menu")
    obj.buttoncreatefolderselected()
  
@then("verify system and folder created System Explorer Node in system explorer")
def step_impl():
    """verify system and folder created System Explorer Node in system explorer"""
    CommonUtil.write_text_file("\nThen verify system and folder created System Explorer Node in system explorer")
    obj.buttonsystemexplorernodeverifysystemandfoldercreated()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I RClick on Folder which is created latest in system explorer")
def step_impl():
    """I RClick on Folder which is created latest in system explorer"""
    CommonUtil.write_text_file("\nWhen I RClick on Folder which is created latest in system explorer")
    obj.buttonwhichiscreatedlatestrclickonfolder()
  
@when("I selected Create System in context menu")
def step_impl():
    """I selected Create System in context menu"""
    CommonUtil.write_text_file("\nWhen I selected Create System in context menu")
    obj.buttoncreatesystemselected()
  
@when("I Wait for Circular Progress Bar To Complete in system explorer")
def step_impl():
    """I Wait for Circular Progress Bar To Complete in system explorer"""
    CommonUtil.write_text_file("\nWhen I Wait for Circular Progress Bar To Complete in system explorer")
    obj.buttontocompletewaitforcircularprogressbar()
  
@then("verify context menu items System Explorer Node in system explorer")
def step_impl():
    """verify context menu items System Explorer Node in system explorer"""
    CommonUtil.write_text_file("\nThen verify context menu items System Explorer Node in system explorer")
    obj.buttonfromrclickmenuitemsverifycontextmenuitems()
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Create system and verify context menu System Explorer Node in system explorer as {arg}")
def step_impl(systemExplorer):
    """Create system and verify context menu System Explorer Node in system explorer as 'System Explorer'"""
    CommonUtil.write_text_file("\nThen Create system and verify context menu System Explorer Node in system explorer as 'System Explorer'")
    obj.buttonsystemexplorernodecreatesystemandverifycontextmenu(systemExplorer)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected System_1 folder in system explorer")
def step_impl():
    """I selected System_1 folder in system explorer"""
    CommonUtil.write_text_file("\nWhen I selected System_1 folder in system explorer")
    obj.buttonsystem1folderselected()
  
@when("I navigate to explorers MainToolBar in system explorer as {arg}")
def step_impl(maintoolbar1):
    """I navigate to explorers MainToolBar in system explorer as '<MainToolBar1>'"""
    CommonUtil.write_text_file("\nWhen I navigate to explorers MainToolBar in system explorer as \""+maintoolbar1+"\"")
    obj.textboxmaintoolbarnavigatetoexplorers(maintoolbar1)
  
@then("verify Tabs Explorer tab in system explorer as {arg}")
def step_impl(explorerTab2):
    """verify Tabs Explorer tab in system explorer as '<Explorer tab2>'"""
    CommonUtil.write_text_file("\nThen verify Tabs Explorer tab in system explorer as \""+explorerTab2+"\"")
    obj.textboxexplorertabverifytabs(explorerTab2)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected System Explorer Canvas in system explorer")
def step_impl():
    """I selected System Explorer Canvas in system explorer"""
    CommonUtil.write_text_file("\nWhen I selected System Explorer Canvas in system explorer")
    obj.buttonsystemexplorercanvasselected()
  
@then("verify Explorer warning message Warning popup in system explorer as {arg}")
def step_impl(warningPopup2):
    """verify Explorer warning message Warning popup in system explorer as '<Warning popup2>'"""
    CommonUtil.write_text_file("\nThen verify Explorer warning message Warning popup in system explorer as \""+warningPopup2+"\"")
    obj.textboxwarningpopupverifyexplorerwarningmessage(warningPopup2)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Popup Ok in system explorer")
def step_impl():
    """I selected Popup Ok in system explorer"""
    CommonUtil.write_text_file("\nWhen I selected Popup Ok in system explorer")
    obj.buttonpopupokselected()
  
@when("I PE warning Popup Close in system explorer")
def step_impl():
    """I PE warning Popup Close in system explorer"""
    CommonUtil.write_text_file("\nWhen I PE warning Popup Close in system explorer")
    obj.buttonpopupclosepewarning()
  
@when("I Right Click on nodes System_1 in system_1 node as {arg}")
def step_impl(system11):
    """I Right Click on nodes System_1 in system_1 node as '<System_11>'"""
    CommonUtil.write_text_file("\nWhen I Right Click on nodes System_1 in system_1 node as \""+system11+"\"")
    obj.buttonsystemexplorernoderightclickonnodes(system11)
  
@then("verify context menu items ContextMenu in system explorer")
def step_impl():
    """verify context menu items ContextMenu in system explorer"""
    CommonUtil.write_text_file("\nThen verify context menu items ContextMenu in system explorer")
    obj.buttonfromrclickmenuitemsverifycontextmenuitems()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I selected Open Project in system_1 node")
def step_impl():
    """I selected Open Project in system_1 node"""
    CommonUtil.write_text_file("\nWhen I selected Open Project in system_1 node")
    obj.buttonopenprojectselected()
  
@when("I Click on shortcut Keys Press shortcut keys in system explorer as {arg}")
def step_impl(pressShortcutKeys1):
    """I Click on shortcut Keys Press shortcut keys in system explorer as '<Press shortcut keys1>'"""
    CommonUtil.write_text_file("\nWhen I Click on shortcut Keys Press shortcut keys in system explorer as \""+pressShortcutKeys1+"\"")
    obj.textboxpressshortcutkeysclickonshortcutkeys(pressShortcutKeys1)
  
@when("I selected System explorer menu in system explorer")
def step_impl():
    """I selected System explorer menu in system explorer"""
    CommonUtil.write_text_file("\nWhen I selected System explorer menu in system explorer")
    obj.buttonsystemexplorermenuselected()
  
@when("I Right Click on nodes System Explorer Node in system explorer")
def step_impl():
    """I Right Click on nodes System Explorer Node in system explorer"""
    CommonUtil.write_text_file("\nWhen I Right Click on nodes System Explorer Node in system explorer")
    obj.buttonsystemexplorernoderightclickonnodes()
  
@when("I selected Open Application in system_1 node")
def step_impl():
    """I selected Open Application in system_1 node"""
    CommonUtil.write_text_file("\nWhen I selected Open Application in system_1 node")
    obj.buttonopenapplicationselected()
  
@when("I Click on Nodes System Explorer Node in system explorer as {arg}")
def step_impl(systemsExplorer):
    """I Click on Nodes System Explorer Node in system explorer as 'Systems Explorer'"""
    CommonUtil.write_text_file("\nWhen I Click on Nodes System Explorer Node in system explorer as 'Systems Explorer'")
    obj.buttonsystemexplorernodeclickonnodes(systemsExplorer)
  
@when("I Right Click on nodes System_1 folder in system explorer as {arg}")
def step_impl(system1):
    """I Right Click on nodes System_1 folder in system explorer as 'System_1'"""
    CommonUtil.write_text_file("\nWhen I Right Click on nodes System_1 folder in system explorer as 'System_1'")
    obj.buttonsystemexplorernoderightclickonnodes(system1)
  
@when("I selected Open Topology in system explorer")
def step_impl():
    """I selected Open Topology in system explorer"""
    CommonUtil.write_text_file("\nWhen I selected Open Topology in system explorer")
    obj.buttonopentopologyselected()
  
@when("I selected Rename in context menu")
def step_impl():
    """I selected Rename in context menu"""
    CommonUtil.write_text_file("\nWhen I selected Rename in context menu")
    obj.buttonrenameselected()
  
@then("verify folder has entered editing field for selected Folder in system explorer as {arg}")
def step_impl(folder1):
    """verify folder has entered editing field for selected Folder in system explorer as 'Folder_1'"""
    CommonUtil.write_text_file("\nThen verify folder has entered editing field for selected Folder in system explorer as 'Folder_1'")
    obj.buttonforselectedfolderverifyfolderhasenterededitingfield(folder1)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Rename Folder as per requirement in system explorer as {arg}")
def step_impl(asPerRequirement1):
    """I Rename Folder as per requirement in system explorer as '<as per requirement1>'"""
    CommonUtil.write_text_file("\nWhen I Rename Folder as per requirement in system explorer as \""+asPerRequirement1+"\"")
    obj.textboxasperrequirementrenamefolder(asPerRequirement1)
  
@then("Verify_Folder_Renamed as per requirement in system explorer")
def step_impl():
    """Verify_Folder_Renamed as per requirement in system explorer"""
    CommonUtil.write_text_file("\nThen Verify_Folder_Renamed as per requirement in system explorer")
    obj.buttonasperrequirementverifyfolderrenamed()
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I create system_1 System Explorer Node in system explorer")
def step_impl():
    """I create system_1 System Explorer Node in system explorer"""
    CommonUtil.write_text_file("\nWhen I create system_1 System Explorer Node in system explorer")
    obj.buttonsystemexplorernodecreatesystem1()
  
@when("I select system 1 application explorer Open Application in system explorer")
def step_impl():
    """I select system 1 application explorer Open Application in system explorer"""
    CommonUtil.write_text_file("\nWhen I select system 1 application explorer Open Application in system explorer")
    obj.buttonopenapplicationselectsystem1applicationexplorer()
  
@when("I Click on Enter Press shortcut keys in system explorer")
def step_impl():
    """I Click on Enter Press shortcut keys in system explorer"""
    CommonUtil.write_text_file("\nWhen I Click on Enter Press shortcut keys in system explorer")
    obj.textboxpressshortcutkeysclickonenter()
  
@when("I selected System Explorer Node in system explorer")
def step_impl():
    """I selected System Explorer Node in system explorer"""
    CommonUtil.write_text_file("\nWhen I selected System Explorer Node in system explorer")
    obj.buttonsystemexplorernodeselected()
  
@when("I select system 1 application explorer System Explorer Node in system explorer")
def step_impl():
    """I select system 1 application explorer System Explorer Node in system explorer"""
    CommonUtil.write_text_file("\nWhen I select system 1 application explorer System Explorer Node in system explorer")
    obj.buttonopenapplicationselectsystem1applicationexplorer()
  
@when("Pre condition for navigation positive")
def step_impl():
    Systemserverutility.Pre_Condition_Navigation_SE2()
    

@then("Delete the system Folder as {arg}")
def step_impl(node_name1):
    CommonUtil.write_text_file("\nThen verify Tabs Explorer tab in system explorer as \""+node_name1+"\"")
    Applicationexplorertabutility.delete_system_Folder(node_name1)   
        
    
@when("I Create system and context menu System Explorer Node in system explorer as {arg}")
def step_impl(systemExplorer):
    """I Create system and context menu System Explorer Node in system explorer as 'System Explorer'"""
    CommonUtil.write_text_file("\nWhen I Create system and context menu System Explorer Node in system explorer as 'System Explorer'")
    obj.buttonsystemexplorernodecreatesystemandcontextmenu(systemExplorer)
    
@when("I Rename Network as per requirement in system explorer as {arg}")
def step_impl(asPerRequirement1):
    """I Rename Folder as per requirement in system explorer as '<as per requirement1>'"""
    CommonUtil.write_text_file("\nWhen I Rename Folder as per requirement in system explorer as \""+asPerRequirement1+"\"")
    obj.textboxasperrequirementrenamefolder(asPerRequirement1)
    
@when("I Click on Browse Button in System backup Window")
def step_impl():
    """I Click on Browse Button in System backup Window"""
    CommonUtil.write_text_file("\nWhen I Click on Browse Button in System backup Window")
    obj.buttonsystemexplorerbrowse()
    
@when("I selected Create System in context menu with password")
def step_impl():
    """I selected Create System in context menu"""
    CommonUtil.write_text_file("\nWhen I selected Create System in context menu")
    obj.buttoncreatesystemselectedwithpassword()