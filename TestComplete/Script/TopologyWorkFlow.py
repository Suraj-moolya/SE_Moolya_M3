"""TopologyWorkFlow"""  

from Topology import Topology
import Applicationutility
import Engineeringclientutility
import Topologyutility
import Actionutility
import Topologyexplorerutility
from SystemExplorerScreen import SystemExplorerScreen
from ControlExpert import ControlExpert

class TopologyWorkFlow:
    """TopologyWorkFlow"""
    topology_obj = Topology()
    ses_obj = SystemExplorerScreen()
    con_obj = ControlExpert()
        
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
            Topologyutility.search_template_browser_EC(search_text)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeselecttemplateec(self,param):
        """textboxtopologyexplorertreeselecttemplateec"""
        try:
            Topologyutility.Select_template_EC(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreedblclicktemplatete(self,temp_name):
        """textboxtopologyexplorertreedblclicktemplatete"""
        try:
            Topologyutility.DblClick_template_TE(temp_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeexpandcommunicationtabte(self,val):
        """textboxtopologyexplorertreeexpandcommunicationtabte"""
        try:
            Topologyutility.Expand_communication_tab_TE(val)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreeeditipaddress(self,param):
        """textboxtopologyexplorertreeeditipaddress"""
        try:
            Topologyutility.edit_IP_Address(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorertreerclicktemplatete(self,temp_name):
        """textboxtopologyexplorertreerclicktemplatete"""
        try:
            Topologyutility.RClick_template_TE(temp_name)
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
            
    def textboxtopologyexplorerdoubleclickonaddwindow(self,property):
        """textboxtopologyexplorerhardwarecatalogdevices"""
        try:
            Topologyexplorerutility.Double_Click_on_Channel(property)
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
            
    def textboxtopologyexplorerhardwarecatalogdevices(self,smp):
        """textboxtopologyexplorerhardwarecatalogdevices"""
        try:
            Topologyutility.Verify_Device_Hardware_Catalog_TE(smp)
        except Exception as ex:
            raise Exception(ex) from ex

    def rightclickcontroller(self, item):
            """rightclickinstalledprm"""
            try:
              Topologyexplorerutility.rclickController(item)
            except Exception as ex:
                raise Exception(ex) from ex
            
    def opennetworksfolder(self, node):
            """opennetworksfolder"""
            try:
              Topologyexplorerutility.open_networks_folder(node)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def opennetwork(self, ethernet):
                """opennetwork"""
                try:
                  Topologyexplorerutility.open_ethernetnetwork(ethernet)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def verifynetworkpanel(self, interface, controller):
                    """verifynetworkpanel"""
                    try:
                      Topologyexplorerutility.network_panel(interface, controller)
                    except Exception as ex:
                        raise Exception(ex) from ex
                    
    def textboxtopologyexplorerhardwarecatalogdevices(self,smp):
        """textboxtopologyexplorerhardwarecatalogdevices"""
        try:
            Topologyutility.Verify_Device_Hardware_Catalog_TE(smp)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorerdoubleclickonftdconfigurationwindow(self,property):
        """textboxtopologyexplorerdoubleclickonftdconfigurationwindow"""
        try:
            Topologyexplorerutility.double_click_on_ftdconfiguration_window(property)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorerselectslotinftdconfigurationwindow(self,slot, module):
        """textboxtopologyexplorerdoubleclickonftdconfigurationwindow"""
        try:
            Topologyexplorerutility.select_slots_in_ftdconfiguration(slot, module)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorerclickbuttoninfigurationwindow(self, button):
        """textboxtopologyexplorerclickbuttoninfigurationwindow"""
        try:
            Topologyexplorerutility.Click_button_in_ftdconfiguration(button)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxtopologyexplorerverifydtmdeviceinfigurationwindow(self):
        """textboxtopologyexplorerverifydtmdeviceinfigurationwindow"""
        try:
            Topologyexplorerutility.verify_dtm_device()
        except Exception as ex:
            raise Exception(ex) from ex    
        
    def selectsubmenuoptioninmodaldialogue(self, option):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.select_submenu_options_in_controlexpert_modaldialogue(option)
        except Exception as ex:
            raise Exception(ex) from ex  
        
    def selectfinaloptioninmodaldialogue(self, option):
        """clickbtninnewdevicepopup"""
        try:
          Topologyexplorerutility.select_final_option_in_controlexpert_modaldialogue(option)
        except Exception as ex:
            raise Exception(ex) from ex    
            
    def importmodulesinftdconfigwindow(self, modules):
        """importmodulesinftdconfigwindow"""
        try:
            Topologyexplorerutility.import_modules_in_ftdconfig(modules)
        except Exception as ex:
            raise Exception(ex) from ex  
            
    def clickbuttoninftdconfigwindow(self, button):
        """clickbuttoninftdconfigwindow"""
        try:
            Topologyexplorerutility.click_button_in_fdtconfig(button)
        except Exception as ex:
            raise Exception(ex) from ex 
            
    def clickchannelinftdconfigwindow(self, property):
        """clickchannelinftdconfigwindow"""
        try:
            Topologyexplorerutility.click_dtm_channel_in_fdtconfig(property)
        except Exception as ex:
            raise Exception(ex) from ex  
            
    def selecttabinftdconfigwindow(self, tab_name):
        """selecttabinftdconfigwindow"""
        try:
            Topologyexplorerutility.select_tab_in_FDTConfig(tab_name)
        except Exception as ex:
            raise Exception(ex) from ex   
            
    def updateipinftdconfigwindow(self, ip):
        """updateipinftdconfigwindow"""
        try:
            Topologyexplorerutility.update_ip_address_in_fdtconfig(ip)
        except Exception as ex:
            raise Exception(ex) from ex   
            
    def clickcheckboxinupdateprojectwindow(self, prop):
        """updateipinftdconfigwindow"""
        try:
            Topologyexplorerutility.select_checkbox_in_updateproject(prop)
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxconfirmpasswordboxentercontrollerpassworddeployscreente(self,password):
            """textboxconfirmpasswordboxentercontrollerpassworddeployscreente"""
            try:
                Topologyutility.Enter_Controller_Password_deploy_screen_TE(password)
            except Exception as ex:
                raise Exception(ex) from ex

    def dblclickpropertiesworkstation(self,text):
        """dblclickpropertiesworkstation"""
        try:
            Topologyutility.DBlClick_Properties_workstation(text)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def expandpropertiesworkstation(self,text):
        """expandpropertiesworkstation"""
        try:
            Topologyutility.Expand_Properties_workstation(text)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def changeportnumberworkstation(self,text):
        """expandpropertiesworkstation"""
        try:
            Topologyutility.change_port_number_workstation_TE(text)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def rightclickonprojectbrowserpane(self,item):
        """expandpropertiesworkstation"""
        try:
            Topologyexplorerutility.Right_Click_ProjectBrowser(item)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def selecttabonprojectbrowserproperties(self,item):
        """selecttabonprojectbrowserproperties"""
        try:
            Topologyexplorerutility.Select_Tab_in_Project_Properties(item)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def setoldpasswordandnewpasswordinmodifypassworddialogue(self,op, np):
        """selecttabonprojectbrowserproperties"""
        try:
            Topologyexplorerutility.Set_Password_for_Firmware(op, np)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxsystemprojectrightclickselectedprojectbrowseritemce(self,param):
        """textboxsystemprojectrightclickselectedprojectbrowseritemce"""
        try:
            Controlexpertutility.Right_click_selected_project_browser_item_CE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxsystemprojectclickmenuitemtoolbarce(self,menu_option):
        """textboxsystemprojectclickmenuitemtoolbarce"""
        try:
            Controlexpertutility.click_MenuItem_Toolbar_CE(menu_option)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxsystemprojectselectnetworkce(self,menu_option):
        """textboxsystemprojectselectnetworkce"""
        try:
            Controlexpertutility.Select_network_CE(menu_option)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxoutputwindowpanelverifyerrormessagesinconsole(self,text):
            """textboxoutputwindowpanelverifyerrormessagesinconsole"""
            try:
                Topologyutility.Verify_error_messages_in_Console(text)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def textboxconfirmpasswordboxentercontrollerpassworddeployscreente(self,password):
        """textboxconfirmpasswordboxentercontrollerpassworddeployscreente"""
#       try:
        Topologyutility.Enter_Controller_Password_deploy_screen_TE(password)
#       except Exception as ex:
#         raise Exception(ex) from ex

    def textboxnewpasswordboxentercontrollerpasswordte(self,param):
                """textboxnewpasswordboxentercontrollerpasswordte"""
                try:
                    Topologyexplorerutility.Enter_Controller_Password_TE(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def checkboxcheckautomaticblocking(self):
                """textboxnewpasswordboxentercontrollerpasswordte"""
                try:
                    TopologyWorkFlow.topology_obj.CheckAutomaticBlocking.object.Click()
                except Exception as ex:
                    raise Exception(ex) from ex