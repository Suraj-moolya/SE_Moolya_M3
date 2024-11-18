"""MessageBoxWorkFlow"""  

from MessageBox import MessageBox
import Applicationutility
import Engineeringclientutility
import Applicationexplorertabutility
import Actionutility
import Topologyutility


class MessageBoxWorkFlow:
    """MessageBoxWorkFlow"""
    messagebox_obj = MessageBox()

        
    def buttonlicensemanagementpopupcheckforlicensemanagementwindowin(self):
        """buttonlicensemanagementpopupcheckforlicensemanagementwindowin"""
        try:
            Engineeringclientutility.License_management_pop_up_check()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonlicensemanagementokclickonokbuttonfrom(self):
        """buttonlicensemanagementokclickonokbuttonfrom"""
        try:
            Engineeringclientutility.License_management_pop_up_ok()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttontraillicensepopupcheckecostruxurecontrolexpertin(self):
        """buttontraillicensepopupcheckecostruxurecontrolexpertin"""
        try:
            Engineeringclientutility.Trail_license_window_validation()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonlicensemanagementpopupclickonenter(self):
        """buttonlicensemanagementpopupclickonenter"""
        try:
            Engineeringclientutility.Keyboard_action_Enter()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxrenamepopupverifyrenamewarningmessage(self,Popup_Message):
        """textboxrenamepopupverifyrenamewarningmessage"""
        try:
            Engineeringclientutility.verify_Rename_Popup_Message_SES(Popup_Message)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonrenamepopupokselected(self):
        """messagebox_obj.renamepopupokbutton"""
        MessageBoxWorkFlow.messagebox_obj.renamepopupokbutton.click()
        
        
    def textboxrenamepopupverifyrenamewarningpopup(self,):
        """textboxrenamepopupverifyrenamewarningpopup"""
        try:
            Engineeringclientutility.Rename_error_pop_up_check_SES()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxrenamepopupclickonokfromrenamewarningpopup(self,):
        """textboxrenamepopupclickonokfromrenamewarningpopup"""
        try:
            Engineeringclientutility.Rename_error_pop_up_ok()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxrenamepopupcloseecpopup(self,):
        """textboxrenamepopupcloseecpopup"""
        try:
            Engineeringclientutility.warning_popup_close()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttondeletepopupverifydeletepopupae(self,message):
        """buttondeletepopupverifydeletepopupae"""
        try:
            Applicationexplorertabutility.verify_delete_popup_message(message)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttondeletepopupclickonbuttonsinpopupwindow(self,button_name):
        """buttondeletepopupclickonbuttonsinpopupwindow"""
        try:
            Applicationexplorertabutility.MessageWindow_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttondeletepopupverifyactionmessageinnotificationpannel(self,message):
        """buttondeletepopupverifyactionmessageinnotificationpannel"""
        try:
            Applicationexplorertabutility.verify_template_deleted(message)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonexportenterfilenameandfilelocationinexportwindowae(self,file_format):
        """buttonexportenterfilenameandfilelocationinexportwindowae"""
        
        Applicationexplorertabutility.Enter_systemName_systemlocation_ExportWindow_AE(file_format)
        
        
    def buttonexportclickonbuttoninaeexplorerwindow(self,button_name):
        """buttonexportclickonbuttoninaeexplorerwindow"""
        try:
            Applicationexplorertabutility.Explorer_buttons_AE(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonexportverifyexportsystem1exportpopupae(self,message):
        """buttonexportverifyexportsystem1exportpopupae"""
        try:
            Applicationexplorertabutility.export_System1_Export_Popup_AE(message)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonexportclickonexportsystem1exportpopupaebuttons(self,button_name):
        """buttonexportclickonexportsystem1exportpopupaebuttons"""
        try:
            Applicationexplorertabutility.export_System1_Export_Popup_AE_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonexportverifyextractedtemplatecsvdataandtemplatedetails(self):
        """buttonexportverifyextractedtemplatecsvdataandtemplatedetails"""
        try:
            Applicationexplorertabutility.extract_template_csvdata_AE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonexportverifyextractedtemplatexmldataandtemplatedetails(self):
        """buttonexportverifyextractedtemplatexmldataandtemplatedetails"""
        try:
            Applicationexplorertabutility.extract_template_xmldata_AE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxnotificationpannelverifymessagefromnotificationpanelae(self):
        """textboxnotificationpannelverifymessagefromnotificationpanelae"""
        try:
            Applicationexplorertabutility.Verify_Notification_Message()
        except Exception as ex:
            raise Exception(ex) from ex
        
            
    def buttondeletepopupverifymessagefromnotificationpanelae(self,message_to_verify):
            """buttondeletepopupverifymessagefromnotificationpanelae"""
            try:
                Applicationexplorertabutility.Verify_Notification_Message(message_to_verify)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def textboxmanagenetworkvariablesrightclickonvariable(self,var_name):
            """textboxmanagenetworkvariablesrightclickonvariable"""
            try:
                Projectexplorertabutility.Right_click_on_variable(var_name)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def textboxmodaldialogwindowaddnewtextmodaldialogwindow(self,param):
        """textboxmodaldialogwindowaddnewtextmodaldialogwindow"""
        try:
            Actionutility.modal_dialog_window_textbox(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxmodaldialogwindowclickmodaldialogwindow(self,button_name):
        """textboxmodaldialogwindowclickmodaldialogwindow"""
        try:
            Actionutility.modal_dialog_window_button(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxmodaldialogwindowselectipadressfromdeployprojectbuildte(self,IP_address):
        """textboxmodaldialogwindowselectipadressfromdeployprojectbuildte"""
        try:
            Topologyutility.Select_IP_from_ControlProjectDeployment(IP_address)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxmodaldialogwindow1clickpopupbuttonobject(self,param):
        """textboxmodaldialogwindow1clickpopupbuttonobject"""
        try:
            Actionutility.Click_popup_button(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxnotificationpannelverifynotificationpanelmessage(self,Message):
        """textboxnotificationpannelverifynotificationpanelmessage"""
        try:
            Applicationexplorertabutility.Verify_Notification_pannel_Message(Message)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxmodaldialogwindow1verifymodaldialogwindowtext(self,param):
        """textboxmodaldialogwindow1verifymodaldialogwindowtext"""
        try:
            Actionutility.modal_dialog_window_dialog(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    
      