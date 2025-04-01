####################### Milestone 3 Topology ################################

import Applicationutility 
from Topology import Topology
from ApplicationExplorerTab import ApplicationExplorerTab
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
import Actionutility
from EngineeringClient import EngineeringClient
from RefineOffline import RefineOffline
from TopologyExplorerTab import TopologyExplorerTab
from MessageBox import MessageBox

topology_obj =  Topology()
aet_obj = ApplicationExplorerTab()
proj_obj = ProjectExplorerTab()
syse_obj = SystemExplorerScreen()
eng_obj = EngineeringClient()
refoff_obj = RefineOffline()
topo_obj = TopologyExplorerTab()
msg_obj = MessageBox()

###############################################################################
# Function : search_template_browser_EC
# Description : Searches for a template in the browser using the provided text.
# Parameter : search_text (str) - Text to search for in the template browser.
# Example : search_template_browser_EC("Modbus TCP Device")
###############################################################################
def search_template_browser_EC(search_text):
  temp_browser = msg_obj.exportpopupbutton.object
  Uc_Browser = temp_browser.Find(('ClrClassName','SearchLabelText'), ('UcBrowser','Search Modbus TCP Device I/O Templates'), 10)
  Uc_Browser.Click(Uc_Browser.width/2 , 20)
  Delay(2000)
  Sys.Keys(search_text)
  Log.Message(search_text + " is searched")
  Delay(2000,"Wait")

###############################################################################
# Function : Select_template_EC
# Description : Selects a template from the list based on the template name and version.
# Parameter : param (str) - Template name and version separated by "$$".
# Example : Select_template_EC("TemplateName$$1.0")
###############################################################################
def Select_template_EC(param):
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

###############################################################################
# Function : DblClick_template_TE
# Description : Double-clicks a template in the template explorer.
# Parameter : temp_name (str) - Name of the template to double-click.
# Example : DblClick_template_TE("ETesysTHW")
###############################################################################
def DblClick_template_TE(temp_name):
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row()
  for temp in temp_list:
    if temp.Visible:
      if temp_name in temp.DataContext.Identifier.OleValue:
          temp.DblClick()
          Log.Checkpoint(f'{temp.DataContext.Identifier.OleValue} is double clicked') 
          break
  else:
    Log.Warning(f'The {temp_name} is not present')

###############################################################################
# Function : Expand_communication_tab_TE
# Description : Expands the "Communication" tab in the system explorer.
# Parameter : val (str) - Tab name to expand (default is "Communication").
# Example : Expand_communication_tab_TE("Communication")
###############################################################################
def Expand_communication_tab_TE(val):
  val = "Communication"
  sections = syse_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName","GroupHeaderRow",1000)
  for section in sections:
    if val in section.DataContext.Name.OleValue:
      section.IsExpanded = True
      Log.Message(f'{section.DataContext.Name.OleValue} is expanded')
      break
  else:
    Log.Warning(f'{val} not found')

###############################################################################
# Function : edit_IP_Address
# Description : Edits the IP address of a specific device in the system explorer.
# Parameter : param (str) - Device name and new IP address separated by "$$".
# Example : edit_IP_Address("DeviceName$$192.168.1.1")
###############################################################################
def edit_IP_Address(param):
    name,IP_add =  param.split('$$')
    grid_row_obj = syse_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName", "GridViewRow", 1000)  
    for grid_row in grid_row_obj:
      grid_cell_obj = grid_row.FindAllChildren("ClrClassName", "GridViewCell", 100)
      for cell_val in grid_cell_obj:
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
    Log.Message(IP.DataContext.FormattedAddress.OleValue)
    Log.Message(IP_address)
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

def Verify_Device_Hardware_Catalog_TE(smp):
  obj_lst = refoff_obj.fbdsectionwindowtextbox.object.FindAllChildren("Name",f"TextObject({smp})",10)
  for obj in obj_lst:
    if obj.Text == smp:
      Log.Checkpoint(f'{obj.Text} is verified sucessfully')
      break
  else:
    Log.Warning(f'{obj.Text} is not verified')

#Author: Suraj 
#Created for double click the properties when workstation is open 
#some of the properties are controlExpert_1,NIC,OFS ..etc

def DBlClick_Properties_workstation(Text):
  properties = proj_obj.assignmentsdocktextbox.object.FindAllChildren("ClrClassName","GridViewRow",100)
  for property in properties:
    if Text == property.DataContext.Identifier.OleValue:
      property.DblClick()
      Log.Message(f'{property.DataContext.Identifier.OleValue} is clicked')
      break
  else:
     Log.Message(f'{property.DataContext.Identifier.OleValue} property doesnt exists')
     
     
#Author: Suraj 
#Created for Expanding  the properties when workstation is open 
#some of the properties are Configuration,$System ..etc

def Expand_Properties_workstation(Text):
  properties = topology_obj.propertywindowtextbox.object.FindAllChildren("ClrClassName","GroupHeaderRow",100)
  for property in properties:
    if Text == property.DataContext.Name.OleValue:
      property.IsExpanded = True
      Log.Message(f'{property.DataContext.Name.OleValue} is Expanded')
      break
  else:
     Log.Message(f'{property.DataContext.Name.OleValue} property doesnt exists')
     
     
def change_port_number_workstation_TE(param):
  heading, activeport, portvalue = param.split("$$")
  ports = topology_obj.propertywindowtextbox.object.FindAllChildren("ClrClassName","GridViewRow",100)
  for port in ports:
    Log.Message(port.Item.Category)
    Log.Checkpoint(heading)
    
    if str(port.Item.Category) == heading:
      Log.Message(port.Item.Category)
      values = port.FindAllChildren("ClrClassName","GridViewCell",100)
      for value in values:
        if activeport in value.WPFControlText:
          value.Click()
          Sys.Keys(portvalue)
          Sys.Keys("[Enter]")
  else:
    Log.Message(f'{activeport} check and enter valid active port')

def Verify_error_messages_in_Console(text):
#  text = "0 Error"
  output_msg = topology_obj.outputwindowpaneltextbox.object.FindAllChildren("WndClass","RichEdit20W",10)
  for msg in output_msg:
    if text in msg.wText and msg.Visible:
      Log.Checkpoint(msg.wText + " error messages is displayed in Console")
      break
  else:
    Log.Message(f'{text} error messages not displayed in Console')

###############################################################################
# Function : Enter_Controller_Password_deploy_screen_TE
# Description : Enters the controller password on the deployment screen.
# Parameter : password (str) - Password to be entered.
# Example : Enter_Controller_Password_deploy_screen_TE("password123")
###############################################################################
def Enter_Controller_Password_deploy_screen_TE(password):
      PW_box = topology_obj.PasswordControlBoxtextbox   
      PW_box.enter_password(password)
      Log.Message(str(PW_box.object.PasswordText) + " entered in Password")