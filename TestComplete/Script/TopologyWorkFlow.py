"""TopologyWorkFlow"""  

from Topology import Topology
import Applicationutility
import Engineeringclientutility
import Topologyutility
import Actionutility
import Topologyexplorerutility

class TopologyWorkFlow:
    """TopologyWorkFlow"""
    topology_obj = Topology()

        
    def textboxtopologyexplorertreeselectcontextmenuitemec(self,menu_item):
        """textboxtopologyexplorertreeselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectdropdownselectdeploypopupdropdownvaluete(self,param):
        """textboxprojectdropdownselectdeploypopupdropdownvaluete"""
        try:
            Topologyutility.select_dropdown_value_popup_TE(param)
        except Exception as ex:
            raise Exception(ex) from ex
      
    def textboxbackupdatadescriptionentered(self,backupDataDescription3):
        """topology_obj.backupdatadescriptiontextbox"""
        TopologyWorkFlow.topology_obj.backupdatadescriptiontextbox.enter_text(backupDataDescription3)
        
    def textboxdeploydataselectiongridselectdeploydatafromselectiongridte(self):
        """textboxdeploydataselectiongridselectdeploydatafromselectiongridte"""
        try:
            Topologyutility.select_latest_backup_data_TE()
        except Exception as ex:
            raise Exception(ex) from ex  
            
    def startenginecheckboxclickafterrefineonline(self,param):
        """textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte"""
        try:
            TopologyWorkFlow.topology_obj1.deploycheckbox.click()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def okbuttonclickafterrefineonline(self,param):
        """textboxnewpasswordboxverifyenteredcontrollerpasswordvalidinvalidte"""
        try:
            TopologyWorkFlow.topology_obj1.deployokbutton.click()
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxtopologyexplorertreesearchtemplatebrowserec(self,search_text):
        """textboxtopologyexplorertreesearchtemplatebrowserec"""
        try:
            Topologyexplorerutility.search_template_browser_EC(search_text)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeselecttemplateec(self,param):
        """textboxtopologyexplorertreeselecttemplateec"""
        try:
            Topologyexplorerutility.Select_template_EC (param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreedblclicktemplatete(self,temp_name):
        """textboxtopologyexplorertreedblclicktemplatete"""
        try:
            Topologyexplorerutility.DblClick_template_TE(temp_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeexpandcommunicationtabte(self,val):
        """textboxtopologyexplorertreeexpandcommunicationtabte"""
        try:
            Topologyexplorerutility.Expand_communication_tab_TE(val)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeeditipaddress(self,param):
        """textboxtopologyexplorertreeeditipaddress"""
        try:
            Topologyexplorerutility.edit_IP_Address(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreerclicktemplatete(self,temp_name):
        """textboxtopologyexplorertreerclicktemplatete"""
        try:
            Topologyexplorerutility.RClick_template_TE(temp_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeclickonmenuiteminte(self,menu_option):
        """textboxtopologyexplorertreeclickonmenuiteminte"""
        try:
            Topologyexplorerutility.click_MenuItem_Toolbar(menu_option)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreemodaldialogwindowselectitem(self,val):
        """textboxtopologyexplorertreemodaldialogwindowselectitem"""
        try:
            Actionutility.modal_dialog_windo_selectItem(val)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttonexplorerbuttonte(self,button):
        """textboxtopologyexplorertreemodaldialogwindowselectitem"""
        try:
            Applicationexplorertabutility.Explorer_buttons_TE(button)
        except Exception as ex:
            raise Exception(ex) from ex