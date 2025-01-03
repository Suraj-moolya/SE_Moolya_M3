"""ProjectExplorerTabWorkFlow"""
from ProjectExplorerTabWorkFlow import ProjectExplorerTabWorkFlow
import CommonUtil
import Applicationutility
import Projectexplorertabutility
import ProjectExplorerTab

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
#    Applicationutility.wait_for_execution()
    obj.textboxprojectbrowserselectcontextmenuitemec(projectBrowser2)
    
@when("I Select controller in context menu as {arg}")
def step_impl(controller):
    """I Select controller in context menu as '<controller name>'"""
    CommonUtil.write_text_file("\nWhen I Select controller in context menu as \""+controller+"\"")
    obj.textboxprojectbrowserselectcontextsubmenuitemec(controller)
    
@when("I rename the ControlProject as {arg}")
def step_impl(controller_name):
    """I rename the ControlProject as '<controller_name>'"""
    CommonUtil.write_text_file("\nWhen I rename the ControlProject as \""+controller_name+"\"")
    obj.textboxprojectbrowserrename(controller_name)        
  
@when("I Wait for Execution project browser in project explorer")
def step_impl():
    """I Wait for Execution project browser in project explorer"""
    CommonUtil.write_text_file("\nWhen I Wait for Execution project browser in project explorer")
    obj.textboxprojectbrowserwaitforexecution()
  
