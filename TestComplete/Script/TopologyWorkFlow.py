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
            
    def doubleclickcatalogbrowserte(self,main_folder, subfolder, final_item):
        """doubleclickcatalogbrowserte"""
        try:
            Topologyexplorerutility.double_click_selected_catalog_browser_item_TE(main_folder, subfolder, final_item)
        except Exception as ex:
            raise Exception(ex) from ex

        
    def setipandsubnetinstbpropertieste(self, ip_address, subnet_mask):
        """setipandsubnetinstbpropertieste"""
        try:
            Topologyexplorerutility.set_ip_and_subnet(ip_address, subnet_mask)
        except Exception as ex:
            raise Exception(ex) from ex

        
    def configureethernetnetworkinphysicalconnectionte(self, network):
        """configureethernetnetworkinphysicalconnectionte"""
        try:
            Topologyexplorerutility.configure_ethernet_network(network)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def clickbuttontoolbar(self, menu):
        """clickbuttontoolbar"""
        try:
          Applicationutility.wait_in_seconds(2000,'wait')
          Topologyexplorerutility.click_tools_in_topo_configuration(menu)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def clickbuttontoolmenubar(self, menu_item):
        """clickbuttontoolmenubar"""
        try:
          Applicationutility.wait_in_seconds(2000,'wait')
          Topologyexplorerutility.click_menu_item_in_topo_configuration(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def selecttabinhardwarecatalog(self, tabname):
        """selecttabinhardwarecatalog"""
        try:
          Topologyexplorerutility.select_tab_in_topo_config(tabname)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def dblclickpropinhardwarecatalog(self, property):
        """dblclickpropinhardwarecatalog"""
        try:
          Topologyexplorerutility.Dblclick_config_panel_item_TE(property)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def updatebtninhardwarecatalog(self):
        """updatebtninhardwarecatalog"""
        try:
          Topologyexplorerutility.click_update_in_config()
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def selectclosebutton(self):
        """selectclosebutton"""
        try:
          Topologyexplorerutility.close_button_selected()
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def controlexppopup(self, button):
        """controlexppopup"""
        try:
          Topologyexplorerutility.controlexp_popup(button)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def selectbtnplc(self, button):
        """selectbtnplc"""
        try:
          Topologyexplorerutility.select_button_PLC(button)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def selectrackplc(self, number):
        """selectrackplc"""
        try:
          Topologyexplorerutility.select_rack_in_PLC(number)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def hardwarecatalogclosebtn(self, button):
        """controlexppopup"""
        try:
          Topologyexplorerutility.close_hardware_catalog(button)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def bmeselectbtn(self, button):
        """bmeselectbtn"""
        try:
          Topologyexplorerutility.select_button_BME_window(button)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def dblclickinstalledprm(self, item):
        """dblclickinstalledprm"""
        try:
          Topologyexplorerutility.double_click_item_in_DTM(item)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def rightclickinstalledprm(self, item):
        """rightclickinstalledprm"""
        try:
          Topologyexplorerutility.right_click_item_in_DTM(item)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def dblclicksettingsprm(self, item):
        """dblclicksettingsprm"""
        try:
          Topologyexplorerutility.double_click_settings_in_PRM(item)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def updateipaddresinprm(self, ip_address):
        """updateipaddresinprm"""
        try:
          Topologyexplorerutility.update_ip_address(ip_address)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def clickbtninprm(self, button_name):
        """clickbtninprm"""
        try:
          Topologyexplorerutility.click_button_in_prm(button_name)
        except Exception as ex:
            raise Exception(ex) from ex 
        
    def clickbtninnewdevicepopup(self, button_name):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.modaldialogue_window_ce(button_name)
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def selectoptioninmodaldialogue(self, option):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.select_options_in_controlexpert_modaldialogue(option)
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def selectprotocolinadddevice(self, option, device):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.select_protocol_in_add_device(option, device)
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def selectbtninadddeviceprop(self, button):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.select_btn_device_prop(button)
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def clickchannelcheckboxinhart(self, channel):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.click_checkbox_in_hart(channel)
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def validatebtnincontrolconfig(self):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.click_validate_btn_in_control_config()
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def selectipindeployworkstationte(self, ip):
        """selectipindeployworkstationte"""
        try:
          Topologyexplorerutility.select_ip_in_deploy_workstation(ip)
        except Exception as ex:
            raise Exception(ex) from ex 

    def buttonexplorerbuttonte(self,button):
        """textboxtopologyexplorertreemodaldialogwindowselectitem"""
        try:
            Applicationexplorertabutility.Explorer_buttons_TE(button)
        except Exception as ex:
            raise Exception(ex) from ex

