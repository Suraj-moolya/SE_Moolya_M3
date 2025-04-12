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
  Uc_Browser.Click(Uc_Browser.width / 2, 20) 
  Delay(2000) 
  Sys.Keys(search_text) 
  Log.Message(search_text + " is searched") 
  Delay(2000, "Wait")

############################################################################### 
# Function : Select_template_EC 
# Description : Selects a template from the list based on the template name and version. 
# Parameter : param (str) - Template name and version separated by "$$". 
# Example : Select_template_EC("TemplateName$$1.0") 
############################################################################### 
def Select_template_EC(param): 
  template, version = param.split('$$') 
  template_list = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000) 
  if not template_list: 
    Log.Message("No templates found.") 
    return 
  for i in range(len(template_list)): 
    if template_list[i].Visible: 
      if str(template) in str(template_list[i].Item.Identifier.OleValue): 
        if str(version) == str(template_list[i].Item.ViewModel.Version.OleValue): 
          template_list[i].DblClick() 
          Log.Message(template + " is double clicked") 
          Delay(3000) 
          break 
  else: 
    Log.Message(f"Template '{template}' with version '{version}' not found.")

############################################################################### 
# Function : DblClick_template_TE 
# Description : Double-clicks a template in the template explorer. 
# Parameter : temp_name (str) - Name of the template to double-click. 
# Example : DblClick_template_TE("ETesysTHW") 
############################################################################### 
def DblClick_template_TE(temp_name): 
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row() 
  if not temp_list: 
    Log.Message("No templates found in the grid view.") 
    return 
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
  sections = syse_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName", "GroupHeaderRow", 1000) 
  if not sections: 
    Log.Message("No sections found.") 
    return 
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
  name, IP_add = param.split('$$') 
  grid_row_obj = syse_obj.systemexplorernodebutton.object.FindAllChildren("ClrClassName", "GridViewRow", 1000) 
  if not grid_row_obj: 
    Log.Message("No grid rows found.") 
    return 
  for grid_row in grid_row_obj: 
    grid_cell_obj = grid_row.FindAllChildren("ClrClassName", "GridViewCell", 100) 
    if not grid_cell_obj: 
      Log.Message("No grid cells found.") 
      return 
    for cell_val in grid_cell_obj: 
      if name in cell_val.WPFControlText: 
        grid_row.DataContext.Expression = IP_add 
        if grid_row.DataContext.Expression == IP_add: 
          Log.Checkpoint(name + " is updated as " + IP_add) 
          break 
        else: 
          Log.Warning(name + " is not updated as " + IP_add) 
    else: 
      Log.Message(f"Device '{name}' not found in grid cells.")

############################################################################### 
# Function : RClick_template_TE 
# Description : Right-clicks on a template in the template explorer. 
# Parameter : temp_name (str) - Name of the template to right-click. 
# Example : RClick_template_TE("ETesysTHW") 
############################################################################### 
def RClick_template_TE(temp_name): 
  temp_list = proj_obj.assignmentsdocktextbox.find_children_for_grid_view_row() 
  if not temp_list: 
    Log.Message("No templates found in the grid view.") 
    return 
  for temp in temp_list: 
    if temp.Visible: 
      if temp_name in temp.DataContext.Identifier.OleValue: 
        temp.ClickR() 
        Log.Checkpoint(f'{temp.DataContext.Identifier.OleValue} is right-clicked') 
        break 
  else: 
    Log.Warning(f'The {temp_name} is not present')

############################################################################### 
# Function : select_dropdown_value_popup_TE 
# Description : Selects a value from a dropdown in a popup window. 
# Parameter : param (str) - Format: "Screen$$Property$$DropdownValue". 
# Example : select_dropdown_value_popup_TE("Screen1$$Property1$$Value1") 
############################################################################### 
def select_dropdown_value_popup_TE(param): 
  Screen, property, dropdown_value = param.split('$$') 
  para = Screen + '$$' + property 
  object_ = Actionutility.get_obj(para) 
  for i in range(object_.object.Items.Count): 
    if dropdown_value in object_.object.Items.Item[i].Identifier.OleValue: 
      object_.object.SelectedIndex = i 
      Log.Checkpoint(f'The selected value is {object_.object.Items.Item[i].Identifier.OleValue}') 
      break 
  else: 
    Log.Warning(f'The value {dropdown_value} is not available in the dropdown')

############################################################################### 
# Function : Select_IP_from_ControlProjectDeployment 
# Description : Selects an IP address from the dropdown in the control project deployment screen. 
# Parameter : IP_address (str) - IP address to select. 
# Example : Select_IP_from_ControlProjectDeployment("192.168.1.1") 
############################################################################### 
def Select_IP_from_ControlProjectDeployment(IP_address): 
  name = topology_obj.primaryaddresslistdropdown.object 
  name.Click() 
  Dropdown_options = eng_obj.userdropdownmenuitemtextbox.object 
  Dropdown_IPList = Dropdown_options.FindAllChildren("ClrClassName", "RadComboBoxItem", 10) 
  if not Dropdown_IPList: 
    Log.Message("No IP addresses found in the dropdown.") 
    return 
  for IP in Dropdown_IPList: 
    if IP_address in IP.DataContext.FormattedAddress.OleValue: 
      IP.Click() 
      Log.Message(f'{IP.DataContext.FormattedAddress.OleValue} was selected from Dropdown option') 
      break 
  else: 
    Log.Message(f'{IP_address} did not exist in Dropdown option')

