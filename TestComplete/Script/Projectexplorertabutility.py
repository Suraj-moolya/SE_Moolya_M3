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
import Actionutility
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



def right_click_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  for item in proj_list:
    if item.Visible:
      if identifier == item.DataContext.Identifier.OleValue:
        item.ClickR()
        Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is Right Clicked.')
        break
  else:
    Log.Warning("Please Enter the Valid item from control project browser pane")
    
   
def double_click_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  for item in proj_list:
    if item.Visible and identifier in item.DataContext.Identifier.OleValue:
      #if not item.IsExpanded:
        item.DblClick()
        Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is Double Clicked.')
        Applicationutility.wait_in_seconds(2000, "Wait")
        break
  else:
    Log.Checkpoint(item.DataContext.Identifier.OleValue + ' is already expanded.')
        
def expand_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow() 
  for item in proj_list:
    if item.Visible and item.DataContext.Identifier != None:
      if identifier in item.DataContext.Identifier.OleValue:
        item.IsExpanded = True
        Log.Message(item.DataContext.Identifier.OleValue + ' is Expanded.')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Delay(2000,"Wait")
        break
  else:
    Log.Message(item.DataContext.Identifier.OleValue + ' is not available for expansion')
        

  
def control_executeable_combo_box_PE(param): 
  service, combo_item = param.split('$$')
  services = proj_obj.servicemapingeditortextbox.object
  service_list = services.FindAllChildren('ClrClassName', 'ComboBox', 100)
  for item in service_list:
    if service in item.DataContext.Service.OleValue:
      for i in range(item.Items.Count):
        if combo_item in item.Items.Item[i].Identifier.OleValue:
          item.SelectedIndex = i
          Log.Message('The item ' + str(item.Items.Item[i].Identifier.OleValue) + ' is seclected from the combo box.')
          break
      else:
        Log.Message('No combo box item : ' + str(item.Items.Item[i].Identifier.OleValue))
  
  
def select_instance_drag_drop_container_dock_PE(identifier):
  instance_dock = proj_obj.instancedocktextbox
  container_dock = proj_obj.containerdocktextbox
  tox = container_dock.screenleft
  toy = container_dock.screentop
  instance_list = instance_dock.find_children_for_treeviewrow()
  for item in instance_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        fromx = item.Width
        fromy = item.Height
        reg1 = item.ScreenLeft
        reg2 = item.ScreenTop/2
        item.Drag(fromx/2, fromy/2, tox-reg1, toy-reg2)
        Log.Message('Dragging and dropping ' + str(item.DataContext.Identifier.OleValue) + ' to containers dock.')
        break

def create_fbd_section(num_sections):
  num_sections = int(num_sections)
  container_dock = proj_obj.containerdocktextbox.object
  container_list = container_dock.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
  for containers in container_list:
    if containers.Value == "ControlProject_1":
      for i in range(num_sections):
        containers.ClickR()
        Log.Message(f"Creating FBD Section {i + 1}")
        Engineeringclientutility.select_ContextMenu_Items_EC("Create FBD Section")
        Actionutility.modal_dialog_window_button("OK")
      break
   

def select_instance_drag_drop_container_dock_PE1(identifier, dropping_point):
    
    instance_dock = proj_obj.instancedocktextbox
    container_dock = proj_obj.containerdocktextbox.object
    container_list = container_dock.FindAllChildren('ClrClassName', 'GridViewCell', 1000)
    instance_list = instance_dock.find_children_for_treeviewrow()

    fromx = fromy = tox = toy = None

    for item in instance_list:
        if item.Visible and identifier in item.DataContext.Identifier.OleValue:
            fromx = item.ScreenLeft + (item.Width / 2)
            fromy = item.ScreenTop + (item.Height / 2)
            Log.Message(f"Found instance: {identifier}, fromx: {fromx}, fromy: {fromy}")
            break
    else:
        Log.Message(f"No visible instance found with identifier: {identifier}")
        return

    for container in container_list:
        text_blocks = container.FindAllChildren('ClrClassName', 'TextBlock', 1000)
        
        for texts in text_blocks:
            if dropping_point in texts.WPFControlText:
                tox = texts.ScreenLeft + (texts.Width / 2)
                toy = texts.ScreenTop + (texts.Height / 2)
                Log.Message(f"Found dropping point: {dropping_point}, tox: {tox}, toy: {toy}")
                break
        if tox and toy:
            break

    if tox is None or toy is None:
        Log.Message(f"No match found for dropping point: {dropping_point}")
        return

    item.Drag(fromx - item.ScreenLeft, fromy - item.ScreenTop, tox - fromx, toy - fromy)
    Applicationutility.wait_in_seconds(3000, 'Wait')
    Log.Message(f"Dragging from ({fromx}, {fromy}) to ({tox}, {toy}) completed.")
    if dropping_point == "ControlProject_1":
      Actionutility.modal_dialog_window_button("OK")
      
                
