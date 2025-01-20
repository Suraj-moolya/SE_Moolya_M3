
"""UIElement"""


###################################################################
 #   UIElement file := This Class  Consist's of all The Deafult actions,
 #       here all the Deafult TestComplete methods and properties 
 #       are Overwritten by considering OOP'S Principles.
###################################################################

class UIElement:
    """UIElement Class"""
    def __init__(self, element):
        self.element = element
        
    @property  
    def object(self):
      return self.element
      
###################################################################
 #  verifyradiobutton :-- This  method is used to verify control
 #                      is selected or not  (return's boolean)              

###################################################################
    @property
    def verifyradiobutton(self):
        """verifyradiobutton"""
        return self.element.IsSelected
        
###################################################################
 #check_for_caption :--This  method is used to get the Caption 
 #                     of the control (return's String)              

###################################################################      

    @property
    def check_for_caption(self):
        """check_for_caption"""
        return self.element.Caption
###################################################################
 #   bounds :-- This  method is used to get info of text portion
 #sub methods (left|top|width|height) (return's float and int)              

###################################################################

    @property
    def bounds(self):
        """bounds"""
        return self.element.Bounds
               
###################################################################
 #  selected_index :-This  method is used to get selected child  
 #                  index of the editable control(return's int)
###################################################################

    @property
    def selected_index(self):
        """selected_index"""
        return self.element.wSelectedIndex
        
        
#############################################################
 #selected_text :-This  method is used to get win selected text   
 #                 of the editable control(return's string)
#############################################################

    @property
    def selected_text(self):
        """selected_text"""
        return self.element.wSelectedText
        
###################################################################
 #selected_item_text :-this function return's string  text of 
 #                      selected  tree view items
###################################################################
      
    @property
    def selected_item_text(self):
        """selected_item_text"""
        return self.element.getSelectedItem().toString()
        
#############################################################
 #selected_item_index:- this function is Specific to the
 # (MSAA Combobox objects ) used to get the index of selected 
 #                                               - comboxitem                      
#############################################################
    @property
    def selected_item_index(self):
        """selected_item_index"""
        return self.element.getSelectedIndex()
 
###################################################################
#list_items:- this function return's list of string holding 
#             all the item Captions of the separated list controls  
#            as Combobox listbox etc-                      
###################################################################       
    @property
    def list_items(self):
        """list_items"""
        return self.element.wItemList.split(self.element.wListSeparator)
        
               
###################################################################
#items:- this function return's a treeviewitemcollection
# treeviewitemcollection (obj containing data of all the tree 
#                           view items)               
###################################################################       

    @property
    def items(self):
        """items"""
        return self.element.wItems
###################################################################
#item_at:- this function return's a index of item in 
# treeviewitemcollection (obj containing data of all the tree 
#                           view items)               
###################################################################       

    def item_at(self, index):
        """item_at"""
        return self.element.items.Item[index]
        
           
###################################################################
#item_count:- this function return's total number of direct child
#             items for the current test item.        
###################################################################      

    @property
    def item_count(self):
        """item_at"""
        return self.element.wItemCount
        
###################################################################
#get_tab_name:- this function return's the caption of the tab item  
#                by passing index of the tab item as an argument
###################################################################     
        
        
    def get_tab_name(self, tab_index):
        """get_tab_name"""
        return self.element.wTabCaption[tab_index]
        
###################################################################
#tab_count:- this function return's total number of pages 
#             in the  Tab Control    
###################################################################

    @property
    def tab_count(self):
        """tab_count"""
        return self.element.wTabCount
        
       
###################################################################
#accessible_text:- this function return's string  or variable
#    Holding the accessible class name (belongs to java applications)      
###################################################################        
    @property
    def accessible_text(self):
        """accessible_text"""
        return self.element.AWTComponentAccessibleName
        
###################################################################
#text:- this function return's text of the any control displayed  
#       in  the console(app)       
###################################################################


    @property
    def text(self):
        """text"""
        if self.verify_property("WPFControlText"):
            text = self.element.WPFControlText
            Log.Message(str(text))
        elif self.verify_property("wText"):
            text = self.element.wText
        elif self.verify_property("Value"):
            text = self.element.Value
        elif self.verify_property("Text"):
            text = self.element.Text
            Log.Message('text')
        return text
###################################################################
#wselection:-this function return's text selected in the edit control
#            if no text selected then it return's empty string    
###################################################################

    @property
    def wselection(self):
        """Wselection"""
        return self.element.wSelection
        
