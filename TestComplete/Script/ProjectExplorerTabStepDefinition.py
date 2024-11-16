"""ProjectExplorerTabWorkFlow"""
from ProjectExplorerTabWorkFlow import ProjectExplorerTabWorkFlow
import CommonUtil
import Applicationutility

obj=ProjectExplorerTabWorkFlow()

        
@when("I RClick control project browser project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I RClick control project browser project browser in project explorer as '<project browser1>'"""
    CommonUtil.write_text_file("\nWhen I RClick control project browser project browser in project explorer as \""+projectBrowser1+"\"")
    obj.textboxprojectbrowserrclickcontrolprojectbrowser(projectBrowser1)
  
@when("I Select context menu item EC project browser in project explorer as {arg}")
def step_impl(projectBrowser2):
    """I Select context menu item EC project browser in project explorer as '<project browser2>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC project browser in project explorer as \""+projectBrowser2+"\"")
    obj.textboxprojectbrowserselectcontextmenuitemec(projectBrowser2)
  
@when("I Wait for Execution project browser in project explorer")
def step_impl():
    """I Wait for Execution project browser in project explorer"""
    CommonUtil.write_text_file("\nWhen I Wait for Execution project browser in project explorer")
    obj.textboxprojectbrowserwaitforexecution()
  
@when("I click modal dialog window project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I click modal dialog window project browser in project explorer as '<project browser3>'"""
    CommonUtil.write_text_file("\nWhen I click modal dialog window project browser in project explorer as \""+projectBrowser3+"\"")
    obj.textboxprojectbrowserclickmodaldialogwindow(projectBrowser3)
    
@when("I Select context submenu item TE project browser in project explorer as {arg}")
def step_impl(projectBrowser6):
    """I Select context submenu item TE project browser in project explorer as '<project browser6>'"""
    CommonUtil.write_text_file("\nWhen I Select context submenu item TE project browser in project explorer as \""+projectBrowser6+"\"")
    obj.textboxprojectbrowserselectcontextsubmenuitemte(projectBrowser6)
    
@when("I Dclick Control project broswer project browser in project explorer as {arg}")
def step_impl(projectBrowser7):
    """I Dclick Control project broswer project browser in project explorer as '<project browser7>'"""
    CommonUtil.write_text_file("\nWhen I Dclick Control project broswer project browser in project explorer as \""+projectBrowser7+"\"")
    obj.textboxprojectbrowserdclickcontrolprojectbroswer(projectBrowser7)
  
@when("I Select combo box value properties dock TE project browser in project explorer as {arg}")
def step_impl(projectBrowser9):
    """I Select combo box value properties dock TE project browser in project explorer as '<project browser9>'"""
    CommonUtil.write_text_file("\nWhen I Select combo box value properties dock TE project browser in project explorer as \""+projectBrowser9+"\"")
    obj.textboxprojectbrowserselectcomboboxvaluepropertiesdockte(projectBrowser9)
  
@when("I Executables Properties Executable Property in project explorer as {arg}")
def step_impl(executableProperty10):
    """I Executables Properties Executable Property in project explorer as '<Executable Property10>'"""
    CommonUtil.write_text_file("\nWhen I Executables Properties Executable Property in project explorer as \""+executableProperty10+"\"")
    obj.textboxexecutablepropertyexecutablesproperties(executableProperty10)
  
@when("I Generate and build controller project browser in project explorer")
def step_impl():
    """I Generate and build controller project browser in project explorer"""
    CommonUtil.write_text_file("\nWhen I Generate and build controller project browser in project explorer")
    obj.textboxprojectbrowsergenerateandbuildcontroller()

  
@when("I Close all tab Deletes system project browser in project explorer")
def step_impl():
    """I Close all tab Deletes system project browser in project explorer"""
    CommonUtil.write_text_file("\nWhen I Close all tab Deletes system project browser in project explorer")
    obj.textboxprojectbrowserclosealltabdeletessystem()

@when("I Right Click on the Facet in Assignments Section as {arg}")
def step_impl(facet_name):
    """I Right Click on the Facet in Assignments Section as <facet_name>"""
    CommonUtil.write_text_file("\nWhen I Right Click on the Facet in Assignments Section \""+facet_name+"\"")
    obj.assignmentsrightclickunlinkfacets(facet_name)

  
@then("I verify Unlinked Status updated in Generation Section as {arg}")
def step_impl(param1):
    """I verify Unlinked Status updated in Generation Section as <param>"""
    CommonUtil.write_text_file("\nThen I verify Unlinked Status updated in Generation Section")
    obj.assignmentsunlinkfacets(param1)
    
@then("I verify Status updated in Generation Section as {arg}")
def step_impl(param1):
    """I verify Unlinked Status updated in Generation Section as <param>"""
    CommonUtil.write_text_file("\nThen I verify Unlinked Status updated in Generation Section")
    obj.assignmentsunlinkfacets(param1)
    
@when("I Click on FBDSection in Container Section {arg}")
def step_impl(param1):
    """I Click on FBDSection in Container Section '<FBDSection>'"""
    CommonUtil.write_text_file("\nThen I Click on FBDSection in Container Section ")
    obj.click_fbdsection_select_pasteinstance(param1)
  
@when("I RClick on FBDSection in Container Section and select menu item as {arg}")
def step_impl(param1):
    obj.Rclick_fbdsection_select_pasteinstance(param1)
    
@when("I Copy instances from FBDSection and paste in another FBDSection as {arg}")
def step_impl(param1):
    """I Copy instances from FBDSection and paste in another FBDSection as '<Param1>'"""
    CommonUtil.write_text_file("\nWhen I Copy instances from FBDSection and paste in another FBDSection as  ")
    obj.copyfromfbdinstancepastefbd(param1)

  
@when("I Right click container dock context menu item PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I Right click container dock context menu item PE container dock in project explorer as '<container dock1>'"""
    CommonUtil.write_text_file("\nWhen I Right click container dock context menu item PE container dock in project explorer as \""+containerDock1+"\"")
    obj.textboxcontainerdockrightclickcontainerdockcontextmenuitempe(containerDock1)
  
@when("I click modal dialog window container dock in project explorer as {arg}")
def step_impl(containerDock2):
    """I click modal dialog window container dock in project explorer as '<container dock2>'"""
    CommonUtil.write_text_file("\nWhen I click modal dialog window container dock in project explorer as \""+containerDock2+"\"")
    obj.textboxcontainerdockclickmodaldialogwindow(containerDock2)
  
@then("Verify Section Deleted in Control Project containers container dock in project explorer as {arg}")
def step_impl(containerDock3):
    """Verify Section Deleted in Control Project containers container dock in project explorer as '<container dock3>'"""
    CommonUtil.write_text_file("\nThen Verify Section Deleted in Control Project containers container dock in project explorer as \""+containerDock3+"\"")
    obj.textboxcontainerdockverifysectiondeletedincontrolprojectcontainers(containerDock3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I Delete Section in ControlProject by using Keyboard actions PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I Delete Section in ControlProject by using Keyboard actions PE container dock in project explorer as '<container dock1>'"""
    CommonUtil.write_text_file("\nWhen I Delete Section in ControlProject by using Keyboard actions PE container dock in project explorer as \""+containerDock1+"\"")
    obj.textboxcontainerdockdeletesectionincontrolprojectbyusingkeyboardactionspe(containerDock1)

@when("I Click on container section PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I Click on container section PE container dock in project explorer as '<container dock1>'"""
    CommonUtil.write_text_file("\nWhen I Click on container section PE container dock in project explorer as \""+containerDock1+"\"")
    obj.textboxcontainerdockclickoncontainersectionpe(containerDock1)
  
@when("I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock2):
    """I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as '<assignmentsdock2>'"""
    CommonUtil.write_text_file("\nWhen I Drag and drop facet from assignment to container sections PE assignmentsdock in project explorer as \""+assignmentsdock2+"\"")
    obj.textboxassignmentsdockdraganddropfacetfromassignmenttocontainersectionspe(assignmentsdock2)
  
@when("I Right click container dock context menu item PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock3):
    """I Right click container dock context menu item PE assignmentsdock in project explorer as '<assignmentsdock3>'"""
    CommonUtil.write_text_file("\nWhen I Right click container dock context menu item PE assignmentsdock in project explorer as \""+assignmentsdock3+"\"")
    obj.textboxassignmentsdockrightclickcontainerdockcontextmenuitempe(assignmentsdock3)
  
@when("I Wait for Execution assignmentsdock in project explorer")
def step_impl():
    """I Wait for Execution assignmentsdock in project explorer"""
    CommonUtil.write_text_file("\nWhen I Wait for Execution assignmentsdock in project explorer")
    obj.textboxassignmentsdockwaitforexecution()
  
@then("Verify generation status of facet from assignments PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock4):
    """Verify generation status of facet from assignments PE assignmentsdock in project explorer as '<assignmentsdock4>'"""
    CommonUtil.write_text_file("\nThen Verify generation status of facet from assignments PE assignmentsdock in project explorer as \""+assignmentsdock4+"\"")
    obj.textboxassignmentsdockverifygenerationstatusoffacetfromassignmentspe(assignmentsdock4)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Select context menu item EC container dock in project explorer as {arg}")
def step_impl(containerDock2):
    """I Select context menu item EC container dock in project explorer as '<container dock2>'"""
    CommonUtil.write_text_file("\nWhen I Select context menu item EC container dock in project explorer as \""+containerDock2+"\"")
    obj.textboxcontainerdockselectcontextmenuitemec(containerDock2)
  
@then("Verify Action message in notification pannel container dock in project explorer as {arg}")
def step_impl(containerDock3):
    """Verify Action message in notification pannel container dock in project explorer as '<container dock3>'"""
    CommonUtil.write_text_file("\nThen Verify Action message in notification pannel container dock in project explorer as \""+containerDock3+"\"")
    obj.textboxcontainerdockverifyactionmessageinnotificationpannel(containerDock3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("Verify Action message in notification pannel project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """Verify Action message in notification pannel project browser in project explorer as '<project browser3>'"""
    CommonUtil.write_text_file("\nThen Verify Action message in notification pannel project browser in project explorer as \""+projectBrowser3+"\"")
    obj.textboxcontainerdockverifyactionmessageinnotificationpannel(projectBrowser3)
    Applicationutility.take_screenshot("Full Screenshot")
  
@when("I customize CPB header checkbox PE project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I customize CPB header checkbox PE project browser in project explorer as '<project browser3>'"""
    CommonUtil.write_text_file("\nWhen I customize CPB header checkbox PE project browser in project explorer as \""+projectBrowser3+"\"")
    obj.textboxprojectbrowsercustomizecpbheadercheckboxpe(projectBrowser3)
  
@when("I Click popup button object project browser in project explorer as {arg}")
def step_impl(projectBrowser4):
    """I Click popup button object project browser in project explorer as '<project browser4>'"""
    CommonUtil.write_text_file("\nWhen I Click popup button object project browser in project explorer as \""+projectBrowser4+"\"")
    obj.textboxprojectbrowserclickpopupbuttonobject(projectBrowser4)
  
@then("Verify header control project browser PE project browser in project explorer as {arg}")
def step_impl(projectBrowser5):
    """Verify header control project browser PE project browser in project explorer as '<project browser5>'"""
    CommonUtil.write_text_file("\nThen Verify header control project browser PE project browser in project explorer as \""+projectBrowser5+"\"")
    obj.textboxprojectbrowserverifyheadercontrolprojectbrowserpe(projectBrowser5)
    Applicationutility.take_screenshot("Full Screenshot")
  
@then("verify context menu item project browser in project explorer as {arg}")
def step_impl(menu_item):
    """verify context menu items project browser in project explorer"""
    CommonUtil.write_text_file("\nThen verify context menu items project browser in project explorer")
    obj.textboxprojectbrowserverifycontextmenuitem(menu_item)
    Applicationutility.take_screenshot("Full Screenshot")

@when(r"I Right Click on the Facet in Assignments Section as '(.*) (.*)'")
def step_impl(facet_name, action):
    """I Right Click on the Facet in Assignments Section as '<facet_name>' '<action>'"""
    CommonUtil.write_text_file("\nWhen I Right Click on the Facet in Assignments Section as\""+facet_name+action+"\"")
    obj.rightclickinstanceselectactioninassignments(facet_name, action)
    
    
@then(r"I verify Status updated in Generation Section as '(.*) (.*)'")
def step_impl(facet_name, status):
    """I verify Status updated in Generation Section as '<facet_name>' '<status>'"""
    CommonUtil.write_text_file("\nWhen I verify Status updated in Generation Section as\""+facet_name+status+"\"")
    obj.verifyassignmentsstatus(facet_name, status)
    
@then("I Verify the facet generation status of all facets in Assignments Dock")
def step_impl():
    """I Verify the facet generation status of all facets in Assignments Dock"""
    CommonUtil.write_text_file("\nthen I Verify the facet generation status of all facets in Assignments Dock")
    obj.projectexplorertabutilityverifyallfacetgenerationstatusassignmentdock()
    
@then("I Verify the new fbd section created")
def step_impl():
    """I Verify the new fbd section created"""
    CommonUtil.write_text_file("\nthen I Verify the new fbd section created")
    obj.projectexplorertabutility_verify_section_containers_dock()
    
@when("I Collapse control project browser PE project browser in project explorer")
def step_impl():
    """I Collapse control project browser PE project browser in project explorer"""
    CommonUtil.write_text_file("\nWhen I Collapse control project browser PE project browser in project explorer")
    obj.textboxprojectbrowsercollapsecontrolprojectbrowserpe()

  
@when("I Expand control project browser PE project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I Expand control project browser PE project browser in project explorer as '<project browser1>'"""
    CommonUtil.write_text_file("\nWhen I Expand control project browser PE project browser in project explorer as \""+projectBrowser1+"\"")
    obj.textboxprojectbrowserexpandcontrolprojectbrowserpe(projectBrowser1)
  

@then("Verify build state of control executable PE project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """Verify build state of control executable PE project browser in project explorer as '<project browser3>'"""
    CommonUtil.write_text_file("\nThen Verify build state of control executable PE project browser in project explorer as \""+projectBrowser3+"\"")
    obj.textboxprojectbrowserverifybuildstateofcontrolexecutablepe(projectBrowser3)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I selected Close in refine offline")
def step_impl():
    """I selected Close in refine offline"""
    CommonUtil.write_text_file("\nWhen I selected Close in refine offline")
    obj.buttoncloseselected()

@when("I entered Refine online window in refine offline")
def step_impl():
    """I entered Refine online window in refine offline"""
    CommonUtil.write_text_file("\nWhen I entered Refine online window in refine offline")
    obj.textboxrefineonlinewindowentered()
    
@when("I RClick CPB in project explorer as {arg}")
def step_impl(projectBrowser2):
    """I RClick control project browser project browser in project explorer as '<project browser1>'"""
    CommonUtil.write_text_file("\nWhen I RClick control project browser project browser in project explorer as \""+projectBrowser2+"\"")
    obj.textboxprojectbrowserrCPB(projectBrowser2)

#@when("I Dclick Control project broswer project browser in project explorer as {arg}")
#def step_impl(projectBrowser3):
#    """I Dclick Control project broswer project browser in project explorer as '<project browser3>'"""
#    CommonUtil.write_text_file("\nWhen I Dclick Control project broswer project browser in project explorer as \""+projectBrowser3+"\"")
#    obj.textboxprojectbrowserdclickcontrolprojectbroswer(projectBrowser3)
#  
@when("I Control executable dropdown PE project browser in project explorer as {arg}")
def step_impl(projectBrowser4):
    """I Control executable dropdown PE project browser in project explorer as '<project browser4>'"""
    CommonUtil.write_text_file("\nWhen I Control executable dropdown PE project browser in project explorer as \""+projectBrowser4+"\"")
    obj.textboxprojectbrowsercontrolexecutabledropdownpe(projectBrowser4)
    
@when("I Right click facet from assignment dock PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock1):
    """I Right click facet from assignment dock PE assignmentsdock in project explorer as '<assignmentsdock1>'"""
    CommonUtil.write_text_file("\nWhen I Right click facet from assignment dock PE assignmentsdock in project explorer as \""+assignmentsdock1+"\"")
    obj.textboxassignmentsdockrightclickfacetfromassignmentdockpe(assignmentsdock1)
  
@when("I select context submenu EC assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock2):
    """I select context submenu EC assignmentsdock in project explorer as '<assignmentsdock2>'"""
    CommonUtil.write_text_file("\nWhen I select context submenu EC assignmentsdock in project explorer as \""+assignmentsdock2+"\"")
    obj.textboxassignmentsdockselectcontextsubmenuec(assignmentsdock2)
  
@then("Verify Facets Added or Removed context menu PE assignmentsdock in project explorer as {arg}")
def step_impl(assignmentsdock3):
    """Verify Facets Added or Removed context menu PE assignmentsdock in project explorer as '<assignmentsdock3>'"""
    CommonUtil.write_text_file("\nThen Verify Facets Added or Removed context menu PE assignmentsdock in project explorer as \""+assignmentsdock3+"\"")
    obj.textboxassignmentsdockverifyfacetsaddedorremovedcontextmenupe(assignmentsdock3)
    Applicationutility.take_screenshot("Full Screenshot")
  