def multidraganddrop(controllers, sections):

  controller_list = controllers.split("$$")
  section_list = sections.split("$$")

  control_dict = dict(zip(controller_list, section_list))
  for identifier, dropping_point in control_dict.items():
    Log.Message(f"Processing: {identifier} -> {dropping_point}")
    select_instance_drag_drop_container_dock_PE1(identifier, dropping_point)
  
        
def right_click_container_dock_context_menu_item_PE(param):
  identifier, Context_menu_item = param.split('$$')
  container_dock = proj_obj.containerdocktextbox
  #Log.Message(str(container_dock))
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
    
def mika():
  right_click_container_dock_context_menu_item_PE("Page_1$$Edit")

        
def Executables_Properties(Identifier_Textvalue):
  Identifier,Textvalue = Identifier_Textvalue.split("$$")
  Identifier_list = proj_obj.executablepropertytextbox.object.FindAllChildren('ClrClassName', 'PropertyGridField', 100)
  Log.Message(len(Identifier_list))
  for i in Identifier_list:
    if Identifier in i.DataContext.DisplayName.OleValue:
      Log.Message(i.DataContext.DisplayName.OleValue)
      TextBlock = i.FindAllChildren('ClrClassName', 'TextBox', 100)
      Log.Message(TextBlock[0].Text)
      Log.Message(Textvalue)
      TextBlock[0].Text = Textvalue

def scroll_to_elements(element):
    if not isinstance(element, WPFObject):
        Log.Error("Not a WPFObject")
        return

    while not element.wItemRect().Visible:
        Log.Message("Scrolling down...")
        Aliases.MainWindow.ScrollViewer.ScrollDown()
    Log.Message("Element is now visible.")
 

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
      
def right_click_instance_in_assignments(facet_name):
  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for instance in instance_list:
    if instance.Visible == True:
      if instance.DataContext.Identifier.OleValue == facet_name:
        instance.ClickR()
        break
  else:
     Log.Warning("element not found")
     

    
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
        Log.Message('The Facet selected to Drag is : ' + str(facet.DataContext.Identifier.OleValue))
        facet.Drag(fromx/2, fromy/2, -((fromL + fromx/2)-(toL + tox/2)), -((fromT + fromy/2) - (toT + toy/2)))
        break
  else:
    Log.Warning(f'{facet_name} facet not found in Assignements dock')
    
def gsgsgs():
  select_facet_drag_drop_section_dock_PE('ValveGP_1$$Supervision_Test')

def click_on_section_container_dock_PE(identifier):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.Click()  
        break 
    

def click_facet_in_assignments(facet_name):
  instance_list = proj_obj.assignmentstextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  Log.Message(len(instance_list))
  for instance in instance_list:
    if instance.Visible == True:
      if instance.DataContext.Identifier.OleValue == facet_name:
        instance.Click()
        break
    
### copy from fbd instance paste fbd         
def copy_fromfbd_instance_pastefbd(param):
  from_FBDSection,from_instance,to_FBDSection = param.split("$$")
  click_FBDsection(from_FBDSection)
  Applicationutility.wait_in_seconds(2000, 'Wait')
  click_facet_in_assignments(from_instance) 
  Applicationutility.wait_in_seconds(2000, 'Wait')    
  Sys.Keys('^c')
  Applicationutility.wait_in_seconds(2000, 'Wait')
  click_FBDsection(to_FBDSection)
  Applicationutility.wait_in_seconds(2000, 'Wait')
  Sys.Keys('^v')
  
def gsgsgs2323():
  copy_fromfbd_instance_pastefbd('System_1$$SSMotorGP_1_MotorGP$$FBDSection_1')
        
def verify_facet_assignment(param):
  facet_name, GenerationState = param.split("$$") 
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for facet in facet_list:
    if facet.Visible:
      if facet_name in facet.DataContext.Identifier.OleValue:
        if GenerationState in facet.DataContext.GenerationState.OleValue:
          Log.Checkpoint(f'The facet {facet.DataContext.Identifier.OleValue} has Generation state as {facet.DataContext.GenerationState.OleValue}') 
          break
  else:
    Log.Warning(f'The {facet_name} does not have {GenerationState}')
   
          