###################################################################
#wvalue:- this function return's the Current Value Displayed in 
#         Control .(instance-value)      
###################################################################

    @property
    def wvalue(self):
        """wvalue"""
        return self.element.wValue
        
###################################################################
#value:- this function return's value of the array item
#         value may be(string,int,object ,referance array)      
###################################################################

    @property
    def value(self):
        """value"""
        return self.element.Value
        
        
###################################################################
#position:- this function is used to get or set the Value that is 
#           Currently Displayed Up down, and The value is with in 
#           wMax and wMin(Bounds)        
###################################################################

    @property
    def position(self):
        """position"""
        return self.element.wPosition
        
        
        
###################################################################
#wMax:- this function return's Maximum value in which UpDown
#               Control can take on      
###################################################################

    @property
    def max(self):
        """max"""
        return self.element.wMax
        
        
###################################################################
#wMin:- this function return's Minimum value in which UpDown
#      Control can take on        
###################################################################

    @property
    def min(self):
        """min"""
        return self.element.wMin
        
        
###################################################################
#enabled :- this function used to check wheather object|Component is 
#          responding for mouse and keyboard events.return's Boolean        
###################################################################

    @property
    def enabled(self):
        """enabled"""
        return self.element.Enabled
        
        
###################################################################
#expanded:- this function return's Boolean When Group is Expanded 
#          return's true or When the Group is Collapsed retrun's false        
###################################################################

    @property
    def expanded(self):
        """expanded"""
        return self.element.Expanded
        
        
###################################################################
#refreshmappinginfo:- this function used to clears cached or mapped 
#  object reference in TestComplete and searches for object again
###################################################################       
        
    @property
    def refreshmappinginfo(self):
        """expanded"""
        return self.element.RefreshMappingInfo()
        
        
###################################################################
#exists:- this function used to check wheather the given object is
#         Exist in the System.  return's Boolean       
###################################################################

    @property
    def exists(self):
        """exists"""
        return self.element.Exists
        
        
###################################################################
#wstatechecked:- this function return's the Current state of the
#                control (if checkbox is checked return's "True or 1"
#                elif  checkbox is unchecked return's "False or 0")    
###################################################################

    @property
    def wstatechecked(self):
        """wstatechecked"""
        return self.element.wState == 1
        
        
###################################################################
#checked:- this function used to check the state of tcxCheckbox returns
#          true if currently checkbox checked False if  checkbox
#          unchecked       
###################################################################

    @property
    def checked(self):
        """checked"""
        return self.element.Checked
        
        
###################################################################
#verifychecked:- this function used to verify whether checkbox is
#               checked or not  
                 
###################################################################
    @property
    def verifychecked(self):
        """verifychecked"""
        checked=self.element.Checked
        if checked==True:
          Log.Checkpoint("checkbox is checked")
        else:
          Log.Error("checkbox is unchecked")
        
        
        
###################################################################
#selected:- this function used to check whether the listbox item 
#       is Selected or unselected (True if specified item is Selected 
#                             False if specified item is UnSelected)
###################################################################

    @property
    def selected(self):
        """selected"""
        return aqObject.GetPropertyValue(self.element, "wChecked")
        
  
###################################################################
#data_context:- is a concept that allows to elements to inherit
#               Information from parent elements   
###################################################################       
        
        
  
    def data_context(self):
        """data context"""
        data = DataContext.CurrentPatientPosition.OleValue
        return data
        
        
###################################################################
#visible:- this function used to Specifies whether the component or obj  
#           appears on screen at run time   (returns Boolean)     
###################################################################

    @property
    def visible(self):
        """visible"""
        return self.element.Visible
        
        
###################################################################
#visible_on_screen:- this function return's Boolean.return's True if
#            whole object or any of its parts are visible,else False.
###################################################################

    @property
    def visible_on_screen(self):
        """visible_on_screen"""
        return self.element.VisibleOnScreen
        
###################################################################
#multiple_click:- this function will parmeter where click count is 
#required, according to that count, those many click action will be
#performed
###################################################################

    def multiple_click(self, param1):
        """mulitiple_click"""
        if "," in param1:
            param = param.split(",")
            param1= param[0]
            delay= param[1]
            for _ in range(int(param1)):
                self.element.Click()
        else:
            userinput = int(param1)
            for _ in range(userinput):
                self.element.Click()
            
###################################################################
#height :- this function return's integer value that specifies
#          height of the object or control        
###################################################################

    @property
    def height(self):
        """height"""
        return self.element.Height
        
