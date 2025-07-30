"""PreCondition and Post Condition Utility"""
import datetime
import Engineeringclientutility
import Applicationexplorertabutility
import Applicationutility
from EngineeringClient import EngineeringClient
from ECWarningPopup import ECWarningPopup
from SystemExplorerScreen import SystemExplorerScreen
from CurrentScreen import CurrentScreen
from MessageBox import MessageBox
from ApplicationExplorerTab import ApplicationExplorerTab
import Actionutility

eng_obj = EngineeringClient()
war_obj = ECWarningPopup()
ec_obj = ECWarningPopup()
ses_obj = SystemExplorerScreen()
cs_obj = CurrentScreen()
lm_obj = MessageBox()
aet_obj = ApplicationExplorerTab()


def Precondition_TC_EPE_AE_0007():
  Engineeringclientutility.create_system_1_timestamp()
  Engineeringclientutility.select_system_1_application_explorer()
  Applicationexplorertabutility.right_click_application_browser_folder_AE("System1")
  Engineeringclientutility.select_ContextMenu_Items_EC("Create Folder")
  Applicationutility.wait_in_seconds(1000, 'wait')
  Applicationexplorertabutility.right_click_application_browser_folder_AE("System1")
  Engineeringclientutility.select_ContextMenu_Items_EC("Create Folder")
  Applicationexplorertabutility.search_template_browser_AE("MotorGP")
  Applicationutility.wait_in_seconds(2000, 'wait')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("MotorGP$$1.0.123$$Folder_1")
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("MotorGP$$1.0.123$$Folder_2")
  Applicationexplorertabutility.search_template_browser_AE("ValveGP")
  Applicationutility.wait_in_seconds(2000, 'wait')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("ValveGP$$1.0.100$$Folder_1")
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("ValveGP$$1.0.100$$Folder_2")
  
  
def Create_Multiple_folders_and_Multiple_instances_AE():
  Applicationexplorertabutility.right_click_application_browser_folder_AE("System1")
  Engineeringclientutility.select_ContextMenu_Items_EC("Create Folder")
  Applicationutility.wait_in_seconds(1000, 'wait')
  Applicationexplorertabutility.right_click_application_browser_folder_AE("System1")
  Engineeringclientutility.select_ContextMenu_Items_EC("Create Folder")
  Applicationexplorertabutility.search_template_browser_AE("MotorGP")
  Applicationutility.wait_in_seconds(2000, 'wait')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("MotorGP$$1.0.123$$Folder_3")
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("MotorGP$$1.0.123$$Folder_4")
  Applicationexplorertabutility.search_template_browser_AE("ValveGP")
  Applicationutility.wait_in_seconds(2000, 'wait')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("ValveGP$$1.0.100$$Folder_3")
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_folder_AE("ValveGP$$1.0.100$$Folder_4")
  

  
def Post_Conditions_AE():
  Engineeringclientutility.close_all_tab_except_Systems_explorer_EC()
  Engineeringclientutility.clickR_node_SE(Project.Variables.system_1)
  Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
  Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")
  ses_obj.circularprogressbarbutton.wait_for_element_property('Exists', None, 20000)
  
  
def Post_Conditions_AE_027_032():
  Engineeringclientutility.close_all_tab_except_Systems_explorer_EC()
  Engineeringclientutility.clickR_node_SE(Project.Variables.system_1)
  Engineeringclientutility.select_ContextMenu_Items_EC("Delete")
  Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons("Yes")

  
def Precondition_TC_EPE_AE_0039_Create_Multiple_instances_and_template_AE():
  Engineeringclientutility.create_system_1_timestamp()
  Engineeringclientutility.select_system_1_application_explorer()
  Applicationexplorertabutility.search_template_browser_AE("MotorGP")
  Applicationutility.wait_in_seconds(2000, 'wait')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_system1_AE("MotorGP$$1.0.123")
  Applicationexplorertabutility.search_template_browser_AE("ValveGP")
  Applicationutility.wait_in_seconds(2000, 'wait')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_system1_AE("ValveGP$$1.0.100")
  
### Assign the instance in control project and perform 'generate' before replace the template in AE ### standalone M580

def Pre_Con_TC_EPE_AE_0039():
  Engineeringclientutility.create_system_1_timestamp()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Engineeringclientutility.select_system_1_topology_explorer()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.grid_resize_TE()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.expand_physical_view_select_default_TE()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.select_tool_drag_drop_default_physical_view_TE('Modicon PAC controller$$M580 ePAC$$M580 standalone ePAC$$pos_1')
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.select_cpu_reference_TE('3.20$$6040')
  Applicationutility.wait_in_seconds(3000, 'Wait')
  click_M580_1()
  Topologyexplorerutility.select_dropdown_value_properties_TE('SECURITY$$Global Policy$$Security Level$$No')
  Topologyexplorerutility.click_enable_disable_properties_TE('SECURITY$$Password Protection$$Controller$$Disabled')
