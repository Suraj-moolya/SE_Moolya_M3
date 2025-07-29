"Project Explorer Utility"

import Actionutility
import Applicationutility
import Engineeringclientutility
from TopologyExplorerTab import TopologyExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
from MessageBox import MessageBox
from CurrentScreen import CurrentScreen
from ProjectExplorerTab import ProjectExplorerTab
from EngineeringClient import EngineeringClient    
from ApplicationExplorerTab import ApplicationExplorerTab
from RefineOffline import RefineOffline
from SystemServer import SystemServer
from SupervisionProject import SupervisionProject
import datetime
import os
import csv

eng_obj = EngineeringClient()
topo_obj = TopologyExplorerTab()
ses_obj = SystemExplorerScreen()
msg_obj = MessageBox()
proj_obj = ProjectExplorerTab()
aet_obj = ApplicationExplorerTab()
ref_obj = RefineOffline()
sys_obj = SystemServer()
SP_obj = SupervisionProject()

###############################################################################
# Function : right_click_control_project_browser_PE
# Description : This function performs a right-click action on a specific item 
#               in the project browser pane based on the provided identifier.
# Parameter : identifier (str) - The unique identifier of the item to be right-clicked.
# Example : right_click_control_project_browser_PE("ControlProject_1")
###############################################################################
def right_click_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  if proj_list:
    for item in proj_list:
      if item.Visible:
        if identifier == item.DataContext.Identifier.OleValue:
          item.ClickR()
          Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is Right Clicked.')
          break
    else:
      Log.Warning("Please Enter the Valid item from control project browser pane")
  else:
    Log.Warning("No items found in the project browser pane.")

###############################################################################
# Function : double_click_control_project_browser_PE
# Description : This function performs a double-click action on a specific item 
#               in the project browser pane based on the provided identifier.
# Parameter : identifier (str) - The unique identifier of the item to be double-clicked.
# Example : double_click_control_project_browser_PE("ControlProject_1")
###############################################################################
def double_click_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  if proj_list:
    for item in proj_list:
      if item.Visible and identifier in item.DataContext.Identifier.OleValue:
        item.DblClick()
        Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is Double Clicked.')
        Applicationutility.wait_in_seconds(2000, "Wait")
        break
    else:
      Log.Checkpoint(identifier + ' is already expanded or not found.')
  else:
    Log.Warning("No items found in the project browser pane.")

###############################################################################
# Function : expand_control_project_browser_PE
# Description : This function expands a specific item in the project browser pane 
#               based on the provided identifier.
# Parameter : identifier (str) - The unique identifier of the item to be expanded.
# Example : expand_control_project_browser_PE("ControlProject_1")
###############################################################################
def expand_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow() 
  if proj_list:
    for item in proj_list:
      if item.Visible and item.DataContext.Identifier != None:
        if identifier in item.DataContext.Identifier.OleValue:
          item.IsExpanded = True
          Log.Message(item.DataContext.Identifier.OleValue + ' is Expanded.')
          Applicationutility.wait_in_seconds(1000, 'Wait')
          Delay(2000, "Wait")
          break
    else:
      Log.Message(identifier + ' is not available for expansion.')
  else:
    Log.Warning("No items found in the project browser pane.")

###############################################################################
# Function : control_executeable_combo_box_PE
# Description : This function selects an item from a combo box in the project browser pane.
# Parameter : param (str) - A string in the format "service$$combo_item" where:
#                           - service: The service name to locate the combo box.
#                           - combo_item: The item to be selected from the combo box.
# Example : control_executeable_combo_box_PE("Service1$$Item1")
###############################################################################
def control_executeable_combo_box_PE(param): 
  service, combo_item = param.split('$$')
  services = proj_obj.servicemapingeditortextbox.object
  service_list = services.FindAllChildren('ClrClassName', 'ComboBox', 100)
  if service_list:
    for item in service_list:
      if service in item.DataContext.Service.OleValue:
        for i in range(item.Items.Count):
          if combo_item in item.Items.Item[i].Identifier.OleValue:
            item.SelectedIndex = i
            Log.Message('The item ' + str(item.Items.Item[i].Identifier.OleValue) + ' is selected from the combo box.')
            Applicationutility.take_screenshot()
            break
        else:
          Log.Message('No matching combo box item found.')
        break
    else:
      Log.Warning(f"Service '{service}' not found in the combo box.")
  else:
    Log.Warning("No combo boxes found in the service mapping editor.")

###############################################################################
# Function : select_instance_drag_drop_container_dock_PE
# Description : This function drags an instance from the instance dock and drops it 
#               into the container dock based on the provided identifier.
# Parameter : identifier (str) - The unique identifier of the instance to be dragged.
# Example : select_instance_drag_drop_container_dock_PE("Instance_1")
###############################################################################
def select_instance_drag_drop_container_dock_PE(identifier):
  instance_dock = proj_obj.instancedocktextbox
  container_dock = proj_obj.containerdocktextbox
  tox = container_dock.screenleft
  toy = container_dock.screentop
  instance_list = instance_dock.find_children_for_treeviewrow()
  if instance_list:
    for item in instance_list:
      if item.Visible:
        if identifier in item.DataContext.Identifier.OleValue:
          fromx = item.Width
          fromy = item.Height
          reg1 = item.ScreenLeft
          reg2 = item.ScreenTop / 2
          item.Drag(fromx / 2, fromy / 2, tox - reg1, toy - reg2)
          Log.Message('Dragging and dropping ' + str(item.DataContext.Identifier.OleValue) + ' to containers dock.')
          break
    else:
      Log.Warning(f"Instance '{identifier}' not found in the instance dock.")
  else:
    Log.Warning("No instances found in the instance dock.")

###############################################################################
# Function : create_fbd_section
# Description : Creates a specified number of FBD sections in the container dock.
# Parameter : num_sections (int) - The number of FBD sections to create.
# Example : create_fbd_section(3)
###############################################################################
def create_fbd_section(num_sections):
  num_sections = int(num_sections)
  container_dock = proj_obj.containerdocktextbox.object
  container_list = container_dock.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  if container_list:
    for containers in container_list:
      if containers.Value == "ControlProject_1":
        for i in range(num_sections):
          containers.ClickR()
          Log.Message(f"Creating FBD Section {i + 1}")
          Engineeringclientutility.select_ContextMenu_Items_EC("Create FBD Section")
          Actionutility.modal_dialog_window_button("OK")
        break
    else:
      Log.Warning("ControlProject_1 not found in the container dock.")
  else:
    Log.Warning("No containers found in the container dock.")

###############################################################################
# Function : select_instance_drag_drop_container_dock_PE1
# Description : Drags an instance from the instance dock and drops it into a 
#               specified container dock section.
# Parameter : 
#   identifier (str) - The unique identifier of the instance to be dragged.
#   dropping_point (str) - The target section where the instance will be dropped.
# Example : select_instance_drag_drop_container_dock_PE1("Instance_1", "ControlProject_1")
###############################################################################
def select_instance_drag_drop_container_dock_PE1(identifier, dropping_point):
  instance_dock = proj_obj.instancedocktextbox
  container_dock = proj_obj.containerdocktextbox.object
  container_list = container_dock.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  instance_list = instance_dock.find_children_for_treeviewrow()

  if instance_list and container_list:
    fromx = fromy = tox = toy = None

    for item in instance_list:
      if item.Visible and identifier in item.DataContext.Identifier.OleValue:
        fromx = item.ScreenLeft + (item.Width / 2)
        fromy = item.ScreenTop + (item.Height / 2)
        Log.Message(f"Found instance: {identifier}, fromx: {fromx}, fromy: {fromy}")
        break
    else:
      Log.Warning(f"No visible instance found with identifier: {identifier}")
      return

    for container in container_list:
      text_blocks = container.FindAllChildren('ClrClassName', 'TextBlock', 1000)
      if text_blocks:
        for texts in text_blocks:
          if dropping_point in texts.WPFControlText:
            tox = texts.ScreenLeft + (texts.Width / 2)
            toy = texts.ScreenTop + (texts.Height / 2)
            Log.Message(f"Found dropping point: {dropping_point}, tox: {tox}, toy: {toy}")
            break
        if tox and toy:
          break
    else:
      Log.Warning(f"No match found for dropping point: {dropping_point}")
      return

    item.Drag(fromx - item.ScreenLeft, fromy - item.ScreenTop, tox - fromx, toy - fromy)
    Applicationutility.wait_in_seconds(3000, 'Wait')
    Log.Message(f"Dragging from ({fromx}, {fromy}) to ({tox}, {toy}) completed.")
    if dropping_point == "ControlProject_1":
      Actionutility.modal_dialog_window_button("OK")
  else:
    Log.Warning("No instances or containers found for drag-and-drop operation.")

###############################################################################
# Function : multidraganddrop
# Description : Performs drag-and-drop operations for multiple controllers to 
#               their respective sections.
# Parameter : 
#   controllers (str) - A string of controller identifiers separated by "$$".
#   sections (str) - A string of section identifiers separated by "$$".
# Example : multidraganddrop("Controller1$$Controller2", "Section1$$Section2")
###############################################################################
def multidraganddrop(controllers, sections):
  controller_list = controllers.split("$$")
  section_list = sections.split("$$")

  control_dict = dict(zip(controller_list, section_list))
  for identifier, dropping_point in control_dict.items():
    Log.Message(f"Processing: {identifier} -> {dropping_point}")
    select_instance_drag_drop_container_dock_PE1(identifier, dropping_point)

###############################################################################
# Function : right_click_container_dock_context_menu_item_PE
# Description : Performs a right-click on a container dock item and selects a 
#               context menu item.
# Parameter : 
#   param (str) - A string in the format "identifier$$Context_menu_item" where:
#                 - identifier: The unique identifier of the container dock item.
#                 - Context_menu_item: The menu item to select.
# Example : right_click_container_dock_context_menu_item_PE("Page_1$$Edit")
###############################################################################
def right_click_container_dock_context_menu_item_PE(param):
  identifier, Context_menu_item = param.split('$$')
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  if container_list:
    for item in container_list:
      if item.Visible:
        if identifier in item.DataContext.Identifier.OleValue:
          item.ClickR()
          Applicationutility.wait_in_seconds(750, 'Wait')
          Engineeringclientutility.select_ContextMenu_Items_EC(Context_menu_item)
          break
    else:
      Log.Warning(f"{identifier} not in container") 
  else:
    Log.Warning('No Container objects present')   

###############################################################################
# Function : Executables_Properties
# Description : Updates the property value of an executable in the property grid.
# Parameter : 
#   Identifier_Textvalue (str) - A string in the format "Identifier$$Textvalue" where:
#                                - Identifier: The property name to update.
#                                - Textvalue: The new value to set.
# Example : Executables_Properties("PropertyName$$NewValue")
###############################################################################
def Executables_Properties(Identifier_Textvalue):
  Identifier,Textvalue = Identifier_Textvalue.split('$$')
  Identifier_list = proj_obj.executablepropertytextbox.object.FindAllChildren('ClrClassName', 'PropertyGridField', 100)
  Log.Message(len(Identifier_list))
  for i in Identifier_list:
    if Identifier in i.DataContext.DisplayName.OleValue:
      Log.Message(i.DataContext.DisplayName.OleValue)
      TextBlock = i.FindAllChildren('ClrClassName', 'TextBox', 100)
      Log.Message(TextBlock[0].Text)
      Log.Message(Textvalue)
      TextBlock[0].Text = Textvalue