def Verify_Section_Deleted_in_ControlProject_containers(identifier):
  Applicationutility.wait_for_execution()
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        Log.Error(identifier+" Section not Deleted in Control Project containers")
        break
        Applicationutility.wait_in_seconds(750, 'Wait')
  else:
    Log.Checkpoint(identifier+" Section is Deleted in Control Project containers")
          
def Delete_Section_in_ControlProject_by_Keyboard_actions_PE(identifier):
  container_dock = proj_obj.containerdocktextbox
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.Click()
        Log.Message(item.DataContext.Identifier.OleValue+" is selected")
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Sys.Keys("[Del]")
        Log.Message("Delete button is clicked")
    Log.Warning(f'The {facet_name} does not have {GenerationState}')


def Rclick_CP_header_context_menu_PE(Context_menu_item):
  Cp_browser = proj_obj.projectbrowsertextbox.object
  id_headers = Cp_browser.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
  for header in id_headers:
    if 'Identifier' in header.WPFControlText:
      header.ClickR()
      Applicationutility.wait_in_seconds(1000, 'Wait')
      Engineeringclientutility.select_ContextMenu_Items_EC(Context_menu_item)
      break
  
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
 
def verify_added_headder_CPB_PE(header_name):
  Cp_browser = proj_obj.projectbrowsertextbox.object
  id_headers = Cp_browser.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
  for header in id_headers:
    if header_name in header.WPFControlText:
      Log.Checkpoint(f'The Header : {header_name}, is present in Control Project Browser.')
      break
  else:
    Log.Warning(f'The Header : {header_name}, is not present in Control Project Browser.')
         
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
        
def Collapse_control_project_browser_PE():
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow() 
  for item in proj_list:
    if item.Visible:
      if "System" not in item.DataContext.Identifier.OleValue:
        item.IsExpanded = False
        Log.Message(item.DataContext.Identifier.OleValue + ' is Collapsed.')
        Delay(2000,"Wait")
               
def Verify_Facets_Added_or_Removed_context_menu_PE(facet_name): 
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for facet in facet_list:
    if facet.Visible:
      if facet_name == facet.DataContext.Identifier.OleValue:
          Log.Message(facet.DataContext.Identifier.OleValue+" is Added")
          break 
  else:
    Log.Message(facet_name+" is Removed")        

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
    
def Create_Multiple_section_Containers_Dock_verify(param):
  identifier,Context_menu_item,n = param.split('$$')
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
      

def Drag_instance_drop_container_section(param):
  instance_identifier,section_identifier = param.split("$$")
  instance_dock = proj_obj.instancedocktextbox
  container_dock = proj_obj.containerdocktextbox
  section_list = container_dock.find_children_for_grid_view_row()
  instance_list = instance_dock.find_children_for_treeviewrow() 
  for section in section_list:
    if section.visible and section_identifier in section.DataContext.Identifier.OleValue:
      tox = section.Top
      
  for instance in instance_list:
    if instance.Level == 0:
      instance.IsExpanded = True
      Log.Message("Folder with indent level zero is expanded")
    if instance_identifier in instance.DataContext.Identifier.OleValue :
      fromx = instance.Top
      fromy = instance.Height / 2
      Applicationutility.wait_in_seconds(1000, 'Wait')
      instance.Click()
      instance.Drag(fromx,fromy,0,tox/2+25)
      Log.Message("Drag and drop operation was performed")
      break
    

def double_click_instance_in_assignments(facet_name):
  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for instance in instance_list:
    if instance.Visible == True:
      if instance.DataContext.Identifier.OleValue == facet_name:
        instance.DblClick()
        break
  else:
     Log.Warning("element not found")
     
     
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
          
          
def saveinstanceeditor(button_name):
  aet_obj.instanceeditorsavebutton.click()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  try:
    button = Actionutility.modal_dialog_window_button(button_name)
    if button:
      button.Click()
  except Exception as e:
    Log.Message(f"No '{button_name}' button found, skipping this step.")

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
          
def gsgsgsg():
  rightclickandgeneratecontainers("M580_Standalone")

        
        
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
    
