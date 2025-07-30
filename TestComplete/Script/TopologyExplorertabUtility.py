from TopologyExporerTab import TopologyExporerTab
topo_obj = TopologyExporerTab()

###############################################################################
# Function : Click_on_toolbar_icon_TE
# Description : Clicks on a toolbar icon in the Topology Explorer tab based on the icon name.
# Parameter : icon_name (str) - Name of the toolbar icon to click. Example: "Save"
###############################################################################
def Click_on_toolbar_icon_TE(icon_name):##
  manager_list = topo_obj.roottextbox.object.FindAllChildren('ClrClassName', 'Border', 1000)
  if not manager_list:
    Log.Message("No toolbar icons found.")
    return
  for item in manager_list:
    if icon_name in item.DataContext.ToolTip.Data.OleValue:
      item.Click()
      break
  else:
    Log.Message(f"Icon '{icon_name}' not found.")

###############################################################################
# Function : click_MenuItem_Toolbar
# Description : Clicks on a menu item in the toolbar based on the menu option name.
# Parameter : menu_option (str) - Name of the menu option to click. Example: "Open"
###############################################################################
def click_MenuItem_Toolbar(menu_option):##
  menu_items = topo_obj.popuproottextbox.object.FindAllChildren('ClrClassName', 'MenuItem', 1000)
  if not menu_items:
    Log.Message("No menu items found.")
    return
  Log.Message(len(menu_items))
  for item in menu_items:
    Log.Message((item.WPFControlText))
    if menu_option in item.WPFControlText:
      item.click()
      break
  else:
    Log.Message(f"Menu option '{menu_option}' not found.")

###############################################################################
# Function : click_tab_properties_toolbar_Verify
# Description : Verifies and clicks on a specific tab item under the "PROPERTIES" tab.
# Parameter : TabItem (str) - Name of the tab item to verify and click. Example: "General"
###############################################################################
def click_tab_properties_toolbar_Verify(TabItem):##
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  if not Tab_list:
    Log.Message("No tabs found.")
    return
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      TabItem_List = tab.FindAllChildren('ClrClassName', 'TabItem', 1000)
      if not TabItem_List:
        Log.Message("No tab items found under 'PROPERTIES'.")
        return
  for i in TabItem_List:
    if TabItem in i.WPFControlText:
      i.Click()
      Log.Message(f'{i.WPFControlText} has been verified')
      break
  else:
    Log.Message(f"Tab item '{TabItem}' not found.")

###############################################################################
# Function : Expand_Propertiestab
# Description : Expands a specific property item under the "PROPERTIES" tab if it is expandable.
# Parameter : PropertyItem (str) - Name of the property item to expand. Example: "Network Settings"
###############################################################################
def Expand_Propertiestab(PropertyItem):###
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  if not Tab_list:
    Log.Message("No tabs found.")
    return
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      if not ViewList:
        Log.Message("No property items found.")
        return
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and view_item.IsExpandable:
          view_item.IsExpanded = True
          break
      else:
        Log.Message(f"Property '{PropertyItem}' does not exist or is not expandable.")