###############################################################################
# Function : scroll_to_elements
# Description : Scrolls down until the specified element becomes visible.
# Parameter : 
#   element (WPFObject) - The element to scroll to.
# Example : scroll_to_elements(some_element)
###############################################################################
def scroll_to_elements(element):
  if not isinstance(element, WPFObject):
    Log.Error("Not a WPFObject")
    return

  while not element.wItemRect().Visible:
    Log.Message("Scrolling down...")
    Aliases.MainWindow.ScrollViewer.ScrollDown()
  Log.Message("Element is now visible.")

###############################################################################
# Function : verify_assignment
# Description : Verifies if a specific value and status are present in the 
#               assignments dock.
# Parameter : 
#   value_name (str) - The name of the value to verify.
#   status (str) - The status to verify.
# Example : verify_assignment("ValueName", "Status")
###############################################################################
def verify_assignment(value_name, status):
  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  facet_names = value_name.split("$$") if "$$" in value_name else [value_name]  
  for facet in facet_names:
    for instance in instance_list:
      objects = instance.FindAllChildren('ClrClassName', 'GridViewCell', 100)
      object_list = [i.Value for i in objects if hasattr(i, 'Value') and i.Value is not None]
      if facet in object_list and status in object_list:
        Log.Checkpoint(f"{facet} and status '{status}' are verified")
        break
    else:
      Log.Warning(f"{facet} and status '{status}' are not verified")   

###############################################################################
# Function : right_click_instance_in_assignments
# Description : Performs a right-click on an instance in the assignments dock.
# Parameter : 
#   facet_name (str) - The unique identifier of the instance to right-click.
# Example : right_click_instance_in_assignments("Instance_1")
###############################################################################
def right_click_instance_in_assignments(facet_name):
  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for instance in instance_list:
    if instance.Visible == True:
      if instance.DataContext.Identifier.OleValue == facet_name:
        instance.ClickR()
        break
  else:
     Log.Warning("element not found")

###############################################################################
# Function : click_FBDsection
# Description : Clicks on a specific FBD section in the container dock.
# Parameter : 
#   identifier (str) - The unique identifier of the FBD section to click.
# Example : click_FBDsection("FBDSection_1")
###############################################################################
def click_FBDsection(identifier):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier == item.DataContext.Identifier.OleValue:
        item.Click()
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Log.Message(f'{item.DataContext.Identifier.OleValue} is clicked')
        break
  else:
    Log.Message(f'{item.DataContext.Identifier.OleValue} was not clicked')

###############################################################################
# Function : select_facet_drag_drop_section_dock_PE
# Description : Drags a facet from the assignments dock and drops it into a 
#               specified section in the container dock.
# Parameter : 
#   param (str) - A string in the format "facet_name$$section_name" where:
#                 - facet_name: The name of the facet to drag.
#                 - section_name: The name of the section to drop into.
# Example : select_facet_drag_drop_section_dock_PE("Facet1$$Section1")
###############################################################################
def select_facet_drag_drop_section_dock_PE(param):
  facet_name, section_name = param.split('$$') 
  assignment_dock = proj_obj.assignmentsdocktextbox
  container_dock = proj_obj.containerdocktextbox
  facet_list = assignment_dock.find_children_for_grid_view_row()
  section_list = container_dock.find_children_for_grid_view_row()
  for section in section_list:
    if section.Visible:
      if section_name in section.DataContext.Identifier.OleValue:
        tox = section.Width
        toy = section.Height
        toL = section.ScreenLeft
        toT = section.ScreenTop
        Log.Message('The Section selected to Drop to is : ' + str(section.DataContext.Identifier.OleValue))
        break
  else:
    Log.Warning(f'{section_name} section not found in Containers dock') 
  for facet in facet_list:
    if facet.Visible:
      if facet_name in facet.DataContext.Identifier.OleValue:
        fromx = facet.Width
        fromy = facet.Height
        fromL = facet.ScreenLeft
        fromT = facet.ScreenTop
        Log.Message('The Facet selecteed to Drag is ' + str(facet.DataContext.Identifier.OleValue))
        facet.Drag(fromx/2, fromy/2, -((fromL + fromx/2)-(toL + tox/2)), -((fromT + fromy/2) - (toT + toy/2)))
        break
  else:
    Log.Warning(f'{facet_name} facet not found in Assignements dock')

###############################################################################
# Function : click_on_section_container_dock_PE
# Description : Locates and clicks on a specific section in the container dock
#               based on the provided identifier. The function searches through
#               visible container items and performs a click action when found.
# Parameter : 
#   identifier (str) - The unique identifier or partial name of the section to click
# Test Data : "FBDSection_1", "Supervision_Test"
# Example : click_on_section_container_dock_PE("FBDSection_1")
###############################################################################
def click_on_section_container_dock_PE(identifier):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.Click()  
        break 
    

###############################################################################
# Function : click_facet_in_assignments
# Description : Finds and clicks on a specific facet in the assignments textbox.
#               The function searches through visible GridViewCell items for a
#               matching facet identifier.
# Parameter : 
#   facet_name (str) - The exact identifier of the facet to be clicked
# Test Data : "ValveGP_1", "MotorGP_1" 
# Example : click_facet_in_assignments("ValveGP_1")
###############################################################################
def click_facet_in_assignments(facet_name):
  instance_list = proj_obj.assignmentstextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  Log.Message(len(instance_list))
  for instance in instance_list:
    if instance.Visible == True:
      if instance.DataContext.Identifier.OleValue == facet_name:
        instance.Click()
        break
    
###############################################################################
# Function : copy_fromfbd_instance_pastefbd
# Description : Performs a copy-paste operation of an instance between FBD sections.
#               The function:
#               1. Clicks on source FBD section
#               2. Selects and copies the specified instance
#               3. Navigates to target FBD section
#               4. Pastes the copied instance
# Parameter : 
#   param (str) - A string containing three parts separated by "$$":
#                 fromFBDSection - Source FBD section name
#                 fromInstance - Instance to be copied
#                 toFBDSection - Target FBD section name
# Test Data : "System_1$$SSMotorGP_1_MotorGP$$FBDSection_1"
#            "Section1$$Instance1$$Section2"
# Example : copy_fromfbd_instance_pastefbd("System_1$$SSMotorGP_1_MotorGP$$FBDSection_1")
###############################################################################
def copy_fromfbd_instance_pastefbd(param):
  from_FBDSection, from_instance, to_FBDSection = param.split("$$")
  click_FBDsection(from_FBDSection)
  Applicationutility.wait_in_seconds(2000, 'Wait')
  click_facet_in_assignments(from_instance) 
  Applicationutility.wait_in_seconds(2000, 'Wait')    
  Sys.Keys('^c')
  Applicationutility.wait_in_seconds(2000, 'Wait')
  click_FBDsection(to_FBDSection)
  Applicationutility.wait_in_seconds(2000, 'Wait')
  Sys.Keys('^v')
  
###############################################################################
# Function : verify_facet_assignment
# Description : Verifies the generation state of a specific facet in the assignments dock.
# Parameter : 
#   param (str) - A string in the format "facet_name$$GenerationState" where:
#                 - facet_name: The name of the facet to verify.
#                 - GenerationState: The expected generation state.
# Example : verify_facet_assignment("Facet1$$Generated")
###############################################################################
def verify_facet_assignment(param):
  facet_name, GenerationState = param.split('$$') 
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for facet in facet_list:
    if facet.Visible:
      if facet_name in facet.DataContext.Identifier.OleValue:
        if GenerationState in facet.DataContext.GenerationState.OleValue:
          Log.Checkpoint(f'The facet {facet.DataContext.Identifier.OleValue} has Generation state as {facet.DataContext.GenerationState.OleValue}') 
          break
  else:
    Log.Warning(f'The {facet_name} does not have {GenerationState}')

###############################################################################
# Function : Verify_Section_Deleted_in_ControlProject_containers
# Description : Verifies if a specific section has been deleted from the control 
#               project containers.
# Parameter : 
#   identifier (str) - The unique identifier of the section to verify.
# Example : Verify_Section_Deleted_in_ControlProject_containers("Section1")
###############################################################################
def Verify_Section_Deleted_in_ControlProject_containers(identifier):
  Applicationutility.wait_for_execution()
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        Log.Error(identifier + " Section not Deleted in Control Project containers")
        break
        Applicationutility.wait_in_seconds(750, 'Wait')
  else:
    Log.Checkpoint(identifier + " Section is Deleted in Control Project containers")

###############################################################################
# Function : Delete_Section_in_ControlProject_by_Keyboard_actions_PE
# Description : Deletes a specific section in the control project using keyboard actions.
# Parameter : 
#   identifier (str) - The unique identifier of the section to delete.
# Example : Delete_Section_in_ControlProject_by_Keyboard_actions_PE("Section1")
###############################################################################
def Delete_Section_in_ControlProject_by_Keyboard_actions_PE(identifier):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.Click()
        Log.Message(item.DataContext.Identifier.OleValue + " is selected")
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Sys.Keys("[Del]")
        Log.Message("Delete button is clicked")
    Log.Warning(f'The {facet_name} does not have {GenerationState}')

###############################################################################
# Function : Rclick_CP_header_context_menu_PE
# Description : Performs a right-click on the Control Project header and selects
#               a context menu item.
# Parameter : 
#   Context_menu_item (str) - The name of the context menu item to select.
# Example : Rclick_CP_header_context_menu_PE("Add Header")
###############################################################################
def Rclick_CP_header_context_menu_PE(Context_menu_item):
  Cp_browser = proj_obj.projectbrowsertextbox.object
  id_headers = Cp_browser.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
  for header in id_headers:
    if 'Identifier' in header.WPFControlText:
      header.ClickR()
      Applicationutility.wait_in_seconds(1000, 'Wait')
      Engineeringclientutility.select_ContextMenu_Items_EC(Context_menu_item)
      break

###############################################################################
# Function : customize_CP_header_checkbox_PE
# Description : Customizes the Control Project header by toggling a checkbox.
# Parameter : 
#   param (str) - A string in the format "check_item$$check_state" where:
#                 - check_item: The name of the checkbox.
#                 - check_state: The desired state (0 or 1).
# Example : customize_CP_header_checkbox_PE("HeaderName$$1")
###############################################################################
def customize_CP_header_checkbox_PE(param):
  check_item, check_state = param.split('$$')
  menu = eng_obj.rclickmenutextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "CheckBox", 50)    
  for item in menu_items:
    if check_item in item.WPFControlText:
      item.wState = int(check_state)
      Log.Message(f'The CheckBox for {item.WPFControlText} is changed to {check_state}')
      break
  else:
    Log.Warning('The CheckBox item {check_item} not found in list !')

###############################################################################
# Function : verify_added_headder_CPB_PE
# Description : Verifies if a specific header is added to the Control Project Browser.
# Parameter : 
#   header_name (str) - The name of the header to verify.
# Example : verify_added_headder_CPB_PE("HeaderName")
###############################################################################
def verify_added_headder_CPB_PE(header_name):
  Cp_browser = proj_obj.projectbrowsertextbox.object
  id_headers = Cp_browser.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
  for header in id_headers:
    if header_name in header.WPFControlText:
      Log.Checkpoint(f'The Header : {header_name}, is present in Control Project Browser.')
      break
  else:
    Log.Warning(f'The Header : {header_name}, is not present in Control Project Browser.')

