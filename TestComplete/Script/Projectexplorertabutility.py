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


eng_obj = EngineeringClient()
topo_obj = TopologyExplorerTab()
ses_obj = SystemExplorerScreen()
msg_obj = MessageBox()
proj_obj = ProjectExplorerTab()
aet_obj = ApplicationExplorerTab()


def right_click_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  for item in proj_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.ClickR()
        Log.Message(item.DataContext.Identifier.OleValue + ' is Right Clicked.')
        break
  else:
    Log.Warning("Please Enter the Valid item from control project browser pane")
  
        
def gsgsgsg():
  right_click_control_project_browser_PE('ControlProject_4')
        
def double_click_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow()
  for item in proj_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.DblClick()
        Log.Message(item.DataContext.Identifier.OleValue + ' is Double Clicked.')
        Delay(2000,"Wait")
        
        
        
def expand_control_project_browser_PE(identifier):
  proj = proj_obj.projectbrowsertextbox
  proj_list = proj.find_children_for_treeviewrow() 
  for item in proj_list:
    if item.Visible:
      if identifier in item.DataContext.Identifier.OleValue:
        item.IsExpanded = True
        Log.Message(item.DataContext.Identifier.OleValue + ' is Expanded.')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        Delay(2000,"Wait")
        

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
  container_list = container_dock.find_children_for_grid_view_row()
  for item in container_list:
    if item.Visible:
      if identifier == item.DataContext.Identifier.OleValue:
        item.ClickR()
        Applicationutility.wait_in_seconds(750, 'Wait')
        Engineeringclientutility.select_ContextMenu_Items_EC(Context_menu_item)
        
        
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

          
def right_click_instance_select_action_in_assignments(param, action):
  facet_names = []
    
  if "$$" in param:
    facet_names = param.split("$$")
  else:
    facet_names = [param]

  instance_list = proj_obj.assignmentstextbox.object.FindAllChildren('ClrClassName', 'GridViewCell', 100)
  found_facet_names = set()

  for instance in instance_list:
    if instance.Visible:
      for facet_name in facet_names:
        if instance.DataContext.Identifier.OleValue == facet_name and facet_name not in found_facet_names:
          instance.ClickR()
          Engineeringclientutility.select_ContextMenu_Items_EC(action)
          Log.Message(f"{action}  was  selected for  facet  name:  {facet_name}")
          found_facet_names.add(facet_name)
          break
          
          
def sgsgsg():
  right_click_instance_select_action_in_assignments("AnalogInputGP_1_AInputGP","Relink")
          



def verify_assignment(value_name, status):
  instance_list = proj_obj.assignmentstextbox.object.FindAllChildren('ClrClassName', 'GridViewRow', 100)
  facet_names = value_name.split('$$')
  for facet in facet_names:
    for instance in instance_list:
      objects = instance.FindAllChildren('ClrClassName', 'GridViewCell', 100)
      object_list = [i.Value for i in objects]
      if facet in object_list and status in object_list:
        Log.Message(f"{facet} and status '{status}' are verified")
        break
    else:
      Log.Warning(value_name + ", " + status + " is not verified")

         
      
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
                Applicationutility.wait_in_seconds(750, 'Wait')
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
    Facet_obj = proj_obj.assignmentsdocktextbox.object
    facet_No = Facet_obj.Items.Count
    Log.Message(f'Total Facet Count : " {facet_No} " in " {Facet_obj.Items.Item[0].ContainerName} " Container Assignments Dock')
    for i in range(facet_No):
      if proj_obj.assignmentsdocktextbox.object.Items.Item[i].GenerationState == "NonGenerated":
        Log.Checkpoint(f'Facet : {Facet_obj.Items.Item[i].Identifier.OleValue} ; Generation status : {Facet_obj.Items.Item[i].GenerationState}')
      else:
        Log.Checkpoint(f'Facet : {Facet_obj.Items.Item[i].Identifier.OleValue} ; Generation status : {Facet_obj.Items.Item[i].GenerationState}')
    
def verify_section_containers_dock(): 
  Applicationutility.wait_in_seconds(750, 'Wait')
  sections_list = proj_obj.containerdocktextbox.find_children_for_grid_view_row()
  sections_name_list = [section.DataContext.Identifier.OleValue for section in sections_list if section.dataContext != None]
  if len(sections_name_list) > 2:
    Log.Message(sections_name_list[0]+' was created')
  else:
    Log.Warning("FBD section was not created")
    
def Create_Multiple_section_Containers_Dock():
  n = 10
  for i in range(10):
    right_click_container_dock_context_menu_item_PE('ControlProject_1$$Create FBD Section')
    Actionutility.modal_dialog_window_button('OK')
    sections_list = proj_obj.containerdocktextbox.find_children_for_grid_view_row()
    sections_name_list = [section.DataContext.Identifier.OleValue for section in sections_list if section.dataContext != None]
    if len(sections_name_list) > 2:
      Log.Message(sections_name_list[0]+' was created')
    else:
      Log.Warning("FBD section was not created")


