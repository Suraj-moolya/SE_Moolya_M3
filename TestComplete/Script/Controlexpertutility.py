"Control Expert Utility"

from RefineOffline import RefineOffline
from MessageBox import MessageBox
import Applicationutility
import Topologyexplorerutility
from CurrentScreen import CurrentScreen
from DialogCE import DialogCE    
from ControlExpert import ControlExpert  
from ProjectExplorerTab import ProjectExplorerTab
from TopologyExplorerTab import TopologyExplorerTab

diace_obj = DialogCE()
ce_obj = ControlExpert()
cs_obj = CurrentScreen()
msg_obj = MessageBox()
refoff_obj = RefineOffline()
proj_obj = ProjectExplorerTab()
topoexo_obj = TopologyExplorerTab()

###############################################################################
#Author : Preetham S R
#Function : Select main folder project browser CE
#Parameter : No
###############################################################################
def select_main_folder_project_browser_CE():
  project_browser = refoff_obj.projectbrowserrotextbox.object
  project_browser.wItems.Item[0].Select()
  Applicationutility.wait_in_seconds(1000, 'Wait')

###############################################################################
#Author : Priyanka T
#Function : Select value from dropdown in project browser item CE
#Parameter : dropdown text value 
###############################################################################
def select_project_browser_item_CE(val):
  project_browser = refoff_obj.projectbrowserrotextbox.object
  count = project_browser.wItemCount 
  for i in range(count):
    if val in project_browser.wItem[i]:
      project_browser.SelectItem(val)
      Log.Message(val + ' is selected')
      break
  else:
    Log.Message(val + ' is not selected')

      
###############################################################################
#Author : Preetham S R
#Function : double click in project browser item CE
#Parameter : double click text value 
###############################################################################     
def doubleclick_project_browser_item_CE(val):  
  project_browser = refoff_obj.projectbrowserrotextbox.object
  count = project_browser.wItems.Item[0].Items.Count
  for i in range(count+1):
    if val in project_browser.wItem[i]:
      project_browser.DblClickItem(val)
      break
  else:
    Log.Warning(val + ' is not Click')

    
###############################################################################
#Author : Priyanka T
#Function : Right click in project browser item CE
#Parameter : Right click text value 
###############################################################################      
def rightclick_project_browser_item_CE(val):  
  project_browser = refoff_obj.projectbrowserrotextbox.object
  count = project_browser.wItems.Item[0].Items.Count
  for i in range(count):
    if val in project_browser.wItem[i]:
      project_browser.ClickItemR(val)
      break
  else:
    Log.Message(val + ' is not selected')
 
###############################################################################
#Author : Preetham S R
#Function : Maximize MDI Window in project browser
#Parameter : No 
###############################################################################     
def maximize_window_CE():
  try:
    Applicationutility.wait_in_seconds(2000, 'Wait')
    win = refoff_obj.mdiwindowtextbox.object
    win.Maximize()
  except:
    Log.Message('No Window to Maximize')  
      
###############################################################################
#Author : Preetham S R
#Function : double click on item and Maximize MDI Window in project browser
#Parameter : eg. Configuration$$0 : PLC bus 
###############################################################################    
def double_click_selected_project_browser_item_CE(param):
  selection_items_list = param.split('$$')
  select_main_folder_project_browser_CE()  
  max = len(selection_items_list)
  for i in range(max):
    if i != (max-1):
      select_project_browser_item_CE(selection_items_list[i])
      Applicationutility.wait_in_seconds(500, 'wait')
    else:
      doubleclick_project_browser_item_CE(selection_items_list[i])
      Applicationutility.wait_in_seconds(1500, 'wait')
      maximize_window_CE()
      Applicationutility.wait_in_seconds(2000, 'wait')

###############################################################################
#Author : Priyanka T
#Function : right click on item and Maximize MDI Window in project browser
#Parameter : eg. Configuration$$0 : PLC bus 
###############################################################################      
def Right_click_selected_project_browser_item_CE(param):
  selection_items_list = param.split('$$')
  select_main_folder_project_browser_CE()  
  max = len(selection_items_list)
  for i in range(max):
    if i != (max-1):
      select_project_browser_item_CE(selection_items_list[i])
      Applicationutility.wait_in_seconds(500, 'wait')
    else:
      rightclick_project_browser_item_CE(selection_items_list[i])
      Applicationutility.wait_in_seconds(1500, 'wait')
      