###############################################################################
# Function : Verify_build_state_control_executeable_PE
# Description : Verifies the build state of a control executable in the project.
# Parameter : 
#   param (str) - A string in the format "Project_Name$$Control_Executeable_Name$$Build_State".
# Example : Verify_build_state_control_executeable_PE("Project1$$Executable1$$Built")
###############################################################################
def Verify_build_state_control_executeable_PE(param):
  Project_Name, Control_Executeable_Name, Build_State = param.split('$$')
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  expand_control_project_browser_PE(Project_Name)
  expand_control_project_browser_PE('Executables')
  for item in proj_list:
    if item.Visible:
      if Control_Executeable_Name in item.DataContext.Identifier.OleValue:
        if Build_State in item.DataContext.BuiltState.OleValue:
          Log.Checkpoint(f'The build status of {item.DataContext.Identifier.OleValue} of {Project_Name} is {item.DataContext.BuiltState.OleValue}')
          break
        else:
          Log.Warning(f'The build status of {item.DataContext.Identifier.OleValue} of {Project_Name} is {item.DataContext.BuiltState.OleValue}')
          break
  else:
    Log.Warning(f'The project {Project_Name} or {Control_Executeable_Name} not found !!!')    

###############################################################################
# Function : Collapse_control_project_browser_PE
# Description : Collapses all items in the Control Project Browser except "System".
# Parameter : None
# Example : Collapse_control_project_browser_PE()
###############################################################################
def Collapse_control_project_browser_PE():
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow() 
  for item in proj_list:
    if item.Visible:
      if "System" not in item.DataContext.Identifier.OleValue:
        item.IsExpanded = False
        Log.Message(item.DataContext.Identifier.OleValue + ' is Collapsed.')
        Delay(2000, "Wait")

###############################################################################
# Function : Verify_Facets_Added_or_Removed_context_menu_PE
# Description : Verifies if a facet is added or removed in the context menu.
# Parameter : 
#   facet_name (str) - The name of the facet to verify.
# Example : Verify_Facets_Added_or_Removed_context_menu_PE("FacetName")
###############################################################################
def Verify_Facets_Added_or_Removed_context_menu_PE(facet_name): 
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for facet in facet_list:
    if facet.Visible:
      if facet_name == facet.DataContext.Identifier.OleValue:
          Log.Message(facet.DataContext.Identifier.OleValue + " is Added")
          break 
  else:
    Log.Message(facet_name + " is Removed")

###############################################################################
# Function : verify_all_facet_generation_status_assignmentdock
# Description : Verifies the generation status of all facets in the assignments dock.
# Parameter : None
# Example : verify_all_facet_generation_status_assignmentdock()
###############################################################################
def verify_all_facet_generation_status_assignmentdock(): 
  Applicationutility.wait_in_seconds(2000, 'Wait')
  proj_obj.assignmentsdocktextbox.object.Refresh()
  Facet_obj = proj_obj.assignmentsdocktextbox.object
  facet_No = Facet_obj.Items.Count
  Log.Message(f'Total Facet Count : " {facet_No} " in " {Facet_obj.Items.Item[0].ContainerName} " Container Assignments Dock')
  for i in range(facet_No):
    if proj_obj.assignmentsdocktextbox.object.Items.Item[i].GenerationState == "NonGenerated":
      Log.Checkpoint(f'Facet : {Facet_obj.Items.Item[i].Identifier.OleValue} ; Generation status : {Facet_obj.Items.Item[i].GenerationState}') 
    else:
      Log.Checkpoint(f'Facet : {Facet_obj.Items.Item[i].Identifier.OleValue} ; Generation status : {Facet_obj.Items.Item[i].GenerationState}')

###############################################################################
# Function : verify_section_containers_dock
# Description : Verifies the sections in the container dock and identifies the latest one.
# Parameter : None
# Example : verify_section_containers_dock()
###############################################################################
def verify_section_containers_dock(): 
  proj_obj.containerdocktextbox.refresh()
  sections_list = proj_obj.containerdocktextbox.find_children_for_grid_view_row()
  fbdsections = {}
  for section in sections_list:
    if section.DataContext != None :
      fbdsections.update({section.Panel_ZIndex:section.DataContext.Identifier.OleValue})
  if len(fbdsections) > 1:
    Log.Message(f'{fbdsections[max(fbdsections)]} is created latest')
  else:
    Log.Message(f'Nothing new was created')

###############################################################################
# Function : Create_Multiple_section_Containers_Dock_verify
# Description : Creates multiple sections in the container dock and verifies them.
# Parameter : 
#   param (str) - A string in the format "identifier$$Context_menu_item$$n" where:
#                 - identifier: The identifier of the section.
#                 - Context_menu_item: The context menu item to select.
#                 - n: The number of sections to create.
# Example : Create_Multiple_section_Containers_Dock_verify("Section1$$Create$$3")
###############################################################################
def Create_Multiple_section_Containers_Dock_verify(param):
  identifier, Context_menu_item, n = param.split('$$')
  for i in range(int(n)):
    container_dock = proj_obj.containerdocktextbox
    proj_obj.containerdocktextbox.object.Click()
    Sys.Keys('[PageUp]')
    container_list = container_dock.find_children_for_grid_view_row()
    for item in container_list:
      if item.DataContext != None:
        if identifier in item.DataContext.Identifier.OleValue:
          item.ClickR()
          Applicationutility.wait_in_seconds(750, 'Wait')
          Engineeringclientutility.select_ContextMenu_Items_EC(Context_menu_item)
    Actionutility.modal_dialog_window_button('OK')
    verify_section_containers_dock()

###############################################################################
# Function : Drag_instance_drop_container_section
# Description : Drags an instance and drops it into a specified container section.
# Parameter : 
#   param (str) - A string in the format "instance_identifier$$section_identifier".
# Example : Drag_instance_drop_container_section("Instance1$$Section1")
###############################################################################
def Drag_instance_drop_container_section(param):
  instance_identifier, section_identifier = param.split("$$")
  instance_dock = proj_obj.instancedocktextbox
  container_dock = proj_obj.containerdocktextbox
  section_list = container_dock.find_children_for_grid_view_row()
  instance_list = instance_dock.find_children_for_treeviewrow() 
  for section in section_list:
    if section.visible and section_identifier in section.DataContext.Identifier.OleValue:
      tox = section.Top
      Log.Message(tox)
      
  for instance in instance_list:
    if instance.Level == 0:
      instance.IsExpanded = True
      Log.Message("Folder with indent level zero is expanded")
    if instance.Visible and instance_identifier in instance.DataContext.Identifier.OleValue :
      fromx = instance.Top
      fromy = instance.Height / 2
      Applicationutility.wait_in_seconds(1000, 'Wait')
      instance.Click()
      instance.Drag(fromx, fromy, 0, tox - fromx)
      Log.Message("Drag and drop operation was performed")
      break

###############################################################################
# Function : double_click_instance_in_assignments
# Description : Double-clicks on an instance in the assignments dock.
# Parameter : 
#   facet_name (str) - The unique identifier of the instance to double-click.
# Example : double_click_instance_in_assignments("Instance_1")
###############################################################################
def double_click_instance_in_assignments(facet_name):
  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for instance in instance_list:
    if instance.Visible == True:
      if instance.DataContext.Identifier.OleValue == facet_name:
        instance.DblClick()
        break
  else:
     Log.Warning("element not found")

###############################################################################
# Function : click_checkbox_in_instance_editor
# Description : Clicks on checkboxes in the instance editor for the specified values.
# Parameter : 
#   instance_name (str) - A string of instance names separated by "$$".
# Example : click_checkbox_in_instance_editor("Instance1$$Instance2")
###############################################################################
def click_checkbox_in_instance_editor(instance_name):
  values_to_check = [val.strip() for val in instance_name.split('$$')]
  instances = proj_obj.instanceeditortextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  for instance in instances:
    names = instance.FindAllChildren('ClrClassName', 'GridViewCell', 100)
    for name in names:
      if name.Value in values_to_check:
        checkbox = name.FindAllChildren('ClrClassName', 'CheckBox', 100)
        for check in checkbox:
          check.Click()

###############################################################################
# Function : saveinstanceeditor
# Description : Saves the instance editor and optionally clicks a button in a modal dialog.
# Parameter : 
#   button_name (str) - The name of the button to click in the modal dialog.
# Example : saveinstanceeditor("OK")
###############################################################################
def saveinstanceeditor(button_name):
  aet_obj.instanceeditorsavebutton.click()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  try:
    button = Actionutility.modal_dialog_window_button(button_name)
    if button:
      button.Click()
  except Exception as e:
    Log.Message(f"No '{button_name}' button found, skipping this step.")

###############################################################################
# Function : rightclickandgeneratecontainers
# Description : Performs a right-click on a container and selects the "Generate" option.
# Parameter : 
#   container (str) - The unique identifier of the container to generate.
# Example : rightclickandgeneratecontainers("Container1")
###############################################################################
def rightclickandgeneratecontainers(container):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  
  for item in container_list:
    if item.Visible:
      if container == item.DataContext.Identifier.OleValue:
        item.ClickR()
        Engineeringclientutility.select_ContextMenu_Items_EC("Generate")
        try:
          yes_button = Actionutility.modal_dialog_window_button("Yes")
          if yes_button:
            yes_button.Click()
        except Exception as e:
          Log.Message("No 'Yes' button found, skipping this step.", "error", e)
        try:
          Actionutility.modal_dialog_window_button("OK")
        except Exception as e:
          Log.Message("Good Job Broo")

###############################################################################
# Function : verify_facet_assignment_state
# Description : Verifies the assignment state of a specific facet in the assignments dock.
# Parameter : 
#   param (str) - A string in the format "facet_name$$GenerationState" where:
#                 - facet_name: The name of the facet to verify.
#                 - GenerationState: The expected generation state.
# Example : verify_facet_assignment_state("Facet1$$Generated")
###############################################################################
def verify_facet_assignment_state(param):
  facet_name, GenerationState = param.split("$$") 
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for facet in facet_list:
    if facet.Visible:
      if facet_name in facet.DataContext.Identifier.OleValue:
        if GenerationState in facet.DataContext.AssignmentState.OleValue:
          Log.Checkpoint(f'The facet {facet.DataContext.Identifier.OleValue} has AssignmentState state as {facet.DataContext.AssignmentState.OleValue}') 
          break
  else:
    Log.Warning(f'The {facet_name} does not have {AssignmentState}')

###############################################################################
# Function : verify_facet_assignment_state1
# Description : Verifies the assignment state of multiple facets against their 
#               expected states.
# Parameter : 
#   facet_names (str) - A string of facet names separated by "$$"
#   generation_state (str) - A string of expected states separated by "$$"
# Example : verify_facet_assignment_state1("Facet1$$Facet2", "Generated$$NotGenerated")
###############################################################################
def verify_facet_assignment_state1(facet_names, generation_state):
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  facet_name_list = facet_names.split("$$")
  generation_state_list = generation_state.split("$$")
  
  if len(facet_name_list) != len(generation_state_list):
    Log.Error("The number of facet names and generation states do not match.")
    return

  for facet_name, generation_state in zip(facet_name_list, generation_state_list):
    Applicationutility.wait_in_seconds(3000, 'Wait')
    Log.Message(f'Checking facet {facet_name} for generation state {generation_state}')
    for facet in facet_list:
      if facet.Visible:
        if facet_name in facet.DataContext.Identifier.OleValue:
          if generation_state in facet.DataContext.AssignmentState.OleValue:
            Log.Checkpoint(f'The facet {facet.DataContext.Identifier.OleValue} has AssignmentState state as {facet.DataContext.AssignmentState.OleValue}') 
            break
    else:
      Log.Message(f'The facet {facet_name} does not have the expected generation state: {generation_state}')

