"""ApplicationExplorerTabWorkFlow"""  

from ApplicationExplorerTab import ApplicationExplorerTab
import Applicationutility
import Applicationexplorertabutility
import Engineeringclientutility
import Actionutility
import Conditionsutility

class ApplicationExplorerTabWorkFlow:
    """ApplicationExplorerTabWorkFlow"""
    applicationexplorertab_obj = ApplicationExplorerTab()

        
    def textboxtemplatesbrowserapplicationexpandtemplatebrowserae(self,identifiers_list):
        """textboxtemplatesbrowserapplicationexpandtemplatebrowserae"""
        try:
            Applicationexplorertabutility.expand_templates_browser(identifiers_list)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxtemplatesbrowserverifycompositetemplateae(self):
        """textboxtemplatesbrowserverifycompositetemplateae"""
        try:
            Applicationexplorertabutility.check_composite_templates_temp_browser()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxstahlcollapsetemplatebrowserae(self,identifiers_list):
        """textboxstahlcollapsetemplatebrowserae"""
        try:
            Applicationexplorertabutility.collapse_templates_browser(identifiers_list)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxtemplatesbrowserscrolldowntemplatebrowserae(self,count):
        """textboxtemplatesbrowserscrolldowntemplatebrowserae"""
        try:
            Applicationexplorertabutility.click_on_scroll_down_temp_browser(count)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxtemplatesbrowserverifytemplatebrowserae(self):
        """textboxtemplatesbrowserverifytemplatebrowserae"""
        try:
            Applicationexplorertabutility.check_temp_browser_list()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxtemplatesbrowserclosealltabsexceptsystemexplorerec(self):
        """textboxtemplatesbrowserclosealltabsexceptsystemexplorerec"""
        try:
            Engineeringclientutility.close_all_tab_except_Systems_explorer_EC()
            Applicationutility.wait_in_seconds(1000,'wait')
            Applicationexplorertabutility.delete_created_system1_Project_Variable()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxtemplatesbrowsersearchtexttemplatebrowserae(self,search_text):
        """textboxtemplatesbrowsersearchtexttemplatebrowserae"""
        try:
            Applicationexplorertabutility.search_template_browser_AE(search_text)
        except Exception as ex:
           raise Exception(ex) from ex
        
    def textboxtemplatesbrowserdragcompositetemplatedropapplicationbrowsersystem1ae(self,param):
        """textboxtemplatesbrowserdragcompositetemplatedropapplicationbrowsersystem1ae"""
        try:
            Applicationexplorertabutility.drag_composite_template_drop_app_browser_system1_AE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassetworkspacerclickassetworkspacefolderae(self,identifier):
        """textboxassetworkspacerclickassetworkspacefolderae"""
        try:
            Applicationexplorertabutility.right_click_asset_workspace_folder_AE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassetworkspaceselectcontextmenuitemec(self,menu_item):
        """textboxassetworkspaceselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassertworkspaceeditordragtemplateinapplicationbrowserdropassetworkspaceeditorae(self,template):
        """textboxassertworkspaceeditordragtemplateinapplicationbrowserdropassetworkspaceeditorae"""
        try:
            Applicationexplorertabutility.drag_app_browser_drop_asset_workspace_editor_AE(template)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassertworkspaceeditorverifytemplateae(self,template):
        """textboxassertworkspaceeditorverifytemplateae"""
        try:
            Applicationexplorertabutility.verify_Template_node_Asset_Workstation_editor_AE(template)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonnodeinstancelinkfromrangenodetorangenodeae(self,param):
        """buttonnodeinstancelinkfromrangenodetorangenodeae"""
        try:
            Applicationexplorertabutility.Link_from_ranged_node_to_ranged_node(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonnodeinstanceverifylinkstatus(self):
        """buttonnodeinstanceverifylinkstatus"""
        try:
            Applicationexplorertabutility.Verify_Link_Status()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxapplicationbrowserrclickapplicationbrowserfolderae(self,identifier):
        """textboxapplicationbrowserrclickapplicationbrowserfolderae"""
        try:
            Applicationexplorertabutility.right_click_application_browser_folder_AE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxapplicationbrowserrclickapplicationbrowsertemplateae(self,param):
        """textboxapplicationbrowserrclickapplicationbrowsertemplateae"""
        try:
            Applicationexplorertabutility.right_click_application_browser_template_AE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxapplicationbrowserselectcontextmenuitemec(self,menu_item):
        """textboxapplicationbrowserselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def textboxRenameInsatnce(self,Name):
            """textboxapplicationbrowserselectcontextmenuitemec"""
            try:
                Engineeringclientutility.Rename_Insatnce(Name)
            except Exception as ex:
                raise Exception(ex) from ex
        
    def textboxinspectinstancetreeverifyinspectinstancewindowopen(self,name):
        """textboxinspectinstancetreeverifyinspectinstancewindowopen"""
        try:
            Applicationexplorertabutility.verify_inspect_instance_window_name(name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoninspectinstanceokselected(self):
        """applicationexplorertab_obj.inspectinstanceokbutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.inspectinstanceokbutton.click()
        
        
    def textboxinspectinstancewindowcloseinspectinstancewindowae(self):
        """textboxinspectinstancewindowcloseinspectinstancewindowae"""
        try:
            Applicationexplorertabutility.close_inspect_instance()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinspectinstancewindowesckeyboardaction(self):
        """textboxinspectinstancewindowesckeyboardaction"""
        try:
            Actionutility.escape_key_action()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoncreatemultipleinstancecreatesystemandcreateinstance(self):
        """buttoncreatemultipleinstancecreatesystemandcreateinstance"""
        try:
            Conditionsutility.Precondition_TC_EPE_AE_0007()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxidentifierverifyfoldercreated(self,identifier):
        """textboxidentifierverifyfoldercreated"""
        try:
            Applicationexplorertabutility.verify_folder_and_template_application_browser(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxidentifiermotorgp1verifytemplatecreated(self,identifier):
        """textboxidentifiermotorgp1verifytemplatecreated"""
        try:
            Applicationexplorertabutility.verify_folder_and_template_application_browser(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxidentifierdoubleclickontemplate(self,identifier):
        """textboxidentifierdoubleclickontemplate"""
        try:
            Applicationexplorertabutility.double_click_identifier_application_browser(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinstanceeditorverifytemplateinstanceeditor(self,identifier):
        """textboxinstanceeditorverifytemplateinstanceeditor"""
        try:
            Applicationexplorertabutility.verify_application_explorer_instance_editor_tab(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinstanceeditortakeevidence(self):
        """textboxinstanceeditortakeevidence"""
        try:
            Actionutility.take_screenshot(msg="taking screenshot of current screen")
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinstanceeditorchecklistcheckinstanceeditor(self,param):
        """textboxinstanceeditorchecklistcheckinstanceeditor"""
        try:
          Applicationexplorertabutility.template_checkbox(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoninstancedescriptionenterdescriptionae(self):
        """buttoninstancedescriptionenterdescriptionae"""
        try:
            Applicationexplorertabutility.enter_instance_description_AE_instance_editor()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoninstanceeditorsaveselected(self):
        """applicationexplorertab_obj.instanceeditorsavebutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.instanceeditorsavebutton.click()
        
        
    def textboxinstanceeditorclosecloseinstanceeditortab(self,identifier):
        """textboxinstanceeditorclosecloseinstanceeditortab"""
        try:
            Applicationexplorertabutility.application_explorer_instance_editor_tab_close(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxsavechangesdialogboxverifypopupae(self,name):
        """textboxsavechangesdialogboxverifypopupae"""
        try:
            Applicationexplorertabutility.verify_save__changes_popup_AE(name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsavechangesdialogboxyesselected(self):
        """applicationexplorertab_obj.savechangesdialogboxyesbutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.savechangesdialogboxyesbutton.click()
        
        
    def buttonsavechangesdialogboxnoselected(self):
        """applicationexplorertab_obj.savechangesdialogboxnobutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.savechangesdialogboxnobutton.click()
        
        
    def buttonsavechangesdialogboxcancelselected(self):
        """applicationexplorertab_obj.savechangesdialogboxcancelbutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.savechangesdialogboxcancelbutton.click()
        
        
    def textboxcontextmenuverifycontextmenuitems(self):
        """textboxcontextmenuverifycontextmenuitems"""
        try:
            Engineeringclientutility.Verify_ContextMenu_Items()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxverifyinstancevalidity(self):
            try:
                Applicationexplorertabutility.verify_instance_validity()
            except Exception as ex:
                raise Exception(ex) from ex
        
    def textboxwarningpopupwindowverifyinstancelockpopup(self,message):
        """textboxwarningpopupwindowverifyinstancelockpopup"""
#        try:
        Applicationexplorertabutility.Verify_Warning_Popup_locked_instance_AE(message)
#        except Exception as ex:
#            raise Exception(ex) from ex
        
    def buttonaewarningpopupokselected(self):
        """applicationexplorertab_obj.aewarningpopupokbutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.aewarningpopupokbutton.click()
        
        
    def buttoncreatemultipleinstancecreatemultiplefoldersandinstancesae(self):
        """buttoncreatemultipleinstancecreatemultiplefoldersandinstancesae"""
        try:
            Conditionsutility.Create_Multiple_folders_and_Multiple_instances_AE()
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxtemplatesbrowseruncheckallfilterstempbrowserae(self):
        """textboxtemplatesbrowseruncheckallfilterstempbrowserae"""
        try:
            Applicationexplorertabutility.expand_uncheck_all_filters_temp_browser_AE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxapplicationbrowserentered_999(self):
        """applicationexplorertab_obj.applicationbrowsertextbox"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.updateinstanceokbutton.click()
        
    def textboxapplicationbrowserentered(self,applicationBrowser):
        """applicationexplorertab_obj.applicationbrowsertextbox"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.applicationbrowsertextbox.enter_text(applicationBrowser)
        
    def textboximportenterfilelocationandfilenametobeimported(self,file_format):
        """textboximportenterfilelocationandfilenametobeimported"""
        try:
            Applicationexplorertabutility.Enter_systemName_systemlocation_ImportWindow_AE(file_format)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboximportclickonbuttonsinimportsystem1popupae(self,button_name):
        """textboximportclickonbuttonsinimportsystem1popupae"""
        try:
            Applicationexplorertabutility.Import_System1_Popup_AE_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboximportwaitforimportpopup(self):
        """textboximportwaitforimportpopup"""
        try:
            Applicationexplorertabutility.Wait_for_Import_pop_up_AE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonimportdialogclickonbuttonsinimportdialogpopupae(self,button_name):
        """buttonimportdialogclickonbuttonsinimportdialogpopupae"""
        try:
            Applicationexplorertabutility.importdialog_popup_button_AE_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxapplicationbrowserverifytemplateaddedinapplicationbrowserae(self,template_name):
        """textboxapplicationbrowserverifytemplateaddedinapplicationbrowserae"""
        try:
            Applicationexplorertabutility.Verify_latest_template_added_Application_browser_AE(template_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboximportconflictdialogclickonbuttonsinconflictdialogpopup(self,button_name):
        """textboximportconflictdialogclickonbuttonsinconflictdialogpopup"""
        try:
            Applicationexplorertabutility.ConflictWindow_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def textboxapplicationbrowserverifyinstancelockpopup(self,message):
        """textboxapplicationbrowserverifyinstancelockpopup"""
        try:
            Applicationexplorertabutility.Verify_Warning_Popup_locked_instance_AE(message)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttonrelativeradioselected(self):
            """applicationexplorertab_obj.relativeradiobutton"""
            ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.relativeradiobutton.click()
            
            
    def textboxapplicationbrowserclickonbuttonsinpopupwindow(self,button_name):
            """textboxapplicationbrowserclickonbuttonsinpopupwindow"""
            try:
                Applicationexplorertabutility.MessageWindow_buttons(button_name)
            except Exception as ex:
                raise Exception(ex) from ex

    def verifyaeapplicationbrowsertemplate(self,applicationBrowser):
        """applicationexplorertab_obj.applicationbrowsertextbox"""
        Applicationutility.wait_in_seconds(1000, 'wait')
        Applicationexplorertabutility.verify_application_browser_template_AE(applicationBrowser)
        
        
    def buttonspecifictemplatecopyandpasteusingshortcutkeys(self):
        """buttonspecifictemplatecopyandpasteusingshortcutkeys"""
        try:
            Applicationexplorertabutility.TC_EPE_AE_00012_and_TC_EPE_AE_00014()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttonspecifictemplatecopyandpasteusingshortcutkeys_1(self):
        """buttonspecifictemplatecopyandpasteusingshortcutkeys"""
        try:
            Applicationexplorertabutility.TC_EPE_AE_00012_and_TC_EPE_AE_00014_1()
        except Exception as ex:
            raise Exception(ex) from ex
                
    def textboxmotorgptemplateverifydeletewindowae(self,message):
        """textboxmotorgptemplateverifydeletewindowae"""
        try:
            Applicationexplorertabutility.Verify_DeleteMessage_content_AE(message)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxinstanceeditortakeevidence(self):
        """textboxinstanceeditortakeevidence"""
        try:
            Actionutility.take_screenshot(msg="taking screenshot of current screen")
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxmotorgptemplateclicktemplateae(self,param):
        """textboxmotorgptemplateclicktemplateae"""
        try:
            Applicationexplorertabutility.click_application_browser_template_AE(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    
    def textboxmotorgptemplatepressshortkeys(self):
        """textboxmotorgptemplatepressshortkeys"""
        try:
            Actionutility.delete_key_AE()
        except Exception as ex:
            raise Exception(ex) from ex
                
                
    def textboxidentifierdoubleclickontemplate(self,identifier):
        """textboxidentifierdoubleclickontemplate"""
        try:
            Applicationexplorertabutility.double_click_identifier_application_browser(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def textboxwarningpopupwindowclickonbuttonsinpopupwindow(self,button_name):
        """textboxwarningpopupwindowclickonbuttonsinpopupwindow"""
        try:
            Applicationexplorertabutility.MessageWindow_buttons(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def textboxwarningpopupwindowwarningpopupclose(self):
        """textboxwarningpopupwindowwarningpopupclose"""
        try:
            Applicationexplorertabutility.instance_locked_close_AE()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttondeletepopupverifymessagefromnotificationpanelae(self,message_to_verify):
        """buttondeletepopupverifymessagefromnotificationpanelae"""
        try:
            Applicationexplorertabutility.Verify_Notification_Message(message_to_verify)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttoncreatemultipleinstancecreatesystemandcreateinstance(self):
        """buttoncreatemultipleinstancecreatesystemandcreateinstance"""
        try:
            Applicationexplorertabutility.Precondition_TC_EPE_AE_0007()
        except Exception as ex:
            raise Exception(ex) from ex
                
    def expandfoldersystem(self):
        """buttoncreatemultipleinstancecreatesystemandcreateinstance"""
        try:
            Applicationexplorertabutility.expand_folder_system()
        except Exception as ex:
            raise Exception(ex) from ex
                    
    def verifySameNameErrorboxapplicationbrowser(self):
        try:
            Applicationexplorertabutility.verify_SameName_Errorbox_application_browser()
        except Exception as ex:
            raise Exception(ex) from ex
                
    def renameinstancepopupbutton(self,button_1):
        try:
            Applicationexplorertabutility.rename_instance_popup_button(button_1)
        except Exception as ex:
            raise Exception(ex) from ex
                    
    def modaldialogwindowclose(self):
        try:
            Applicationutility.modal_dialog_window_close()
        except Exception as ex:
            raise Exception(ex) from ex
              
    def replacetemplatecomb(self,ReplaceTemplate):
        try:
            Applicationexplorertabutility.replace_template_combo_AE(ReplaceTemplate)
        except Exception as ex:
            raise Exception(ex) from ex
           
    def modaldiawindow(self,Buttonname):
        try:
            Applicationutility.modal_dialog_window_button(Buttonname)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def verifyobject(self,Window):
        try:
            ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.replacetemplatetextbox.verify_object(Window)
        except Exception as ex:
            Log.Warning(Window + ' is not visible on screen.')           
            
    def verifytemplatebrowserinae(self, Template):
        try:  
            Applicationexplorertabutility.verify_template_application_browser(Template)
        except Exception as ex:
            raise Exception(ex) from ex


    def textboxidentifierdoubleclickontemplate(self,identifier):
        """textboxidentifierdoubleclickontemplate"""
        try:
            Applicationexplorertabutility.double_click_identifier_application_browser(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinstanceeditorchecklistcheckinstanceeditor(self,param):
        """textboxinstanceeditorchecklistcheckinstanceeditor"""
        try:
            Applicationexplorertabutility.template_checkbox(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoninstancedescriptionenterdescriptionae(self):
        """buttoninstancedescriptionenterdescriptionae"""
        try:
            Applicationexplorertabutility.enter_instance_description_AE_instance_editor()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoninstanceeditorsaveselected(self):
        """applicationexplorertab_obj.instanceeditorsavebutton"""
        ApplicationExplorerTabWorkFlow.applicationexplorertab_obj.instanceeditorsavebutton.click()
        
        
    def buttoninstanceeditorsaveclickmodaldialogwindow(self,button_name):
        """buttoninstanceeditorsaveclickmodaldialogwindow"""
        try:
            Actionutility.modal_dialog_window_button(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def labelmessagedisplayed(self,content):
        """applicationexplorertab_obj.messagelabel"""
        Applicationutility.screen_displayed()
            
            
    def dragtemplatefromapplicationbrowsertolinkeditor(self,template):
            """dragtemplatefromapplicationbrowsertolinkeditor"""
            try:
                Applicationexplorertabutility.drag_app_browser_drop_asset_workspace_editor_with_POS_AE(template)
            except Exception as ex:
                raise Exception(ex) from ex

                
    def textboxidentifierdoubleclickontemplate(self,identifier):
        """textboxidentifierdoubleclickontemplate"""
        try:
            Applicationexplorertabutility.double_click_identifier_application_browser(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinstanceeditorchecklistcheckinstanceeditor(self,param):
        """textboxinstanceeditorchecklistcheckinstanceeditor"""
        try:
            Applicationexplorertabutility.template_checkbox(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoninstancedescriptionenterdescriptionae(self):
        """buttoninstancedescriptionenterdescriptionae"""
        try:
            Applicationexplorertabutility.enter_instance_description_AE_instance_editor()
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxassertworkspaceeditorremovepvrangedlinkae(self):
        """textboxassertworkspaceeditorremovepvrangedlinkae"""
        try:
            Applicationexplorertabutility.remove_PV_ranged_link_AE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassertworkspaceeditorverifylinktwoinstancesassetworkspace(self):
        """textboxassertworkspaceeditorverifylinktwoinstancesassetworkspace"""
        try:
            Applicationexplorertabutility.Verify_node_link_line_asset_work_AE(param)
        except Exception as ex:
            raise Exception(ex) from ex

    def textboximportemptypagesenterfilelocationandfilenametobeimported(self,file_format):
            """textboximportenterfilelocationandfilenametobeimported"""
            try:
                Applicationexplorertabutility.EmptyPages_ImportWindow_PE(file_format)
            except Exception as ex:
                raise Exception(ex) from ex