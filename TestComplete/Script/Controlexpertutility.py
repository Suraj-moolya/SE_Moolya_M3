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
# Function: select_main_folder_project_browser_CE
# Description: Selects the main folder in the project browser of Control Expert.
# Parameter: None
###############################################################################
def select_main_folder_project_browser_CE():
    project_browser = refoff_obj.projectbrowserrotextbox.object
    project_browser.wItems.Item[0].Select()
    Applicationutility.wait_in_seconds(1000, 'Wait')

###############################################################################
# Function: select_project_browser_item_CE
# Description: Selects a specific item in the project browser of Control Expert.
# Parameter: val (str) - The name of the item to be selected.
# Example: select_project_browser_item_CE("MainFolder")
###############################################################################
def select_project_browser_item_CE(val):
    project_browser = refoff_obj.projectbrowserrotextbox.object
    count = project_browser.wItemCount
    for i in range(count):
        if val in str(project_browser.wItem[i]):
            project_browser.SelectItem(project_browser.wItem[i])
#            Log.Message(project_browser.wItem[i] + 'is selected')
            break
    else:
        Log.Warning(val + ' is not selected')

###############################################################################
# Function: doubleclick_project_browser_item_CE
# Description: Double-clicks a specific item in the project browser of Control Expert.
# Parameter: val (str) - The name of the item to be double-clicked.
# Example: doubleclick_project_browser_item_CE("SubFolder")
###############################################################################
def doubleclick_project_browser_item_CE(val):
    project_browser = refoff_obj.projectbrowserrotextbox.object
    count = project_browser.wItems.Item[0].Items.Count
    for i in range(count + 1):
        if val in project_browser.wItem[i]:
            project_browser.DblClickItem(project_browser.wItem[i])
#            Log.Message(project_browser.wItem[i] + 'is selected' )
            break
    else:
        Log.Warning(val + ' is not Click')

###############################################################################
# Function: rightclick_project_browser_item_CE
# Description: Right-clicks a specific item in the project browser of Control Expert.
# Parameter: val (str) - The name of the item to be right-clicked.
# Example: rightclick_project_browser_item_CE("SubFolder")
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
# Function: maximize_window_CE
# Description: Maximizes the currently active window in Control Expert.
# Parameter: None
###############################################################################
def maximize_window_CE():
    try:
        Applicationutility.wait_in_seconds(2000, 'Wait')
        win = refoff_obj.mdiwindowtextbox.object
        win.Maximize()
    except:
        Log.Message('No Window to Maximize')

###############################################################################
# Function: double_click_selected_project_browser_item_CE
# Description: Navigates through a hierarchy of items in the project browser and double-clicks the last item.
# Parameter: param (str) - A string of items separated by "$$", representing the hierarchy.
# Example: double_click_selected_project_browser_item_CE("MainFolder$$SubFolder$$Item")
###############################################################################
def double_click_selected_project_browser_item_CE(param):
    selection_items_list = param.split('$$')
    select_main_folder_project_browser_CE()
    max = len(selection_items_list)
    for i in range(max):
        if i != (max - 1):
            select_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(500, 'wait')
        else:
            doubleclick_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(1500, 'wait')
            maximize_window_CE()
            Applicationutility.wait_in_seconds(2000, 'wait')

###############################################################################
# Function: Right_click_selected_project_browser_item_CE
# Description: Navigates through a hierarchy of items in the project browser and right-clicks the last item.
# Parameter: param (str) - A string of items separated by "$$", representing the hierarchy.
# Example: Right_click_selected_project_browser_item_CE("MainFolder$$SubFolder$$Item")
###############################################################################
def Right_click_selected_project_browser_item_CE(param):
    selection_items_list = param.split('$$')
    select_main_folder_project_browser_CE()
    max = len(selection_items_list)
    for i in range(max):
        if i != (max - 1):
            select_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(500, 'wait')
        else:
            rightclick_project_browser_item_CE(selection_items_list[i])
            Applicationutility.wait_in_seconds(1500, 'wait')

###############################################################################
# Function: rclick_window_CE
# Description: Performs a right-click action on the center of the active window and interacts with various UI elements.
# Parameter: None
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