def verify_facet_assignment_state1(facet_names, generation_state):
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  facet_name_list = facet_names.split("$$")
  generation_state_list = generation_state.split("$$")
  
  if len(facet_name_list) != len(generation_state_list):
    Log.Error("The number of facet names and generation states do not match.")
    return

  for facet_name, generation_state in zip(facet_name_list, generation_state_list):
    Log.Message(f'Checking facet {facet_name} for generation state {generation_state}')
    for facet in facet_list:
      if facet.Visible:
        if facet_name in facet.DataContext.Identifier.OleValue:
          if generation_state in facet.DataContext.AssignmentState.OleValue:
            Log.Checkpoint(f'The facet {facet.DataContext.Identifier.OleValue} has AssignmentState state as {facet.DataContext.AssignmentState.OleValue}') 
            break
    else:
      Log.Warning(f'The facet {facet_name} does not have the expected generation state: {generation_state}')
   

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
        
def ahfdhjv():
  right_click_instance_select_action_in_assignments('MotorGP_1_MotorGP',"Unlink")        
 
#def right_click_instance_select_action_in_assignments(param):
#  #facet_names = param.split("$$") if "$$" in param else [param]
#  instance_list = proj_obj.assignmentsdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
##  for facet_name in facet_names:
#  for instance in instance_list:
#    if instance.Visible:
#      if instance.DataContext.Identifier.OleValue == facet_name:
#        instance.ClickR()
#          #Engineeringclientutility.select_ContextMenu_Items_EC(action)
#        Log.Message(f"{facet_name} was right clicked")
#        break

def right_click_control_project_browser_PE2(identifier):
  proj = proj_obj.projectbrowsertextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 100)
  for pro in proj:
    if pro.DataContext is not None:
      if pro.DataContext.Identifier.OleValue == identifier:
        pro.ClickR()
        Log.Checkpoint(pro.DataContext.Identifier.OleValue + 'is Right Clicked.')
        
        
def rename(controller):
  Sys.Keys(controller)
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Sys.Keys("[Enter]")
  Applicationutility.take_screenshot('Taking screenshot')

def verify_facet_assignment_before_generate(facet_name):
  facet_names = facet_name.split("$$") if "$$" in facet_name else [facet_name]
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
  
  
def click_on_mapping_tab(mapname):
  instances = proj_obj.controlexecutablesproperty.object.FindAllChildren('ClrClassName', 'RadPane', 100)
  for ins in instances:
    if ins.DataContext.Header.OleValue == mapname:
      ins.Click()
      
def verify_device_available(variables):
  devices = proj_obj.servercommunicationcounterpartsdeviceio.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"'{var}' is available for mapping.") if any(dev.DataContext is not None and hasattr(dev.DataContext, 'Identifier') and dev.DataContext.Identifier == var for dev in devices) else Log.Error(f"'{var}' is not available for mapping")

  
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
  
                
def right_click_communication_channel(server):
    devices = [dev for dev in proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
               if dev.WPFControlText == server]
    
    if len(devices) > 1:
        devices[1].ClickR()

def verify_network_variable_mapping(variables):
  network_cells = proj_obj.networkvariabletab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"Network Variable '{var}' is available") if any(net.DataContext is not None and hasattr(net.DataContext, 'Identifier') and net.DataContext.Identifier == var for net in network_cells) else Log.Error(f"Network Variable '{var}' is not available")
  
  
def verify_hardware_instance_available_for_mapping(variables):
  channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"'{var}' is available for mapping.") if any(ch.DataContext is not None and hasattr(ch.DataContext, 'Identifier') and ch.DataContext.Identifier == var for ch in channels) else Log.Error(f"'{var}' is not available for mapping")

          
def verify_network_variable(variables):
  network = proj_obj.managenetworkvariablestab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for var in variables.split('$$') if '$$' in variables else [variables]:
    Log.Checkpoint(f"Network Variable '{var}' is available") if any(net.DataContext is not None and hasattr(net.DataContext, 'VariableName') and net.DataContext.VariableName == var for net in network) else Log.Error(f"Network Variable '{var}' is not available")

    
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

        
def create_instance(value):
  template = proj_obj.createinstancetab.object.FindChild('ClrClassName', 'EditableComboBox', 100)
  template.Click()
  Log.Checkpoint("Template DropDown was Clicked")
  Sys.Keys(value)
  Sys.Keys("[Enter]")
  Log.Checkpoint("Template '{}' was selected.".format(value))
#  root = proj_obj.createinstancetab.object.FindChild('ClrClassName', 'MaskPresenter', 100)
#  root.Click()
#  Log.Checkpoint("Instance Location Button was Clicked")

def sgsgsg():
  create_instance("MotorGP")
  
