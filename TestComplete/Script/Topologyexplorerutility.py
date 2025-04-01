from TopologyExplorerTab import TopologyExplorerTab
from EngineeringClient import EngineeringClient
import Applicationutility
from MessageBox import MessageBox
from RefineOffline import RefineOffline
from ControlExpert import ControlExpert
from ProjectExplorerTab import ProjectExplorerTab
from SystemExplorerScreen import SystemExplorerScreen
from CurrentScreen import CurrentScreen

topo_obj = TopologyExplorerTab()
msg_obj = MessageBox()
eng_obj = EngineeringClient()
refo_obj = RefineOffline()
con_obj = ControlExpert()
proj_obj = ProjectExplorerTab()
sys_obj = SystemExplorerScreen()
cur_obj = CurrentScreen()

###############################################################################
# Function: select_tool_drag_drop_default_physical_view_TE
# Description: Selects a tool from the toolbox and drags it to a specified position in the default physical view.
# Parameter: param (str) - Format: "folder1$$folder2$$tool$$dropposition"
# Example: "FolderA$$FolderB$$ToolName$$pos_1"
###############################################################################
def select_tool_drag_drop_default_physical_view_TE(param):
  folder1, folder2, tool, dropposition = param.split('$$')
  dict = {'pos_1': 1, 'pos_2': 1.3, 'pos_3': 1.9, 'pos_4': 3.3}
  if dropposition in dict:
    pos = dict[dropposition]
  toolbox = topo_obj.toolboxcatalogbutton
  toolbox_list = toolbox.find_children_for_group_header_row()
  diagram = topo_obj.partdiagramcontroltextbox.object
  tox = diagram.ScreenLeft
  toy = diagram.ScreenTop
  for item in toolbox_list:
    if item.Visible:
      if folder1 in item.DataContext.Name.OleValue:
        if not item.IsExpanded:
          item.IsExpanded = True
      else:
        item.IsExpanded = False
  Applicationutility.wait_in_seconds(1000, 'Wait')
  toolbox_list1 = topo_obj.toolboxcatalogbutton.find_children_for_group_header_row()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  for ele in toolbox_list1:
      if ele.Visible:
        if folder2 in ele.DataContext.Name.OleValue:
          if not ele.IsExpanded:
            ele.IsExpanded = True
  Applicationutility.wait_in_seconds(2000, 'Wait')          
  list = topo_obj.toolboxcatalogbutton.find_children_for_grid_view_row()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  for row in list:
    if row.Visible:
      if tool in row.DataContext.PartNumber.OleValue:
        fromx = row.Width
        fromy = row.Height
        reg1 = row.ScreenLeft
        reg2 = row.ScreenTop
        row.Drag(50, fromy/2, tox-reg1, toy-(reg2/pos))
        break

###############################################################################
# Function: expand_physical_view_select_default_TE
# Description: Expands the "Physical Views" tree and selects the "Default Physical View".
# Parameter: None
###############################################################################
def expand_physical_view_select_default_TE():
  sys_proj = topo_obj.systemprojecttextbox
  sys_list = sys_proj.find_children_for_treeviewrow()
  Log.Message(len(sys_list))
  for item in sys_list:
    if item.Visible:
      if 'Physical Views' in item.DataContext.DisplayName.OleValue:
        item.DataContext.IsExpanded = True
        #sys_proj.refresh()
  Applicationutility.wait_in_seconds(2000, 'Wait')
  sys_list = sys_proj.find_children_for_treeviewrow()
  for ele in sys_list:
    if ele.Visible:
      if 'Default Physical View' in ele.DataContext.DisplayName.OleValue:
        ele.DblClick()
        Applicationutility.wait_in_seconds(2000, 'Wait')
        break