###############################################################################
#Author : Preetham S R
#Function : Modify refine window, add data section, IN1, IN2 and OUT
#Parameter : No
###############################################################################    
def rclick_window_CE(): 
  win = refoff_obj.mdiwindowtextbox.object
  win.ClickR((win.Width/2)-100, win.Height/2)
  
  data_selection = refoff_obj.dataselectiontextbox.object
  data_selection.Click()
  
  comb = refoff_obj.windowcomboboxtextbox.object
  comb.Keys('XOR')
  comb.Keys('[Enter]')
  #Topologyexplorerutility.modaldialogue_window_ce("Yes")
  win.Click((win.Width/2)-100, win.Height/2)
  win.Keys('[Esc]')
  win1 = refoff_obj.fbdsectionwindowtextbox.object 
  Applicationutility.wait_in_seconds(1500, 'wait')
  win1.TextObject("IN2").DblClick()
  comb.Keys('Int2')
  comb.Keys('[Enter]')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('[Enter]')
  Applicationutility.wait_in_seconds(1000, 'wait') 
  win1.TextObject("OUT").DblClick()
  comb.Keys('Int3')
  comb.Keys('[Enter]')
  Applicationutility.wait_in_seconds(1000, 'wait')
  Sys.Keys('[Enter]')
  Applicationutility.wait_in_seconds(1000, 'wait')

   
#def rclick_window_CE(): 
#  win = refoff_obj.mdiwindowtextbox.object
#  text = refoff_obj.face+ttextbox.object.ClickR()
#  
#  data_selection = refoff_obj.dataselectiontextbox.object
#  data_selection.Click()
#  
#  comb = refoff_obj.windowcomboboxtextbox.object
#  comb.Keys('XOR')
#  comb.Keys('[Enter]')
#  win.Click(win.Width/2, win.Height/2)
#  win.Keys('[Esc]')
#  win1 = refoff_obj.fbdsectionwindowtextbox.object 
#  Applicationutility.wait_in_seconds(1500, 'wait')
#
#  win1.TextObject("IN2").DblClick()
#  comb.Keys('Int2')
#  comb.Keys('[Enter]')
#  Applicationutility.wait_in_seconds(1000, 'wait')
#  comb1 = refoff_obj.typecomboboxtextbox.object
#  for i in range(comb1.wItemCount):
#    if 'BOOL' in comb1.wItem[i]:
#      comb1.Value = comb1.wItem[i]
#      break
#  Applicationutility.wait_in_seconds(1000, 'wait')
#  validate = refoff_obj.createvariablebutton.object
#  validate.Click()
#  
#  win1.TextObject("OUT").DblClick()
#  comb.Keys('Int3')
#  comb.Keys('[Enter]')
#  Applicationutility.wait_in_seconds(1000, 'wait')
#  comb1 = refoff_obj.typecomboboxtextbox.object
#  for i in range(comb1.wItemCount):
#    if 'BOOL' in comb1.wItem[i]:
#      comb1.Value = comb1.wItem[i]
#      break
#  Applicationutility.wait_in_seconds(1000, 'wait')
#  validate = refoff_obj.createvariablebutton.object
#  validate.Click()

#def rclick_window_CE(): 
#  win = refoff_obj.mdiwindowtextbox.object
#  text = refoff_obj.facettextbox.object.ClickR()
#  
#  data_selection = refoff_obj.dataselectiontextbox.object
#  data_selection.Click()
#  
#  comb = refoff_obj.windowcomboboxtextbox.object
#  comb.Keys('XOR')
#  comb.Keys('[Enter]')
#  win.Click(win.Width/2, win.Height/2)
#  win.Keys('[Esc]')
#  win1 = refoff_obj.fbdsectionwindowtextbox.object 
#  Applicationutility.wait_in_seconds(1500, 'wait')

  
###############################################################################
#Author : Priyanka T
#Function : Right Click on Block Refine Offline window
#Parameter : Block name text
###############################################################################   
def RClick_on_Block_Refine_Offline(identifier):  
  Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
  for Window_Text in Window:
    if identifier in Window_Text.Text and Window_Text.Visible:
        Window_Text.ClickR()
        Log.Message(Window_Text.Text + ' is Right Clicked.')
        break
  else:
    Log.Message(Window_Text.Text + ' is not visible in the Window')
        