def verify_instance(template):
  instance_dock = proj_obj.instancedocktextbox.object
  instance_list = instance_dock.FindAllChildren("ClrClassName", 'GridViewCell', 100)
  for instance in instance_list:
    if instance.Value == template:
      Log.Checkpoint(f"'{template}' is Available")
      break
    else:
      Log.Checkpoint(f"'{template}' is Not Available")


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
      
      
def verify_facets_in_hardware_mapping_editor(facet):
  appfacets = facet.split('$$')
  hardware = proj_obj.hardwareinstancetab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for appfacet in appfacets:
    if any(getattr(hard.DataContext, 'ProjectFacetIdentifier', None) == appfacet for hard in hardware if hard.DataContext is not None):
      Log.Checkpoint(f"'{appfacet}' successfully mapped in Hardware Mapping Editor")
    else:
      Log.Error(f"'{appfacet}' not found in Hardware Mapping Editor")

def verify_server_variables(identifiers):
  identifier_list = identifiers.split('$$')
  channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for identi in identifier_list:
    if any(cell.DataContext is not None and hasattr(cell.DataContext, 'Identifier') and cell.DataContext.Identifier == identi for cell in channels):
      Log.Checkpoint(f"'{identi}' found in Read From Server Window")
    else:
      Log.Warning(f"'{identi}' not found in Read From Server Window")
      
      
def checkbox_click_in_deployment_file_section(filenames):
  files = proj_obj.deploymentfilesectiontab.object.FindAllChildren('ClrClassName', 'CheckBox', 100)
  for file in files:
    if hasattr(file.DataContext, 'FileName') and file.DataContext.FileName == filenames:
      file.Click()
      Log.Checkpoint(f"'{filenames}' was selected in Deployment File Section")
      return
  Log.Warning(f"'{filenames}' was not found in Deployment File Section")

def kadfj():
  checkbox_click_in_deployment_file_section("Includes")
  

def double_click_in_container(identifier):
  container_doc = proj_obj.containerdocktextbox.object.Refresh()
  container_list = proj_obj.containerdocktextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for container in container_list:
    if getattr(container.DataContext, 'Identifier', None) == identifier:
      container.DblClick()
      Log.Checkpoint(f"Double-clicked on '{identifier}'")
      Applicationutility.wait_in_seconds(1000, 'Wait')
      
        
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
        

def click_button_on_sp_editpage(button):
  for pro in proj_obj.supervisioneditpagepropertiestab.object.FindAllChildren('ClrClassName', 'ContentPresenter', 100):
    tooltip = getattr(pro.DataContext, 'ToolTip', None)
    if tooltip == button:
      pro.Click()
      Log.Checkpoint(f"'{button}' Was Clicked in Properties.")
      Applicationutility.wait_in_seconds(1000, 'Wait')
      
      
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

#def click_browse_button():
#  browse_buttons = proj_obj.restoreprojecttab.object.FindAllChildren('WndCaption', '&Browse...', 100)
#  if browse_buttons:
#    browse_buttons[0].Click()
#    Log.Checkpoint("Browse button was clicked successfully.")
#  else:
#    Log.Error("Browse button was not found.")
    
    
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

    
def click_button_in_aveva(button):
  for buttons in proj_obj.restorepopuptab.object.FindAllChildren('WndClass', "Button", 100):
    if button in buttons.WndCaption:
      buttons.click()
      Log.Checkpoint(f"'{button}' button clicked.")
      return
  Log.Error(f"'{button}' button not found.")
      
def skdfh():
  click_button_in_aveva("Yes")
    
    
def click_sidebar_button_in_plant_scada(sidebar):
  for item in proj_obj.sidebartab.object.FindAllChildren('ClrClassName', 'ListBoxItem', 100):
    if item.ToolTip == sidebar:
      Log.Checkpoint(f"Clicking on the '{sidebar}' button.")
      item.Click()
      Applicationutility.wait_in_seconds(1000, 'Wait')
      return
  Log.Warning(f"Button '{sidebar}' not found.")
  
  
def login_to_plant_scada(username, password):
  Applicationutility.wait_in_seconds(1000, 'Wait for Login Page')
  credential_window = proj_obj.loginpageplantscada.object.FindAllChildren('WndClass', 'SysCredential', 100)
  for window in credential_window:
    editable_fields = window.FindAllChildren('WndClass', 'Edit', 100)
    if len(editable_fields) >= 2:
      username_field, password_field = editable_fields[0], editable_fields[1]
      if username_field.Exists and username_field.Enabled: username_field.SetText(username)
      if password_field.Exists and password_field.Enabled: password_field.SetText(password)

      
