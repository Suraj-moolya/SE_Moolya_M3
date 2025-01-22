"""GlobalTemplatesTabWorkFlow"""  

from GlobalTemplatesTab import GlobalTemplatesTab
import Applicationutility
import Globaltemplatesutility
import Engineeringclientutility
class GlobalTemplatesTabWorkFlow:
    """GlobalTemplatesTabWorkFlow"""
    globaltemplatestab_obj = GlobalTemplatesTab()

        
    def textboxglobaltemplatesearchsearchtextandselectgte(self,param):
        """textboxglobaltemplatesearchsearchtextandselectgte"""
        try:
            Globaltemplatesutility.search_and_double_click_search_text_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplatecorerightclickonthesearchedtemplategte(self,param):
        """textboxglobaltemplatecorerightclickonthesearchedtemplategte"""
        try:
            Globaltemplatesutility.rclick_idedntifier_explorer_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplatecoreselectcontextmenuitemec(self,menu_item):
        """textboxglobaltemplatecoreselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonokduuplicateselected(self):
        """globaltemplatestab_obj.okduuplicatebutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.okduuplicatebutton.click()
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.duplicatewindowtextbox.wait_for_object_disapear()
        
        
    def textboxduplicatewindowwaitforobjectdisapear(self,):
        """textboxduplicatewindowwaitforobjectdisapear"""
        try:
            undefined
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplatecorewaitforcircularprogressbar(self):
        """textboxglobaltemplatecorewaitforcircularprogressbar"""
        try:
            Engineeringclientutility.circularprogressbar_Wait()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttontoolboxselected(self):
        """globaltemplatestab_obj.toolboxbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.toolboxbutton.click()
        
        
    def textboxtoolbooxtabledraganddroptoolboxitemcompositeeditorgte(self,name):
        """textboxtoolbooxtabledraganddroptoolboxitemcompositeeditorgte"""
        try:
            Globaltemplatesutility.drag_toolbox_item_drop_composite_editor_GTE(name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsaveascompositeeditorselected(self):
        """globaltemplatestab_obj.saveascompositeeditorbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.saveascompositeeditorbutton.click()
        
        
    def textboxdescriptionentered(self,description7):
        """globaltemplatestab_obj.descriptiontextbox"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.descriptiontextbox.enter_text(description7)
        
    def buttonsaveselected(self):
        """globaltemplatestab_obj.savebutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.savebutton.click()
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.savebutton.wait_for_object_disapear()
        
    def buttoncancelselected(self):
        """globaltemplatestab_obj.cancelbutton"""
        Applicationutility.modal_dialog_window_button('Cancel')
        
    def buttonsaveselected1(self):
            """globaltemplatestab_obj.savebutton"""
            GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.savebutton.click()
            
            
    def closeduuplicateselected(self):
        """globaltemplatestab_obj.okduuplicatebutton"""    
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.duplicatewindowtextbox.object.Close()
        
        
    def verify_dup_win(self):
       try:
          win = GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.duplicatewindowtextbox
          if win:
            Log.Message('The Duplicate window is open')
       except:
          Log.Checkpoint('The duplicate window is closed')
               
    def verifytittlebar(self, tabname):
        """verifytittlebar"""
        try:
            Globaltemplatesutility.verify_title_bar(tabname)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesearchsearchtextandrightclickgte(self,param):
        """textboxglobaltemplatesearchsearchtextandselectgte"""
        try:
            Globaltemplatesutility.search_and_right_click_search_text_GTE(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplateselecttabgte(self,param):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.select_tab_in_gtw(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatedraganddroptoolsgte(self,param):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.drag_and_drop_toolbox_to_window(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesaveaswindowclickbuttongte(self,param):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.click_item_in_save_as_window(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesaveaswindownameandversiongte(self, name, version):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.change_template_name_and_version(name, version)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxglobaltemplatesaveaswindowndescgte(self, desc):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.description_for_save_as_window(desc)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonnextselected(self, button):
        """globaltemplatestab_obj.buttonnextselected"""
        try:
            Globaltemplatesutility.panel_button_gtw(button)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonbrowseselected(self):
        """globaltemplatestab_obj.buttonbrowseselected"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.browsebuttonselected.click()
        
    def buttonaddselected(self, elem):
        """globaltemplatestab_obj.buttonaddselected"""
        try:
            Globaltemplatesutility.click_add_icon_gtw(elem)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxglobaltemplateexpandpropertiesgte(self, elem):
        """globaltemplatestab_obj.buttonaddselected"""
        try:
            Globaltemplatesutility.expand_librarys_in_gtw(elem)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplateselecttaggte(self, desc):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.select_tag_gtw(desc)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplatedraganddropgeniegte(self, prop):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.drag_and_drop_genie_to_genie_facet_in_gtw(prop)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplateclicklibrarygte(self, prop):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.click_library_in_gtw(prop)
        except Exception as ex:
            raise Exception(ex) from ex 
    
    def textboxglobaltemplaterightclickcreatedtemplategte(self, prop):
        """textboxglobaltemplateselecttabgte"""
        try:
            Globaltemplatesutility.right_click_created_template_gtw(prop)
        except Exception as ex:
            raise Exception(ex) from ex 
            
    def GTimportfilenamefilelocation(self, path, folder, file):
        """GTimportfilenamefilelocation"""
        try:
            Globaltemplatesutility.GlobalTemplates_Import(path, folder, file)
        except Exception as ex:
            raise Exception(ex) from ex
                ##
    def rclickcontroltemplateheader(self):
        """globaltemplatestab_obj.controltemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.controltemplateheader.right_click()
        
    def rclickmotortemplateheader(self):
        """globaltemplatestab_obj.motortemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.motortemplateheader.right_click()
        
    def rclicklogictemplateheader(self):
        """globaltemplatestab_obj.controltemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.logictemplateheader.right_click()
        
    def clicktemplatizerbutton(self):
        """globaltemplatestab_obj.templatizerbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.templatizerbutton.click()
        
    def clickopencontrolparticipantbutton(self):
        """globaltemplatestab_obj.opencontrolparticipantbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.opencontrolparticipantbutton.click()
        
    def rclicksupervisiontemplateheader(self):
        """globaltemplatestab_obj.supervisiontemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.supervisiontemplateheader.right_click()
        
    def rclickgeniestemplateheader(self):
        """globaltemplatestab_obj.geniestemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.geniestemplateheader.right_click()
        
    def rclickpumprightgenietemplateheader(self):
        """globaltemplatestab_obj.pumprightgenietemplateheader"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.pumprightgenietemplateheader.right_click()
        
    def clickfittocontentbutton(self):
        """globaltemplatestab_obj.fittocontentbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.fittocontentbutton.click()
        
    def clickopenparticipantbutton(self):
        """globaltemplatestab_obj.opencontrolparticipantbutton"""
        GlobalTemplatesTabWorkFlow.globaltemplatestab_obj.openparticipantbutton.click()
    
        