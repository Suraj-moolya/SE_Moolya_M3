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
            Engineeringclientutility.circularprogressbar_Wait(self)
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