def click_button_to_login_scada_page(button):
  buttons = proj_obj.loginpageplantscada.object.FindAllChildren('WndClass', 'Button', 100)
  for b in buttons:
    if b.WndCaption == button:
      b.Click()
      Log.Checkpoint(f"'{button}' was clicked in Login Page")

def click_button_on_scada_popup(button):
  buttons = proj_obj.errorpopupplantscada.object.FindAllChildren('WndClass', 'Button', 100)
  for b in buttons:
    if b.WndCaption == button:
      b.Click()
      Log.Checkpoint(f"'{button}' was clicked in Popup")
      
      
def verify_master_page_main_window():
  window = proj_obj.masterpagemainwindowplantscada
  if window is not None and window.object.Exists:
    Log.Checkpoint("The 'Master (startup) page for HD1080 res' window is opened successfully.")
  else:
    Log.Warning("The 'Master (startup) page for HD1080 res' window is NOT opened.")

    
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
    
def hadj(): 
  drag_and_drop_device_to_channel("ControlExecutable")  
  
def sfkj():
  channels = proj_obj.communicationchanneltab.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  for ch in channels:
    if ch.DataContext.MappingInterfaceTemplateIdentifier:
      Log.Message(ch.DataContext.MappingInterfaceTemplateIdentifier)
      

def After_Generation_dialog_window_Message():
  TextBlock_list = msg_obj.modaldialogwindowtextbox.object.FindAllChildren('ClrClassName', 'TextBlock', 1000)
  for i in TextBlock_list:
      if "perform generation" in i.WPFControlText:
        Log.Message(f'{i.WPFControlText} Message successfully verified')
        break
  else:
    Log.Message("Message not successfully verified")
          
        
def drag_and_drop_P2P_to_channel(val):#ControlExecutable
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
    Log.Message(field+" not found")
 
def Right_click_on_variable(var_name):
  items = msg_obj.managenetworkvariablestextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for item in items:
    if var_name == item.DataContext.VariableName.OleValue:
      item.ClickR()
      Log.Message( item.DataContext.VariableName.OleValue+ " is right clicked")      
      Click_on_remove()
      break
      
def sssg():
  Right_click_on_variable("Var5")
            
def Click_on_remove():
  remove = eng_obj.rclickmenutextbox.object.FindAllChildren('Name', 'WPFObject("MenuItem", "Remove", 1)', 10)
  remove[0].Click()
  Log.Message("Clicked on Remove button")

  
def Navigate_CP_SP_Tab_PE(identifier):
  proj = proj_obj.projectbrowsertextbox.object
  proj_list = proj.FindAllChildren('ClrClassName', 'RadPane', 100)
  for item in proj_list:
    if item.Visible:
      if identifier in item.WPFControlName:
        item.Click()
        Log.Message(item.WPFControlName + ' is  Clicked.')
        Delay(2000,"Wait")
  else:
    Log.Message('No identifier found : ' + item.WPFControlName)
    
def gsgsg():
  Navigate_CP_SP_Tab_PE("SupervisionProject")

def Verify_CP_SP_Tab_PE():
  proj = proj_obj.projectbrowsertextbox.object
  proj_list = proj.FindAllChildren('ClrClassName', 'RadPane', 100)
  for item in proj_list:
    if item.IsActive:
        Log.Message(item.WPFControlName + ' is  Active and verified.')
        
def Click_On_EngineValue_notassigned(service):
  Map = proj_obj.controlexecutablesproperty.object
  Map_List = Map.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Map_List:
    if service in str(i.DataContext.Service):
      service_list = i.FindAllChildren('ClrClassName', 'TextBlock', 100)
      for j in service_list:
          if j.Text.OleValue == "Not Assigned":
            j.Click()
            break
      
          
def map_workstation(param):
  service, engine = param.split("$$")
  Click_On_EngineValue_notassigned(service)
  Map = proj_obj.servicemapdropdownbox.object
  Map_List = Map.FindAllChildren('ClrClassName', 'TextBlock', 100)
  for i in Map_List:
    if i.Text == engine:
      i.Click()
      Log.Message(f'{i.Text} was clicked')
      break
  else:
    Log.Message(f'{i.Text} doesnt exists')
   