@when("I click modal dialog window project browser in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I click modal dialog window project browser in project explorer as '<project browser3>'"""
    CommonUtil.write_text_file("\nWhen I click modal dialog window project browser in project explorer as \""+projectBrowser3+"\"")
    Applicationutility.wait_for_execution()
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

@when(r"I Right Click on the Facet in Assignments Section as {arg} {arg}")
def step_impl(facet_name,action):
    obj.assignmentsrightclickunlinkfacets(facet_name,action)

  
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
    Applicationutility.wait_in_seconds(1000, 'wait')
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
    
@when(r"I Right Click Facet in Assignment section as '(.*)' and Click '(.*)'")
def step_impl(facet_name, action):
    """I Right Click Facet in Assignment section as '<facet_name>' and Click '<action>'"""
    CommonUtil.write_text_file(f"\nWhen I Right Click Facet in Assignment section as '{facet_name}' and Click '{action}'")
    obj.rightclickinstanceandperformaction(facet_name, action)    
    
@then(r"I verify Status updated in Generation Section as '(.*)' '(.*)'")
def step_impl(facet_name, status):
    """I verify Status updated in Generation Section as '<facet_name>' '<status>'"""
    CommonUtil.write_text_file(f"\nThen I verify Status updated in Generation Section as '{facet_name}' '{status}'")
    obj.verifyassignmentsstatus(facet_name, status)
    
@then("I Verify the facet generation status of all facets in Assignments Dock")
def step_impl():
    """I Verify the facet generation status of all facets in Assignments Dock"""
    CommonUtil.write_text_file("\nthen I Verify the facet generation status of all facets in Assignments Dock")
    Applicationutility.wait_for_execution()
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
    Applicationutility.take_screenshot("Full Screenshot")
  

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
  
@when("I Create multiple FBD Sections and Verify as {arg}")
def step_impl(assignmentsdock2):
    """I Create multiple FBD Sections and Verify as '<assignmentsdock3>'"""
    CommonUtil.write_text_file("\nThen I Create multiple FBD Sections and Verify as \""+assignmentsdock2+"\"")
    obj.projectexplorertabutility_Create_Multiple_section_Containers_Dock_verify(assignmentsdock2)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I Assign Instances from instance dock to sections in containers dock as {arg}")
def step_impl(param):
    """I Assign Instances from instance dock to sections in containers dock as '<param>'"""
    CommonUtil.write_text_file("\nWhen I Assign Instances from instance dock to sections in containers dock as as \""+param+"\"")
    obj.projectexplorertabutility_Drag_instance_drop_container_section(param)
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I Double Click on the Facet in Assingnment section as {arg}")
def step_impl(facet_name):
    """I Double Click on the Facet in Assingnment section as '<facet_name>'"""
    CommonUtil.write_text_file("\nWhen I Double Click on the Facet in Assingnment section as \""+facet_name+"\"")
    obj.doubleclickinstanceinassignments(facet_name)
    
@when("I Check Any of the Facet Boxes to be added as {arg}")
def step_impl(instance_names):
    """I Check Any of the Facet Boxes to be added as '<instance_names>''"""
    CommonUtil.write_text_file("\nWhen I Check Any of the Facet Boxes to be added as \""+instance_names+"\"")
    obj.clickcheckboxininstanceedittor(instance_names)
    
@when("I click button on the Instance editor window as {arg}")
def step_impl(button_name):
    """I click button on the Instance editor window as '<button_name>''"""
    CommonUtil.write_text_file("\nWhen I click button on the Instance editor window as \""+button_name+"\"")
    obj.savebuttoninstanceeditor(button_name) 
      
@when("I Right Click on the Particular Section and Click on Generate {arg}")
def step_impl(container):
    """I Right Click on the Particular Section and Click on Generate '<container>'"""
    CommonUtil.write_text_file("\nWhen I Right Click on the Particular Section and Click on Generate \""+container+"\"")
    obj.rightclickandgeneratecontainerssection(container)
    
@then("I verify the section is generated successfully as '(.*)' '(.*)'")
def step_impl(facet_names, generation_state):
    """I verify the section is generated successfully as '<param>'"""
    CommonUtil.write_text_file("\nThen I verify the section is generated successfully as \""+facet_names+generation_state+"\"")
    obj.verifyassignmentsstate(facet_names, generation_state)
    
@when(r"Right Click on any one of the Facet in Assignments Section of PE-Container and Click Go Into Instance as '(.*)' and perform '(.*)'")
def step_impl(facet_name, action):
    CommonUtil.write_text_file(f"When Right Click on any one of the Facet in Assignments Section of PE-Container and Click Go Into Instance as '{facet_name}' and perform '{action}'")
    obj.rightclickinstanceandperformaction(facet_name, action)
    
@when("I Double Click on Containers as {arg}")
def step_impl(identifier):
    """I Double Click on Containers as '<identifier>'"""
    CommonUtil.write_text_file("\nWhen I Double Click on Containers as \""+identifier+"\"")
    obj.textboxprojectbrowserdclickcontrolprojectbroswer(identifier)
    
@when("I Drag and Drop the Instance to in Container as '(.*)'")
def step_impl(Instance):
    """I Drag and Drop the Instance to in Container"""
    #CommonUtil.write_text_file("\nWhen I Drag and Drop the Instance in Container to section as\""+controller+section+"\"")
    obj.draganddropfrominstancetocontainer(Instance)
    
@when("I drag and Drop the Each instance to Each Sections as '(.*)' '(.*)'")
def step_impl(controller, section):
    """I drag and Drop the Each instance to Each Sections as '<controller>' '<section>'"""
    CommonUtil.write_text_file("\nWhen I Drag and Drop the Instance in Container to section as\""+controller+section+"\"")
    obj.draganddropfromcontainertosection(controller, section)
    
@when("I Right click on the ControlProject_1 in Containers window and create FBDSections as {arg}")
def step_impl(num_sections):
    """I Right click on the ControlProject_1 in Containers window and create FBDSections as '<num_sections>'"""
    CommonUtil.write_text_file("\nWhen I Right click on the ControlProject_1 in Containers window and create FBDSections as\""+num_sections+"\"")
    obj.createfbdsections(num_sections)
   
@when("I Click {arg} on service mapping edittor window")
def step_impl(tabname):
    """I Click '<tabname>' on service mapping edittor window"""
    CommonUtil.write_text_file("\nWhen I Click \""+tabname+"\" on service mapping edittor windownum_sections")
    obj.clickonmappingtab(tabname)    
    
@when("I Verify if the added device is available for mapping as {arg}")
def step_impl(variables):
    """I Verify if the added device is available for mapping as '<variables>'"""
    CommonUtil.write_text_file("\nWhen I Verify if the added device is available for mapping as \""+variables+"\"")
    obj.verifydeviceavailbe(variables)
        
@when("I Verify if the Hardware Instances and App Instance Facets are available for mapping as {arg}")
def step_impl(variables):
    """I Verify if the Hardware Instances and App Instance Facets are available for mapping as '<variables>'"""
    CommonUtil.write_text_file("\nWhen I Verify if the Hardware Instances and App Instance Facets are available for mapping as \""+variables+"\"")
    obj.verifyhardwareinstanceavailableformapping(variables)
    
@when("I Verify if the Network Variables are available as {arg}")
def step_impl(identifiers):
    """I Verify if the Network Variables are available as '<identifiers>'"""
    CommonUtil.write_text_file("\nWhen I Verify if the Network Variables are available as \""+identifiers+"\"")
    obj.verifynetworkvariable(identifiers)    
    
@when("I Drag and drop the EPE Managed Device from devices to channels as {arg}")
def step_impl(server):
    """I Drag and drop the EPE Managed Device from devices to channels as '<server>'"""
    CommonUtil.write_text_file("\nWhen I Drag and drop the EPE Managed Device from devices to channels as \""+server+"\"")
    obj.draganddropdevicetochannel(server)
    
@when("I Click on {arg} in the dialog box")
def step_impl(button):
    """I Click on '<button>' in the dialog box"""
    CommonUtil.write_text_file("\nWhen I Click on  \""+button+"\" in the dialog box")
    obj.textboxcontainerdockclickmodaldialogwindow(button)


@then("I verify {arg} disappered in assignments")
def step_impl(facet_name):
    """I verify '<facet_name>' disappered in assignments"""
    CommonUtil.write_text_file("\nThen I Verify  \""+facet_name+"\" disappered in assignments")
    obj.verifyfacetbeforegenerate(facet_name)    
        
@then(r"I verify Status updated in Assignment Section as '(.*)' '(.*)'")
def step_impl(facet_name, status):
    """I verify Status updated in Assignment Section as '<facet_name>' '<status>'"""
    CommonUtil.write_text_file("\nWhen I verify Status updated in Assignment Section as '{facet_name}' '{status}'")
    obj.verifyassignmentsstatus(facet_name, status)
    
@when("I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as {arg}")
def step_impl(appfacet):
    """I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as '<appfacet>'"""
    CommonUtil.write_text_file("\nWhen I drag and drop DOChannel facets to HWInstance with DOChannel HWInterfaceType as \""+appfacet+"\"")
    obj.draganddropprojecttoserver(appfacet)
    
@when("I Right Click on the Communication Channels section of Communication Mapping Editor as {arg}")
def step_impl(server):
    """I Right Click on the Communication Channels section of Communication Mapping Editor as '<server>'"""
    CommonUtil.write_text_file("\nWhen I Right Click on the Communication Channels section of Communication Mapping Editor as  \""+server+"\"")
    obj.rightclickcommunicationchannel(server)
    

@when("I Drag and Drop variables from network variables to read from server pane as {arg}")
def step_impl(identifiers):
  CommonUtil.write_text_file("\nWhen I Drag and Drop variables from network variables to read from server pane as \"" + identifiers + "\"")
  obj.draganddropnetworktoserver(identifiers)
  
  
@when("I Verify if the Network Variables are available in network variable window as {arg}")
def step_impl(variables):
  CommonUtil.write_text_file("\nWhen I Verify if the Network Variables are available in network variable window as \"" + variables + "\"")
  obj.verifynetworkvariablemapping(variables)
  
@then("I selected Ok in Manage Network Variable Window")
def step_impl():
    """I selected Ok in Manage Network Variable Window"""
    CommonUtil.write_text_file("\nThen I selected Ok in Manage Network Variable Window")
    obj.buttonokselected()
    
@when("I Search and select a template in the Template Section as {arg}")
def step_impl(value):
  CommonUtil.write_text_file("\nWhen I Search and select a template in the Template Section as \"" + value + "\"")
  obj.createinstance(value)
  
@then("I verify that the template is available in the instance window as {arg}")
def step_impl(value):
    """I verify that the template is available in the instance window as '<value>'"""
    CommonUtil.write_text_file("\nThen I verify that the template is available in the instance window as \"" + value + "\"")
    obj.verifyinstance(value)
    
@then("I verify that all App facets {arg} are correctly mapped in the Hardware Instance")
def step_impl(appfacet):
    """I verify that all App facets '<appfacet>' are correctly mapped in the Hardware Instance"""
    CommonUtil.write_text_file(f"\nThen I verify that all App facets '{appfacet}' are correctly mapped in the Hardware Instance")
    obj.verifyfacetsinhardwaremappingeditor(appfacet)
    
@then("I Verify all {arg} are mapped in read from server pane")
def step_impl(identifiers):
    """I Verify all '<identifiers>' are mapped in read from server pane"""
    CommonUtil.write_text_file(f"\nThen I Verify all '{identifiers}' are mapped in read from server pane")
    obj.verifyservervariables(identifiers)
    
@when("I double-click on a {arg} in the Containers tab")
def step_impl(identifier):
  CommonUtil.write_text_file(f"\nWhen I double-click on a '{identifier}' in the Containers tab")
  obj.doubleclickincontainer(identifier)
  
@when(r"I drag and drop the '(.*)' onto the edit page and click on the '(.*)' option afterward")
def step_impl(facetnames, option):
  CommonUtil.write_text_file(f"\nWhen I drag and drop the '{facetnames}' onto the edit page and click on the '{option}' option afterward")
  Applicationutility.wait_for_execution()
  obj.draganddropinstancetoeditpage(facetnames, option)
  
@when("I click on the {arg} in Edit Page Properties")
def step_impl(arg):
  CommonUtil.write_text_file(f"\nWhen I click on the '{arg}' in Edit Page Properties")
  Applicationutility.wait_for_execution()
  obj.clickbuttononspeditpage(arg)
  
@when(r"I Click on the '(.*)' in Scada properties and Click '(.*)'")
def step_impl(button, drop_button):
  CommonUtil.write_text_file(f"\nWhen I Click on the '{button}' in Scada properties and Click '{drop_button}'")
  Applicationutility.wait_for_execution()
  obj.clickpropertiesonplantscada(button, drop_button)
  
@when("I Click on the {arg} in Restore project window")
def step_impl(arg):
  CommonUtil.write_text_file(f"\nWhen I click on the '{arg}' in Restore project window")
  obj.clickbuttonplantscada(arg)
  
@when("I Select the {arg} in Backup-Restore window")
def step_impl(arg):
  CommonUtil.write_text_file(f"\nWhen I Select the '{arg}' in Backup-Restore window")
  obj.verifyandselectfileplantscada(arg)

@when("I Check Any of the files to be added in Deployment File Section as {arg}")
def step_impl(instance_names):
    """I Check Any of the files to be added in Deployment File Section as '<instance_names>'"""
    CommonUtil.write_text_file("\nWhen I Check Any of the files to be added in Deployment File Section as \""+instance_names+"\"")
    obj.checkboxclickindeploymentfilesection(instance_names)
    
@when("I clicks on the {arg} icon from the vertical menubar")
def step_impl(sidebar):
    """I  clicks on the '<sidebar>' icon from the vertical menubar"""
    CommonUtil.write_text_file(f"\nWhen I  clicks on the '{sidebar}' icon from the vertical menubar")
    obj.clicksidebarbuttoninplantscada(sidebar)
    
@when("I Enters the '(.*)' and '(.*)' in Aveva Plant Scada Window")
def step_impl(username, password):
    """I Enters the '<username>' and '<password>' in Aveva Plant Scada Window"""
    CommonUtil.write_text_file(f"\nWhen I Enters the '{username}' and '{password}' in Aveva Plant Scada Window")
    Applicationutility.wait_for_execution()
    obj.logintoplantscada(username, password)
    
@when("I clicks the {arg} in the login dialog box")
def step_impl(button):
    """I clicks the '<button>' in the login dialog box"""
    CommonUtil.write_text_file(f"\nWhen I clicks the '{button}' in the login dialog box")
    obj.clickbuttontologinscadapage(button)
    
@when("I clicks the {arg} in the Plant Scada popup dialog box")
def step_impl(button):
    """I clicks the '<button>' in the Plant Scada popup dialog box"""
    CommonUtil.write_text_file(f"\nWhen I clicks the '{button}' in the popup dialog box")
    obj.clickbuttononscadapopup(button)
    
@then("I verifies that the Master (startup) page for HD1080 res window is opened")
def step_impl():
    """I verifies that the Master (startup) page for HD1080 res window is opened"""
    CommonUtil.write_text_file(f"\nThen I verifies that the Master (startup) page for HD1080 res window is opened")
    obj.verifymasterpagemainwindow()
    
@then("I verifies that {arg} Created in Project Explorer")
def step_impl(identifier):
    """I verifies that '<identifier>' Created in Project Explorer"""
    CommonUtil.write_text_file(f"\nThen I verifies that '{identifier}' Created in Project Explorer")
    obj.verifycontrolproject(identifier)
    
@then("I Verify the Generation PopUp Window Message")
def step_impl():
    """I Verify the Generation PopUp Window Message"""
    CommonUtil.write_text_file("\nThen I Verify the Generation PopUp Window Message")
    obj.projectexplorertabutility_After_Generation_dialog_window_Message()
    
@when("I RClick on Block Refine Offline project browser in project explorer as {arg}")
def step_impl(projectBrowser1):
    """I RClick on Block Refine Offline project browser in project explorer as '<project browser1>'"""
    CommonUtil.write_text_file("\nWhen I RClick on Block Refine Offline project browser in project explorer as \""+projectBrowser1+"\"")
    obj.textboxprojectbrowserrclickonblockrefineoffline(projectBrowser1)
    
@when("I drag and drop P2P to channel Communication Peer to Peer Pannel in communication mapping as {arg}")
def step_impl(communicationPeerToPeerPannel1):
    """I drag and drop P2P to channel Communication Peer to Peer Pannel in communication mapping as '<Communication Peer to Peer Pannel1>'"""
    CommonUtil.write_text_file("\nWhen I drag and drop P2P to channel Communication Peer to Peer Pannel in communication mapping as \""+communicationPeerToPeerPannel1+"\"")
    obj.textboxcommunicationpeertopeerpanneldraganddropp2ptochannel(communicationPeerToPeerPannel1)
  
@when("I edit P2P Properties Communication Channels Pannel in communication mapping as {arg}")
def step_impl(communicationChannelsPannel2):
    """I edit P2P Properties Communication Channels Pannel in communication mapping as '<Communication Channels Pannel2>'"""
    CommonUtil.write_text_file("\nWhen I edit P2P Properties Communication Channels Pannel in communication mapping as \""+communicationChannelsPannel2+"\"")
    obj.textboxcommunicationchannelspanneleditp2pproperties(communicationChannelsPannel2)
    
@when("I drag instance drop container page SP instance dock in supervision project as {arg}")
def step_impl(instanceDock1):
    """I drag instance drop container page SP instance dock in supervision project as '<instance dock1>'"""
    CommonUtil.write_text_file("\nWhen I drag instance drop container page SP instance dock in supervision project as \""+instanceDock1+"\"")
    obj.textboxinstancedockdraginstancedropcontainerpagesp(instanceDock1)
  
@when("I Select value list view SVP instance dock in supervision project as {arg}")
def step_impl(instanceDock2):
    """I Select value list view SVP instance dock in supervision project as '<instance dock2>'"""
    CommonUtil.write_text_file("\nWhen I Select value list view SVP instance dock in supervision project as \""+instanceDock2+"\"")
    obj.textboxinstancedockselectvaluelistviewsvp(instanceDock2)

@when("I Navigate to {arg} tab in project explorer tab")
def step_impl(CP_SP_Tab):
    """I Navigate to '<CP_SP_Tab>' tab in project explorer tab"""
    obj.Navigate_to_supervision_controlproject_tab(CP_SP_Tab)
    
@then("I Verify Navigation tab in project explorer")
def step_impl():
    """I Verify Navigation tab in project explorer"""
    CommonUtil.write_text_file("\nThen I Verify Navigation tab in project explorer")
    obj.Verify_supervision_controlproject_tab()
    
@when("I Map workstation available for respective service and engine for supervision project as {arg}")
def step_impl(Service_Engine):
    """I Map workstation available for respective service and engine for supervision project as '<Service_Engine>'"""
    CommonUtil.write_text_file("\nWhen I Map workstation available for respective service and engine for supervision project as '<Service_Engine>'")
    obj.Map_Workstation_Supervision_project(Service_Engine)
  
@when("I double click container PE container dock in project explorer as {arg}")
def step_impl(containerDock1):
    """I double click container PE container dock in project explorer as '<container dock1>'"""
    CommonUtil.write_text_file("\nWhen I double click container PE container dock in project explorer as \""+containerDock1+"\"")
    obj.textboxcontainerdockdoubleclickcontainerpe(containerDock1)
  
@then("verify supervision mapping PE service maping editor in project explorer")
def step_impl():
    """verify supervision mapping PE service maping editor in project explorer"""
    CommonUtil.write_text_file("\nThen verify supervision mapping PE service maping editor in project explorer")
    obj.textboxservicemapingeditorverifysupervisionmappingpe()
    Applicationutility.take_screenshot("Full Screenshot")
    
@when("I change controller properties with drop down options as {arg}")
def step_impl(options):
    """I change controller properties with drop down options as '<options>'"""
    CommonUtil.write_text_file("\nWhen I change controller properties with drop down options as '<options>'")
    Projectexplorertabutility.Change_Password_Protection_Controller(options)
    Applicationutility.take_screenshot("Full Screenshot")

@when("I change Settings option with drop down options as {arg}")
def step_impl(options):
    """I change Settings option with drop down options as '<options>'"""
    CommonUtil.write_text_file("\nWhen I change Settings option with drop down options as '<options>'")
    Projectexplorertabutility.Change_SettingsOption(options)
    Applicationutility.take_screenshot("Full Screenshot") 
    
@when("I change SettingsHeader  in settings window as {arg}")
def step_impl(options):
    """I change SettingsHeader  in settings window as '<Setting_Header>'"""
    CommonUtil.write_text_file("\nWhen I change SettingsHeader  in settings window as '<Setting_Header>'")
    Projectexplorertabutility.Click_on_Settings_Header(options)
    
@when("I click on Yes button in Message Box")
def step_impl():
    """I click on Yes button in Message Box"""
    CommonUtil.write_text_file("\nWhen I click on Yes button in Message Box")
    obj.yesbuttoninsettings()
    
@when("I Click tabitem in EIO configaration window in control expert as {arg}")
def step_impl(identifiers):
    """I Click tabitem in EIO configaration window in control expert as '<identifiers>'"""
    CommonUtil.write_text_file("\nWhen I Click tabitem in EIO configaration window in control expert as \""+identifiers+"\"")
    obj.ClicktabitemEIOconfigwindow(identifiers)  
    
    
@when("I Double Click on Elementary variables in Refine, configure window")
def step_impl():
    """I Double Click on Elementary variables in Refine, configure window"""
    CommonUtil.write_text_file("\nWhen I Double Click on Elementary variables in Refine, configure window")
    obj.elementvariabledoubleclick()  
    
@when("I Enter Variable name and select HMI option under Data Editor window")
def step_impl():
    """I Enter Variable name and select HMI option under Data Editor window"""
    CommonUtil.write_text_file("\nWhen I Enter Variable name and select HMI option under Data Editor window")
    obj.entervariableselecthmi()
    
@when("I Uncheck the pack CheckBox in P2P Communication Configuration window for variable {arg}")
def step_impl(identifier):
    """I Uncheck the pack CheckBox in P2P Communication Configuration window for variable '<identifier>'"""
    CommonUtil.write_text_file("\nWhen I Uncheck the pack CheckBox in P2P Communication Configuration window for variable as \""+identifier+"\"")
    obj.UnpackvariableP2Pconfigurationwindow(identifier)
    
@when("I Unmap variable in P2P communication configuration window by Context menu as {arg}")
def step_impl(identifier):
    """I Unmap variable in P2P communication configuration window by Context menu as '<identifier>'"""
    CommonUtil.write_text_file("\nWhen I Unmap variable in P2P communication configuration window by Context menu as \""+identifier+"\"")
    obj.UnmapP2Pvariablebycontextmenu(identifier)
    
@when("I Unmap variable in P2P communication configuration window by keyboard action as {arg}")
def step_impl(identifier):
    """I Unmap variable in P2P communication configuration window by keyboard action as '<identifier>'"""
    CommonUtil.write_text_file("\nWhen I Unmap variable in P2P communication configuration window by keyboard action as \""+identifier+"\"")
    obj.UnmapP2Pvariablebykeyboardaction(identifier)
    
@when("I Right Click on Variables from elementary variables tab named as {arg}")
def step_impl(identifier):
    """I Right Click on Variables from elementary variables tab named as '<identifier>'"""
    obj.RClickVariableElementaryVariableTab(identifier)
    
@when("I Run PLC Simulator")
def step_impl():
    """I Run PLC Simulator"""
    obj.RunPLCsimulator()
    
@when("I Verify backup data PE in project explorer as {arg}")
def step_impl(projectBrowser3):
    """I Verify backup data PE in project explorer as '<project browser2>'"""
    CommonUtil.write_text_file("\nWhen I Verify backup data PE in project explorer as \""+projectBrowser3+"\"")
    obj.textboxprojectbrowserverifybackupdata(projectBrowser3)
    
@when("I Drag and drop from remote varaibles to source variables in P2P as {arg}")
def step_impl(server):
    """I Drag and drop from remote varaibles to source variables in P2P as '<server>'"""
    CommonUtil.write_text_file("\nWhen I Drag and drop from remote varaibles to source variables in P2P as \""+server+"\"")
    Applicationutility.wait_in_seconds(1000,"wait")
    obj.textboxdraganddropremotetolocalP2P(server)
    
    
@when("I Enter Consecutive Variable name and select HMI option under Data Editor window and enter parameters as {arg}")
def step_impl(server):
    """I Enter Consecutive Variable name and select HMI option under Data Editor window and enter parameters as '<param>'"""
    CommonUtil.write_text_file("\nWhen I Drag and drop from remote varaibles to source variables in P2P as \""+server+"\"")
    obj.textboxclickp2pcreateconsecutivevariables(server)