###############################################################################
# Function: RClick_on_Block_Refine_Offline
# Description: Right-clicks on a specific block in the Refine Offline window based on its identifier.
# Parameter: identifier (str) - The text identifier of the block to be right-clicked.
# Example: RClick_on_Block_Refine_Offline("BlockName")
###############################################################################
def RClick_on_Block_Refine_Offline(identifier):  
    Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Warning("No blocks found in the Refine Offline window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text and Window_Text.Visible:
            Window_Text.ClickR()
            Log.Message(Window_Text.Text + ' is Right Clicked.')
            break
    else:
        Log.Message(Window_Text.Text + ' is not visible in the Window')

###############################################################################
# Function: Unlock_Dialog_popup
# Description: Interacts with the "Unlock" dialog popup and clicks a specified button.
# Parameter: button_name (str) - The name of the button to be clicked.
# Example: Unlock_Dialog_popup("Yes")
###############################################################################
def Unlock_Dialog_popup(button_name):
    obj = Sys.Process("ControlExpert", 4).Dialog("Unlock")
    buttons_list = obj.FindAllChildren('WndClass', 'Button', 1000)
    for button in buttons_list:
        if button_name in str(button.WndCaption):
            button.click()
            Log.Message('Clicked ' + str(button.WndCaption) + ' button.')
            break
    else:
        Log.Warning("Button name mentioned doesnt exists")

###############################################################################
# Function: Delete_link_Refine_Offline
# Description: Deletes a link in the Refine Offline window based on its identifier.
# Parameter: identifier (str) - The text identifier of the link to be deleted.
# Example: Delete_link_Refine_Offline("LinkName")
###############################################################################
def Delete_link_Refine_Offline(identifier):
    Window = refoff_obj.mdiwindowtextbox.object
    Window_lst = Window.FindAllChildren("Name", "TextObject*", 1000)
    if not Window_lst:
        Log.Warning("No links found in the Refine Offline window.")
        return
    for obj in Window_lst:
        if identifier in obj.Text:
            Window.Click(obj.Left+50+obj.Width, obj.Top+40+(obj.Height/2))
            Delay(1000)
            #Sys.Keys("[Del]")

###############################################################################
# Function: Consistency_Check_Select_All
# Description: Selects all items in the consistency check popup by interacting with the "Check/Uncheck All" checkbox.
# Parameter: None
###############################################################################
def Consistency_Check_Select_All():
    headers = msg_obj.exportpopupbutton.object.FindAllChildren('ClrClassName', 'GridViewHeaderCell', 25)
    if not headers:
        Log.Warning("No headers found in the consistency check popup.")
        return
    buttons_list = headers[0].FindAllChildren('ClrClassName', 'CheckBox', 1000)
    if not buttons_list:
        Log.Warning("No checkboxes found in the consistency check popup.")
        return
    for button in buttons_list:
        if "Check/Uncheck All" == button.ToolTip.Content.OleValue:
            button.IsChecked = True
            Log.Message('Select all button is Checked')       
            break
        else:
            Log.Message(str(button.WPFControlText) + " button is Enabled")

###############################################################################
# Function: Verify_modifications_available_in_Refine_Offline
# Description: Verifies if a specific block is available in the Refine Offline window.
# Parameter: identifier (str) - The text identifier of the block to be verified.
# Example: Verify_modifications_available_in_Refine_Offline("BlockName")
###############################################################################
def Verify_modifications_available_in_Refine_Offline(identifier):        
    Window = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Warning("No blocks found in the Refine Offline window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text:
            Log.Checkpoint(Window_Text.Text + " block is available")
            break
    else: 
        Log.Warning(identifier + " block is not available")

###############################################################################
# Function: RClick_on_filter_Refine_Offline
# Description: Right-clicks on the filter button in the Refine Offline window.
# Parameter: None
###############################################################################
def RClick_on_filter_Refine_Offline(): 
    Button = refoff_obj.mdiwindowtextbox.object.FindChild("ClassName", "CDFIButton", 1000)
    Button.ClickR()

###############################################################################
# Function: Select_Column_Configuration
# Description: Selects a specific column configuration in a dialog window based on its identifier.
# Parameter: identifier (str) - The text identifier of the column to be selected.
# Example: Select_Column_Configuration("ColumnName")
###############################################################################
def Select_Column_Configuration(identifier):
    Window = refoff_obj.parentdialogwindowce.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Warning("No columns found in the dialog window.")
        return
    for obj in Window:
        if identifier in obj.Text:
            Window.Click(obj.Left-50+obj.Width, obj.Top+40+(obj.Height/2))
            Log.Message(obj.Text + " is selected")

###############################################################################
# Function: Add_variable_name_in_name_column
# Description: Adds a variable name in the "Name" column of a grid.
# Parameter: var_name (str) - The variable name to be added.
# Example: Add_variable_name_in_name_column("Variable1")
###############################################################################
def Add_variable_name_in_name_column(var_name):
    Delay(3000)
    for i in range(10):
        Sys.Keys("[Down]")
    Sys.Keys("[Enter]")
    Sys.Keys(var_name)
    Sys.Keys("[Enter]")

###############################################################################
# Function: click_on_elipsis
# Description: Simulates a click on the ellipsis button in the UI.
# Parameter: None
###############################################################################
def click_on_elipsis():
    Sys.Keys("[Right]")
    Sys.Keys("[Enter]")

###############################################################################
# Function: select_variable_type_Dialog_popup_CE
# Description: Selects a variable type in a dialog popup and confirms the selection.
# Parameter: None
###############################################################################
def select_variable_type_Dialog_popup_CE():
    Delay(3000,"Wait")
    Click_button_Dialog_popup_CE("REF_TO")
    Click_button_Dialog_popup_CE("OK")

###############################################################################
# Function: Click_button_Dialog_popup_CE
# Description: Clicks a specified button in a dialog popup.
# Parameter: button_name (str) - The name of the button to be clicked.
# Example: Click_button_Dialog_popup_CE("OK")
###############################################################################
def Click_button_Dialog_popup_CE(button_name):
    obj = Sys.Process("ControlExpert", 4).Dialog("*")
    buttons_list = obj.FindAllChildren('WndClass', 'Button', 1000)
    for button in buttons_list:
        if button_name in str(button.WndCaption):
            button.Click()
            Log.Message('Clicked ' + str(button.WndCaption) + ' button.')
            break
    else:
        Log.Warning("Button name mentioned doesnt exists")

###############################################################################
# Function: select_variable_type
# Description: Selects a variable type from a dropdown menu.
# Parameter: val (str) - The variable type to be selected.
# Example: select_variable_type("Int")
###############################################################################
def select_variable_type(val):
    Sys.Keys("[Right]")
    Sys.Keys("[Enter]")
    Sys.Keys(val)
    Sys.Keys("[Enter]") 

###############################################################################
# Function: select_Constant_check_box
# Description: Selects the "Constant" checkbox in the UI.
# Parameter: None
###############################################################################
def select_Constant_check_box():
    Delay(3000)
    for i in range(10):
        Sys.Keys("[Right]")
        Delay(500)
    Delay(1000)
    Sys.Keys("[Enter]")

###############################################################################
# Function: Enter_P2P_in_Custom_box
# Description: Enters "P2P" in a custom input box.
# Parameter: None
###############################################################################
def Enter_P2P_in_Custom_box():
    Delay(3000)
    Sys.Keys("[Right]")
    Sys.Keys("[Enter]")
    Sys.Keys("P2P")
    Sys.Keys("[Enter]")  

###############################################################################
# Function: select_AdvSettings_properties_SVP
# Description: Selects advanced settings properties in the supervision project or AVEVA.
# Parameter: param (str) - A string in the format "parent$$val$$val1".
# Example: select_AdvSettings_properties_SVP("supervision project$$MainFolder$$SubFolder")
###############################################################################
def select_AdvSettings_properties_SVP(param):
    parent,val,val1 = param.split('$$')

    if parent.lower() == "supervision project":
        project_browser = refoff_obj.projectbrowserrotextbox.object
    elif parent.lower() == "aveva":
        project_browser = aveva_obj.systreeviewtextbox.object
    else:
        Log.Warning("Invalid parent passed") 

    project_browser.wItems.Item[0].Select()
    count = project_browser.wItemCount 
    Log.Message(str(count) + ' PB count')
    for i in range(count):
        if val in project_browser.wItem[i]:
            project_browser.SelectItem(val)
            Log.Message(val + " is selected")
            Applicationutility.wait_in_seconds(1500, 'wait')
            count1 = project_browser.wItems.Item[0].Items.Item[i].Items.Count
            for j in range(count1):
                if val1 in project_browser.wItems.Item[0].Items.Item[i].Items.Item[j].Text:
                    project_browser.wItems.Item[0].Items.Item[i].Items.Item[j].Select()
                    Log.Message(val1 + " is selected")
                    break
            break  

###############################################################################
# Function: Edit_Parameter_Value_AdvSettings_SVP
# Description: Edits the parameter value in advanced settings.
# Parameter: val (str) - The value to be entered.
# Example: Edit_Parameter_Value_AdvSettings_SVP("NewValue")
###############################################################################
def Edit_Parameter_Value_AdvSettings_SVP(val): 
    obj_Parent = Sys.Process("EngineeringClient")
    obj_value = obj_Parent.Find("Name","Window('Static', 'Value:', *)",100)
    Top = obj_value.Top
    value_field = obj_Parent.FindAllChildren("Name","Window('Edit', '', *)",100)
    for value in value_field:
        Sys.HighlightObject(value,1)
        if value.Top <= obj_value.Top+10 and value.Top >= obj_value.Top-10:
            value.wText = val
            Log.Message(val + " is entered")
            break

###############################################################################
# Function: Verify_Parameter_Value_AdvSettings_SVP
# Description: Verifies the parameter value in advanced settings.
# Parameter: param (str) - A string in the format "parent$$val".
# Example: Verify_Parameter_Value_AdvSettings_SVP("supervision project$$ExpectedValue")
###############################################################################
def Verify_Parameter_Value_AdvSettings_SVP(param): 
    parent,val = param.split('$$')

    if parent.lower() == "supervision project":
        obj_Parent = Sys.Process("EngineeringClient")
    elif parent.lower() == "aveva":
        obj_Parent = aveva_obj.mainparenttextbox.object
    else:
        Log.Warning("Invalid parent passed") 

    obj_value = obj_Parent.Find("Name","Window('Static', 'Value:', *)",100)
    Top = obj_value.Top
    value_field = obj_Parent.FindAllChildren("Name","Window('Edit', '', *)",100)
    for value in value_field:
        Sys.HighlightObject(value,1)
        if value.Top <= obj_value.Top+10 and value.Top >= obj_value.Top-10:
            if str(value.wText) == str(val):
                Log.Checkpoint(value.wText + " is updated") 
                break
            else:
                Log.Warning(val + " updated value is incorrect")

###############################################################################
# Function: drag_instance_drop_container_page_SP
# Description: Drags an instance and drops it onto the container page.
# Parameter: template (str) - The name of the template to be dragged.
# Example: drag_instance_drop_container_page_SP("TemplateName")
###############################################################################
def drag_instance_drop_container_page_SP(template):
    template_list = proj_obj.containerpagedocktextbox.object.FindAllChildren('ClrClassName', 'TreeListViewRow', 1000)
    if not template_list:
        Log.Warning("No templates found in the container page.")
        return
    Workspace_editor = proj_obj.mdiclientwindowtextbox.object
    tox = Workspace_editor.ScreenLeft+10
    for i in range(len(template_list)):
        if template_list[i].Visible: 
            if template == str(template_list[i].DataContext.Identifier.OleValue):
                fromx = template_list[i].Width/2
                fromy = template_list[i].Height/2
                Log.Message('The object selected to drag is : ' + str(template_list[i].DataContext.Identifier.OleValue))
                Applicationutility.wait_in_seconds(2000, 'Wait')
                template_list[i].Click()
                Applicationutility.wait_in_seconds(2000, 'Wait')
                template_list[i].Drag(fromx-70, fromy, tox+100, 0)
                Applicationutility.wait_in_seconds(2000, 'Wait')
                break

###############################################################################
# Function: select_value_listview_SVP
# Description: Selects a value from a list view in the supervision project.
# Parameter: val (str) - The value to be selected.
# Example: select_value_listview_SVP("ValueName")
###############################################################################
def select_value_listview_SVP(val):
    list_items = proj_obj.listviewtextbox.object.FindAllChildren('ClrClassName', 'ListViewItem', 100)  
    if not list_items:
        Log.Warning("No items found in the list view.")
        return
    for list in list_items:
        if val in list.DataContext.Identifier.OleValue:
            Applicationutility.wait_in_seconds(1000, 'Wait')
            list.Click()
            Applicationutility.wait_in_seconds(2000, 'Wait')
            break

###############################################################################
# Function: Double_click_on_header_OC
# Description: Double-clicks on a specific header in the Operation Client.
# Parameter: None
###############################################################################
def Double_click_on_header_OC():
    identifier = "Process Expert"
    parent = Sys.Process("OperationClient").WPFObject("HwndSource: Main")
    object = parent.FindAllChildren("ClrClassName", "TextBlock", 1000)
    for obj in object:
        if identifier in obj.WPFControlText:      
            obj.DblClick() 
            Delay(2000)
            Log.Message("Double clicked")

###############################################################################
# Function: Verify_screen_visible
# Description: Verifies if a specific screen is visible in the Operation Client.
# Parameter: None
###############################################################################
def Verify_screen_visible():
    obj2 = Sys.Process("OperationClient").WPFObject("HwndSource: Main")
    if obj2.VisibleOnScreen:
        Log.Message("Visible On Screen")
    else:
        Log.Message("Not Visible On Screen")  

###############################################################################
# Function: Verify_variable_is_removed_Refine_Offline
# Description: Verifies if a specific variable is removed in the Refine Offline window.
# Parameter: var_name (str) - The name of the variable to be verified.
# Example: Verify_variable_is_removed_Refine_Offline("Variable1")
###############################################################################
def Verify_variable_is_removed_Refine_Offline(var_name):
    var_name = "V1" 
    variables = refoff_obj.mdiwindowtextbox.object.FindAllChildren("Name", "TextObject*", 100)
    if not variables:
        Log.Warning("No variables found in the Refine Offline window.")
        return
    for var in variables:
        if var.Text == var_name:
            Log.Warning(var.Text + " is not removed")
            break
    else:
        Log.Checkpoint(var_name + " is removed")

###############################################################################
# Function: edit_IP_Address
# Description: Edits the IP address of a specific object in the Refine Offline window.
# Parameter: param (str) - A string in the format "Identifier$$value".
# Example: edit_IP_Address("Device1$$192.168.1.1")
###############################################################################
def edit_IP_Address(param):
    Identifier, value = param.split('$$')
    obj = refoff_obj.mdiwindowtextbox.object.FindAllChildren("ObjectType","IpAddress",100)
    if not obj:
        Log.Warning("No IP address objects found.")
        return
    for IP_obj in obj:
        if str(IP_obj.ObjectIdentifier) == Identifier:
            IP_obj.wAddress = value
            Log.Checkpoint(Identifier + " is updated as " + IP_obj.wAddress)
            break
    else: 
        Log.Warning(Identifier + " is not updated - IP : " + IP_obj.wAddress)

###############################################################################
# Function: Verify_Mapped_DTM_device_present_CE
# Description: Verifies if a specific DTM device is present in the Control Expert topology explorer.
# Parameter: Identifier (str) - The identifier of the DTM device.
# Example: Verify_Mapped_DTM_device_present_CE("Device1")
###############################################################################
def Verify_Mapped_DTM_device_present_CE(Identifier):
    objects = topoexo_obj.dtmbrowserprop.object.FindAllChildren("ObjectType","OutlineItem",200)
    if not objects:
        Log.Warning("No DTM devices found in the topology explorer.")
        return
    for obj in objects:
        if Identifier in str(obj.ObjectIdentifier):
            Log.Checkpoint(str(obj.ObjectIdentifier) + " DTM device added")
            break
    else:
        Log.Warning(Identifier + " DTM device not added")

###############################################################################
# Function: Dblclick_dialog_panel_item_CE
# Description: Double-clicks a specific item in the dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be double-clicked.
# Example: Dblclick_dialog_panel_item_CE("ItemName")
###############################################################################
def Dblclick_dialog_panel_item_CE(param):
    panel_child = diace_obj.dialogpanelcetextbox.object.FindAllChildren('Text', '*', 100)
    if not panel_child:
        Log.Warning("No items found in the dialog panel.")
        return
    for item in panel_child:
        if param == item.Text:
            item.DblClick()
            Log.Checkpoint(item.Text + ' is Double Clicked.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else:
        Log.Warning(param + ' not found.')    

###############################################################################
# Function: Click_dialog_panel_item_CE
# Description: Clicks a specific item in the dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be clicked.
# Example: Click_dialog_panel_item_CE("ItemName")
###############################################################################
def Click_dialog_panel_item_CE(param):
    Applicationutility.wait_in_seconds(1000, 'Wait')
    panel_child = diace_obj.dialogpanelcetextbox.object.FindAllChildren('Text', '*', 100)
    if not panel_child:
        Log.Warning("No items found in the dialog panel.")
        return
    for item in panel_child:
        if param == item.Text:
            item.Click()
            Log.Checkpoint(item.Text + ' is Selected.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else:
        Log.Warning(param + ' not found.')  

###############################################################################
# Function: Select_bottom_listitem_dialog_panel_item_CE
# Description: Selects a specific item from the bottom list in the dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be selected.
# Example: Select_bottom_listitem_dialog_panel_item_CE("ItemName")
###############################################################################
def Select_bottom_listitem_dialog_panel_item_CE(param):
    io_device = diace_obj.dialoglistboxcetextbox.object 
    if io_device.wItemCount == 0:
        Log.Warning("No items found in the bottom list.")
        return
    for i in range(io_device.wItemCount):
        if param in io_device.wItem[i]:
            io_device.ClickItem(i)
            Log.Message(io_device.wItem[i] + ' is Selected.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else: 
        Log.Message(param + ' not found.')

###############################################################################
# Function: Rclick_Drops_EIO_add_new_device_CE
# Description: Right-clicks on the EIO drops section and adds a new device in Control Expert.
# Parameter: None
###############################################################################
def Rclick_Drops_EIO_add_new_device_CE():
    obj = refoff_obj.fbdsectionwindowtextbox.object
    obj.ClickR((obj.Width*.04), (obj.Height*.15))
    ce_obj.newdevicecetextbox.click()

###############################################################################
# Function: Select_bottom_listitem_EIO_dialog_panel_item_CE
# Description: Selects a specific item from the bottom list in the EIO dialog panel of Control Expert.
# Parameter: param (str) - The name of the item to be selected.
# Example: Select_bottom_listitem_EIO_dialog_panel_item_CE("ItemName")
###############################################################################
def Select_bottom_listitem_EIO_dialog_panel_item_CE(param):
    io_device = diace_obj.dialoglistboxce1textbox.object.FindAllChildren('Text', '*')
    if not io_device:
        Log.Warning("No items found in the EIO dialog panel.")
        return
    for item in io_device:
        if param in item.Text:
            item.Click()
            Log.Message(item.Text + ' is Selected.')
            Applicationutility.wait_in_seconds(1000, 'Wait')
            break
    else: 
        Log.Message(param + ' not found.')

###############################################################################
# Function: select_PLC_bus_combobox_item_CE
# Description: Selects a specific item from the PLC bus combobox in Control Expert.
# Parameter: param (str) - The name of the item to be selected.
# Example: select_PLC_bus_combobox_item_CE("BusName")
###############################################################################
def select_PLC_bus_combobox_item_CE(param):
    obj = refoff_obj.windowcomboboxtextbox.object
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

###############################################################################
# Function: create_logical_network
# Description: Creates a logical network by interacting with the controller properties in the topology explorer.
# Parameter: None
###############################################################################
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

###############################################################################
# Function: Click_tab_item_EIO_config_window
# Description: Clicks on a specific tab item in the EIO configuration window.
# Parameter: identifier (str) - The name of the tab to be clicked.
# Example: Click_tab_item_EIO_config_window("TabName")
###############################################################################
def Click_tab_item_EIO_config_window(identifier):
    Window = proj_obj.mdiclientwindowtextbox.object.FindAllChildren("Name", "TextObject*", 1000)
    if not Window:
        Log.Warning("No tab items found in the EIO configuration window.")
        return
    for Window_Text in Window:
        if identifier in Window_Text.Text:
            Window_Text.Click()
            Log.Checkpoint(Window_Text.Text + " is Clicked")
            break
    else: 
        Log.Warning(identifier + " is not available")

###############################################################################
# Function: Add_Vairable_Logic_Block_link_P2P
# Description: Adds a variable to a logic block link in the P2P configuration.
# Parameter: param (str) - A string in the format "identifier$$variable".
# Example: Add_Vairable_Logic_Block_link_P2P("BlockName$$VariableName")
###############################################################################
def Add_Vairable_Logic_Block_link_P2P(param):
    identifier , variable = param.split("$$")
    Window = proj_obj.mdiclientwindowtextbox.object
    Window_lst = Window.FindAllChildren("Name", "TextObject*", 1000)
    if not Window_lst:
        Log.Warning("No logic blocks found in the P2P configuration.")
        return
    for obj in Window_lst:
        if identifier in obj.Text and obj.Visible:
            obj.DblClick()
            Sys.Keys(variable)
            Sys.Keys("[Enter]")
            Log.Checkpoint(obj.Text + " is Double Clicked")
            break
    else:
        Log.Warning(identifier + " is not available")

###############################################################################
# Function: change_Port_Number_PLC_Simulator
# Description: Changes the port number in the PLC simulator.
# Parameter: None
###############################################################################
def change_Port_Number_PLC_Simulator():
    Simulator_Textbox = diace_obj.simulatorporttextbox.object
    Simulator_Textbox.SetText("503")

###############################################################################
# Function: click_MenuItem_Toolbar_CE
# Description: Clicks a specific menu item in the toolbar of Control Expert.
# Parameter: menu_option (str) - The name of the menu option to be clicked.
# Example: click_MenuItem_Toolbar_CE("OptionName")
###############################################################################
def click_MenuItem_Toolbar_CE(menu_option):
    menu_items = ce_obj.modaldialogewindowoptionsce.object.FindAllChildren('ObjectType', 'MenuItem', 1000)
    for item in menu_items:
        if menu_option in str(item.ObjectIdentifier):
            item.click()
            break

###############################################################################
# Function: Select_network_CE
# Description: Selects a specific network in the Control Expert network configuration.
# Parameter: menu_option (str) - The name of the network to be selected.
# Example: Select_network_CE("NetworkName")
###############################################################################
def Select_network_CE(menu_option):
    menu_items = ce_obj.okmodaldialoguewindowce.object.FindChild('wText', 'No Selection', 10)
    menu_items.ClickItem(menu_option)
    Log.Message(menu_items.wText + " is selected")

###############################################################################
# Function: Click_ok_button_add_network_popup_CE
# Description: Clicks the "OK" button in the add network popup of Control Expert.
# Parameter: button (str) - The name of the button to be clicked.
# Example: Click_ok_button_add_network_popup_CE("OK")
###############################################################################
def Click_ok_button_add_network_popup_CE(button):
    menu_items = ce_obj.okmodaldialoguewindowce.object.FindChild(('WndClass', 'WndCaption'),('Button',button), 10)
    menu_items.Click()
    Log.Message("Ok is Clicked")

###############################################################################
# Function: select_item_mdi_window_CE
# Description: Selects a specific item in the MDI window of Control Expert.
# Parameter: identifier (str) - The name of the item to be selected.
# Example: select_item_mdi_window_CE("ItemName")
###############################################################################
def select_item_mdi_window_CE(identifier):        
    menu_items = refoff_obj.mdiwindowtextbox.object.FindAllChildren('WndClass', 'ComboBox',20)
    for item in menu_items:
        if identifier in str(item.wItemList): 
            item.ClickItem(identifier)
            Log.Message(item.wText + " is selected")
            break
    else:
        Log.Message(identifier + " is not selected")

        