###############################################################################
# Function : right_click_instance_select_action_in_assignments 
# Description : Right-clicks on specified instances in the assignments dock and
#               performs the specified action.
# Parameter : 
#   param (str) - Instance identifier(s) separated by "$$"
#   action (str) - The action to perform from context menu
# Example : right_click_instance_select_action_in_assignments("Instance1", "Remove")
###############################################################################
def right_click_instance_select_action_in_assignments(param, action):
  facet_names = param.split("$$") if "$$" in param else [param]
  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for facet_name in facet_names:
    for instance in instance_list:
      if instance.Visible and instance.DataContext.Identifier.OleValue == facet_name and facet_name:
        instance.ClickR()
        Engineeringclientutility.select_ContextMenu_Items_EC(action)
        Log.Checkpoint(f"{action} was selected for facet name: {facet_name}")
        break

###############################################################################
# Function : right_click_control_project_browser_PE2
# Description : Performs a right-click action on a control project browser item.
#               Similar to right_click_control_project_browser_PE but uses different
#               selection method.
# Parameter : 
#   identifier (str) - The identifier of the item to right-click
# Example : right_click_control_project_browser_PE2("ControlProject_1")
###############################################################################
def right_click_control_project_browser_PE2(identifier):
  proj = proj_obj.projectbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  for pro in proj:
    if pro.DataContext is not None:
      if pro.DataContext.Identifier.OleValue == identifier:
        pro.ClickR()
        Log.Checkpoint(pro.DataContext.Identifier.OleValue + 'is Right Clicked.')

###############################################################################
# Function : rename
# Description : Renames a controller using keyboard actions, enters the new name,
#               and takes a screenshot.
# Parameter : 
#   controller (str) - The new name for the controller.
# Example : rename("NewControllerName")
###############################################################################
def rename(controller):
  Sys.Keys(controller)
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Sys.Keys("[Enter]")
  Applicationutility.take_screenshot('Taking screenshot')

###############################################################################
# Function : verify_facet_assignment_before_generate
# Description : Verifies if a facet is still assigned before generation.
# Parameter : 
#   facet_name (str) - The name of the facet to verify, supports multiple facets
#                      separated by "$$".
# Example : verify_facet_assignment_before_generate("Facet1$$Facet2")
###############################################################################
def verify_facet_assignment_before_generate(facet_name):
  facet_names = facet_name.split('$$') if "$$" in facet_name else [facet_name]
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()

  for name in facet_names:
    facet_found = False

    for facet in facet_list:
      if facet.Visible:
        if name in facet.DataContext.Identifier.OleValue:
          facet_found = True
          Log.Checkpoint(f"{name} is still assigned.")
          break

    if not facet_found:
      Log.Checkpoint(f'{name} has been successfully unassigned and is no longer visible.')
    else:
      Log.Warning(f'{name} is still present.')

###############################################################################
# Function : click_on_mapping_tab
# Description : Clicks on a specified mapping tab in the control executables property.
# Parameter : 
#   mapname (str) - The name of the mapping tab to click.
# Example : click_on_mapping_tab("MappingTabName")
###############################################################################
def click_on_mapping_tab(mapname):
  instances = proj_obj.controlexecutablesproperty.object.FindAllChildren('ClrClassName', 'RadPane', 100)
  for ins in instances:
    if ins.DataContext.Header.OleValue == mapname:
      ins.Click()

###############################################################################
# Function : verify_device_available
# Description : Verifies if specified devices are available for mapping.
# Parameter : 
#   variables (str) - Device identifiers separated by "$$".
# Example : verify_device_available("Device1$$Device2")
###############################################################################
def verify_device_available(variables):
  devices = proj_obj.servercommunicationcounterpartsdeviceio.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"'{var}' is available for mapping.") if any(dev.DataContext is not None and hasattr(dev.DataContext, 'Identifier') and dev.DataContext.Identifier == var for dev in devices) else Log.Error(f"'{var}' is not available for mapping")

###############################################################################
# Function : drag_and_drop_device_to_channel
# Description : Drags and drops a specified device to a free communication channel.
# Parameter : 
#   server (str) - The name of the server (device) to drag and drop.
# Example : drag_and_drop_device_to_channel("ServerName")
###############################################################################
def drag_and_drop_device_to_channel(server):
  devices = proj_obj.servercommunicationcounterpartsdeviceio.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for device in devices:
    if device.WPFControlText == server:
      from_x = device.ScreenLeft + (device.Width / 2)
      from_y = device.ScreenTop + (device.Height / 2)
      break
  else:
    Log.Message("No visible device found with identifier")
  for channel in channels:
    if channel.WPFControlText == "Free":
      to_x = channel.ScreenLeft + (channel.Width / 2)
      to_y = channel.ScreenTop + (channel.Height / 2)
      break
  device.Drag(from_x - device.ScreenLeft, from_y - device.ScreenTop, to_x - from_x, to_y - from_y)
  Log.Message(f"Dragging from ({from_x}, {from_y}) to ({to_x}, {to_y}) completed.")

  
###############################################################################
# Function : right_click_communication_channel
# Description : Right-clicks on a communication channel.
# Parameter : 
#   server (str) - The name of the server associated with the channel.
# Example : right_click_communication_channel("ServerName")
###############################################################################
def right_click_communication_channel(server):
  devices = [dev for dev in proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
             if dev.WPFControlText == server]
  
  if len(devices) > 1:
    devices[1].ClickR()

###############################################################################
# Function : verify_network_variable_mapping
# Description : Verifies if specified network variables are available for mapping.
# Parameter : 
#   variables (str) - Network variable identifiers separated by "$$".
# Example : verify_network_variable_mapping("Variable1$$Variable2")
###############################################################################
def verify_network_variable_mapping(variables):
  network_cells = proj_obj.networkvariabletab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"Network Variable '{var}' is available") if any(net.DataContext is not None and hasattr(net.DataContext, 'Identifier') and net.DataContext.Identifier == var for net in network_cells) else Log.Error(f"Network Variable '{var}' is not available")

###############################################################################
# Function : verify_hardware_instance_available_for_mapping
# Description : Verifies if specified hardware instances are available for mapping.
# Parameter : 
#   variables (str) - Hardware instance identifiers separated by "$$".
# Example : verify_hardware_instance_available_for_mapping("Instance1$$Instance2")
###############################################################################
def verify_hardware_instance_available_for_mapping(variables):
  channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"'{var}' is available for mapping.") if any(ch.DataContext is not None and hasattr(ch.DataContext, 'Identifier') and ch.DataContext.Identifier == var for ch in channels) else Log.Error(f"'{var}' is not available for mapping")

###############################################################################
# Function : verify_network_variable
# Description : Verifies if specified network variables exist.
# Parameter : 
#   variables (str) - Network variable names separated by "$$".
# Example : verify_network_variable("Variable1$$Variable2")
###############################################################################
def verify_network_variable(variables):
  network = proj_obj.managenetworkvariablestab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"Network Variable '{var}' is available") if any(net.DataContext is not None and hasattr(net.DataContext, 'VariableName') and net.DataContext.VariableName == var for net in network) else Log.Error(f"Network Variable '{var}' is not available")

###############################################################################
# Function : drag_and_drop_network_to_server
# Description : Drags and drops specified network variables to a server.
# Parameter : 
#   identifiers (str) - Network variable identifiers separated by "$$".
# Example : drag_and_drop_network_to_server("Variable1$$Variable2")
###############################################################################
def drag_and_drop_network_to_server(identifiers):
  Log.Message(f"Dragging and dropping with identifiers: {identifiers}")
  identifier_list = identifiers.split('$$') if '$$' in identifiers else [identifiers]
  network_cells = proj_obj.networkvariabletab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for identifier in identifier_list:
    proj_obj.communicationchanneltab.object.Refresh()
    channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
    from_cell = next((cell for cell in network_cells if cell.DataContext is not None and hasattr(cell.DataContext, 'Identifier') and cell.DataContext.Identifier == identifier), None)
    to_cell = next((cell for cell in channels if cell.DataContext is not None and hasattr(cell.DataContext, 'Identifier') and cell.DataContext.Identifier == "Empty"), None)
    if from_cell is not None and to_cell is not None:
      from_x = from_cell.ScreenLeft + from_cell.Width / 2
      from_y = from_cell.ScreenTop + from_cell.Height / 2
      to_x = to_cell.ScreenLeft + to_cell.Width / 2
      to_y = to_cell.ScreenTop + to_cell.Height / 2
      from_cell.Drag(from_x - from_cell.ScreenLeft, from_y - from_cell.ScreenTop, to_x - from_x, to_y - from_y)
      Log.Message(f"Dragging '{identifier}' from ({from_x}, {from_y}) to ({to_x}, {to_y}) completed.")
      Applicationutility.wait_in_seconds(1000, 'Wait')
    else:
      Log.Error(f"Target element not found for identifier '{identifier}'. Retrying...")
      proj_obj.communicationchanneltab.object.Refresh()
      channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
      to_cell_retry = next((cell for cell in channels if cell.DataContext is not None and hasattr(cell.DataContext, 'Identifier') and cell.DataContext.Identifier == "Empty"), None)
      if to_cell_retry is not None:
        to_x_retry = to_cell_retry.ScreenLeft + to_cell_retry.Width / 2
        to_y_retry = to_cell_retry.ScreenTop + to_cell_retry.Height / 2
        from_cell.Drag(from_x - from_cell.ScreenLeft, from_y - from_cell.ScreenTop, to_x_retry - from_x, to_y_retry - from_y)
        Log.Message(f"Retry succeeded. Dragging '{identifier}' completed.")
      else:
        Log.Error(f"Retry failed. '{identifier}' could not be dropped.")

###############################################################################
# Function : create_instance
# Description : Creates an instance using a specified template.
# Parameter : 
#   value (str) - The template name to use for creating the instance.
# Example : create_instance("TemplateName")
###############################################################################
def create_instance(value):
  template = proj_obj.createinstancetab.object.FindChild('ClrClassName', 'EditableComboBox', 100)
  template.Click()
  Log.Checkpoint("Template DropDown was Clicked")
  Sys.Keys(value)
  Sys.Keys("[Enter]")
  Log.Checkpoint("Template '{}' was selected.".format(value))

###############################################################################
# Function : verify_instance
# Description : Verifies if a specified instance exists.
# Parameter : 
#   template (str) - The name of the instance to verify.
# Example : verify_instance("InstanceName")
###############################################################################
def verify_instance(template):
  instance_dock = proj_obj.instancedocktextbox.object
  instance_list = instance_dock.FindAllChildren("ClrClassName", 'GridViewCell', 100)
  for instance in instance_list:
    if instance.Value == template:
      Log.Checkpoint(f"'{template}' is Available")
      break
    else:
      Log.Checkpoint(f"'{template}' is Not Available")