###################################################################
#width:- this function return's desktop width i,e Horizontal screen
#        Resoulution in pixels       
###################################################################

    @property
    def width(self):
        """width"""
        return self.element.Width
        
      
###################################################################
#handle:- this function return's integer Object's Window handel(HWND)
#  used to find window or control is an active window with resp to time     
###################################################################
    @property
    def handle(self):
        """handle"""
        return self.element.Handle       
        
###################################################################
#screenleft:- this function return's horizontal position of the
#             left side of the onscreenobj by co-ordinates     
###################################################################

    @property
    def screenleft(self):
        """screenleft"""
        return self.element.ScreenLeft
        
        
###################################################################
#ole_value:- this function return's decimal|Object|data enumarator
#             string etc...
###################################################################       
        
    @property
    def ole_value(self):
        """screenleft"""
        return self.element.OleValue
        
        
        
###################################################################
#currentpatientposition:- this function return's Patients pos
###################################################################      
            
    @property
    def currentpatientposition(self):
        """screenleft"""
        return self.element.CurrentPatientPosition


        
###################################################################
#orientationlabel:- this .net property retruns OrientationLabel of
#           patient
###################################################################      
        
    @property
    def orientationlabel(self):
        """orientationlabel"""
        return self.element.OrientationLabel   
        
        
        
        
        
        
###################################################################
#screentop:- this function return's vertical position of the top of 
#            the  Onscreenobject      
###################################################################

    @property
    def screentop(self):
        """screentop"""
        return self.element.ScreenTop
        
###################################################################
#left:- this function return's horizantal co -ordinates of component's
#       left edge relative to its Parent component     
###################################################################

    @property
    def left(self):
        """left"""
        return self.element.Left
###################################################################
#top:- this function return's total number of direct child
#               items for the current test item.        
###################################################################

    @property
    def top(self):
        """top"""
        return self.element.Top
        
        
###################################################################
#child_count:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    @property
    def child_count(self):
        """child_count"""
        return self.element.ChildCount
        
###################################################################
#row_count:- this function return's total number of direct Row 's for 
#            the  specificed element  
###################################################################

    @property
    def row_count(self):
        """row_count"""
        return self.element.wRowCount
        
        
###################################################################
#column_count:- this function return's total number of direct Coloumn's
#             count for the current test item.        
###################################################################

    @property
    def column_count(self):
        """column_count"""
        return self.element.wColumnCount
        
        
###################################################################
#column_name:- this function return's name of the coloumn by coloumn
#               index .        
###################################################################

    def column_name(self, column_index):
        """column_name"""
        column_name = self.element.getColumnName(column_index).OleValue
        return column_name
        
        
###################################################################
#get_row_index:- this function return's row index by coloumn index and 
#              value of row .      
###################################################################

    def get_row_index(self, column_index, value):
        """get_row_index"""
        return self.element.FindRow(column_index, value)
        
###################################################################
#selected_row_index:- this function return's selected item row index      
###################################################################
    @property
    def selected_row_index(self):
        """selected_row_index"""
        return self.element.getSelectedRow()
        
        
###################################################################
#parent:- this function return's direct parent of the item.        
###################################################################

    @property
    def parent(self):
        """parent"""
        return UIElement(self.element.Parent)
        
        
###################################################################
#check_colour_b:- this function return's background colour 
#             items for the current test item.        
###################################################################

    @property
    def check_colour_b(self):
        """check_colour_b"""
        return self.element.Background.Color.B
###################################################################
#check_colour_r:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    @property
    def check_colour_r(self):
        """check_colour_r"""
        return self.element.Background.Color.R
        
        
###################################################################
#check_colour_g:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    @property
    def check_colour_g(self):
        """check_colour_g"""
        return self.element.Background.Color.G



      
###################################################################
#watermarkhelper_watermarkcontent:- this function return's watermark
#             content presented in applicarion        
###################################################################


    @property
    def watermarkhelper_watermarkcontent(self):
        """watermarkhelper_watermarkcontent"""
        return self.element.WatermarkHelper_WatermarkConten     
        
###################################################################
#child:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def child(self, index):
        """child"""
        child_element = self.element.Child(index)
        return UIElement(child_element)
###################################################################
#find:- this function return's  propertie's and values of item under 
#             test      
###################################################################
    def find(self, prop_names, prop_values):
        """find"""
        return UIElement(self.element.Find(prop_names, prop_values, 20))