###############################################################################
# Function: grid_resize_TE
# Description: Resizes the grid layout in the topology explorer to ensure proper visibility of elements.
# Parameter: None
###############################################################################
def grid_resize_TE():
  dia = topo_obj.managerbutton.object
  sys = topo_obj.systemprojecttextbox
  prop = topo_obj.propertyinspectorviewbutton
  if sys.width < 180:
    dia.drag(sys.width+5, dia.height/2, 100, 0)
  if prop.width < 180:
    dia.drag((dia.width-prop.width-5), dia.height/2, -275, 0)

###############################################################################
# Function: select_cpu_reference_TE
# Description: Selects a CPU reference based on the version number and processor name.
# Parameter: param (str) - Format: "version_number$$processor_name"
# Example: "V1.0$$ProcessorX"
###############################################################################
def select_cpu_reference_TE(param):
  version_number, processor_name = param.split('$$')
  cpu_ref = topo_obj.catalogviewtextbox.object
  #cpu_list = cpu_ref.find_children_for_group_header_row()
  cpu_list = cpu_ref.FindAllChildren('ClrClassName', 'GroupHeaderRow', 1000)
  for version in cpu_list:
    if version.Visible:
      if version_number in str(version.DataContext.Name):
        version.IsExpanded = True
      else:
        version.IsExpanded = False
  part = cpu_ref.FindAllChildren('ClrClassName', 'GridViewRow', 1000)
  for processor in part:
    if processor.Visible:
      if version_number in str(processor.DataContext.PlcVersion.OleValue):
        if processor_name in str(processor.DataContext.PlcReference.OleValue):
          processor.IsSelected = True
          break
  Applicationutility.wait_in_seconds(2000, 'Wait')
  ok =  topo_obj.okbuttonbutton.object
  ok.Click()