###############################################################################
# Function : project_to_hardware
# Description : Maps project facets to hardware.
# Parameter : 
#   appfacet (str) - Application facets separated by "$$".
# Example : project_to_hardware("Facet1$$Facet2")
###############################################################################
def project_to_hardware(appfacet):
  facets = appfacet.split('$$')
  scrollable_area = proj_obj.hardwareinstancetab.object
  for facet in facets:
    channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
    for channel in channels:
      if getattr(channel.DataContext, 'Identifier', None) and getattr(channel.DataContext.Identifier, 'OleValue', None) == facet:
        project_facet_value = str(channel.DataContext.MappingInterfaceTemplateIdentifier)
        from_x, from_y = channel.ScreenLeft + channel.Width / 2, channel.ScreenTop + channel.Height / 2
        break    
    while True:
      hardware = scrollable_area.FindAllChildren('ClrClassName', 'GridViewRow', 100)
      for hard in hardware:
        data_context = getattr(hard, 'DataContext', None)
        if data_context is not None:
          hardware_template = getattr(data_context, 'MappingInterfaceTemplateIdentifier', None)
          project_facet = getattr(data_context, 'ProjectFacetIdentifier', None)
          if hardware_template == project_facet_value and not project_facet:
            to_x, to_y = hard.ScreenLeft + hard.Width / 2, hard.ScreenTop + hard.Height / 2
            if hard.VisibleOnScreen:
              channel.Drag(from_x - channel.ScreenLeft, from_y - channel.ScreenTop, to_x - from_x, to_y - from_y)
              Log.Checkpoint(f"Dragged {facet} to hardware.")
              break
      else:
        scrollable_area.MouseWheel(-1)
        continue
      break

###############################################################################
# Function : verify_facets_in_hardware_mapping_editor
# Description : Verifies if specified facets are mapped in the Hardware Mapping Editor.
# Parameter : 
#   facet (str) - Application facets separated by "$$".
# Example : verify_facets_in_hardware_mapping_editor("Facet1$$Facet2")
###############################################################################
def verify_facets_in_hardware_mapping_editor(facet):
  appfacets = facet.split('$$')
  hardware = proj_obj.hardwareinstancetab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for appfacet in appfacets:
    if any(getattr(hard.DataContext, 'ProjectFacetIdentifier', None) == appfacet for hard in hardware if hard.DataContext is not None):
      Log.Checkpoint(f"'{appfacet}' successfully mapped in Hardware Mapping Editor")
    else:
      Log.Error(f"'{appfacet}' not found in Hardware Mapping Editor")

###############################################################################
# Function : verify_server_variables
# Description : Verifies if specified server variables are found in the Read From Server Window.
# Parameter : 
#   identifiers (str) - Server variable identifiers separated by "$$".
# Example : verify_server_variables("Variable1$$Variable2")
###############################################################################
def verify_server_variables(identifiers):
  identifier_list = identifiers.split('$$')
  channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for identi in identifier_list:
    if any(cell.DataContext is not None and hasattr(cell.DataContext, 'Identifier') and cell.DataContext.Identifier == identi for cell in channels):
      Log.Checkpoint(f"'{identi}' found in Read From Server Window")
    else:
      Log.Warning(f"'{identi}' not found in Read From Server Window")

###############################################################################
# Function : checkbox_click_in_deployment_file_section
# Description : Clicks a checkbox in the deployment file section.
# Parameter : 
#   filenames (str) - The filename to select.
# Example : checkbox_click_in_deployment_file_section("FileName.txt")
###############################################################################
def checkbox_click_in_deployment_file_section(filenames):
  files = proj_obj.deploymentfilesectiontab.object.FindAllChildren('ClrClassName', 'CheckBox', 100)
  for file in files:
    if hasattr(file.DataContext, 'FileName') and file.DataContext.FileName == filenames:
      file.Click()
      Log.Checkpoint(f"'{filenames}' was selected in Deployment File Section")
      return
  Log.Warning(f"'{filenames}' was not found in Deployment File Section")

###############################################################################
# Function : double_click_in_container
# Description : Double-clicks on a container in the container dock.
# Parameter : 
#   identifier (str) - The identifier of the container to double-click.
# Example : double_click_in_container("ContainerIdentifier")
###############################################################################
def double_click_in_container(identifier):
  container_doc = proj_obj.containerdocktextbox.object.Refresh()
  container_list = proj_obj.containerdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for container in container_list:
    if getattr(container.DataContext, 'Identifier', None) == identifier:
      container.DblClick()
      Log.Checkpoint(f"Double-clicked on '{identifier}'")
      Applicationutility.wait_in_seconds(1000, 'Wait')

###############################################################################
# Function : drag_and_drop_instance_to_editpage
# Description : Drags and drops an instance to the edit page.
# Parameter : 
#   facetnames (str) - Facet names separated by "$$".
#   option (str) - Options separated by "$$".
# Example : drag_and_drop_instance_to_editpage("Facet1$$Facet2", "Option1$$Option2")
###############################################################################
def drag_and_drop_instance_to_editpage(facetnames, option):
  facets = facetnames.split('$$')
  options = option.split('$$')
  facet_option_dict = dict(zip(facets, options))
  for facet, opt in facet_option_dict.items():
    instance = proj_obj.containerseditpagetab.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
    for ins in instance:
      if getattr(ins.DataContext, 'Identifier', None) and getattr(ins.DataContext.Identifier, 'OleValue', None) == facet:
        from_x, from_y = ins.ScreenLeft + ins.Width / 2, ins.ScreenTop + ins.Height / 2
        location = proj_obj.instanceeditpagetab.object
        to_x, to_y = location.ScreenLeft + location.Width / 2, location.ScreenTop + location.Height / 2
        ins.Drag(from_x - ins.ScreenLeft, from_y - ins.ScreenTop, to_x - from_x, to_y - from_y)
        Log.Checkpoint(f"Dragged '{facet}' to the edit page.")
        break
    MenuItem = proj_obj.instancelistitemtab.object.FindAllChildren('ClrClassName', 'TextBlock', 100)
    for menu in MenuItem:
      if menu.WPFControlText == opt:
        menu.Click()
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Log.Checkpoint(f"'{opt}' was selected from the menu.")
        break

###############################################################################
# Function : click_button_on_sp_editpage
# Description : Clicks a button on the supervision project edit page.
# Parameter : 
#   button (str) - The tooltip of the button to click.
# Example : click_button_on_sp_editpage("ButtonToolTip")
###############################################################################
def click_button_on_sp_editpage(button):
  for pro in proj_obj.supervisioneditpagepropertiestab.object.FindAllChildren('ClrClassName', 'ContentPresenter', 100):
    tooltip = getattr(pro.DataContext, 'ToolTip', None)
    if tooltip == button:
      pro.Click()
      Log.Checkpoint(f"'{button}' Was Clicked in Properties.")
      Applicationutility.wait_in_seconds(1000, 'Wait')

###############################################################################
# Function : click_properties_on_plant_scada
# Description : Clicks properties on the Plant SCADA tab.
# Parameter : 
#   button (str) - The label of the button to click.
#   dropdown_button (str) - The label of the dropdown button to click.
# Example : click_properties_on_plant_scada("ButtonLabel", "DropdownButtonLabel")
###############################################################################
def click_properties_on_plant_scada(button, dropdown_button):
  TestedApps.CitectIDE.Run()
  Applicationutility.wait_in_seconds(2000, 'Waiting for CitectIDE to load') 
  properties = proj_obj.plantscadapropertiestab.object.FindAllChildren('ClrClassName', 'SplitButton', 100)
  for pro in properties:
    if pro.Label == button:
      pro.Click(pro.Width - 5, pro.Height / 2)
      Log.Checkpoint(f"'{button}' Was Clicked in Scada Properties Tab")
  Applicationutility.wait_in_seconds(1000, 'Wait')    
  menuitems = proj_obj.menuitemtab.object.FindAllChildren('ClrClassName', 'Button', 100)
  for menu in menuitems:
    if menu.Label == dropdown_button:
      menu.Click()
      Log.Checkpoint(f"'{menu.Label}' Was Clicked in '{button}' DropDown")

###############################################################################
# Function : verify_and_select_file
# Description : Verifies and selects a file in the backup/restore tab.
# Parameter : 
#   file_name (str) - The name of the file to verify and select.
# Example : verify_and_select_file("BackupFile.zip")
###############################################################################
def verify_and_select_file(file_name):
  folder_views = proj_obj.backuprestoretab.object.FindAllChildren('WndClass', 'SysListView32', 100)
  edit_controls = proj_obj.backuprestoretab.object.FindAllChildren('WndClass', 'Edit', 100)
  open_button = proj_obj.backuprestoretab.object.FindAllChildren('WndCaption', '&Open', 100)
  if folder_views and edit_controls and open_button:
    if any(file_name == folder_view.wItem[i] for folder_view in folder_views for i in range(folder_view.wItemCount)):
      Log.Checkpoint(f"File '{file_name}' found and selected.")
      edit_controls[0].SetText(file_name)
      Applicationutility.wait_in_seconds(1000, 'Wait')
      open_button[0].Click()
      Log.Checkpoint(f"Open button clicked for file '{file_name}'.")
    else:
      Log.Error(f"File '{file_name}' not found.")

###############################################################################
# Function : click_button_in_aveva
# Description : Clicks a button in the AVEVA restore popup.
# Parameter : 
#   button (str) - The caption of the button to click.
# Example : click_button_in_aveva("Restore")
###############################################################################
def click_button_in_aveva(button):
  for buttons in proj_obj.restorepopuptab.object.FindAllChildren('WndClass', "Button", 100):
    if button in buttons.WndCaption:
      buttons.click()
      Log.Checkpoint(f"'{button}' button clicked.")
      return
  Log.Error(f"'{button}' button not found.")

###############################################################################
# Function : click_sidebar_button_in_plant_scada
# Description : Clicks a sidebar button in Plant SCADA.
# Parameter : 
#   sidebar (str) - The tooltip of the sidebar button to click.
# Example : click_sidebar_button_in_plant_scada("Graphics")
###############################################################################
def click_sidebar_button_in_plant_scada(sidebar):
  for item in proj_obj.sidebartab.object.FindAllChildren('ClrClassName', 'ListBoxItem', 100):
    if item.ToolTip == sidebar:
      Log.Checkpoint(f"Clicking on the '{sidebar}' button.")
      item.Click()
      Applicationutility.wait_in_seconds(1000, 'Wait')
      return
  Log.Warning(f"Button '{sidebar}' not found.")

###############################################################################
# Function : login_to_plant_scada
# Description : Logs in to Plant SCADA.
# Parameter : 
#   username (str) - The username for login.
#   password (str) - The password for login.
# Example : login_to_plant_scada("Admin", "Password")
###############################################################################
def login_to_plant_scada(username, password):
  Applicationutility.wait_in_seconds(1000, 'Wait for Login Page')
  credential_window = proj_obj.loginpageplantscada.object.FindAllChildren('WndClass', 'SysCredential', 100)
  for window in credential_window:
    editable_fields = window.FindAllChildren('WndClass', 'Edit', 100)
    if len(editable_fields) >= 2:
      username_field, password_field = editable_fields[0], editable_fields[1]
      if username_field.Exists and username_field.Enabled: username_field.SetText(username)
      if password_field.Exists and password_field.Enabled: password_field.SetText(password)