#  Topologyexplorerutility.select_dropdown_value_properties_TE('SECURITY$$Password Protection$$Controller$$Disabled')
  Topologyexplorerutility.confirmation_pop_up_TE('Yes')
  Topologyexplorerutility.click_tab_properties_TE('CONFIGURATION')
  Topologyexplorerutility.Expand_Propertiestab('Interfaces')
  Topologyexplorerutility.Expand_Propertiestab('Embedded Interface')
  Topologyexplorerutility.Expand_Propertiestab('MainIP')
  Topologyexplorerutility.Expand_Propertiestab('Logical Network')
  Topologyexplorerutility.select_combobox_TE('Logical Network$$New')
  Topologyexplorerutility.confirm_pop('Ok')
  Applicationutility.wait_in_seconds(3000, 'Wait')
  rclick_M580_1()
  Topologyexplorerutility.select_ContextMenu_Items_TE('PAC')
  Topologyexplorerutility.select_context_submenu_Items_TE('Configure')
  Applicationutility.wait_for_execution()
  Applicationutility.wait_in_seconds(3000, 'Wait')
  Topologyexplorerutility.close_tab_item('M580_1')
  Engineeringclientutility.open_application_explorer()
  Applicationutility.wait_in_seconds(3000, 'Wait')
  Applicationexplorertabutility.search_template_browser_AE('MotorGP')
  Applicationexplorertabutility.drag_composite_template_drop_app_browser_system1_AE('MotorGP$$1.0.123')
  Applicationutility.wait_in_seconds(2000, 'Wait')
  Engineeringclientutilityeng_obj = EngineeringClient()
  Engineeringclientutility.open_project_explorer()
  Applicationutility.wait_in_seconds(2000, 'Wait')
  Projectexplorertabutility.right_click_control_project_browser_PE('System1')
  Engineeringclientutility.select_ContextMenu_Items_EC('Create Control Project')
  Engineeringclientutility.select_Context_SubMenu_Items_EC('M580')
  Projectexplorertabutility.double_click_control_project_browser_PE('Container')
  Applicationutility.wait_in_seconds(3000, 'Wait')
  Projectexplorertabutility.select_instance_drag_drop_container_dock_PE('System1')
  Applicationutility.modal_dialog_window_button('OK')
  Applicationutility.wait_in_seconds(3000, 'Wait')
  Projectexplorertabutility.right_click_container_dock_context_menu_item_PE('System1$$Generate')
  Applicationutility.wait_for_execution()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Projectexplorertabutility.expand_control_project_0browser_PE('Executable')
  Projectexplorertabutility.double_click_control_project_browser_PE('ControlExecutable_1')
  Projectexplorertabutility.control_executeable_combo_box_PE('ControlExecutive_1$$Standalone_Controller_1')
  
def click_M580_1():
  M580_1 = topo_obj.partdiagramcontroltextbox.controller_objects('M580_1')
  for item in M580_1:
    if 'BME P58 6040' in item:
      obj = M580_1[item]
      obj[-1].Click()
      
def rclick_M580_1():
  M580_1 = topo_obj.partdiagramcontroltextbox.controller_objects('M580_1')
  for item in M580_1:
    if 'BME P58 6040' in item:
      obj = M580_1[item]
      obj[-1].ClickR()
      
      
def Pre_Con_TC_EPE_WS_0041_Export_Workstations():
  Engineeringclientutility.create_system_1_timestamp()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Engineeringclientutility.select_system_1_topology_explorer()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.grid_resize_TE()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.expand_physical_view_select_default_TE()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Topologyexplorerutility.select_tool_drag_drop_default_physical_view_TE('Workstations$$Generic$$Workstation$$pos_2')
  Topologyexplorerutility.click_tab_properties_TE('SERVICES')
  Topologyexplorerutility.WorkStation_Items('Control Services$$1')
  Topologyexplorerutility.WorkStation_Items('OFS$$1')
  Topologyexplorerutility.WorkStation_Items('Supervision Service$$1')
  Topologyexplorerutility.click_tab_properties_TE('SECURITY')
  Topologyexplorerutility.enable_disable_properties_TE('Simulator$$Disabled')
  Topologyexplorerutility.confirmation_pop_up_TE('Yes')
  Topologyexplorerutility.click_tab_properties_TE('CONFIGURATION')
  Topologyexplorerutility.Expand_Propertiestab('Ethernet Interface')
  Topologyexplorerutility.Expand_Propertiestab('IP Address')
  Topologyexplorerutility.Expand_Propertiestab('Logical Network')
  Topologyexplorerutility.select_combobox_TE('Logical Network$$New')
  Topologyexplorerutility.confirm_pop('Ok')
  Applicationutility.wait_in_seconds(3000, 'Wait')
  
def Verify_Facets_Added_or_Removed_context_menu_PE(): 
  facet_name = "CompactHWGP_1_OF"
  facet_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for facet in facet_list:
    if facet.Visible:
      if facet_name in facet.DataContext.Identifier.OleValue:
          Log.Checkpoint(facet.DataContext.Identifier.OleValue) 
         
  else:
    Log.Warning(f'The {facet_name} does not have {GenerationState}')
  