############################################################################### 
# Function : select_latest_backup_data_TE 
# Description : Selects the latest backup data from the backup selection grid. 
# Parameter : None 
############################################################################### 
def select_latest_backup_data_TE(): 
  obj = Sys.Process("EngineeringClient").WPFObject("HwndSource: ModalDialogWindow", "").WPFObject("ModalDialogWindow", "", 1).WPFObject("RestoreDataConfirmationPanel", "", 1).WPFObject("Grid", "", 1).WPFObject("GroupBox", "Select Backup Data", 3).WPFObject("SelectionGrid") 
  list = [int(obj.Items.Item[i].BackupTime.OleValue) for i in range(obj.Items.Count)] 
  latest = max(list) 
  for j in range(obj.Items.Count): 
    if int(obj.Items.Item[j].BackupTime.OleValue) == latest: 
      obj.Items.Item[j].IsSelected = True 
      Log.Checkpoint(f'The item with Time stamp {obj.Items.Item[j].BackupTime.OleValue} is selected.') 
      Applicationutility.take_screenshot('Taking screenshot of the selected') 
      break

############################################################################### 
# Function : Verify_Device_Hardware_Catalog_TE 
# Description : Verifies the presence of a specific device in the hardware catalog. 
# Parameter : smp (str) - Name of the device to verify. 
# Example : Verify_Device_Hardware_Catalog_TE("DeviceName") 
############################################################################### 
def Verify_Device_Hardware_Catalog_TE(smp): 
  obj_lst = refoff_obj.fbdsectionwindowtextbox.object.FindAllChildren("Name", f"TextObject({smp})", 10) 
  if not obj_lst: 
    Log.Message("No devices found in the hardware catalog.") 
    return 
  for obj in obj_lst: 
    if obj.Text == smp: 
      Log.Checkpoint(f'{obj.Text} is verified successfully') 
      break 
  else: 
    Log.Warning(f'{smp} is not verified')

############################################################################### 
# Function : DBlClick_Properties_workstation 
# Description : Double-clicks on a specific property in the workstation. 
# Parameter : Text (str) - Name of the property to double-click. 
# Example : DBlClick_Properties_workstation("ControlExpert_1") 
############################################################################### 
def DBlClick_Properties_workstation(Text): 
  properties = proj_obj.assignmentsdocktextbox.object.FindAllChildren("ClrClassName", "GridViewRow", 100) 
  if not properties: 
    Log.Message("No properties found in the workstation.") 
    return 
  for property in properties: 
    if Text == property.DataContext.Identifier.OleValue: 
      property.DblClick() 
      Log.Message(f'{property.DataContext.Identifier.OleValue} is clicked') 
      break 
  else: 
    Log.Message(f'{Text} property does not exist')

############################################################################### 
# Function : Expand_Properties_workstation 
# Description : Expands a specific property in the workstation. 
# Parameter : Text (str) - Name of the property to expand. 
# Example : Expand_Properties_workstation("Configuration") 
############################################################################### 
def Expand_Properties_workstation(Text): 
  properties = topology_obj.propertywindowtextbox.object.FindAllChildren("ClrClassName", "GroupHeaderRow", 100) 
  if not properties: 
    Log.Message("No properties found in the workstation.") 
    return 
  for property in properties: 
    if Text == property.DataContext.Name.OleValue: 
      property.IsExpanded = True 
      Log.Message(f'{property.DataContext.Name.OleValue} is Expanded') 
      break 
  else: 
    Log.Message(f'{Text} property does not exist')

############################################################################### 
# Function : change_port_number_workstation_TE 
# Description : Changes the port number for a specific heading and active port in the workstation. 
# Parameter : param (str) - Format: "Heading$$ActivePort$$PortValue". 
# Example : change_port_number_workstation_TE("Heading1$$Port1$$8080") 
############################################################################### 
def change_port_number_workstation_TE(param): 
  heading, activeport, portvalue = param.split("$$") 
  ports = topology_obj.propertywindowtextbox.object.FindAllChildren("ClrClassName", "GridViewRow", 100) 
  for port in ports: 
    if str(port.Item.Category) == heading:  
      if port.Item.Value == activeport:
        object = port.FindAllChildren("ClrClassName", "GridViewCell", 10)
        for obj in object:
          if obj.Value == activeport :
            obj.Click()
            Applicationutility.wait_in_seconds(1000, 'Wait')
            Sys.Keys(portvalue)
            Sys.Keys('[Enter]')
  #          if obj.DataContext.Expression == portvalue
          
        
#        Actionutility.modal_dialog_window_button('Yes')
      else: 
        Log.Message(f'{activeport} port not found in values.') 
        break
  else: 
    Log.Message(f'{heading} heading not found in ports.')

############################################################################### 
# Function : Verify_error_messages_in_Console 
# Description : Verifies if a specific error message is displayed in the console. 
# Parameter : text (str) - Error message to verify. 
# Example : Verify_error_messages_in_Console("0 Error") 
############################################################################### 
def Verify_error_messages_in_Console(text): 
  output_msg = topology_obj.outputwindowpaneltextbox.object.FindAllChildren("WndClass", "RichEdit20W", 10) 
  if not output_msg: 
    Log.Message("No messages found in the console.") 
    return 
  for msg in output_msg: 
    if text in msg.wText and msg.Visible: 
      Log.Checkpoint(msg.wText + " error messages are displayed in Console") 
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
  PW_box = topology_obj.PasswordControlBoxtextbox.object
  PW_box.Keys(password) 
  Log.Message(str(PW_box.Password) + " entered in Password")