###############################################################################
# Function : click_button_to_login_scada_page
# Description : Clicks a button on the SCADA login page.
# Parameter : 
#   button (str) - The caption of the button to click.
# Example : click_button_to_login_scada_page("OK")
###############################################################################
def click_button_to_login_scada_page(button):
  buttons = proj_obj.loginpageplantscada.object.FindAllChildren('WndClass', 'Button', 100)
  for b in buttons:
    if b.WndCaption == button:
      b.Click()
      Log.Checkpoint(f"'{button}' was clicked in Login Page")

###############################################################################
# Function : click_button_on_scada_popup
# Description : Clicks a button on a SCADA popup.
# Parameter : 
#   button (str) - The caption of the button to click.
# Example : click_button_on_scada_popup("OK")
###############################################################################
def click_button_on_scada_popup(button):
  buttons = proj_obj.errorpopupplantscada.object.FindAllChildren('WndClass', 'Button', 100)
  for b in buttons:
    if b.WndCaption == button:
      b.Click()
      Log.Checkpoint(f"'{button}' was clicked in Popup")

###############################################################################
# Function : verify_master_page_main_window
# Description : Verifies if the master page main window is opened successfully.
# Parameter : None
# Example : verify_master_page_main_window()
###############################################################################
def verify_master_page_main_window():
  window = proj_obj.masterpagemainwindowplantscada
  if window is not None and window.object.Exists:
    Log.Checkpoint("The 'Master (startup) page for HD1080 res' window is opened successfully.")
  else:
    Log.Warning("The 'Master (startup) page for HD1080 res' window is NOT opened.")

###############################################################################
# Function : verify_control_project
# Description : Verifies if a control project was created in the Project Explorer.
# Parameter : 
#   identifier (str) - The identifier of the control project to verify.
# Example : verify_control_project("ControlProjectName")
###############################################################################
def verify_control_project(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  if proj_list:
    for item in proj_list:
      if item.Visible:
        if item.DataContext.Identifier.OleValue == identifier:
          Log.Checkpoint(f"'{item.DataContext.Identifier.OleValue}' Was Created in Project Explorer")
          break
    else:
      Log.Warning(f'{identifier} was not created')
  else:
    Log.Warning('No objects created')

###############################################################################
# Function : After_Generation_dialog_window_Message
# Description : Verifies the message in the After Generation dialog window.
# Parameter : None
# Example : After_Generation_dialog_window_Message()
###############################################################################
def After_Generation_dialog_window_Message():
  TextBlock_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  for i in TextBlock_list:
    if "perform generation" in i.WPFControlText:
      Log.Message(f'{i.WPFControlText} Message successfully verified')
      break
  else:
    Log.Message("Message not successfully verified")

###############################################################################
# Function : drag_and_drop_P2P_to_channel
# Description : Drags and drops a P2P communication to a channel.
# Parameter : 
#   val (str) - The value to identify the P2P communication.
# Example : drag_and_drop_P2P_to_channel("P2PCommunicationName")
###############################################################################
def drag_and_drop_P2P_to_channel(val):
  SCC_P2P = proj_obj.communicationpeertopeerpanneltextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  channels = proj_obj.communicationchannelspanneltextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  
  for P2P in SCC_P2P:
    if val in P2P.WPFControlText:
      Sys.HighlightObject(P2P)
      from_x = P2P.ScreenLeft + (P2P.Width / 2)
      from_y = P2P.ScreenTop + (P2P.Height / 2)
      break
  else:
    Log.Message("No visible device found with identifier")
  for channel in channels:
    if channel.WPFControlText == "Free":
      Sys.HighlightObject(channel)
      to_x = channel.ScreenLeft + (channel.Width / 2)
      to_y = channel.ScreenTop + (channel.Height / 2)
      break
     
  P2P.Drag(from_x - P2P.ScreenLeft, from_y - P2P.ScreenTop, to_x - from_x, to_y - from_y)
  Log.Message(f"Dragging from ({from_x}, {from_y}) to ({to_x}, {to_y}) completed.")    

###############################################################################
# Function : edit_P2P_Properties
# Description : Edits properties of a P2P communication channel.
# Parameter : 
#   param (str) - A string in the format "field$$val" where:
#                 - field: The name of the property to edit.
#                 - val: The new value for the property.
# Example : edit_P2P_Properties("FieldName$$NewValue")
###############################################################################
def edit_P2P_Properties(param):
  field, val = param.split('$$')
  items = msg_obj.channelpropertiesdialogtextbox.object.FindAllChildren('ClrClassName', 'ContentPresenter', 100)
  for item in items:
    if item.DataContext.DisplayName.OleValue == field:
      text_box = item.FindAllChildren('ClrClassName', 'TextBox', 10)
      text_box[0].wText = val 
      Log.Message(text_box[0].wText + " is entered")
      break
  else:
    Log.Message(field + " not found")

###############################################################################
# Function : Right_click_on_variable
# Description : Right-clicks on a variable in the manage network variables tab.
# Parameter : 
#   var_name (str) - The name of the variable to right-click.
# Example : Right_click_on_variable("VariableName")
###############################################################################
def Right_click_on_variable(var_name):
  items = msg_obj.managenetworkvariablestextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for item in items:
    if var_name == item.DataContext.VariableName.OleValue:
      item.ClickR()
      Log.Message(item.DataContext.VariableName.OleValue + " is right clicked")      
      Click_on_remove()
      break

def Click_on_remove():
  remove = eng_obj.rclickmenutextbox.object.FindAllChildren('Name', 'WPFObject("MenuItem", "Remove", 1)', 10)
  remove[0].Click()
  Log.Message("Clicked on Remove button")

###############################################################################
# Function : Navigate_CP_SP_Tab_PE
# Description : Navigates to a specific tab in the Control Project or Supervision Project.
# Parameter : 
#   identifier (str) - The identifier of the tab to navigate to.
# Example : Navigate_CP_SP_Tab_PE("ControlProjectTab")
###############################################################################
def Navigate_CP_SP_Tab_PE(identifier):
  proj = proj_obj.projectbrowsertextbox.object
  proj_list = proj.FindAllChildren('ClrClassName', 'RadPane', 100)
  for item in proj_list:
    if item.Visible:
      if identifier in item.WPFControlName:
        item.Click()
        Log.Message(item.WPFControlName + ' is  Clicked.')
        Delay(2000, "Wait")
  else:
    Log.Message('No identifier found : ' + item.WPFControlName)

###############################################################################
# Function : Verify_CP_SP_Tab_PE
# Description : Verifies if the specified tab in the Control Project or Supervision Project is active.
# Parameter : None
# Example : Verify_CP_SP_Tab_PE()
###############################################################################
def Verify_CP_SP_Tab_PE():
  proj = proj_obj.projectbrowsertextbox.object
  proj_list = proj.FindAllChildren('ClrClassName', 'RadPane', 100)
  for item in proj_list:
    if item.IsActive:
      Log.Message(item.WPFControlName + ' is  Active and verified.')

###############################################################################
# Function : Click_On_EngineValue_notassigned
# Description : Clicks on an engine value that is not assigned in the service mapping editor.
# Parameter : 
#   service (str) - The name of the service to locate the unassigned engine value.
# Example : Click_On_EngineValue_notassigned("ServiceName")
###############################################################################
def Click_On_EngineValue_notassigned(service, state):
#  service, state = param.split("$$")
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Map = proj_obj.supervisionworkspacetextbox.object
  supervision_grid = Map.FindChild('WPFControlName', 'ServiceMappingGrid', 1000)
  Map_List = Map.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Map_List:
    if service in str(i.DataContext.Service):
      service_list = i.FindAllChildren('ClrClassName', 'TextBlock', 100)
      for j in service_list:
        if j.Text.OleValue == state:
          j.Click()
          Applicationutility.wait_in_seconds(1000, 'Wait')
          break

###############################################################################
# Function : map_workstation
# Description : Maps a workstation to a service in the service mapping editor.
# Parameter : 
#   param (str) - A string in the format "service$$engine" where:
#                 - service: The name of the service.
#                 - engine: The name of the engine to map.
# Example : map_workstation("ServiceName$$EngineName")
###############################################################################
def map_workstation(param):
  service, state, engine = param.split("$$")
  Click_On_EngineValue_notassigned(service, state)
  Map = proj_obj.servicemapdropdownbox.object
  Map_List = Map.FindAllChildren('ClrClassName', 'TextBlock', 100)
  
  if Map_List:
    for i in Map_List:
      if i.Text == engine:
        i.Click()
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Log.Message(f'{i.Text} was clicked')
        break
    else:
      Log.Message(f'{i.Text} doesnt exists')
  else:
    Log.Warning('No Service mapping drop down exists.')


###############################################################################
# Function : double_click_container_dock_context_menu_item_PE
# Description : Double-clicks on a container dock item and selects a context menu item.
# Parameter : 
#   identifier (str) - The unique identifier of the container dock item.
# Example : double_click_container_dock_context_menu_item_PE("Page_1$$Edit")
###############################################################################
def double_click_container_dock_context_menu_item_PE(identifier):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.DblClick()
        break
  else:
    Log.Warning(identifier + ' Not in container')

###############################################################################
# Function : verify_supervision_service_maping_PE
# Description : Verifies the mapping of services in the Supervision Project.
# Parameter : None
# Example : verify_supervision_service_maping_PE()
###############################################################################
def verify_supervision_service_maping_PE(): 
  services = proj_obj.servicemapingeditortextbox.object
  service_list = services.FindAllChildren('ClrClassName', 'ComboBox', 100)
  for item in service_list:
    if item.DataContext.Service.OleValue != '':
      if 'Not Assigned' not in item.DataContext.DisplayName.OleValue:
        if item.DataContext.SelectedText.OleValue != '':
          Log.Checkpoint(f'{item.DataContext.Service.OleValue} : is mapped to {item.DataContext.DisplayName.OleValue} and {item.DataContext.SelectedText.OleValue}')
        else:
          Log.Warning(f'NIC is not mapped for {item.DataContext.Service.OleValue}')
      else:
        Log.Warning(f'{item.DataContext.Service.OleValue} : is not mapped')

###############################################################################
# Function : Change_Password_Protection_Controller
# Description : Changes the password protection setting for a controller.
# Parameter : 
#   param (str) - A string in the format "field_label$$options" where:
#                 - field_label: The label of the field to change.
#                 - options: The new option to select.
# Example : Change_Password_Protection_Controller("PasswordProtection$$Enabled")
###############################################################################
def Change_Password_Protection_Controller(param):
  field_label, options = param.split("$$")
  controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
  for control in controller_row:
    Log.Message(getattr(getattr(control, "DataContext", None), "DisplayName", None))
    if getattr(getattr(control, "DataContext", None), "DisplayName", None) == field_label:
      control.Click()
      aqUtils.Delay(500)
      for item in eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "ComboBoxItem", 10):
        if item.WPFControlText == options:
          item.Click() if item.Enabled else Log.Error("Dropdown item 'False' is disabled.")
          return
  Log.Error("Could not find the specific 'Controller' element.")

###############################################################################
# Function : Click_on_Settings_Header
# Description : Clicks on a specific settings header in the Controller settings window.
# Parameter : 
#   settings (str) - The name of the settings header to click.
# Example : Click_on_Settings_Header("GeneralSettings")
###############################################################################
def Click_on_Settings_Header(settings):
  tab_List = proj_obj.projectcontrollersettingtab.find_children_for_treeviewrow()
  for tab in tab_List:
    if settings in tab.DataContext.Identifier.OleValue :
      tab.Click()
      Log.Message(f'{settings}  found in Controller settings window and is Clicked')
      break 
  else:
    Log.Message(f'{settings} not found in Controller settings window')