###############################################################################
#Author : Preetham S R
#Function : Unlock Dialog popup
#Parameter : Block name text
###############################################################################  
def Unlock_Dialog_popup(button_name):
  obj = Sys.Process("ControlExpert", 4).Dialog("Unlock")
  buttons_list = obj.FindAllChildren('WndClass', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WndCaption) :
      button.click()
      Log.Message('Clicked ' + str(button.WndCaption) + ' button.')
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    

###############################################################################
#Author : Priyanka T
#Function : Delete link in Refine Offline
#Parameter : text
###############################################################################   
def Delete_link_Refine_Offline(identifier):
  Window = refoff_obj.mdiwindowtextbox.object
  Window_lst = Window.FindAllChildren("Name", "TextObject*", 1000)
  for obj in Window_lst:
    if identifier in obj.Text:
      Window.Click(obj.Left+50+obj.Width,obj.Top+40+(obj.Height/2))
      Delay(1000)
      #Sys.Keys("[Del]")
      
###############################################################################
#Author : Priyanka T
#Function : Click on Check/Uncheck All button
#Parameter : No
###############################################################################          
def Consistency_Check_Select_All():
  headers = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
  buttons_list = headers[0].FindAllChildren('ClrClassName', 'CheckBox', 1000)
  for button in buttons_list:
    if "Check/Uncheck All" == button.ToolTip.Content.OleValue:
        button.IsChecked = True
        Log.Message( 'Sellect all button is Checked')       
        break
    else:
        Log.Message(str(button.WPFControlText) +" button is Enabled")

###############################################################################
#Author : Priyanka T
#Function : Click on Check/Uncheck All button
#Parameter : No
###############################################################################
def Verify_modifications_available_in_Refine_Offline(identifier):        
  Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
  for Window_Text in Window:
    if identifier in Window_Text.Text:
      Log.Checkpoint(Window_Text.Text + " block is available")
      break
  else: 
    Log.Warning(identifier + " block is not available")

def RClick_on_filter_Refine_Offline(): 
  Button = refoff_obj.mdiwindowtextbox.object.FindChild("ClassName", "CDFIButton", 1000)
  Button.ClickR()
  
def Select_Column_Configuration(identifier):
  Window = refoff_obj.parentdialogwindowce.object.FindAllChildren("Name", "TextObject*", 1000)
  for obj in Window:
      if identifier in obj.Text:
          Window.Click(obj.Left-50+obj.Width,obj.Top+40+(obj.Height/2))
          Log.Message(obj.Text + " is selected")
   
def Add_variable_name_in_name_column (var_name):
  Delay(3000)
  for i in range(10):
    Sys.Keys("[Down]")
  Sys.Keys("[Enter]")
  Sys.Keys(var_name)
  Sys.Keys("[Enter]")
  
def click_on_elipsis():
  Sys.Keys("[Right]")
  Sys.Keys("[Enter]")
#  Typecolumnelipsis

def select_variable_type_Dialog_popup_CE():
  Delay(3000,"Wait")
  Click_button_Dialog_popup_CE("REF_TO")
  Click_button_Dialog_popup_CE("OK")
  
def Click_button_Dialog_popup_CE(button_name):
#  button_name = "OK"
  obj = Sys.Process("ControlExpert", 4).Dialog("*")
  buttons_list = obj.FindAllChildren('WndClass', 'Button', 1000)
  for button in buttons_list:
    if button_name in str(button.WndCaption) :
      button.Click()
      Log.Message('Clicked ' + str(button.WndCaption) + ' button.')
      break
  else:
    Log.Warning("Button name mentioned doesnt exists")
    
  
def select_variable_type(val):
  Sys.Keys("[Right]")
  Sys.Keys("[Enter]")
  Sys.Keys(val)
  Sys.Keys("[Enter]") 
  
def select_Constant_check_box():
  Delay(3000)
  for i in range(10):
    Sys.Keys("[Right]")
    Delay(500)
  Delay(1000)
  Sys.Keys("[Enter]")
  
  
def Enter_P2P_in_Custom_box():
  Delay(3000)
  Sys.Keys("[Right]")
  Sys.Keys("[Enter]")
  Sys.Keys("P2P")
  Sys.Keys("[Enter]")  

  
