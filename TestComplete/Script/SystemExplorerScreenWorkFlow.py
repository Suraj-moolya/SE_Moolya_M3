"""SystemExplorerScreenWorkFlow"""  

from SystemExplorerScreen import SystemExplorerScreen
import Applicationutility
import Engineeringclientutility
import Systemserverutility
import Actionutility
class SystemExplorerScreenWorkFlow:
    """SystemExplorerScreenWorkFlow"""
    systemexplorerscreen_obj = SystemExplorerScreen()

        
    def buttonprogressbarverifytopologyinitialized(self):
        """buttonprogressbarverifytopologyinitialized"""
        try:
            Engineeringclientutility.verify_Topology_Initiated()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorernoderightclickonnodes(self,node_name):
        """buttonsystemexplorernoderightclickonnodes"""
        try:
            Engineeringclientutility.clickR_node_SE(node_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonfromrclickmenuitemsverifycontextmenuitems(self):
        """buttonfromrclickmenuitemsverifycontextmenuitems"""
        try:
            Engineeringclientutility.Verify_ContextMenu_Items()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoncreatefolderselected(self):
        """systemexplorerscreen_obj.createfolderbutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.createfolderbutton.click()
        
        
    def buttonsystemexplorernodeverifysystemandfoldercreated(self):
        """buttonsystemexplorernodeverifysystemandfoldercreated"""
        try:
            Engineeringclientutility.verify_system_folder()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonwhichiscreatedlatestrclickonfolder(self):
        """buttonwhichiscreatedlatestrclickonfolder"""
        try:
            Engineeringclientutility.clickR_Folder()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoncreatesystemselected(self):
        """systemexplorerscreen_obj.createsystembutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.createsystembutton.click()
        Engineeringclientutility.no_password_system('OK')
        
        
    def buttontocompletewaitforcircularprogressbar(self):
        """buttontocompletewaitforcircularprogressbar"""
        try:
            Engineeringclientutility.circularprogressbar_Wait()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorernodecreatesystemandverifycontextmenu(self,):
        """buttonsystemexplorernodecreatesystemandverifycontextmenu"""
        try:
            Engineeringclientutility.create_system_1_timestamp_and_verify_context_menu_items_()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystem1folderselected(self):
        """systemexplorerscreen_obj.system_1folderbutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.system_1folderbutton.click()
        
        
    def textboxmaintoolbarnavigatetoexplorers(self,Explorername):
        """textboxmaintoolbarnavigatetoexplorers"""
        try:
            Systemserverutility.navigate_to_explorers(Explorername)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxexplorertabverifytabs(self,TabName):
        """textboxexplorertabverifytabs"""
        try:
          Systemserverutility.verify_explorer_tab(TabName)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorercanvasselected(self):
        """systemexplorerscreen_obj.systemexplorercanvasbutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.systemexplorercanvasbutton.click()
        
        
    def textboxwarningpopupverifyexplorerwarningmessage(self,MessageBox):
        """textboxwarningpopupverifyexplorerwarningmessage"""
        try:
            Engineeringclientutility.verify_explorer_warning_message(MessageBox)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonpopupokselected(self):
        """systemexplorerscreen_obj.popupokbutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.popupokbutton.click()
        
        
    def buttonpopupclosepewarning(self):
        """buttonpopupclosepewarning"""
        try:
            Engineeringclientutility.explorer_popup_close()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonopenprojectselected(self):
        """systemexplorerscreen_obj.openprojectbutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.openprojectbutton.click()
        
        
    def textboxpressshortcutkeysclickonshortcutkeys(self,Explorer_Name):
        """textboxpressshortcutkeysclickonshortcutkeys"""
        try:
            Actionutility.explorer_shortcut_key(Explorer_Name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorermenuselected(self):
        """systemexplorerscreen_obj.systemexplorermenubutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.systemexplorermenubutton.click()
        
        
    def buttonopenapplicationselected(self):
        """systemexplorerscreen_obj.openapplicationbutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.openapplicationbutton.click()
        
        
    def buttonsystemexplorernodeclickonnodes(self,node_name):
        """buttonsystemexplorernodeclickonnodes"""
        try:
            Engineeringclientutility.click_node_SE(node_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonopentopologyselected(self):
        """systemexplorerscreen_obj.opentopologybutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.opentopologybutton.click()
        
        
    def buttonrenameselected(self):
        """systemexplorerscreen_obj.renamebutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.renamebutton.click()
        
        
    def buttonforselectedfolderverifyfolderhasenterededitingfield(self,nodename):
        """buttonforselectedfolderverifyfolderhasenterededitingfield"""
        try:
            Engineeringclientutility.Verify_Folder_editable(nodename)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxasperrequirementrenamefolder(self,Foldername):
        """textboxasperrequirementrenamefolder"""
        try:
            Engineeringclientutility.Rename_Folder(Foldername)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonasperrequirementverifyfolderrenamed(self):
        """buttonasperrequirementverifyfolderrenamed"""
        try:
            Engineeringclientutility.Verify_Folder_Renamed()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorernodecreatesystem1(self):
        """buttonsystemexplorernodecreatesystem1"""
        try:
            Engineeringclientutility.create_system_1_timestamp()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonopenapplicationselectsystem1applicationexplorer(self):
        """buttonopenapplicationselectsystem1applicationexplorer"""
        try:
            Engineeringclientutility.select_system_1_application_explorer()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxpressshortcutkeysclickonenter(self):
        """textboxpressshortcutkeysclickonenter"""
        try:
            Engineeringclientutility.Keyboard_action_Enter()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorernodeselected(self):
        """systemexplorerscreen_obj.systemexplorernodebutton"""
        SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.systemexplorernodebutton.click()
        Applicationutility.wait_in_seconds(2000, 'wait')
        
    def buttonsystemexplorernodecreatesystemandcontextmenu(self):
        """buttonsystemexplorernodecreatesystemandcontextmenu"""
        try:
            Engineeringclientutility.create_system_1_timestamp_and_verify_context_menu_items_()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsystemexplorerbrowse(self):
        """systemexplorerscreen_obj.systemexplorernodebutton"""
        try:
            Systemserverutility.browsebutton_backup()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttoncreatesystemselectedwithpassword(self):
                """systemexplorerscreen_obj.createsystembutton"""
                SystemExplorerScreenWorkFlow.systemexplorerscreen_obj.createsystembutton.click()
        
        