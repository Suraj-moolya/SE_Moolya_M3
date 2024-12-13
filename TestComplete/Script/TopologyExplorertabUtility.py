from TopologyExplorerTab import TopologyExplorerTab
topo_obj = TopologyExplorerTab()

        
def Click_on_toolbar_icon_TE(icon_name):##
  manager_list = topo_obj.roottextbox.object.FindAllChildren('ClrClassName', 'Border', 1000)
  for item in manager_list:
    if icon_name  in item.DataContext.ToolTip.Data.OleValue:
      item.Click()
      break
      
def click_MenuItem_Toolbar(menu_option):##
  menu_items = topo_obj.popuproottextbox.object.FindAllChildren('ClrClassName', 'MenuItem', 1000)
  Log.Message(len(menu_items))
  for item in menu_items:
    Log.Message((item.WPFControlText))
    if menu_option in item.WPFControlText:
      item.click()
      
      
def click_tab_properties_toolbar_Verify(TabItem):##
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
      



def Expand_Propertiestab(PropertyItem):###
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and  view_item.IsExpandable  :
          view_item.IsExpanded = True
      else:
        Log.Message("Property doesnt exists")
          
def Dclick_Propertiestab(PropertyItem):
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for view_item in ViewList:
        if PropertyItem in view_item.DataContext.DisplayName.OleValue and  view_item.IsExpandable  :
          view_item.DblClick()
      else:
        Log.Message("Property doesnt exists")
          
          
def Create_Logical_Network_Button(button_name):
  button_list = topo_obj.createlogicalnetworktextbox.object.FindAllChildren('ClrClassName', 'Button', 1000)
  for button in button_list:
    if button_name in button.WPFControlText:
      button.Click()
    else:
      Log.Message("Button doesnt exists")


      
def WorkStation_Items(Item_name_count):
  Item_name,count = Item_name_count.split("$$")
  Tab_list = topo_obj.layoutpanelcontroltextbox.object.FindAllChildren('ClrClassName', 'LayoutAnchorableControl', 1000)
  for tab in Tab_list:
    if tab.DataContext.Title.OleValue == "PROPERTIES":
      tab.Refresh()
      ViewList = tab.FindAllChildren('ClrClassName', 'PropertyGridItem', 1000)
      for i in range(int(count)):
        for view_item in ViewList:
          if Item_name in view_item.DataContext.DisplayName.OleValue :
            tox = view_item.Width - 5
            toy = (view_item.Height)/2
            view_item.Click(tox,toy)
      else:
        Log.Message("Property doesnt exists")
  
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
      
def Verify_DetailMessageDialogBox(message):
  Window_Message = topo_obj.detailmessagedialogboxtextbox.object.Message.OleValue
  if message in Window_Message:
    Log.Message(f'{Window_Message} verified')
  else:
    Log.Message(f'{Window_Message} not verified')
    
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
        
        

        


        

          
          