###################################################################
#find_ex:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def find_ex(self, prop_names, prop_values):
        """find_ex"""
        return UIElement(self.element.FindEx(prop_names, prop_values, 20, True, 60))
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def find_child(self, prop_names, prop_values):
        """find_child"""
        return UIElement(self.element.FindChild(prop_names, prop_values, 20))
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def find_child_ex(self, prop_names, prop_values):
        """find_child_ex"""
        return UIElement(self.element.FindChildEx(prop_names, prop_values, 20, True, 60))
###################################################################
#click:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click(self):
        """click"""
        self.element.Click()
###################################################################
#]click_at:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_at(self, tox, toy):
        """click_at"""
        self.element.Click(tox, toy)
###################################################################
#click_button:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_button(self):
        """click_button"""
        self.element.ClickButton()

###################################################################
#double_click:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def double_click(self):
        """double_click"""
        self.element.DblClick()
###################################################################
#right_click:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def right_click(self):
        """right_click"""
        self.element.ClickR()

###################################################################
#right_click_item:- this function used to
#            right click on items for the current test item.        
###################################################################
    def right_click_item(self, item):
        """right_click_item"""
        self.element.ClickItemR(item)
###################################################################
#hover:- this function hover's mouse pointer on specified element       
###################################################################
    def hover(self):
        """hover"""
        self.element.HoverMouse()
###################################################################
#check:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def check(self):
        """check"""
        self.element.ClickButton(True)
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def uncheck(self):
        """uncheck"""
        self.element.ClickButton(False)
###################################################################
#click_button:- this function helps to click on Button        
###################################################################
    def click_button(self):
        """select"""
        self.click_button()
###################################################################
#select_item:- this function helps to click on items        
###################################################################

    def select_item(self, item):
        """select_item"""
        self.element.ClickItem(item)
###################################################################
#listboxitem:- this function used to enter keys 
#                
###################################################################       

    def listboxitem(self, text):
        """listboxitem"""
        self.element.Keys(text)
        
###################################################################
#enter_password:- this function used enter password for passwordtext
#            propertytextbox        
###################################################################
    def enter_password(self, password):
        """enter_password"""
        self.element.set_PasswordText(password)
###################################################################
#refresh:- this function helps to refresh ObjecrBrowser.        
###################################################################

    def refresh(self):
        """refresh"""
        self.element.Refresh()
        
###################################################################
#click_cell:- this function helps to click the cell by row and coloumn 
#                   number.        
###################################################################

    def click_cell(self, row: int, column: int):
        """click_cell"""
        self.element.ClickCell(row, column)
        
        
###################################################################
#expand_tree_item:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def expand_tree_item(self, item_name):
        """expand_tree_item"""
        self.element.ExpandItem(item_name)
        
###################################################################
#collapse_tree_item:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def collapse_tree_item(self, item_name):
        """collapse_tree_item"""
        self.element.CollapseItem(item_name)
###################################################################
#click_tab:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_tab(self, tab_name_or_index):
        """click_tab"""
        self.element.ClickTab(tab_name_or_index)
###################################################################
#click_item:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_item(self, item_name):
        """click_item"""
        self.element.ClickItem(item_name)
        
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def click_column_header(self, column_index: int):
        """click_column_header"""
        self.element.ClickColumnHeader(column_index)
        
        
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def popupselection(self, index):
        """popupselection"""
        self.element.PopupMenu.Click(index)
        
###################################################################
#drag:- this function drags the 
#             items for the current test item.        
###################################################################

    def drag(self, clientx,clienty,tox,toy):
        """drag"""
        return self.element.Drag(clientx,clienty,tox,toy)
        
###################################################################
#enterkey:- this function return's the keyboard keys{ enter }key
#             items for the current test item.        
###################################################################
    def enterkey(self):
        """enterkey"""
        self.element.Keys("[Enter]")
        
###################################################################
#unchecked:- this function retrun's bool(wheather the control is checked 
#            or not       
###################################################################

    def unchecked(self):
        """unchecked"""
        if self.verify_property("IsChecked"):
            if self.element.IsChecked == False:
                Log.Message("Check box is unchecked default")
            else:
                self.element.Click()
                Log.Message("check box is unchecked")
        elif self.verify_property("Checked"):
            if self.element.Checked == False:
                Log.Message("Check box is unchecked default")
            else:
                self.element.Click()
                Log.Message("check box is unchecked")