def select_AdvSettings_properties_SVP(param):
  parent,val,val1 = param.split('$$')

  if parent.lower() == "supervision project":
    project_browser = refoff_obj.projectbrowserrotextbox.object
  elif parent.lower() == "aveva":
    project_browser = aveva_obj.systreeviewtextbox.object
#    project_browser = Sys.Process("ComputerSetupEditor", 3).Window("#32770", "Computer Setup Editor - [C:\\ProgramData\\AVEVA Plant SCADA 2023 R2\\Config\\citect.ini]", 1).Window("SysTreeView32", "Tree1", 1)
  else:
    Log.Warning("Invalid parent passed") 
    
  #  select_main_folder_project_browser_CE()
  project_browser.wItems.Item[0].Select()
  
  count = project_browser.wItemCount 
  Log.Message(str(count) + ' PB count')
  for i in range(count):
    if val in project_browser.wItem[i]:
      project_browser.SelectItem(val)
      Log.Message(val+" is selected")
      Applicationutility.wait_in_seconds(1500, 'wait')
      count1 = project_browser.wItems.Item[0].Items.Item[i].Items.Count
      for j in range(count1):
        if val1 in project_browser.wItems.Item[0].Items.Item[i].Items.Item[j].Text:
          project_browser.wItems.Item[0].Items.Item[i].Items.Item[j].Select()
          Log.Message(val1+" is selected")
          break
      break  
      
def Edit_Parameter_Value_AdvSettings_SVP(val): 
  obj_Parent = Sys.Process("EngineeringClient")
  obj_value = obj_Parent.Find("Name","Window('Static', 'Value:', *)",100)
  Top = obj_value.Top
  value_field = obj_Parent.FindAllChildren("Name","Window('Edit', '', *)",100)
  for value in value_field:
    Sys.HighlightObject(value,1)
    if value.Top <= obj_value.Top+10 and value.Top >= obj_value.Top-10 : # 147 151
      value.wText = val
      Log.Message(val + " is entered")
      break
      
def Verify_Parameter_Value_AdvSettings_SVP(param): 
  parent,val = param.split('$$')

  if parent.lower() == "supervision project":
    obj_Parent = Sys.Process("EngineeringClient")
  elif parent.lower() == "aveva":
    obj_Parent = aveva_obj.mainparenttextbox.object
    #obj_Parent = Sys.Process("ComputerSetupEditor",3)
  else:
    Log.Warning("Invalid parent passed") 
  
  obj_value = obj_Parent.Find("Name","Window('Static', 'Value:', *)",100)
  Top = obj_value.Top
  value_field = obj_Parent.FindAllChildren("Name","Window('Edit', '', *)",100)
  for value in value_field:
    Sys.HighlightObject(value,1)
    if value.Top <= obj_value.Top+10 and value.Top >= obj_value.Top-10 : # 147 151
      if str(value.wText) == str(val):
        Log.Checkpoint(value.wText+ " is updated") 
        break
      else:
        Log.Warning(val + " updated value is incorrect")
        
        
def drag_instance_drop_container_page_SP(template):
  template_list = proj_obj.containerpagedocktextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
  Workspace_editor = proj_obj.mdiclientwindowtextbox.object
  tox = Workspace_editor.ScreenLeft+10
  for i in range(len(template_list)):
    if template_list[i].Visible: 
      if template == str(template_list[i].DataContext.Identifier.OleValue):
            #Sys.HighlightObject(template_list[i])
            fromx = template_list[i].Width/2
            fromy = template_list[i].Height/2
            Log.Message('The object selected to drag is : ' + str(template_list[i].DataContext.Identifier.OleValue))
            Applicationutility.wait_in_seconds(2000, 'Wait')
            template_list[i].Click()
            Applicationutility.wait_in_seconds(2000, 'Wait')
            template_list[i].Drag(fromx-70, fromy, tox+100, 0)
            Applicationutility.wait_in_seconds(2000, 'Wait')
            break
            
def gsgsg():
  drag_instance_drop_container_page_SP("MotorGP_1")
 
def select_value_listview_SVP(val):
  list_items = proj_obj.listviewtextbox.object.FindAllChildren('ClrClassName', 'ListViewItem', 100)  
  for list in list_items:
    #Sys.HighlightObject(list)
    if val in list.DataContext.Identifier.OleValue:
      Applicationutility.wait_in_seconds(1000, 'Wait')
      list.Click()
      Applicationutility.wait_in_seconds(2000, 'Wait')
      break
  