###############################################################################
# Function : Change_SettingsOption
# Description : Changes a settings option in the Controller settings window.
# Parameter : 
#   option (str) - The name of the option to select.
# Example : Change_SettingsOption("OptionName")
###############################################################################
def Change_SettingsOption(option):
  prop = proj_obj.settingspropertytab.object
  container_list = prop.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  prop.FindAllChildren('ClrClassName', 'ToggleButton', 100)[0].Click()
  dropdown_items = proj_obj.settingsdropdownpropertytab.object.FindAllChildren('ClrClassName', 'ComboBoxItem', 100)
  for drop_item in dropdown_items:
    if drop_item.WPFControlText == option:
      drop_item.Click()
      Log.Checkpoint(f"Clicked on '{option}' item.")
      break
  else:
    Log.Warning(f"{option} not found")

###############################################################################
# Function : Enter_Variable_select_HMI
# Description : Enters a variable name and selects it in the HMI editor.
# Parameter : 
#   Variablename (str) - The name of the variable to enter and select.
# Example : Enter_Variable_select_HMI("VariableName")
###############################################################################
def Enter_Variable_select_HMI(Variablename):
  topo_obj.prmgensettings.object.Click()
  Sys.Keys("[Enter]")
  Sys.Keys(Variablename)
  for i in range(6):
    Sys.Keys("[Right]")
  Sys.Keys("[Enter]")

###############################################################################
# Function : Click_Variable_animation_table_Variable_Tab
# Description : Locates and clicks on a variable in the animation table variable tab.
# Parameter : 
#   variable_name (str) - The name of the variable to locate and click.
# Example : Click_Variable_animation_table_Variable_Tab("VariableName")
###############################################################################
def Click_Variable_animation_table_Variable_Tab(variable_name):
  textbox = proj_obj.animationtablewindow.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in textbox:
    Log.Message((i.Name))
    if variable_name in i.Name:
      Log.Message(len(textbox))
      i.Click()
      Log.Message(f'{variable_name} in data editior was clicked')
      break
  else:
    Log.Message(f'{variable_name} does not exists')

###############################################################################
# Function : Click_on_variable_and_change_data_value_animation_table
# Description : Changes the data value of a variable in the animation table.
# Parameter : 
#   param (str) - A string in the format "presentvalue$$changedValue" where:
#                 - presentvalue: The current value of the variable.
#                 - changedValue: The new value to set.
# Example : Click_on_variable_and_change_data_value_animation_table("OldValue$$NewValue")
###############################################################################
def Click_on_variable_and_change_data_value_animation_table(param):
  presentvalue, changedValue = param.split("$$")
  Click_Variable_animation_table_Variable_Tab(presentvalue)
  Sys.Keys(changedValue)
  Sys.Keys("[Enter]")

###############################################################################
# Function : Click_Variable_Elementary_Initiate_animationtable_Tab
# Description : Initiates a variable in the animation table tab.
# Parameter : 
#   variable_name (str) - The name of the variable to initiate.
# Example : Click_Variable_Elementary_Initiate_animationtable_Tab("VariableName")
###############################################################################
def Click_Variable_Elementary_Initiate_animationtable_Tab(variable_name):
  textbox = topo_obj.prmgensettingsrefineonline.object.FindAllChildren('Name', 'TextObject(*)', 100)
  Log.Message(len(textbox))
  for i in textbox:
    Log.Message(i.Name)
    if variable_name in i.Name:
      i.Click()
      Sys.Keys("^T")
      Log.Message(f'{variable_name} in data editior was clicked')
      break
  else:
    Log.Message(f'{variable_name} does not exists')

###############################################################################
# Function : Click_Variable_Elementary_Variable_Tab
# Description : Locates and clicks on a variable in the elementary variable tab.
# Parameter : 
#   variable_name (str) - The name of the variable to locate and click.
# Example : Click_Variable_Elementary_Variable_Tab("VariableName")
###############################################################################
def Click_Variable_Elementary_Variable_Tab(variable_name):
  textbox = topo_obj.prmgensettingsrefineonline.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in textbox:
    if variable_name in i.Name:
      i.Click()
      Log.Checkpoint(f'{variable_name} in data editior was clicked')
      break
  else:
    Log.Warning(f'{variable_name} does not exists')
###############################################################################
# Function : Verify_Variable_Elementary_Variable_Tab
# Description : Locates and verifies a variable in the elementary variable tab.
# Parameter : 
#   variable_name (str) - The name of the variable to locate and click.
# Example : Verify_Variable_Elementary_Variable_Tab("VariableName")
###############################################################################
def Verify_Variable_Elementary_Variable_Tab(variable_name):
    textbox = topo_obj.prmgensettingsrefineonline.object.FindAllChildren('Name', 'TextObject(*)', 100)
    for i in textbox:
      if variable_name in i.Name:
        Log.Checkpoint(f'{i.Name} in data editior was created')
        break
    else:
      Log.Warning(f'{variable_name} does not exists')
###############################################################################
# Function : Click_P2p_Create_consecutive_variables
# Description : Creates consecutive variables in the P2P configuration.
# Parameter : 
#   param (str) - A string in the format "variable_name$$HMi_Column_no$$desired_variable_name_input" where:
#                 - variable_name: The base variable name.
#                 - HMi_Column_no: The column number in the HMI.
#                 - desired_variable_name_input: The desired variable name prefix.
# Example : Click_P2p_Create_consecutive_variables("BaseVariable$$2$$NewVariable")
###############################################################################
def Click_P2p_Create_consecutive_variables(param):
  variable_name, HMi_Column_no, desired_variable_name_input = param.split("$$")
  variable_number = 1
  for i in range(2):
    desired_variable_name = desired_variable_name_input + str(variable_number)
    Click_Variable_Elementary_Variable_Tab(variable_name)
    Sys.Keys("[Down]")
    Sys.Keys("[Enter]")
    Sys.Keys(desired_variable_name )
    variable_number = 2
    variable_name = desired_variable_name 
    for i in range(int(HMi_Column_no)):
      Sys.Keys("[Right]")
    Sys.Keys("[Enter]")
    Verify_Variable_Elementary_Variable_Tab(desired_variable_name)
###############################################################################
# Function : change_datatype_dataeditor
# Description : Changes the data type of a variable in the data editor.
# Parameter : 
#   param (str) - A string in the format "variablename$$desired_data_type" where:
#                 - variablename: The name of the variable.
#                 - desired_data_type: The new data type to set.
# Example : change_datatype_dataeditor("VariableName$$NewDataType")
###############################################################################
def change_datatype_dataeditor(param):
  variablename, desired_data_type = param.split("$$")
  textbox = topo_obj.prmgensettings.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in textbox:
    Log.Message(i.Name)
    if variablename in i.Name:
      i.Click()
      Sys.Keys("[Right]")
      Sys.Keys(desired_data_type)
      Log.Message(f'data type is successfully changed')
      break
  else:
    Log.Message(f'data type does not exists')

###############################################################################
# Function : Unpack_Variable
# Description : Unpacks a variable in the P2P communication configuration window.
# Parameter : 
#   identifier (str) - The identifier of the variable to unpack.
# Example : Unpack_Variable("VariableIdentifier")
###############################################################################
def Unpack_Variable(identifier):
  Variablename = proj_obj.loadp2pvariablestabcontrol.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Variablename:
    if identifier in i.DataContext.Identifier.OleValue and i.Visible == True:
      i.DataContext.IsPack = "False"
      Log.Message(f'{i.DataContext.Identifier.OleValue} has been successfully changed the Pack Status')
      break
  Log.Message(f'{i.DataContext.Identifier.OleValue} does not exist in the P2P Communication Configuration window')

###############################################################################
# Function : Unmap_Variable
# Description : Unmaps a variable in the P2P communication configuration window.
# Parameter : 
#   identifier (str) - The identifier of the variable to unmap.
# Example : Unmap_Variable("VariableIdentifier")
###############################################################################
def Unmap_Variable(identifier):
  Variablename = proj_obj.loadp2pvariablestabcontrol.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Variablename:
    if identifier in i.DataContext.Identifier.OleValue and i.Visible == True:
      i.ClickR()
      proj_obj.unmapvariable.object.Click()
      Log.Message(f'{i.DataContext.Identifier.OleValue} has been successfully Unmapped')
      break
  Log.Message(f'{i.DataContext.Identifier.OleValue} does not exist in the P2P Communication Configuration window')

###############################################################################
# Function : Unmap_Variable_by_Keyboard_action
# Description : Unmaps a variable using keyboard actions in the P2P communication configuration window.
# Parameter : 
#   identifier2 (str) - The identifier of the variable to unmap.
# Example : Unmap_Variable_by_Keyboard_action("VariableIdentifier")
###############################################################################
def Unmap_Variable_by_Keyboard_action(identifier2):
  Variablename = proj_obj.loadp2pvariablestabcontrol.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Variablename:
    if identifier2 in i.DataContext.Identifier.OleValue and i.Visible == True:
      i.Click()
      Sys.Keys("[Del]")
      Log.Message(f'{i.DataContext.Identifier.OleValue} has been successfully Unmapped')
      break
  Log.Message(f'{i.DataContext.Identifier.OleValue} does not exist in the P2P Communication Configuration window')  

###############################################################################
# Function : change_variable_value
# Description : Changes the value of a variable in the data editor.
# Parameter : 
#   param (str) - A string in the format "Variable$$Value" where:
#                 - Variable: The name of the variable.
#                 - Value: The new value to set.
# Example : change_variable_value("VariableName$$NewValue")
###############################################################################
def change_variable_value(param):
  Variable , Value = param.split("$$")
  textbox = proj_obj.mdiclientwindowtextbox.object.FindAllChildren('WndCaption', 'Table[Data Editor]', 100)
  for i in textbox:
    textbox1 = i.FindAllChildren('Name', 'TextObject(*)', 100)
  for j in textbox1:
    if Variable in j.Text:
      Log.Message(j.Text)
      Log.Message(j.Id)
      j.Click()
      Sys.Keys("[Right]")
      Sys.Keys("[Enter]")
      Sys.Keys(Value)
      Sys.Keys("[Enter]")
      Log.Message(f'Variable value is successfully changed')
      break
  else:
    Log.Message(f'Variable does not exists')

###############################################################################
# Function : change_FBD_Value
# Description : Changes the value of a variable in an FBD block.
# Parameter : 
#   param (str) - A string in the format "source_variable$$desired_variable" where:
#                 - source_variable: The current variable name.
#                 - desired_variable: The new variable name to set.
# Example : change_FBD_Value("OldVariable$$NewVariable")
###############################################################################
def change_FBD_Value(param):
  source_variable, desired_variable = param.split("$$")
  textbox = ref_obj.fbdsectionwindowtextbox.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in textbox:
    if i.Text == source_variable:
      i.DblClick()
      Sys.Keys(desired_variable)
      Sys.Keys("[Enter]")

###############################################################################
# Function : verify_variable_value_FBDBlock
# Description : Verifies the value of a variable in an FBD block.
# Parameter : 
#   value (str) - The value of the variable to verify.
# Example : verify_variable_value_FBDBlock("VariableValue")
###############################################################################
def verify_variable_value_FBDBlock(value):
  textbox = ref_obj.fbdsectionwindowtextbox.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for j in textbox:
    if value in j.Text:
      Log.Message(f'{j.Text} has been successfully verified in the screen')
      Applicationutility.take_screenshot()
      break
  else:
    Log.Message(f'{j.Text} does not exists in the screen')
    Applicationutility.take_screenshot()