###############################################################################
# Function : Dclick_Propertiestab
# Description : Double-clicks on a specific property item under the "PROPERTIES" tab.
# Parameter : PropertyItem (str) - Name of the property item to double-click. Example: "IP Address"
###############################################################################
def Dclick_Propertiestab(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  if not Tab_list:
    Log.Message("No tabs found.")
    return
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      if not ViewList:
        Log.Message("No property items found.")
        return
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and view_item.IsExpandable:
          view_item.DblClick()
          break
      else:
        Log.Message(f"Property '{PropertyItem}' does not exist or is not expandable.")

###############################################################################
# Function : Create_Logical_Network_Button
# Description : Clicks on a button in the "Create Logical Network" section based on the button name.
# Parameter : button_name (str) - Name of the button to click. Example: "Add Network"
###############################################################################
def Create_Logical_Network_Button(button_name):
  button_list = topo_obj.createlogicalnetworktextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  if not button_list:
    Log.Message("No buttons found.")
    return
  for button in button_list:
    if button_name in button.WPFControlText:
      button.Click()
      break
  else:
    Log.Message(f"Button '{button_name}' does not exist.")

###############################################################################
# Function : WorkStation_Items
# Description : Clicks on a specific workstation item multiple times based on the count provided.
# Parameter : Item_name_count (str) - Format: "ItemName$$Count". Example: "Workstation1$$3"
###############################################################################
def WorkStation_Items(Item_name_count):
  Item_name,count = Item_name_count.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  if not Tab_list:
    Log.Message("No tabs found.")
    return
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      if not ViewList:
        Log.Message("No property items found.")
        return
      for i in range(int(count)):
        for view_item in ViewList:
          if Item_name in view_item.DataContext.DisplayName.OleValue :
            tox = view_item.Width - 5
            toy = (view_item.Height)/2
            view_item.Click(tox,toy)
            break
        else:
          Log.Message(f"Property '{Item_name}' does not exist.")
  
###############################################################################
# Function : Security_option_properties
# Description : Updates the security option property to the specified value.
# Parameter : Value (str) - Desired value for the security option. Example: "Enabled"
###############################################################################
def Security_option_properties(Value):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  if not Tab_list:
    Log.Message("No tabs found.")
    return
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'EnumEditBox', 1000)
      if not ViewList:
        Log.Message("No security options found.")
        return
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
          elif Value == Disabled.WPFControlText:
            Disabled.Click()
            break
      else:
        Log.Message(f"Security option '{Value}' does not exist.")
            
###############################################################################
# Function : DetailMessageDialogBox_Buttons
# Description : Clicks on a button in the detail message dialog box based on the button name.
# Parameter : button_name (str) - Name of the button to click. Example: "Yes"
###############################################################################
def DetailMessageDialogBox_Buttons(button_name):
  Popup_buttons = topo_obj.detailmessagedialogboxtextbox.object
  if not Popup_buttons:
    Log.Message("No popup buttons found.")
    return
  if button_name == "Yes" :
    tox = Popup_buttons.Width*0.8
    toy = (Popup_buttons.Height)*0.88
    Popup_buttons.Click(tox,toy)
  elif button_name == "No":
    tox = Popup_buttons.Width*0.95
    toy = (Popup_buttons.Height)*0.88
    Popup_buttons.Click(tox,toy)
  else:
    Log.Message(f"Button '{button_name}' does not exist in the dialog box.")
      
###############################################################################
# Function : Verify_DetailMessageDialogBox
# Description : Verifies the message displayed in the detail message dialog box.
# Parameter : message (str) - Expected message to verify. Example: "Operation Successful"
###############################################################################
def Verify_DetailMessageDialogBox(message):
  Window_Message = topo_obj.detailmessagedialogboxtextbox.object.Message.OleValue
  if not Window_Message:
    Log.Message("No message found in the dialog box.")
    return
  if message in Window_Message:
    Log.Message(f'{Window_Message} verified')
  else:
    Log.Message(f'{Window_Message} not verified')
    
###############################################################################
# Function : Dclick_Propertiestab_entervalue
# Description : Double-clicks on a property item under the "PROPERTIES" tab and enters a value.
# Parameter : PropertyItemValue (str) - Format: "PropertyItem$$Value". Example: "IP Address$$192.168.1.1"
###############################################################################
def Dclick_Propertiestab_entervalue(PropertyItemValue):
  PropertyItem,Value = PropertyItemValue.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  if not Tab_list:
    Log.Message("No tabs found.")
    return
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      if not ViewList:
        Log.Message("No property items found.")
        return
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and view_item.Visible :
          view_item.DblClick()
          Sys.Keys(Value)
          Sys.Keys('[Enter]')
          break
      else:
        Log.Message(f"Property '{PropertyItem}' does not exist.")