# will ad this later need to analyze properly for now we can skip this wont matter much  
#def verify_nic_cards_available_mapping(param):
#  service, engine = param.split("$$")
#  Map = proj_obj.servicemapdropdownbox.object
#  Map_List = Map.FindAllChildren('ClrClassName', 'TextBlock', 100)
#  for i in Map_List:
#    if i.Text == engine:
#      i.Click()
#      Log.Message(f'{i.Text} was clicked')
#      break
#  else:
#    Log.Message(f'{i.Text} doesnt exists')

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
  
  
def Click_on_Settings_Header(settings):
  tab_List = proj_obj.projectcontrollersettingtab.find_children_for_treeviewrow()
  for tab in tab_List:
    if settings in tab.DataContext.Identifier.OleValue :
      tab.Click()
      Log.Message(f'{settings}  found in Controller settings window and is Clicked')
      break 
  else:
    Log.Message(f'{settings} not found in Controller settings window')
  
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
    
 

def Enter_Variable_select_HMI(Variablename):
  topo_obj.prmgensettings.object.Click()
  Sys.Keys("[Enter]")
  Sys.Keys(Variablename)
  for i in range(6):
    Sys.Keys("[Right]")
  Sys.Keys("[Enter]")
  
  
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
    
def shsshhssh():
  Click_Variable_Elementary_Variable_Tab("0")
    
def Click_on_variable_and_change_data_value_animation_table(param):
  presentvalue, changedValue = param.split("$$")
  Click_Variable_animation_table_Variable_Tab(presentvalue)
  Sys.Keys(changedValue)
  Sys.Keys("[Enter]")
  
def gsgsgsgsg():
  Click_on_variable_and_change_data_value_animation_table("0$$162")
  
    
    
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
    
def gsgs1g():
  RClick_Variable_Elementary_Variable_Tab('SE1')
  
def Click_Variable_Elementary_Variable_Tab(variable_name):
  textbox = topo_obj.prmgensettingsrefineonline.object.FindAllChildren('Name', 'TextObject(*)', 100)
  Log.Message(len(textbox))
  for i in textbox:
    Log.Message(i.Name)
    if variable_name in i.Name:
      i.Click()
      Log.Message(f'{variable_name} in data editior was clicked')
      break
  else:
    Log.Message(f'{variable_name} does not exists')

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
       
def change_datatype_dataeditor(param):
  variablename,desired_data_type = param.split("$$")
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
    
def Unpack_Variable(identifier):
  Variablename = proj_obj.loadp2pvariablestabcontrol.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Variablename:
   if identifier in i.DataContext.Identifier.OleValue and i.Visible == True:
    i.DataContext.IsPack = "False"
    Log.Message(f'{i.DataContext.Identifier.OleValue} has been successfully changed the Pack Status')
    break
  Log.Message(f'{i.DataContext.Identifier.OleValue} does not exist in the P2P Communication Configuration window')
    
  
def Unmap_Variable(identifier):
  Variablename = proj_obj.loadp2pvariablestabcontrol.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Variablename:
   if identifier in i.DataContext.Identifier.OleValue and i.Visible == True:
    i.ClickR()
    proj_obj.unmapvariable.object.Click()
    Log.Message(f'{i.DataContext.Identifier.OleValue} has been successfully Unmapped')
    break
  Log.Message(f'{i.DataContext.Identifier.OleValue} does not exist in the P2P Communication Configuration window')
  
def Unmap_Variable_by_Keyboard_action(identifier2):
  Variablename = proj_obj.loadp2pvariablestabcontrol.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Variablename:
   if identifier2 in i.DataContext.Identifier.OleValue and i.Visible == True:
    i.Click()
    Sys.Keys("[Del]")
    Log.Message(f'{i.DataContext.Identifier.OleValue} has been successfully Unmapped')
    break
  Log.Message(f'{i.DataContext.Identifier.OleValue} does not exist in the P2P Communication Configuration window')  
  
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
    
def change_FBD_Value(param):
  source_variable,desired_variable = param.split("$$")
  textbox = ref_obj.fbdsectionwindowtextbox.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for i in textbox:
    if i.Text == source_variable:
      i.DblClick()
      Sys.Keys(desired_variable)
      Sys.Keys("[Enter]")
      
def verify_variable_value_FBDBlock(value):
  textbox = ref_obj.fbdsectionwindowtextbox.object.FindAllChildren('Name', 'TextObject(*)', 100)
  for j in textbox:
    if value in j.Text:
      Log.Message(f'{j.Text} has been sucessfully veried in the screen')
      Applicationutility.take_screenshot()
      break
  else:
    Log.Message(f'{j.Text} does not exists in the screen')
    Applicationutility.take_screenshot()
    
def gsgsg123s():
  verify_variable_value_FBDBlock("162")
  
def Run_PLC_Simulator():
  TestedApps.PLCSimulatorStarter.Run()
  
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
  
def Edit_IODevice_Properties(param):
  field_label, options = param.split("$$")
  controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
  for control in controller_row:
    #Log.Message(getattr(getattr(control, "DataContext", None), "DisplayName", None))
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
   