###############################################################################
# Function : Run_PLC_Simulator
# Description : Launches the PLC Simulator application.
# Parameter : None
# Example : Run_PLC_Simulator()
###############################################################################
def Run_PLC_Simulator():
  TestedApps.PLCSimulatorStarter.Run()

###############################################################################
# Function : Verify_backup_data_PE
# Description : Verifies backup data in the Control Project.
# Parameter : 
#   param (str) - The name of the controller to verify backup data for.
# Example : Verify_backup_data_PE("ControllerName")
###############################################################################
def Verify_backup_data_PE(param):
  param = "Workstation_1"
  row_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for row in row_list:
    if param in row.DataContext.Controller.OleValue:   
      Log.Message("Description: " + row.DataContext.Description.OleValue)
      Log.Message("BackupTime: " + row.DataContext.BackupTime.OleValue)
      Log.Message("User: " + row.DataContext.User.OleValue)
      Log.Message("Executable: " + row.DataContext.Executable.OleValue)
      Log.Message("Controller: " + row.DataContext.Controller.OleValue)       
      break
  else:
    Log.Message("Message not successfully verified")

###############################################################################
# Function : drag_and_drop_remote_to_local_P2P
# Description : Drags and drops a remote variable to a local variable in P2P communication.
# Parameter : 
#   param (str) - A string in the format "target$$source" where:
#                 - target: The target variable.
#                 - source: The source variable.
# Example : drag_and_drop_remote_to_local_P2P("TargetVariable$$SourceVariable")
###############################################################################
def drag_and_drop_remote_to_local_P2P(param):
  target, source = param.split("$$")
  devices = proj_obj.remotevariablebutton.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  channels = proj_obj.sourcevariablebutton.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for device in devices:
    if device.DataContext.Identifier.OleValue == source:
      from_x = device.ScreenLeft + (device.Width / 2)
      from_y = device.ScreenTop + (device.Height / 2)
      break
  else:
    Log.Message("No visible device found with identifier")
  for channel in channels:
    if channel.DataContext.Identifier.OleValue == target:
      to_x = channel.ScreenLeft + (channel.Width / 2)
      to_y = channel.ScreenTop + (channel.Height / 2)
      break
  device.Drag(from_x - device.ScreenLeft, from_y - device.ScreenTop, to_x - from_x, to_y - from_y)
  Log.Message(f"Dragging from ({from_x}, {from_y}) to ({to_x}, {to_y}) completed.")

###############################################################################
# Function : Edit_IODevice_Properties
# Description : Edits the properties of an I/O device.
# Parameter : 
#   param (str) - A string in the format "field_label$$options" where:
#                 - field_label: The label of the field to edit.
#                 - options: The new option to select.
# Example : Edit_IODevice_Properties("DeviceName$$OptionName")
###############################################################################
def Edit_IODevice_Properties(param):
  field_label, options = param.split("$$")
  controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
  for control in controller_row:
    if getattr(getattr(control, "DataContext", None), "DisplayName", None) == field_label:
      control.DblClick()
      aqUtils.Delay(500)
      for item in eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "RadioButton", 100):
        if item.WPFControlText == options:
          if item.Enabled:
            item.Click() 
            Sys.Keys('[Esc]')
          else:
            Log.Error("Dropdown item 'False' is disabled.")
          return
  Log.Error("Could not find the specific 'Controller' element.")

###############################################################################
# Function : Expand_IODevice_section
# Description : Expands a specific I/O device section in the assignments dock.
# Parameter : 
#   param (str) - The name of the I/O device section to expand.
# Example : Expand_IODevice_section("IODeviceName")
###############################################################################
def Expand_IODevice_section(param):
  IODevices_row = proj_obj.assignmentsdocktextbox.object.FindAllChildren("Name", "WPFObject('CheckedVisual')", 100)
  for list in IODevices_row:
    if param == list.DataContext.Identifier.OleValue:
      list.Click()
      Log.Message(list.DataContext.Identifier.OleValue + " is expanded")
      break     
  else:
    Log.Message(param + " is expanded")

###############################################################################
# Function : Map_IO_Devices
# Description : Maps an I/O device to a service in the service mapping editor.
# Parameter : 
#   param (str) - A string in the format "service$$field$$engine" where:
#                 - service: The name of the service.
#                 - field: The field to map.
#                 - engine: The engine to map to.
# Example : Map_IO_Devices("ServiceName$$FieldName$$EngineName")
###############################################################################
def Map_IO_Devices(param):
  service, field, engine = param.split("$$")
  Click_On_Topological_entity_IODvices(service, field)
  Map = proj_obj.servicemapdropdownbox.object
  Map_List = Map.FindAllChildren('ClrClassName', 'TextBlock', 100)
  for i in Map_List:
    if i.Text == engine:
      i.Click()
      Log.Message(f'{i.Text} was clicked')
      break
  else:
    Log.Message(f'{i.Text} doesnt exists')

def Click_On_Topological_entity_IODvices(service, field):
  Map = proj_obj.controlexecutablesproperty.object
  Map_List = Map.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Map_List:
    if service in str(i.DataContext.Identifier.OleValue):
      service_list = i.FindAllChildren('ClrClassName', 'GridViewCell', 100)
      for j in service_list:
        if str(j.WPFControlOrdinalNo) == field:
          j.Click()
          return 

###############################################################################
# Function : Settings_SP
# Description : Navigates to a specific settings section in the Supervision Project.
# Parameter : 
#   header (str) - The name of the settings section to navigate to.
# Example : Settings_SP("PageTemplates")
###############################################################################
def Settings_SP(header):
  window = SP_obj.settingswindow.object
  sections = window.FindAllChildren('ClrClassName', 'TextBlock', 100)
  for section in sections:
    if section.Text == header:
      section.Click()
      Log.Checkpoint("Page Templates is clicked")

###############################################################################
# Function : verify_page_template
# Description : Verifies the default page template in the Supervision Project.
# Parameter : None
# Example : verify_page_template()
###############################################################################
def verify_page_template():
  temp = SP_obj.pagetemplate.object
  default = temp.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for template in default:
    if template.item.IsDefault == True:
      identifier = template.item.Identifier
      Log.Checkpoint(f"{identifier} template selected as default")

###############################################################################
# Function : click_on_systemmodel
# Description : Clicks on a specific button in the system model toolbar.
# Parameter : 
#   button (str) - The automation ID of the button to click.
# Example : click_on_systemmodel("SystemModelButton")
###############################################################################
def click_on_systemmodel(button):
  appbar = SP_obj.refineapplicationbar.object
  verticalbar = appbar.FindAllChildren('ClrClassName', 'Button', 100)
  for menu in verticalbar:
    if menu.WPFControlAutomationId == button:
      menu.Click()
      Log.Checkpoint(f"{button} is clicked")

###############################################################################
# Function : click_on_equipment_exportall
# Description : Clicks the "Export All" button in the equipment toolbar.
# Parameter : 
#   button1 (str) - The automation ID of the "Export All" button.
# Example : click_on_equipment_exportall("ExportAllButton")
###############################################################################
def click_on_equipment_exportall(button1):
  Applicationutility.wait_in_seconds(1000, 'Wait')
  commandbar = SP_obj.refinesystemmodelcommandbar.object
  horizontalbar = commandbar.FindAllChildren('ClrClassName', 'Button', 100)
  for button in horizontalbar:
    if button.WPFControlAutomationId == button1:
      button.Click()
      Log.Checkpoint(f"{button1} is clicked")

###############################################################################
# Function : Enter_systemName_systemlocation_ExportDataWindow_SPRefine
# Description : Enters the system name and location in the export data window.
# Parameter : 
#   name (str) - The name of the system to enter.
# Example : Enter_systemName_systemlocation_ExportDataWindow_SPRefine("SystemName")
###############################################################################
def Enter_systemName_systemlocation_ExportDataWindow_SPRefine(name):
  if not Project.Variables.VariableExists(name):
    Project.Variables.AddVariable(name, "String")
  Project.Variables.SupervisionProject = str(name + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Log.Message(Project.Variables.SupervisionProject)
  Applicationutility.wait_in_seconds(2000, "Wait")
  Export_window = SP_obj.exportdatawindow.object
  
  if Export_window.Exists:
    Sys.Keys("[Del]")
    filename_textbox = SP_obj.exportdatafilename.object
    filename_textbox.Keys(Project.Variables.SupervisionProject)
  else:
    Log.Warning("Export Windows doesnt exists")
  filelocation = SP_obj.exportdatafilelocation
  tox = (filelocation.object.Height) / 2
  toy = 10
  filelocation.click_at(tox, toy)
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")

###############################################################################
# Function : Click_on_Savebutton_in_ExportData
# Description : Clicks the save button in the export data window.
# Parameter : 
#   btn (str) - The caption of the save button to click.
# Example : Click_on_Savebutton_in_ExportData("Save")
###############################################################################
def Click_on_Savebutton_in_ExportData(btn):
  savebutton = SP_obj.exportdatawindow.object.FindAllChildren('WndClass', 'Button', 10)
  for button in savebutton:
    if btn in button.WndCaption:
      button.Click()
      Log.Checkpoint(f"{btn} button is clicked")

###############################################################################
# Function : Click_on_RefineSystemModel_menubar
# Description : Clicks a menu item in the Refine System Model menubar.
# Parameter : 
#   menu (str) - The automation ID of the menu item to click.
# Example : Click_on_RefineSystemModel_menubar("MenuItemID")
###############################################################################
def Click_on_RefineSystemModel_menubar(menu):
  sysmodelmenubar = SP_obj.refinesystemmodelmenubar.object
  menubar = sysmodelmenubar.FindAllChildren('ClrClassName', 'Button', 100)
  for menuitem in menubar:
    if menu in menuitem.WPFControlAutomationId:
      menuitem.Click()
      Applicationutility.wait_in_seconds(1000, 'Wait')
      Log.Checkpoint(f"{menu} is clicked")

      
def drag_between_labels(label1, offset_x=30):
    ref_obj.mdiwindowtextbox.object.Maximize()
    elements = ref_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not elements:
        Log.Warning("No text objects found.")
        return 
    obj1 = next((e for e in elements if label1 in e.Text and e.Visible), None)
    obj2 = next((e for e in elements if "T" in e.Text and e.Visible), None) 
    if obj1 is None or obj2 is None:
        Log.Warning(f"Could not find '{label1}' text objects.")
        return 
    mid_x = ((obj1.ScreenLeft + obj1.Width // 2) + (obj2.ScreenLeft + obj2.Width // 2)) // 2 + offset_x
    mid_y = ((obj1.ScreenTop + obj1.Height // 2) + (obj2.ScreenTop + obj2.Height // 2)) // 2 
    parent = obj1.Parent
    start_x = mid_x - parent.ScreenLeft
    start_y = mid_y - parent.ScreenTop
    end_x = start_x + offset_x
    Applicationutility.wait_in_seconds(1000, 'wait')
    parent.Drag(110, 14, 172, 14)
#    parent.Drag(start_x, start_y, end_x, start_y)
    Log.Message(f"Dragged from ({start_x}, {start_y}) to ({end_x}, {start_y})")

 
def lksdf():
  drag_between_labels("Name")
      