def Double_click_on_header_OC ():
  identifier = "Process Expert"
  parent = Sys.Process("OperationClient").WPFObject("HwndSource: Main")
  object = parent.FindAllChildren("ClrClassName", "TextBlock", 1000)
  for obj in object:
    if identifier in obj.WPFControlText:      
        obj.DblClick() 
        Delay(2000)
        Log.Message("Double clicked")
  
def Verify_screen_visible():
  obj2 = Sys.Process("OperationClient").WPFObject("HwndSource: Main")
  if obj2.VisibleOnScreen:
    Log.Message("Visible On Screen")
  else:
    Log.Message("Not Visible On Screen")  
    
def Verify_variable_is_removed_Refine_Offline(var_name):
  var_name = "V1" 
  variables = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 100)
  for var in variables:
    if var.Text == var_name:
      Log.Warning(var.Text+" is not removed")
      break
  else:
    Log.Checkpoint(var_name+" is removed")
    
    
def edit_IP_Address(param):
  Identifier, value = param.split('$$')
  obj = refoff_obj.mdiwindowtextbox.object.FindAllChildren("ObjectType","IpAddress",100)
  for IP_obj in obj:
    if str(IP_obj.ObjectIdentifier) == Identifier:
      IP_obj.wAddress = value
      Log.Checkpoint(Identifier + " is updated as "+ IP_obj.wAddress)
      break
  else: 
    Log.Warning(Identifier + " is not updated - IP : "+ IP_obj.wAddress)
  
      
def Verify_Mapped_DTM_device_present_CE(Identifier):
  objects = topoexo_obj.dtmbrowserprop.object.FindAllChildren("ObjectType","OutlineItem",200)
  for obj in objects:
    Log.Message(str(obj.ObjectIdentifier))
    if Identifier in str(obj.ObjectIdentifier):
      Log.Checkpoint(str(obj.ObjectIdentifier)+" DTM device added")
      break
  else:
    Log.Warning(Identifier+" DTM device not added")

def Dblclick_dialog_panel_item_CE(param):
  new_device_panel = diace_obj.dialogpanelcetextbox.object
  panel_child = new_device_panel.FindAllChildren('Text', '*', 100)
  Log.Message(len(panel_child))
  for item in panel_child:
    #Log.Message(item.Text)
    if param == item.Text:
      item.DblClick()
      Log.Checkpoint(item.Text + ' is Double Clicked.')
      Applicationutility.wait_in_seconds(1000, 'Wait')
      break
  else:
    Log.Warning(param + ' not found.')    
   
def Click_dialog_panel_item_CE(param):
  Applicationutility.wait_in_seconds(1000, 'Wait')
  new_device_panel = diace_obj.dialogpanelcetextbox.object
  panel_child = new_device_panel.FindAllChildren('Text', '*', 100)
  for item in panel_child:
    if param == item.Text:
      item.Click()
      Log.Checkpoint(item.Text + ' is Selected.')
      Applicationutility.wait_in_seconds(1000, 'Wait')
      break
  else:
    Log.Warning(param + ' not found.')  

    
def Select_bottom_listitem_dialog_panel_item_CE(param):
  io_device = diace_obj.dialoglistboxcetextbox.object 
  for i in range(io_device.wItemCount):
#    Log.Message(io_device.wItem[i])
    if param in io_device.wItem[i]:
#      Log.Checkpoint(io_device.wItem[i])
      io_device.ClickItem(i)
      Log.Message(io_device.wItem[i] + ' is Selected.')
      Applicationutility.wait_in_seconds(1000, 'Wait')
      break
  else: 
    Log.Message(param + ' not found.')
  
def Rclick_Drops_EIO_add_new_device_CE():
    obj = refoff_obj.fbdsectionwindowtextbox.object
    obj.ClickR((obj.Width*.04), (obj.Height*.15))
    ce_obj.newdevicecetextbox.click()

def Select_bottom_listitem_EIO_dialog_panel_item_CE(param):
    io_device = diace_obj.dialoglistboxce1textbox.object.FindAllChildren('Text', '*')
    Log.Message(len(io_device))
    for item in io_device:
      if param in item.Text:
        item.Click()
        Log.Message(item.Text + ' is Selected.')
        Applicationutility.wait_in_seconds(1000, 'Wait')
        break
    else: 
      Log.Message(param + ' not found.')