###################################################################
#wpfcontroltext:- this function return's text 
#             items for the current test item        
###################################################################

    @property
    def wpfcontroltext(self):
        """wpfcontroltext"""
        return self.element.WPFControlText
    

###################################################################
#get_win_caption:- this function return's WndCaption 
#             winitems for the current test item        
###################################################################

    @property
    def get_win_caption(self):
        """get_win_caption"""
        return self.element.WndCaption
###################################################################
#verifycheckbox:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def verifycheckbox(self):
        """verifycheckbox"""
        if self.verify_property("IsChecked"):
            checkbox = self.element.IsChecked
        elif self.verify_property("Checked"):
            checkbox = self.element.Checked
        elif self.verify_property("IsSelected"):
            checkbox = self.element.IsSelected
        return checkbox
###################################################################
#verifynotdisplayed:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def verifynotdisplayed(self):
        """verifynotdisplayed"""
        return self.element.Visible
###################################################################
#get_datacontext:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def get_datacontext(self):
        """get_dataContext"""
        self.element.get_Text()
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def bodyalertctditextbox(self):
        """bodyAlertCTDITextbox"""
        self.element.bodyAlertCTDITextbox()
###################################################################
#clear_set_text:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def clear_set_text(self, text):
        """clear_set_text"""
        self.element.Clear()
        self.element.SetText(text)

###################################################################
#clear_enter_text:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def clear_enter_text(self, text):
        """clear_enter_text"""
        self.element.clear()
        self.element.DblClick()
        self.element.Keys(" [BS] [BS] [BS] [BS] [BS] [BS] ")
        self.element.Keys(text)
        self.enterkey()
        
###################################################################
#checkboxchecked:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def checkboxchecked(self):
        """checked"""
        if self.verify_property("IsChecked"):
            if self.element.IsChecked == True:
                Log.Message("Check box is checked default")
            else:
                self.element.Click()
                Log.Message("check box is checked")
        elif self.verify_property("Checked"):
            if self.element.Checked == True:
                Log.Message("Check box is checked default")
            else:
                self.element.Click()
                Log.Message("check box is checked")

###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def settext(self, text):
        """settext"""
        self.element.Text=text

###################################################################
#waitforpropertyvalue:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def waitforpropertyvalue(self,propertyname, propertyvalue):
        """waitforpropertyvalue"""
        iteration_count = 0
        retry= Project.Variables.retry_count * 15
        time_interval= Project.Variables.time_interval*5
        while iteration_count < retry:
            #element = None
            try:
                value =aqObject.GetPropertyValue(self.element,propertyname)
                if str(value).upper().find(propertyvalue.upper()) != -1:
                    return True
                iteration_count += 1
                Delay(time_interval, "Element is not Visible, Retrying for the element.....")
            except Exception as ex:
                iteration_count += 1
                Delay(time_interval, "Element not found, Retrying for the element.....")
                raise Exception(ex) from ex
        return False
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def waitforpropertyvaluetodisappear(self,propertyname, propertyvalue):
        """waitforpropertyvaluetodisappear"""
        iteration_count = 0
        retry= Project.Variables.retry_count * 15
        time_interval= Project.Variables.time_interval*5
        while iteration_count < retry:
            #element = None
            try:
                value = aqObject.GetPropertyValue(self.element,propertyname)
                if str(value).upper().find(propertyvalue.upper()) == -1:
                    return True
                iteration_count += 1
                Delay(time_interval, "Element is not Visible, Retrying for the element.....")
            except Exception as ex:
                iteration_count += 1
                Delay(time_interval, "Element not found, Retrying for the element.....")
                raise Exception(ex) from ex
        return False
###################################################################
#clickandhold:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def clickandhold(self):
        """clickandhold"""
        LLPlayer.KeyDown(VK_CONTROL, 2000)
        ele = self.element
        for _ in range(310):
            aqUtils.Delay(2000)
            ele.click()
        LLPlayer.KeyUp(VK_CONTROL, 2000)
###################################################################
#setvalue:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def setvalue(self, text):
        """setvalue"""
        self.element.Keys("^A")
        self.element.Keys("[BS]")
        self.element.Keys(text)

###################################################################
#setvalue_cycle:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def setvalue_cycle(self, text):
        """setvalue"""
        self.element.Keys("^A")
        self.element.Keys("[BS]")
        self.element.Keys("[BS]")
        self.element.Keys(text)

###################################################################
#clear_enter_Close:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def clear_enter_close(self):
        """clear_enter_Close"""
        self.element.Close()