###############################################################################
# Function: click_tab_properties_toolbar_Verify
# Description: Verifies if a specific tab item exists in the "PROPERTIES" toolbar and clicks it.
# Parameter: TabItem (str) - Name of the tab item to verify and click.
###############################################################################
def click_tab_properties_toolbar_Verify(TabItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for i in TabItem_List:
    if TabItem in  i.WPFControlText:
      i.Click()
      Log.Message(f'{i.WPFControlText} has been verified')
      break
  else:
    Log.Message(f'{i.WPFControlText} has not been verified')

###############################################################################
# Function: Click_on_toolbar_icon_TE
# Description: Clicks on a specific toolbar icon in the topology explorer.
# Parameter: icon_name (str) - Tooltip text of the icon to click.
###############################################################################
def Click_on_toolbar_icon_TE(icon_name):
  manager_list = topo_obj.roottextbox.object.FindAllChildren('ClrClassName', 'Border', 1000)
  for item in manager_list:
    if icon_name  in item.DataContext.ToolTip.Data.OleValue:
      item.Click()
      break

###############################################################################
# Function: click_MenuItem_Toolbar
# Description: Clicks on a menu item in the toolbar context menu.
# Parameter: menu_option (str) - Name of the menu option to click.
###############################################################################
def click_MenuItem_Toolbar(menu_option):
  menu_items = eng_obj.rclickmenutextbox.object.FindAllChildren('ClrClassName', 'MenuItem', 1000)
  Log.Message(len(menu_items))
  for item in menu_items:
    Log.Message((item.WPFControlText))
    if menu_option in item.WPFControlText:
      item.click()

###############################################################################
# Function: verify_properties_tab_toolbar
# Description: Verifies if a specific tab item exists in the "PROPERTIES" toolbar.
# Parameter: TabItem (str) - Name of the tab item to verify.
###############################################################################
def verify_properties_tab_toolbar(TabItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for i in TabItem_List:
    if TabItem in  i.WPFControlText:
      Log.Message(f'{i.WPFControlText} has been verified')
      break
    else:
      Log.Message(f'{i.WPFControlText} has not been verified')

###############################################################################
# Function: Expand_Propertiestab
# Description: Expands a specific property item in the "PROPERTIES" tab.
# Parameter: PropertyItem (str) - Name of the property item to expand.
###############################################################################
def Expand_Propertiestab(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and  view_item.IsExpandable  :
          view_item.IsExpanded = True

###############################################################################
# Function: Dclick_Propertiestab
# Description: Double-clicks on a specific property item in the "PROPERTIES" tab.
# Parameter: PropertyItem (str) - Name of the property item to double-click.
###############################################################################
def Dclick_Propertiestab(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and  view_item.IsExpandable  :
          view_item.DblClick()

###############################################################################
# Function: Create_Logical_Network_Button
# Description: Clicks on a button to create a logical network.
# Parameter: button_name (str) - Name of the button to click.
###############################################################################
def Create_Logical_Network_Button(button_name):
  button_list = topo_obj.createlogicalnetworktextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  for button in button_list:
    if button_name in button.WPFControlText:
      button.Click()
    else:
      Log.Message("Button doesnt exists")

###############################################################################
# Function: WorkStation_Items
# Description: Clicks on workstation items multiple times based on the count provided.
# Parameter: Item_name_count (str) - Format: "ItemName$$count"
# Example: "Workstation1$$3"
###############################################################################
def WorkStation_Items(Item_name_count):
  Item_name,count = Item_name_count.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for i in range(int(count)):
        for view_item in ViewList:
          if Item_name in view_item.DataContext.DisplayName.OleValue:
            tox = view_item.Width - 5
            toy = (view_item.Height)/2
            view_item.Click(tox,toy)

###############################################################################
# Function: Security_option_properties
# Description: Toggles the security option in the properties tab based on the provided value.
# Parameter: Value (str) - The value to set for the security option (e.g., "Enabled", "Disabled").
###############################################################################
def Security_option_properties(Value):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'EnumEditBox', 1000)
      Log.Message(len(ViewList))
      for view_item in ViewList:
        Log.Message(view_item.Value)
        if Value  != view_item.Value  :
          view_item.Click()
          Enabled = topo_obj.securityoptionenabledbutton.object
          Disabled = topo_obj.securityoptiondisabledbutton.object
          if Value == Enabled.WPFControlText:
            Enabled.Click()
            break
          else:
            Disabled.Click()
            break

###############################################################################
# Function: close_tab_item
# Description: Closes a specific tab item in the topology explorer.
# Parameter: tab_name (str) - Name of the tab to close.
###############################################################################
def close_tab_item(tab_name):
  a = topo_obj.managerbutton.object
  list = a.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for item in list:
    if tab_name in item.DataContext.Title.OleValue:
      item.Click(item.Width-15, item.Height/2)

###############################################################################
# Function: DetailMessageDialogBox_Buttons
# Description: Clicks a button in the detail message dialog box.
# Parameter: button_name (str) - Name of the button to click (e.g., "Yes", "No").
###############################################################################
def DetailMessageDialogBox_Buttons(button_name):
  Popup_buttons = topo_obj.detailmessagedialogboxtextbox.object
  if button_name == "Yes" :
    tox = Popup_buttons.Width*0.8
    toy = (Popup_buttons.Height)*0.88
    Popup_buttons.Click(tox,toy)
  else:
    tox = Popup_buttons.Width*0.95
    toy = (Popup_buttons.Height)*0.88
    Popup_buttons.Click(tox,toy)

###############################################################################
# Function: Verify_DetailMessageDialogBox
# Description: Verifies if a specific message exists in the detail message dialog box.
# Parameter: message (str) - The message to verify.
###############################################################################
def Verify_DetailMessageDialogBox(message):
  Window_Message = topo_obj.detailmessagedialogboxtextbox.object.Message.OleValue
  if message in Window_Message:
    Log.Message(f'{Window_Message} verified')
  else:
    Log.Message(f'{Window_Message} not verified')

###############################################################################
# Function: Dclick_Propertiestab_entervalue
# Description: Double-clicks on a property item in the "PROPERTIES" tab and enters a value.
# Parameter: PropertyItemValue (str) - Format: "PropertyItem$$Value"
# Example: "PropertyName$$Value123"
###############################################################################
def Dclick_Propertiestab_entervalue(PropertyItemValue):
  PropertyItem,Value = PropertyItemValue.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and view_item.Visible :
          view_item.DblClick()
          Sys.Keys(Value)
          Sys.Keys('[Enter]')
      else:
        Log.Message("Property doesnt exists")

###############################################################################
# Function: confirmation_pop_up_TE
# Description: Clicks a button in the confirmation pop-up dialog.
# Parameter: button_value (str) - The button text to click (e.g., "Yes", "No").
###############################################################################
def confirmation_pop_up_TE(button_value):
  popup = msg_obj.detailmessagedialogtextbox.object
#  popup = Sys.Process("ControlExpert.Topology").WPFObject("HwndSource: DetailMessageDialog", "*")
#  #popup.ocr_blockby_text('Yes')
  OCR.Recognize(popup).BlockByText(button_value).Click()

###############################################################################
# Function: confirm_pop
# Description: Clicks a button in the confirmation pop-up for logical network creation.
# Parameter: button_value (str) - The button text to click (e.g., "Ok", "Cancel").
###############################################################################
def confirm_pop(button_value):
  popup = msg_obj.createlogicalnetworktextbox.object
  #Sys.Process("ControlExpert.Topology").WPFObject("HwndSource: Window", "Create Logical Network")
  OCR.Recognize(popup).BlockByText(button_value).Click()

###############################################################################
# Function: select_ContextMenu_Items_TE
# Description: Selects an item from the context menu in the topology explorer.
# Parameter: menu_item (str) - The name of the menu item to select.
###############################################################################
def select_ContextMenu_Items_TE(menu_item):
  menu = topo_obj.rclickmenutetextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 1000)
  
  Applicationutility.wait_in_seconds(2000, 'wait')
  for item in menu_items:
    
    if item.Header.DisplayName: 
      Log.Message(str(item.Header.DisplayName.OleValue))                               
      if str(item.Header.DisplayName.OleValue) == str(menu_item):
        item.Click()
        Log.Message('The Context Menu Item clicked is : ' + str(menu_item))
        break
  Applicationutility.wait_in_seconds(3000, 'wait')

###############################################################################
# Function: select_context_submenu_Items_TE
# Description: Selects a submenu item from the context menu in the topology explorer.
# Parameter: menu_item (str) - The name of the submenu item to select.
###############################################################################
def select_context_submenu_Items_TE(menu_item):
  menu = topo_obj.rclicksubmenutetextbox.object
  menu_items = menu.FindAllChildren("ClrClassName", "MenuItem", 1000)
  Applicationutility.wait_in_seconds(2000, 'wait')
  for item in menu_items: 
    if item.Role.OleValue == "SubmenuItem":                             
      if str(item.DataContext.DisplayName) == str(menu_item):
        item.Click()
        Log.Message('The Context Menu Item clicked is : ' + str(menu_item))
        break
  Applicationutility.wait_in_seconds(3000, 'wait')

###############################################################################
# Function: click_tab_properties_TE
# Description: Clicks on a specific tab item in the "PROPERTIES" tab.
# Parameter: TabItem (str) - Name of the tab item to click.
###############################################################################
def click_tab_properties_TE(TabItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
  for i in TabItem_List:
    if TabItem in  i.WPFControlText:
      i.Click()

###############################################################################
# Function: select_dropdown_value_properties_TE
# Description: Selects a value from a dropdown in the properties tab.
# Parameter: param (str) - Format: "tab_name$$expand_item$$dropdown$$select_value"
# Example: "CONFIGURATION$$Interfaces$$Security Level$$High"
###############################################################################
def select_dropdown_value_properties_TE(param):
  tab_name, expand_item, dropdown, select_value = param.split('$$')
  properties = topo_obj.propertiesgridtextbox.object
  #Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WinFormsObject("WinFormsAdapter", "", 1).WinFormsObject("Panel", "", 2).WPFObject("HwndSource: root").WPFObject("root").WPFObject("Grid").WPFObject("manager").WPFObject("ContentPresenter", "", 1).WPFObject("ToolView", "", 1).WPFObject("DockPanel", "", 1).WPFObject("Grid", "", 1).WPFObject("manager").WPFObject("LayoutPanelControl", "", 1).WPFObject("LayoutPanelControl", "", 1).WPFObject("LayoutPanelControl", "", 1).WPFObject("LayoutAnchorablePaneGroupControl", "", 1).WPFObject("LayoutAnchorablePaneControl", "", 1).WPFObject("LayoutAnchorableControl", "", 1).WPFObject("ContentPresenter", "", 1).WPFObject("ContentPresenter", "", 1).WPFObject("PropertyInspectorView", "", 1).WPFObject("Grid", "", 1).WPFObject("LazyContentControl", "", 1).WPFObject("TabControlAutoHide", "", 1).WPFObject("PropertyGridControl", "", 1)
  click_tab_properties_TE(tab_name)
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Expand_Propertiestab(expand_item)
  property_list = properties.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
  for item in property_list:
    if dropdown in item.DataContext.DisplayName.OleValue:
      item.DataContext.Value = select_value
      Log.Message('The dropdown value ' + str(item.DataContext.Value.OleValue) + ' has been selected')
      break

###############################################################################
# Function: select_combobox_TE
# Description: Selects a value from a combobox in the properties tab.
# Parameter: param (str) - Format: "dropdown$$select_value"
# Example: "Logical Network$$New"
###############################################################################
def select_combobox_TE(param):
  dropdown, select_value = param.split('$$')
  properties = topo_obj.propertiesgridtextbox.object
  #properties = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WinFormsObject("WinFormsAdapter", "", 1).WinFormsObject("Panel", "", 2).WPFObject("HwndSource: root").WPFObject("root").WPFObject("Grid").WPFObject("manager").WPFObject("ContentPresenter", "", 1).WPFObject("ToolView", "", 1).WPFObject("DockPanel", "", 1).WPFObject("Grid", "", 1).WPFObject("manager").WPFObject("LayoutPanelControl", "", 1).WPFObject("LayoutPanelControl", "", 1).WPFObject("LayoutPanelControl", "", 1).WPFObject("LayoutAnchorablePaneGroupControl", "", 1).WPFObject("LayoutAnchorablePaneControl", "", 1).WPFObject("LayoutAnchorableControl", "", 1).WPFObject("ContentPresenter", "", 1).WPFObject("ContentPresenter", "", 1).WPFObject("PropertyInspectorView", "", 1).WPFObject("Grid", "", 1).WPFObject("LazyContentControl", "", 1).WPFObject("TabControlAutoHide", "", 1).WPFObject("PropertyGridControl", "", 1)
  Applicationutility.wait_in_seconds(1000, 'Wait')
  property_list = properties.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
  for item in property_list:
    if dropdown in item.DataContext.DisplayName.OleValue:
      comb_lst = item.FindAllChildren('ClrClassName', 'ComboBox', 1000)
      if len(comb_lst) == 1:
        for i in range(comb_lst[0].wItemCount):
          if select_value in comb_lst[0].Items.Item[i].Identifier.OleValue:
            comb_lst[0].SelectedIndex = i
            Log.Message(str(comb_lst[0].Items.Item[i].Identifier.OleValue) + ' item has been selected.')
            break

###############################################################################
# Function: click_enable_disable_properties_TE
# Description: Enables or disables a property in the properties tab.
# Parameter: param (str) - Format: "tab_name$$expand_item$$dropdown$$select_value"
# Example: "SECURITY$$Password Protection$$Controller$$Disabled