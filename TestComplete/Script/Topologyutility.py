﻿####################### Milestone 3 Topology ################################

import Applicationutility 
from Topology import Topology
from ApplicationExplorerTab import ApplicationExplorerTab
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
import Actionutility
from EngineeringClient import EngineeringClient

topology_obj =  Topology()
aet_obj = ApplicationExplorerTab()
proj_obj = ProjectExplorerTab()
syse_obj = SystemExplorerScreen()
eng_obj = EngineeringClient()

def search_template_browser_EC(search_text):
  temp_browser = msg_obj.exportpopupbutton.object
  Uc_Browser = temp_browser.Find(('ClrClassName','SearchLabelText'), ('UcBrowser','Search Modbus TCP Device I/O Templates'), 10)
  Uc_Browser.Click(Uc_Browser.width/2 , 20)
  Delay(2000)
  Sys.Keys(search_text)
  Log.Message(search_text + " is searched")
  Delay(2000,"Wait")
  
def Select_template_EC (param):
  template,version = param.split('$$')
  template_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  for i in range(len(template_list)):
      if template_list[i].Visible:
        if str(template) in str(template_list[i].Item.Identifier.OleValue):
          if str(version) == str(template_list[i].Item.ViewModel.Version.OleValue):
              template_list[i].DblClick()
              Log.Message(template + " is double clicked")
              Delay(3000)
              break
              
def DblClick_template_TE(temp_name):
#  temp_name = "ETesysTHW"
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()#object.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for temp in temp_list:
    if temp.Visible:
      if temp_name in temp.DataContext.Identifier.OleValue:
          temp.DblClick()
          Log.Checkpoint(f'{temp.DataContext.Identifier.OleValue} is double clicked') 
          break
  else:
    Log.Warning(f'The {temp_name} is not present')        
 
def Expand_communication_tab_TE(val):
  val = "Communication"
  sections = syse_obj.systemexplorermenubutton.object.FindAllChildren("ClrClassName","GroupHeaderRow",100)
  for section in sections:
    if val in section.DataContext.Name.OleValue:
      section.IsExpanded = True
         
def edit_IP_Address(param):
    name,IP_add =  param.split('$$')
    grid_row_obj = topology_obj.topologydeviceeditertextbox.object.FindAllChildren("ClrClassName", "GridViewRow", 1000)  
    for grid_row in grid_row_obj:
      Sys.HighlightObject(grid_row,1)  
      grid_cell_obj = grid_row.FindAllChildren("ClrClassName", "GridViewCell", 100)
      for cell_val in grid_cell_obj:
        Sys.HighlightObject(cell_val,1)
        if name in cell_val.WPFControlText:
          grid_row.DataContext.Expression = IP_add         
          if grid_row.DataContext.Expression == IP_add:
            Log.Checkpoint(name + " is updated as " + IP_add)
            break
          else:  
            Log.Warring(name + " is updated not as " + IP_add)
               
def RClick_template_TE(temp_name):
#  temp_name = "ETesysTHW"
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()#object.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for temp in temp_list:
    if temp.Visible:
      if temp_name in temp.DataContext.Identifier.OleValue:
          temp.ClickR()
          Log.Checkpoint(f'{temp.DataContext.Identifier.OleValue} is double clicked') 
          break
  else:
    Log.Warning(f'The {temp_name} is not present')

def select_dropdown_value_popup_TE(param):
  Screen, property, dropdown_value = param.split('$$')
  para = Screen + '$$' +property
  object_ = Actionutility.get_obj(para)   
  for i in range(object_.object.Items.Count):
    if dropdown_value in object_.object.Items.Item[i].Identifier.OleValue:
      object_.object.SelectedIndex = i
      Log.Checkpoint(f'The selected value is {object_.object.Items.Item[i].Identifier.OleValue}')
      break
  else:
    Log.Warning(f'The value {dropdown_value} is not available in the dropdown')
  
def Select_IP_from_ControlProjectDeployment(IP_address):
  name = topology_obj.primaryaddresslistdropdown.object
  name.Click()
  Dropdown_options = eng_obj.userdropdownmenuitemtextbox.object
  Dropdown_IPList = Dropdown_options.FindAllChildren("ClrClassName","RadComboBoxItem",10)
  for IP in Dropdown_IPList:
    if IP_address in IP.DataContext.FormattedAddress.OleValue:
      IP.Click()
      Log.Message(f'{IP.DataContext.FormattedAddress.OleValue} was selected from Dropdown option')
      break
  else:
    Log.Message(f'{IP_address} did not exist in Dropdown option')


def select_latest_backup_data_TE():
  obj = Sys.Process("EngineeringClient").WPFObject("HwndSource: ModalDialogWindow", "").WPFObject("ModalDialogWindow", "", 1).WPFObject("RestoreDataConfirmationPanel", "", 1).WPFObject("Grid", "", 1).WPFObject("GroupBox", "Select Backup Data", 3).WPFObject("SelectionGrid")
  list = []
  for i in range(obj.Items.Count):
   list.append(int(obj.Items.Item[i].BackupTime.OleValue))
  latest = max(list)
  for j in range(obj.Items.Count):
    if int(obj.Items.Item[j].BackupTime.OleValue) == latest:
      obj.Items.Item[j].IsSelected = True
      #obj.SelectedItem.IsSelected = True
      Log.Checkpoint(f'The item with Time stamp {obj.Items.Item[j].BackupTime.OleValue} is selected.')
      Applicationutility.take_screenshot('Taking screenshot of the selected')
      break
    
      