###################################################################
#right_click_at:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def right_click_at(self,tox,toy):
        """right_click_at"""
        self.element.ClickR(tox,toy)
###################################################################
#minimize_screen:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def minimize_screen(self):
        """minimize_simulator_screen"""
        self.element.Minimize()
###################################################################
#close:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def close(self):
        """close_screen"""
        self.element.Close()
###################################################################
#click_enter_text:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_enter_text(self, text):
        """click_enter_text"""
        self.element.Click()
        self.element.Keys(text)

###################################################################
#find_all_listbox_children:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def find_all_listbox_children(self):
        """find_all_listbox_children"""
        listboxitems = self.element.FindAllChildren("ClrClassName", "ListBoxItem")
        return listboxitems
###################################################################
#drag_drop:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def drag_drop(self, clientx, clienty, tox, toy):
        """drag_drop"""
        self.element.Drag(clientx, clienty, tox, toy)
###################################################################
#click_at_ctrl:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_at_ctrl(self, tox, toy, ctrl):
        """click_at_ctrl"""
        self.element.Click(tox, toy, ctrl)
###################################################################
#hover_at:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def hover_at(self, tox, toy):
        """hover_at"""
        self.element.HoverMouse(tox, toy)
###################################################################
#click_at_r:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def click_at_r(self, tox, toy):
        """click_at_r"""
        self.element.ClickR(tox, toy)
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def drag_drop_zoom(self, clientx, clienty, tox, toy, ctrl):
        """drag_drop_zoom"""
        self.element.Drag(clientx, clienty, tox, toy, ctrl)
###################################################################
#double_click_at:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def double_click_at(self, tox, toy):
        """double_click_at"""
        self.element.DblClick(tox, toy)
###################################################################
#activate_window:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def activate_window(self):
        """activate_window"""
        self.element.Activate()
###################################################################
#waitforelement:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def waitforelement(self, name, propertyvalue, wait):
        """waitforelement"""
        return self.element.WaitProperty(name,propertyvalue,wait)
###################################################################
#drag_drop_manual_scan_button:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def drag_drop_manual_scan_button(self, clientx, clienty, tox, toy):
        """drag_drop_manual_scan_button"""
        for _ in range(30):
            self.element.Drag(clientx, clienty, tox, toy)
###################################################################
#clear_entered_text:- this function helps to clear the text 
#              for the current test item.        
###################################################################
    def clear_entered_text(self, text):
        """clear_enter_text"""
        self.element.Keys(text)

###################################################################
#mouse_wheel:- this function helps to move mouse wheel 
#               by specified text .        
###################################################################
    def mouse_wheel(self, text):
        """mouse_wheel"""
        self.element.MouseWheel(text)
###################################################################
#verify_not_displayed:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def verify_not_displayed(self):
        """verifynotdisplayed"""
        return self.element.ClipToBounds
###################################################################
#wait_for_element_property:- this function helps to  wait for an 
#                          element_property        
###################################################################
    def wait_for_element_property(self, name, propertyvalue, wait):
        """wait_for_element_property"""
        return self.element.WaitProperty(name,propertyvalue,wait)
###################################################################
#verify_property:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def verify_property(self, property_name):
        """verify_property"""
        if aqObject.IsSupported(self.element,property_name):
            return True
        return False
###################################################################
#set_text:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def set_text(self, text):
        """settext"""
        if self.verify_property("Text"):
            self.element.Text = text
        elif self.verify_property("wText"):
            self.element.wText = text
        elif self.verify_property("Value"):
            self.element.Value = text
        elif self.verify_property("WPFControlText"):
            self.element.WPFControlText = text

###################################################################
#verify_method:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def verify_method(self, method_name):
        """verify_method"""
        colmethods = aqObject.GetMethods(self.element)
        while colmethods.HasNext():
            method = colmethods.Next().Name
            if method.upper() == method_name.upper():
                return True
        return False
###################################################################
#clear_text:- this function used to clear text
#              for the current test item.        
###################################################################
    def clear_text(self):
        """clear_text"""
        if self.verify_method("SetText"):
            self.element.SetText("")
        elif self.verify_method("set_Text"):
            self.element.set_Text("")
        elif self.verify_method("Keys"):
            self.element.Keys("^A")
            self.element.Keys("[BS]")
        elif self.verify_method("Clear"):
            self.element.Clear()
        else:
            self.element.DblClick()

