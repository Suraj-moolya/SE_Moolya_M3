"""TopologyWorkFlow"""  

from Topology import Topology
import Applicationutility
import Engineeringclientutility
import Topologyutility

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
            
    def checkboxstartenginecheckbox(self):
        """checkboxstartenginecheckbox"""
        TopologyWorkFlow.topology_obj.startenginecheckbox.click()