def Expand_IODevice_section(param):
  IODevices_row = proj_obj.assignmentsdocktextbox.object.FindAllChildren("Name", "WPFObject('CheckedVisual')", 100)
  for list in IODevices_row:
    #Sys.HighlightObject(list)
    if param == list.DataContext.Identifier.OleValue:
      list.Click()
      Log.Message(list.DataContext.Identifier.OleValue+ " is expanded")
      break     
  else:
    Log.Message(param+" is expanded")
    
def Map_IO_Devices(param):
  service,field,engine = param.split("$$")
  Click_On_Topological_entity_IODvices(service,field)
  Map = proj_obj.servicemapdropdownbox.object
  Map_List = Map.FindAllChildren('ClrClassName', 'TextBlock', 100)
  for i in Map_List:
    if i.Text == engine:
      i.Click()
      Log.Message(f'{i.Text} was clicked')
      break
  else:
    Log.Message(f'{i.Text} doesnt exists')

def Click_On_Topological_entity_IODvices(service,field):
  Map = proj_obj.controlexecutablesproperty.object
  Map_List = Map.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for i in Map_List:
    #Sys.HighlightObject(i)
    if service in str(i.DataContext.Identifier.OleValue):
      service_list = i.FindAllChildren('ClrClassName', 'GridViewCell', 100)
      for j in service_list:
          if str(j.WPFControlOrdinalNo) == field:
            j.Click()
            return 
            
def Settings_SP(header):
  window = SP_obj.settingswindow.object
  sections = window.FindAllChildren('ClrClassName', 'TextBlock', 100)
  for section in sections:
    if section.Text == header:
      section.Click()
      Log.Checkpoint("Page Templates is clicked")
      
def verify_page_template():
  temp = SP_obj.pagetemplate.object
  default = temp.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  for template in default:
    if template.item.IsDefault == True:
      identifier = template.item.Identifier
      Log.Checkpoint(f"{identifier} template selected as default")
      
def click_on_systemmodel(button):
  appbar = SP_obj.refineapplicationbar.object
  verticalbar = appbar.FindAllChildren('ClrClassName', 'Button', 100)
  for menu in verticalbar:
    if menu.WPFControlAutomationId == button:
      menu.Click()
      Log.Checkpoint(f"{button} is clicked")
      
def click_on_equipment_exportall(button1):
    Applicationutility.wait_in_seconds(1000, 'Wait')
    commandbar = SP_obj.refinesystemmodelcommandbar.object
    horizontalbar = commandbar.FindAllChildren('ClrClassName', 'Button', 100)
    for button in horizontalbar:
      if button.WPFControlAutomationId == button1:
          button.Click()
          Log.Checkpoint(f"{button1} is clicked")
          
def Enter_systemName_systemlocation_ExportDataWindow_SPRefine(name):
  if not Project.Variables.VariableExists(name):
        Project.Variables.AddVariable(name, "String")
  Project.Variables.SupervisionProject = str(name + datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
  Log.Message(Project.Variables.SupervisionProject)
  Applicationutility.wait_in_seconds(2000,"Wait")
  Export_window = SP_obj.exportdatawindow.object
  
  if Export_window.Exists:
    Sys.Keys("[Del]")
    filename_textbox = SP_obj.exportdatafilename.object
    filename_textbox.Keys(Project.Variables.SupervisionProject)
  else:
    Log.Warning("Export Windows doesnt exists")
  filelocation = SP_obj.exportdatafilelocation
  tox = (filelocation.object.Height)/2
  toy = 10
  filelocation.click_at(tox,toy)
  Sys.Keys(os.getcwd())
  Sys.Keys("[Enter]")
      
def Click_on_Savebutton_in_ExportData(btn):
  savebutton = SP_obj.exportdatawindow.object.FindAllChildren('WndClass', 'Button', 10)
  for button in savebutton:
    if btn in button.WndCaption:
      button.Click()
      Log.Checkpoint(f"{btn} button is clicked")
      
def Click_on_RefineSystemModel_menubar(menu):
  sysmodelmenubar = SP_obj.refinesystemmodelmenubar.object
  menubar = sysmodelmenubar.FindAllChildren('ClrClassName', 'Button', 100)
  for menuitem in menubar:
    if menu in menuitem.WPFControlAutomationId:
      menuitem.Click()
      Applicationutility.wait_in_seconds(1000, 'Wait')
      Log.Checkpoint(f"{menu} is clicked")
      