###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def enter_text(self, text):
        """enter_text"""
        try:
            self.clear_text()
        except Exception as ex:
            raise Exception(ex) from ex
        if self.verify_method("Keys"):
            self.element.Keys(text)
        elif self.verify_method("set_Text"):
            self.element.set_Text(text)
        elif self.verify_method("SetText"):
            self.element.SetText(text)
        else:
            self.element.Text = text

###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################

    def ocr_text_verification(self,text):
        """ocr_text_verification"""
        OCR.Recognize(self.element).CheckText(text)


###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def find_children_for_result_viewer(self):
        """find_children_for_result_viewer"""
        listboxitems = self.element.FindAllChildren("ClrClassName","TextBlock", 1000, True)
        return listboxitems
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def ocr_full_text(self):
        """ocr_full_text"""
        return OCR.Recognize(self.element).FullText
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    @property
    def value(self):
        """value"""
        return self.element.Value
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def rowvalue(self,i,name):
        """rowvalue"""
        row = "Row " + str(i)
        return self.element.Row(row).Cell(name)
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def datacontextcount(self):
        """datacontextcount"""
        return self.element.DataContext.Menu.Count

###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def datacontext(self,i):
        """datacontext"""
        return self.element.DataContext.Menu.Item[i]
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def enter_data_box(self,text):
        """enter_data_box"""
        self.element.DblClick()
        self.element.Keys(text)
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################



    def picture_masking(self,tox,toy,width,height):
        """picture_masking"""
        return self.element.Picture(tox,toy,width,height,False)
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def row(self):
        """row_count"""
        return self.element.RowCount
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def column(self):
        """column_count"""
        return self.element.ColumnCount
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def item(self,col, row):
        """column_count"""
        return self.element.Item[col, row].Value
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def take_evidence(self):
        """take_evidence"""
        return Log.Picture(self.element,"Full Screenshot", "Extended Message", pmHighest)
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def image_verification_repository(self,image_repository_property):
        """image_verification_repository"""
        image= eval(image_repository_property)
        if image.Exists(self.element):
            Log.Picture()
            return True
        else:
            Log.Picture()
            return False
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def double_click_cell(self,row,col):
        """double_click_cell"""
        self.element.DblClickCell(row,col)
      
###################################################################
#get_tab_name:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def scroll_horizontally(self,pos):
        """scroll_horizontally"""
        self.element.HScroll.Pos = pos
      
###################################################################
#scroll_vertically:- this function helps to scroll vertically by 
#             items for the current test item.        
###################################################################
    def scroll_vertically(self,pos):
        """scroll_vertically"""
        self.element.VScroll.Pos = pos
      
###################################################################
#waiting_for_screen_to_load:- this function 
#             items for the current test item.        
###################################################################
    def waiting_for_screen_to_load(self,param):
        """waiting_for_page"""
        count,message = param.split(',')
        aqUtils.Delay(count,message)
      
###################################################################
#key_board_action:- this function return's total number of direct child
#             items for the current test item.        
###################################################################
    def key_board_action(self,param):
        """key_board_action"""
        req_data,message = param.split(',')
        Sys.Keys(req_data)

###################################################################
#ocr_blockby_text:- this function help's to click on Ocr text 
#             items for the current test item.        
###################################################################
    def ocr_blockby_text(self,param):
        """ocr_blockby_text"""
        return OCR.Recognize(self.element).BlockByText(param).Click()


      
###################################################################
#item_value:- this function return's item_value of the control       
###################################################################
    def item_value(self,i):
        """item_value"""
        return self.element.Items.Item[i]

      
###################################################################
#cell_text:- this function return's cell_text 
#             items for the current test item.        
###################################################################
        
    def cell_text(self, row: int, column: int):
        """cell_text"""
        return self.element.wValue[row, column]
        
      
###################################################################
#findallorientationradiobutton:- this function return's list of all
#           childern   OrientationRadioButton inside tabcontrol   
###################################################################       
        
    def findallchildernorientationradiobutton(self):
        """findallorientationradiobutton"""
        listofradiobtn = self.element.FindAllChildren("ClrClassName","OrientationRadioButton", 1000, True)
        return listofradiobtn
        
        
      
###################################################################
#findallchildern_tab_items:- this function return's listof all childern
#            tabitems inside a control     
###################################################################      
        
    def findallchildern_tab_items(self):
        """findallorientationradiobutton"""
        listofradiobtn = self.element.FindAllChildren("ClrClassName","TabItem", 1000, True)
        return listofradiobtn
        