def select_PLC_bus_combobox_item_CE(param):
  obj = refoff_obj.windowcomboboxtextbox.object
  Log.Message(obj.wItemCount)
  for i in range(len(obj.wItemList)):
    if param in obj.wItemList and obj.Visible:
      count = i
      obj.ClickItem(param)
      Applicationutility.wait_in_seconds(1000, 'Wait')
      Log.Checkpoint(f'{obj.wText} is selected.')
      break
      
  else:
    Log.Warning(f' is not present in combobox.')
  ce_obj.yescebuttonbutton.click()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  ce_obj.yescebuttonbutton.click()
    
  
def create_logical_network():
  controller_row = topo_obj.controllerpropertytab.object.FindAllChildren("ClrClassName", "Grid", 10)
  for control in controller_row:
    if getattr(getattr(control, "DataContext", None), "DisplayName", None) == "Controller":
      control.Click()
      aqUtils.Delay(500)
      for item in eng_obj.userdropdownmenuitemtextbox.object.FindAllChildren("ClrClassName", "ComboBoxItem", 10):
        if item.WPFControlText == "False":
          item.Click() if item.Enabled else Log.Error("Dropdown item 'False' is disabled.")
          return
  Log.Error("Could not find the specific 'Controller' element.")
  

def Click_tab_item_EIO_config_window(identifier):
#  identifier = "IPConfig"
  Window = proj_obj.mdiclientwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
  for Window_Text in Window:
    if identifier in Window_Text.Text:
      Window_Text.Click()
      Log.Checkpoint(Window_Text.Text + " is Clicked")
      break
  else: 
    Log.Warning(identifier + " is not available")

def Add_Vairable_Logic_Block_link_P2P(param):
  identifier , variable = param.split("$$")
  Window = proj_obj.mdiclientwindowtextbox.object
  Window_lst = Window.FindAllChildren("Name", "TextObject*", 1000)
  for obj in Window_lst:
    if identifier in obj.Text and obj.Visible:
      obj.DblClick()
      Sys.Keys(variable)
      Sys.Keys("[Enter]")
      Log.Checkpoint(obj.Text + " is Double Clicked")
      break
  else:
    Log.Warning(identifier + " is not available")
      
    
def change_Port_Number_PLC_Simulator():
  Simulator_Textbox = diace_obj.simulatorporttextbox.object
  Simulator_Textbox.SetText("503")
  
  
def click_MenuItem_Toolbar_CE(menu_option):
  menu_items = ce_obj.modaldialogewindowoptionsce.object.FindAllChildren('ObjectType', 'MenuItem', 1000)
  for item in menu_items:
#    Log.Message(str(item.ObjectIdentifier))
    if menu_option in str(item.ObjectIdentifier):
      item.click()
      break
  
def Select_network_CE(menu_option):
  menu_items = ce_obj.okmodaldialoguewindowce.object.FindChild('wText', 'No Selection', 10)
  Log.Message(menu_items.wText)
  menu_items.ClickItem(menu_option)
  Log.Message(menu_items.wText+" is selected")
       
      
def Click_ok_button_add_network_popup_CE(button):
  menu_items = ce_obj.okmodaldialoguewindowce.object.FindChild(('WndClass', 'WndCaption'),('Button',button), 10)
  menu_items.Click()
  Log.Message("Ok is Clicked")
 
    
def select_item_mdi_window_CE(identifier):        
  menu_items = refoff_obj.mdiwindowtextbox.object.FindAllChildren('WndClass', 'ComboBox',20)
  for item in menu_items:
    if identifier in str(item.wItemList): 
      item.ClickItem(identifier)
      Log.Message(item.wText+" is selected")
      break
  else:
      Log.Message(identifier+" is not selected")
    
    
def afbsdzv():
  list_items = "Communication$$Networks" #"ControlProject_1", 
  Right_click_selected_project_browser_item_CE(list_items)
#  data_selection = refoff_obj.dataselectiontextbox  #.object
  
def knc():
#  Delay(5000)
#  click_MenuItem_Toolbar_CE("New Network")
#  Select_network_CE("Ethernet")
  Click_ok_button_add_network_popup_CE("OK")
#  
#  Click_tab_item_EIO_config_window("Channel 0")
#  select_item_mdi_window_CE("ETH TCP IP")
#  select_item_mdi_window_CE("Ethernet_2")
  
  
  