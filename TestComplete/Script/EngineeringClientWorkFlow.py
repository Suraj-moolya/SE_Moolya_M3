"""EngineeringClientWorkFlow"""  

from EngineeringClient import EngineeringClient
import Applicationutility
import Actionutility
import Engineeringclientutility

class EngineeringClientWorkFlow:
    """EngineeringClientWorkFlow"""
    engineeringclient_obj = EngineeringClient()

    def buttonengineeringclientlaunchengineeringclient(self):
        """buttonengineeringclientlaunchengineeringclient"""
        try:
            Engineeringclientutility.open_EC_ok_on_trial_pop_up()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonlaunchengineeringclientverifydisplayed(self):
        """engineeringclient_obj.launchengineeringclientbutton"""
        try:
            element=EngineeringClientWorkFlow.engineeringclient_obj.launchengineeringclientbutton
            if element is not None:
                Log.Message('LaunchEngineeringClient is displayed')
            else:
                Log.Error('LaunchEngineeringClient is not displayed')
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxsystemexplorerwindowverifycontent(self,systemExplorerWindow1):
        """engineeringclient_obj.systemexplorerwindowtextbox"""
        try:
            content=EngineeringClientWorkFlow.engineeringclient_obj.systemexplorerwindowtextbox.text
            if systemExplorerWindow1 == content:
                Log.Message('Systemexplorerwindow value is : ' + systemExplorerWindow1)
            else:
                Log.Error('Systemexplorerwindow value is not equal to '+systemExplorerWindow1)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttonengineeringclientdialogueboxverifydisplayed(self):
        """engineeringclient_obj.engineeringclientdialogueboxbutton"""
        try:
            element=EngineeringClientWorkFlow.engineeringclient_obj.engineeringclientdialogueboxbutton
            if element is not None:
                Log.Message('EngineeringClientDialogueBox is displayed')
            else:
                Log.Error('EngineeringClientDialogueBox is not displayed')
        except Exception as ex:
            raise Exception(ex) from ex
            


    def buttonlaunchengineeringclientopenengineeringclient(self):
        """buttonlaunchengineeringclientopenengineeringclient"""
        try:
            Engineeringclientutility.open_EC_ok_on_trial_pop_up()
        except:
            Log.Error('EC not open')
        
    def buttonuserdropdownselected(self):
        """engineeringclient_obj.userdropdownbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.userdropdownbutton.click()
        Applicationutility.wait_in_seconds(2000, 'Wait')
        
        
    def buttonuserlockselected(self):
        """engineeringclient_obj.userlockbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.userlockbutton.click()
        
        
    def textboxpasswordentered(self,password1):
        """engineeringclient_obj.passwordtextbox"""
        EngineeringClientWorkFlow.engineeringclient_obj.passwordtextbox.enter_text(password1)
        
    def buttonloginselected(self):
        """engineeringclient_obj.loginbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.loginbutton.click()
        
        
    def buttonopensystemexplorerverifydisplayed(self):
        """engineeringclient_obj.opensystemexplorerbutton"""
        Engineeringclientutility.Verify_logged_in_EC()
            
    def buttonengineeringclientverifydisplayed(self):
        """engineeringclient_obj.engineeringclientbutton"""
        Applicationutility.wait_in_seconds(2000, 'wait')
        Engineeringclientutility.Verify_logged_in_EC()
            
    def buttonuserlogoutselected(self):
        """engineeringclient_obj.userlogoutbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.userlogoutbutton.click()
        
        
    def buttonuserloginselected(self):
        """engineeringclient_obj.userloginbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.userloginbutton.click()
        
        
    def textboxusernameentered(self,userName1):
        """engineeringclient_obj.usernametextbox"""
        EngineeringClientWorkFlow.engineeringclient_obj.usernametextbox.enter_text(userName1)
        
    def windownotificationpanelverifycontent(self):
        """engineeringclient_obj.notificationpanelwindow"""
        try:
            content=EngineeringClientWorkFlow.engineeringclient_obj.notificationpanelwindow.text
            if  ''== content:
                Log.Message('Notificationpanel value is : '  )
            else:
                Log.Error('Notificationpanel value is not equal to ')
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttoncloseecselected(self):
        """engineeringclient_obj.closeecbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.closeecbutton.click()
        Applicationutility.wait_in_seconds(5000, 'wait')
        
        
    def textboxdialogueboxverifycontent(self,dialogueBox3):
        """engineeringclient_obj.dialogueboxtextbox"""
        try:
            content=EngineeringClientWorkFlow.engineeringclient_obj.dialogueboxtextbox.text
            if dialogueBox3 == content:
                Log.Message('dialoguebox value is : ' + dialogueBox3)
            else:
                Log.Error('dialoguebox value is not equal to '+dialogueBox3)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxdialogueboxverifycontent(self,dialogueBox3):
        """engineeringclient_obj.dialogueboxtextbox"""
        obj = Sys.Process("EngineeringClient").WPFObject("HwndSource: ModalDialogWindow", "").WPFObject("ModalDialogWindow", "", 1).WPFObject("LoginDialog", "", 1).WPFObject("Grid", "", 1).WPFObject("Grid", "", 3).WPFObject("TextBlock", "*", 1)
        if str(obj.WPFControlText) == str(dialogueBox3):
          Log.Checkpoint(str(obj.WPFControlText))
        else:
          Log.Warning('The expected message is not displayed ; Message displayed is :' + str(obj.WPFControlText))
            
    def buttonloginterminateengineeringclient(self):
        """buttonloginterminateengineeringclient"""
        try:
            Engineeringclientutility.terminate_engineering_client()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonopenglobaltemplatesexplorerselected(self):
        """engineeringclient_obj.openglobaltemplatesexplorerbutton"""
        Applicationutility.wait_in_seconds(1000, 'wait')
        EngineeringClientWorkFlow.engineeringclient_obj.openglobaltemplatesexplorerbutton.click()
        
        
    def buttonopensystemexplorerselected(self):
        """engineeringclient_obj.opensystemexplorerbutton"""
        EngineeringClientWorkFlow.engineeringclient_obj.opensystemexplorerbutton.click()
        
        
    def textboxVerifyDropdownoptions(self):
            """buttonengineeringclientlaunchengineeringclient"""
            try:
                Engineeringclientutility.Verify_Dropdown_options()
            except Exception as ex:
                raise Exception(ex) from ex
                
                
    def textboxVerifyLogout(self):
                """buttonengineeringclientlaunchengineeringclient"""
                try:
                    Engineeringclientutility.Verify_Logout()
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def keyboardactionenter(self):
                    try:
                        Engineeringclientutility.Keyboard_action_Enter()
                    except Exception as ex:
                        raise Exception(ex) from ex
                        
    def buttonmainscreenclosetabitemsec(self,identifier):
        """buttonmainscreenclosetabitemsec"""
        try:
            Actionutility.close_tab_items_EC(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def closetabitemec(self,tabname):
        """closetabitemec"""
        try:
            Engineeringclientutility.close_tab_EC(tabname)
        except Exception as ex:
            raise Exception(ex) from ex   
            
    def OpenClosefolderTE(self,button):
        """OpenClosefolderTE"""
        try:
            Engineeringclientutility.Open_Close_folder_TE(button)
        except Exception as ex:
            raise Exception(ex) from ex     
            
    def VerifyFolderExpansionstatusTE(self,foldername):
        """VerifyFolderExpansionstatusTE"""
        try:
            Engineeringclientutility.Verify_folder_Content_Status_TE(foldername)
        except Exception as ex:
            raise Exception(ex) from ex  
            
    def closetabec(self,param):
        """closetabec"""
        try:
            Engineeringclientutility.close_the_tab_EC(param)
        except Exception as ex:
            raise Exception(ex) from ex      
            
    def updatereport(self,customer_name, site_name, report_desc, report_author, page_size, orientation, report_footer, report_header):
        """updatereport"""
        try:
            Engineeringclientutility.update_report_details(customer_name, site_name, report_desc, report_author, page_size, orientation, report_footer, report_header)
        except Exception as ex:
            raise Exception(ex) from ex   
            