###################################################################
#findallchildern_radiobuttons:- this function return's listofradiobtn 
#         all childern  RadioButton inside a control     
###################################################################
    def findallchildern_radiobuttons(self):
        """findallorientationradiobutton"""
        listofradiobtn = self.element.FindAllChildren("ClrClassName","RadioButton", 1000, True)
        return listofradiobtn
 
        
###################################################################
#findallchildern_labels:- this function return's listoflabels 
#         all childern  Label inside a control     
###################################################################
               
    def findallchildern_labels(self):
        """findallorientationradiobutton"""
        listoflabel = self.element.FindAllChildren("ClrClassName","Label", 1000, True)
        return listoflabel
    
        
  ###################################################################
  #dataschedulecolumnheader 
  ###################################################################  
 

    def dataschedulecolumnheader(self,nameofheader,coloumnno):
        """dataschedulefilter"""
        return self.element.WPFObject("DataGridColumnHeader", str(nameofheader), int(coloumnno))
    
    

 ###################################################################
  #find_all_textbox_childern returns elements  of classname TextBox
 ###################################################################  


    
    def find_all_textbox_childern(self):
        """find_children_for_result_viewer"""
        listboxitems = self.element.FindAllChildren("ClrClassName","TextBox", 1000, True)
        return listboxitems
    


 ##################################################################################
  #findall_all_static_wndclassitems returns list  of all wndclassname Static
 ################################################################### ############## 



    def findall_all_static_wndclassitems(self):
        """findall_all_static_wndclassitems"""
        static_items = self.element.FindAllChildren("WndClass","Static", 1000, True)
        return  static_items 

 ##################################################################################
#  VERIFY WPF TEXT 
 ################################################################### ############## 
        
    def verify_wpf_text(self,text):
      try:  
        ele = self.element.WPFControlText
        if text in ele:
          Log.Checkpoint(ele)
        else:
          Log.Warning(ele)
      except Exception as ex:
          Log.Error(ex)
        

 ##################################################################################
#  open_system_explorer() clicks on the toolbar in SE engineering client to open 
#  System explorer
 ################################################################### ############## 

    
    def open_system_explorer(self):
      try:
        if 'Open System Explorer' == self.element.ToolTip:
          self.element.Click()
      except Exception as ex:
          Log.Error(ex)
        
###################################################################
#find_all_children:- this function return's all children for the current item         
###################################################################
    def find_children_for_treeviewrow(self):
        """find_all_children"""
        listboxitems = self.element.FindAllChildren("ClrClassName", 'TreeListViewRow', 1500, True)        
        return listboxitems       
          
###################################################################
#find_all_children:- this function return's all children for the current item         
###################################################################
    def find_children_for_explorer_node(self):
        """find_all_children for explorer node"""
        listboxitems = self.element.FindAllChildren("ClrClassName", 'ExplorerNode', 1500, True)        
        return listboxitems       
          
###################################################################
#find_all_children:- this function return's all children for the current item         
###################################################################
    def find_children_for_grid_view_row(self):
        """find_all_children_for_grid_view_row"""
        listboxitems = self.element.FindAllChildren("ClrClassName", 'GridViewRow', 1500, True)        
        return listboxitems       
                
        
###################################################################
#find_all_children:- this function return's all children for the current item         
###################################################################
    def find_children_for_closeable_tab_item(self):
        """find_all_children for Closeable tab item"""
        listboxitems = self.element.FindAllChildren("ClrClassName", 'CloseableTabItem', 1500, True)        
        return listboxitems       
        
###################################################################
#Wait for object disappear:- this function return's all children for the current item         
###################################################################

    def wait_for_object_disapear(self):
        self.element.WaitProperty('Exists', None, 50000)
        
###################################################################
# sys_keys:- this function Enters keyboard vale        
###################################################################          

    def sys_keys(self,Value):
        Sys.Keys(Value)
 
###################################################################
#verify_object:- This function is to verify if object Exists
###################################################################

    def verify_object(self, object):
        """verify_object"""
        try:
          if self.element.Exists:
            Log.Checkpoint(object + ' is visible on screen.')
        except: 
          Log.Warning(object + 'is not visible on screen.')
        
############################################################
#check :- this function is to change checkbox wstate to 1 (checked)
############################################################
    def checkbox_checked(self):
        """checkbox_checked"""
        if self.element.wState != 1:
          self.element.wState = 1
          Log.Checkpoint('Checkbox checked')
        else:
          Log.Message('Checkbox already checked')
		 
    