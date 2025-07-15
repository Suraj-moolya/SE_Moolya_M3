"""RefineOfflineWorkFlow"""  

from RefineOffline import RefineOffline
import Applicationutility
import Controlexpertutility
import Applicationexplorertabutility
class RefineOfflineWorkFlow:
    """RefineOfflineWorkFlow"""
    refineoffline_obj = RefineOffline()

        
    def buttonunlockselected(self):
        """refineoffline_obj.unlockbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.unlockbutton.click()
        
        
    def buttonunlockunlockdialogpopup(self,button_name):
        """buttonunlockunlockdialogpopup"""
        try:
            Controlexpertutility.Unlock_Dialog_popup(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonunlockdeletelinkrefineoffline(self,identifier):
        """buttonunlockdeletelinkrefineoffline"""
        try:
            Controlexpertutility.Delete_link_Refine_Offline(identifier)
        except Exception as ex:
            raise Exception(ex) from ex

        
    def buttonsaverefineofflineselected(self):
        """refineoffline_obj.saverefineofflinebutton"""
        try:
          RefineOfflineWorkFlow.refineoffline_obj.saverefineofflinebutton.click()
          Applicationutility.wait_in_seconds("1000","Wait")
        except Exception as e:
           raise Exception(ex) from ex
        
    def buttonconsistencycheckselected(self):
        """refineoffline_obj.consistencycheckbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.consistencycheckbutton.click()
        
        
    def buttonconsistencycheckconsistencycheckselectall(self):
        """buttonconsistencycheckconsistencycheckselectall"""
        try:
            Controlexpertutility.Consistency_Check_Select_All()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonconsistencycheckclickonexportsystem1exportpopupaebuttons(self,button_name):
        """buttonconsistencycheckclickonexportsystem1exportpopupaebuttons"""
        try:
            Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonconsistencycheckverifymessagefromnotificationpanelae(self,message_to_verify):
        """buttonconsistencycheckverifymessagefromnotificationpanelae"""
        try:
            Applicationexplorertabutility.Verify_Notification_Message(message_to_verify)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonconsistencycheckverifymodificationsavailableinrefineoffline(self,identifier):
        """buttonconsistencycheckverifymodificationsavailableinrefineoffline"""
        try:
            Controlexpertutility.Verify_modifications_available_in_Refine_Offline(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def textboxmdiwindowrclickonfilterrefineoffline(self):
        """textboxmdiwindowrclickonfilterrefineoffline"""
        try:
            Controlexpertutility.RClick_on_filter_Refine_Offline()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoncustomizecolumnsselected(self):
        """refineoffline_obj.customizecolumnsbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.customizecolumnsbutton.click()
        
        
    def buttoncustomizecolumnsselectcolumnconfiguration(self,identifier):
        """buttoncustomizecolumnsselectcolumnconfiguration"""
        try:
            Controlexpertutility.Select_Column_Configuration(identifier)
        except Exception as ex:
            raise Exception(ex) from ex

        
    def textboxmdiwindowaddvariablenameinnamecolumn(self,var_name):
        """textboxmdiwindowaddvariablenameinnamecolumn"""
        try:
            Controlexpertutility.Add_variable_name_in_name_column (var_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxmdiwindowclickonellipsis(self):
        """textboxmdiwindowclickonellipsis"""
        try:
            Controlexpertutility.click_on_elipsis()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttontypecolumnellipsisselected(self):
        """refineoffline_obj.typecolumnellipsisbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.typecolumnellipsisbutton.click()
        
        
    def buttontypecolumnellipsisselectvariabletypedialogpopupce(self):
        """buttontypecolumnellipsisselectvariabletypedialogpopupce"""
        try:
            Controlexpertutility.select_variable_type_Dialog_popup_CE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttontypecolumnellipsisselectconstantcheckbox(self):
        """buttontypecolumnellipsisselectconstantcheckbox"""
        try:
            Controlexpertutility.select_Constant_check_box()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxmdiwindowenterp2pincustombox(self):
        """textboxmdiwindowenterp2pincustombox"""
        try:
            Controlexpertutility.Enter_P2P_in_Custom_box()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxmdiwindowselectvariabletype(self,val):
        """textboxmdiwindowselectvariabletype"""
        try:
            Controlexpertutility.select_variable_type(val)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonmanagenetworkvariablesselected(self):
        """refineoffline_obj.managenetworkvariablesbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.managenetworkvariablesbutton.click()
        
    def textboxmdiwindowverifyvariableisremovedrefineoffline(self,var_name):
        """textboxmdiwindowverifyvariableisremovedrefineoffline"""
        try:
            Controlexpertutility.Verify_variable_is_removed_Refine_Offline(var_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxmdiwindoweditipaddressinconfigure(self,param):
        """textboxmdiwindoweditipaddressinconfigure"""
        try:
            Controlexpertutility.edit_IP_Address(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
        
    def buttoneditbuttonselected(self):
        """refineoffline_obj.editbuttonbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.editbuttonbutton.click()
         
    def buttonvalidateselected(self):
        """refineoffline_obj.validatebutton"""
        RefineOfflineWorkFlow.refineoffline_obj.validatebutton.click()	
    
    def buttoncloserefineofflineselected(self):
        """textboxmdiwindowverifyvariableisremovedrefineoffline"""
        try:
            Applicationutility.wait_for_execution(2000,"wait")
            RefineOfflineWorkFlow.refineoffline_obj.closerefineofflinebutton.click()
            
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttontoolsbuttonselected(self):
        """refineoffline_obj.toolsbuttonbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.toolsbuttonbutton.click()
        
        
    def buttondtmbrowserselected(self):
        """refineoffline_obj.dtmbrowserbutton"""
        #RefineOfflineWorkFlow.refineoffline_obj.dtmbrowserbutton.click()
        Sys.Keys("~!1")
        Applicationutility.wait_in_seconds(1500, 'Wait')
        
    def textboxprojectbrowserroverifymappeddtmdevicepresentce(self,Identifier):
        """textboxprojectbrowserroverifymappeddtmdevicepresentce"""
        try:
            Controlexpertutility.Verify_Mapped_DTM_device_present_CE(Identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            

        
    def textboxprojectbrowserroenterkey(self):
        """textboxprojectbrowserroenterkey"""
        try:
           Sys.Keys('[Enter]')
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonviewbuttonselected(self):
        """refineoffline_obj.viewbuttonbutton"""
        RefineOfflineWorkFlow.refineoffline_obj.viewbuttonbutton.click()
        
        
    def textboxfbdsectionwindowrclickdropseioaddnewdevicece(self):
        """textboxfbdsectionwindowrclickdropseioaddnewdevicece"""
        try:
            Controlexpertutility.Rclick_Drops_EIO_add_new_device_CE()
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxprojectbrowserroverifydisplayed(self):
        """refineoffline_obj.projectbrowserrotextbox"""
        try:
            element=RefineOfflineWorkFlow.refineoffline_obj.projectbrowserrotextbox
            if element is not None:
                Log.Message('ProjectBrowserRO is displayed')
            else:
                Log.Error('ProjectBrowserRO is not displayed')
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxrefineonlinewindowverifydisplayed(self):
        """refineoffline_obj.refineonlinewindowtextbox"""
        try:
            element=RefineOfflineWorkFlow.refineoffline_obj.refineonlinewindowtextbox
            if element is not None:
                Log.Message('Refineonlinewindow is displayed')
            else:
                Log.Error('Refineonlinewindow is not displayed')
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxprojectbrowserronavigatethroughprojectbrowserce(self,val):
        """textboxprojectbrowserronavigatethroughprojectbrowserce"""
        try:
            Controlexpertutility.double_click_selected_project_browser_item_CE(val)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxfbdsectionwindowmodificationsofsectionsce(self):
        """textboxfbdsectionwindowmodificationsofsectionsce"""
        try:
            Controlexpertutility.rclick_window_CE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxfbdsectionwindowverifymodificationsavailableinrefineoffline(self):
        """textboxfbdsectionwindowverifymodificationsavailableinrefineoffline"""
        try:
            Controlexpertutility.Verify_modifications_available_in_Refine_Offline(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsaverefineofflineselected1(self):
        """refineoffline_obj.saverefineofflinebutton"""
        RefineOfflineWorkFlow.refineoffline_obj.saverefineoffline1button.click()
        Applicationutility.wait_in_seconds(1000, 'wait')
        
    def textboxrefineonlinewindowwaitinseconds(self):
        """textboxrefineonlinewindowwaitinseconds"""
        try:
            Applicationutility.wait_in_seconds(20000,'Wait')
        except Exception as ex:
            raise Exception(ex) from ex
        

        
    def textboxprojectbrowserroselectadvsettingspropertiessvp(self,param):
        """textboxprojectbrowserroselectadvsettingspropertiessvp"""
        try:
            Controlexpertutility.select_AdvSettings_properties_SVP(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserroeditparametervalueadvsettingssvp(self,val):
        """textboxprojectbrowserroeditparametervalueadvsettingssvp"""
        try:
            Controlexpertutility.Edit_Parameter_Value_AdvSettings_SVP(val)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsaverefineofflineselected(self):
        """refineoffline_obj.saverefineofflinebutton"""
        RefineOfflineWorkFlow.refineoffline_obj.saverefineofflinebutton.click()
        
        
    def buttoncloserefineofflineselected(self):
        """refineoffline_obj.closerefineofflinebutton"""
        RefineOfflineWorkFlow.refineoffline_obj.closerefineofflinebutton.click()
        
        
    def textboxprojectbrowserroverifyparametervalueadvsettingssvp(self,param):
        """textboxprojectbrowserroverifyparametervalueadvsettingssvp"""
        try:
            Controlexpertutility.Verify_Parameter_Value_AdvSettings_SVP(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def buttonselectPLCbuscomboboxitemCE(self,param):
      """buttonselectPLCbuscomboboxitemCE"""
      try:
        Controlexpertutility.select_PLC_bus_combobox_item_CE(param)
      except Exception as ex:
        raise Exception(ex) from ex  
                
                
    def clickbuilddeploychangesbutton(self):
      """clickbuilddeploychanges"""
      try:
        RefineOfflineWorkFlow.refineoffline_obj.builddeploychangesbutton.click()
      except Exception as ex:
        raise Exception(ex) from ex
        
    def initializerefineofflinemenuitemRF(self):
      """clickbuilddeploychanges"""
      try:
        RefineOfflineWorkFlow.refineoffline_obj.initializerefineofflinemenuitem.click()
      except Exception as ex:
        raise Exception(ex) from ex
        
    def modificationbuttonrefineofflineRF(self):
      """clickbuilddeploychanges"""
      try:
        RefineOfflineWorkFlow.refineoffline_obj.modificationbuttonrefineoffline.click()
      except Exception as ex:
        raise Exception(ex) from ex
        
    def textboxmdiwindowselectitemmdiwindowce(self,identifier):
        """textboxmdiwindowselectitemmdiwindowce"""
        try:
            Controlexpertutility.select_item_mdi_window_CE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex

    def checkboxioddtcechecked(self):
        """refineoffline_obj.ioddtcecheckbox"""
        RefineOfflineWorkFlow.refineoffline_obj.ioddtcecheckbox.checkbox_checked()
        Applicationutility.take_screenshot('Taking Screenshot')
        
    def checkboxdeviceddtcechecked(self):
        """refineoffline_obj.deviceddtcecheckbox"""
        RefineOfflineWorkFlow.refineoffline_obj.deviceddtcecheckbox.checkbox_checked()
        Applicationutility.take_screenshot('Taking Screenshot')
        
    def buttonaccesstounmappedhardwareceselected(self):
        """refineoffline_obj.accesstounmappedhardwarecebutton"""
        RefineOfflineWorkFlow.refineoffline_obj.accesstounmappedhardwarecebutton.click()     
        
    def buttondeviceddtpopupmoveallceselected(self):
        """refineoffline_obj.deviceddtpopupmoveallcebutton"""
        RefineOfflineWorkFlow.refineoffline_obj.deviceddtpopupmoveallcebutton.click()
        
    def buttonselectunlocksecurityCE(self):
        """refineoffline_obj.UnlockSecuritybutton"""
        RefineOfflineWorkFlow.refineoffline_obj.UnlockSecuritybutton.click()
        
    def selecthttpsdropdownCE(self, param):
        """refineoffline_obj.selecthttpsdropdownCE"""
        RefineOfflineWorkFlow.refineoffline_obj.HTTPSbutton.select_item(param)
  
    def selectautomaticserviceportCE(self):
        """refineoffline_obj.BlockserviceportEIOcheckbox"""
        RefineOfflineWorkFlow.refineoffline_obj.BlockserviceportEIOcheckbox.check()
              