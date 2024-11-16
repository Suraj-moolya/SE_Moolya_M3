"""ProjectExplorerTabWorkFlow"""  

from ProjectExplorerTab import ProjectExplorerTab
import Applicationutility
import Projectexplorertabutility
import Engineeringclientutility
import Actionutility
import Applicationexplorertabutility
class ProjectExplorerTabWorkFlow:
    """ProjectExplorerTabWorkFlow"""
    projectexplorertab_obj = ProjectExplorerTab()

        
    def textboxprojectbrowserrclickcontrolprojectbrowser(self,identifier):
        """textboxprojectbrowserrclickcontrolprojectbrowser"""
        try:
            Projectexplorertabutility.right_click_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserselectcontextmenuitemec(self,menu_item):
        """textboxprojectbrowserselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserwaitforexecution(self):
        """textboxprojectbrowserwaitforexecution"""
        try:
            Actionutility.wait_for_execution()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserclickmodaldialogwindow(self,button_name):
        """textboxprojectbrowserclickmodaldialogwindow"""
        try:
            Actionutility.modal_dialog_window_button(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxprojectbrowserselectcontextsubmenuitemte(self,menu_item):
        """textboxprojectbrowserselectcontextsubmenuitemte"""
        try:
            Topologyexplorerutility.select_context_submenu_Items_TE(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserdclickcontrolprojectbroswer(self,identifier):
        """textboxprojectbrowserdclickcontrolprojectbroswer"""
        try:
            Projectexplorertabutility.double_click_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserselectcomboboxvaluepropertiesdockte(self,param):
        """textboxprojectbrowserselectcomboboxvaluepropertiesdockte"""
        try:
            Topologyexplorerutility.select_combobox_TE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxexecutablepropertyexecutablesproperties(self,Identifier_Textvalue):
        """textboxexecutablepropertyexecutablesproperties"""
        try:
            Projectexplorertabutility.Executables_Properties(Identifier_Textvalue)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowsergenerateandbuildcontroller(self):
        """textboxprojectbrowsergenerateandbuildcontroller"""
        try:
            Teststepsutility.Generate_and_build_TC_EPE_AE_0039()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserwaitforexecution(self):
        """textboxprojectbrowserwaitforexecution"""
        try:
            Actionutility.wait_for_execution()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserclosealltabdeletessystem(self):
        """textboxprojectbrowserclosealltabdeletessystem"""
        try:
            Conditionsutility.Post_Conditions_AE()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def assignmentsrightclickunlinkfacets(self, facet_name):
        """assignmentsrightclickunlinkfacets"""
        try:
            Projectexplorertabutility.right_click_instance_in_assignments(facet_name)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def assignmentsunlinkfacets(self, param1):
                """textboxassignmentsrightclickunlinkfacets"""
                try:
                    Projectexplorertabutility.verify_facet_assignment(param1)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def Rclick_fbdsection_select_pasteinstance(self, param1):
                    """Rclick_fbdsection_select_pasteinstance"""
                    try:
                        Projectexplorertabutility.right_click_container_dock_context_menu_item_PE(param1)
                    except Exception as ex:
                        raise Exception(ex) from ex
        
    def click_fbdsection_select_pasteinstance(self, param1):
                        """Rclick_fbdsection_select_pasteinstance"""
                        try:
                            Projectexplorertabutility.click_FBDsection(param1)
                        except Exception as ex:
                            raise Exception(ex) from ex
                            
    def copyfromfbdinstancepastefbd(self, param1):
                        """Rclick_fbdsection_select_pasteinstance"""
                        try:
                            Projectexplorertabutility.copy_fromfbd_instance_pastefbd(param1)
                        except Exception as ex:
                            raise Exception(ex) from ex
                                                
                    
    def textboxcontainerdockrightclickcontainerdockcontextmenuitempe(self,param):
        """textboxcontainerdockrightclickcontainerdockcontextmenuitempe"""
        try:
            Projectexplorertabutility.right_click_container_dock_context_menu_item_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockclickmodaldialogwindow(self,button_name):
        """textboxcontainerdockclickmodaldialogwindow"""
        try:
            Actionutility.modal_dialog_window_button(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockverifysectiondeletedincontrolprojectcontainers(self,identifier):
        """textboxcontainerdockverifysectiondeletedincontrolprojectcontainers"""
        try:
            Projectexplorertabutility.Verify_Section_Deleted_in_ControlProject_containers(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockdeletesectionincontrolprojectbyusingkeyboardactionspe(self,identifier):
        """textboxcontainerdockdeletesectionincontrolprojectbyusingkeyboardactionspe"""
        try:
            Projectexplorertabutility.Delete_Section_in_ControlProject_by_Keyboard_actions_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def textboxcontainerdockclickoncontainersectionpe(self,identifier):
        """textboxcontainerdockclickoncontainersectionpe"""
        try:
            Projectexplorertabutility.click_on_section_container_dock_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassignmentsdockdraganddropfacetfromassignmenttocontainersectionspe(self,param):
        """textboxassignmentsdockdraganddropfacetfromassignmenttocontainersectionspe"""
        try:
            Projectexplorertabutility.select_facet_drag_drop_section_dock_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassignmentsdockrightclickcontainerdockcontextmenuitempe(self,param):
        """textboxassignmentsdockrightclickcontainerdockcontextmenuitempe"""
        try:
            Projectexplorertabutility.right_click_container_dock_context_menu_item_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassignmentsdockwaitforexecution(self):
        """textboxassignmentsdockwaitforexecution"""
        try:
            Actionutility.wait_for_execution()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassignmentsdockverifygenerationstatusoffacetfromassignmentspe(self,param):
        """textboxassignmentsdockverifygenerationstatusoffacetfromassignmentspe"""
        try:
            Projectexplorertabutility.verify_facet_assignment(param)
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxcontainerdockrightclickcontainerdockcontextmenuitempe(self,param):
        """textboxcontainerdockrightclickcontainerdockcontextmenuitempe"""
        try:
            Projectexplorertabutility.right_click_container_dock_context_menu_item_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockselectcontextmenuitemec(self,menu_item):
        """textboxcontainerdockselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockverifyactionmessageinnotificationpannel(self,message):
        """textboxcontainerdockverifyactionmessageinnotificationpannel"""
        try:
            Applicationexplorertabutility.Verify_Notification_pannel_Message(message)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def labelmessagedisplayed(self,content):
        """projectexplorertab_obj.messagelabel"""
        Applicationutility.screen_displayed()
        
    def textboxprojectbrowserrclickcontrolprojectbrowser(self,identifier):
        """textboxprojectbrowserrclickcontrolprojectbrowser"""
        try:
            Projectexplorertabutility.right_click_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserclickmodaldialogwindow(self,button_name):
        """textboxprojectbrowserclickmodaldialogwindow"""
        try:
            Actionutility.modal_dialog_window_button(button_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowsercustomizecpbheadercheckboxpe(self,param):
        """textboxprojectbrowsercustomizecpbheadercheckboxpe"""
        try:
            Projectexplorertabutility.customize_CP_header_checkbox_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserclickpopupbuttonobject(self,param):
        """textboxprojectbrowserclickpopupbuttonobject"""
        try:
            Actionutility.Click_popup_button(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserverifyheadercontrolprojectbrowserpe(self,header_name):
        """textboxprojectbrowserverifyheadercontrolprojectbrowserpe"""
        try:
            Projectexplorertabutility.verify_added_headder_CPB_PE(header_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserverifycontextmenuitem(self,menu_item):
        """textboxprojectbrowserverifycontextmenuitems"""
        try:
            Engineeringclientutility.Verify_ContextMenu_Item(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserexpandcontrolprojectbrowserpe(self,identifier):
        """textboxprojectbrowserexpandcontrolprojectbrowserpe"""
        try:
            Projectexplorertabutility.expand_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserverifybuildstateofcontrolexecutablepe(self,param):
        """textboxprojectbrowserverifybuildstateofcontrolexecutablepe"""
        try:
            Projectexplorertabutility.Verify_build_state_control_executeable_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
    
    def buttoncloseselected(self):
        """newfeature_obj.closebutton"""
        ProjectExplorerTabWorkFlow.projectexplorertab_obj.closebutton.click()
    
    def textboxrefineonlinewindowentered(self):
        """refineoffline_obj.refineonlinewindowtextbox"""
        ProjectExplorerTabWorkFlow.projectexplorertab_obj.refineonlinewindowtextbox.verify_object('Refine Offline')
    
    def textboxprojectbrowserrCPB(self,projectBrowser2):
        """textboxprojectbrowserrclickcontrolprojectbrowser"""
        try:
            Projectexplorertabutility.Rclick_CP_header_context_menu_PE(projectBrowser2)
        except Exception as ex:
            raise Exception(ex) from ex

    def rightclickinstanceselectactioninassignments(self,facet_name, action):
            """rightclickinstanceselectactioninassignments"""
            try:
                Projectexplorertabutility.right_click_instance_select_action_in_assignments(facet_name, action)
            except Exception as ex:
                raise Exception(ex) from ex
                
                
    def verifyassignmentsstatus(self,facet_name, status):
                """verifyassignmentsstatus"""
                try:
                    Projectexplorertabutility.verify_assignment(facet_name, status)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def projectexplorertabutilityverifyallfacetgenerationstatusassignmentdock(self):
            """textboxassignmentsdockverifygenerationstatusoffacetfromassignmentspe"""
            try:
                Projectexplorertabutility.verify_all_facet_generation_status_assignmentdock()
            except Exception as ex:
                raise Exception(ex) from ex                

    def projectexplorertabutility_verify_section_containers_dock(self):
                """projectexplorertabutilityverifysectioncontainersdock"""
                try:
                    Projectexplorertabutility.verify_section_containers_dock()
                except Exception as ex:
                    raise Exception(ex) from ex
                   
    
    def textboxprojectbrowsercollapsecontrolprojectbrowserpe(self):
        """textboxprojectbrowsercollapsecontrolprojectbrowserpe"""
        try:
            Projectexplorertabutility.Collapse_control_project_browser_PE()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserexpandcontrolprojectbrowserpe(self,identifier):
        """textboxprojectbrowserexpandcontrolprojectbrowserpe"""
        try:
            Projectexplorertabutility.expand_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserdclickcontrolprojectbroswer(self,identifier):
        """textboxprojectbrowserdclickcontrolprojectbroswer"""
        try:
            Projectexplorertabutility.double_click_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowsercontrolexecutabledropdownpe(self,param):
        """textboxprojectbrowsercontrolexecutabledropdownpe"""
        try:
            Projectexplorertabutility.control_executeable_combo_box_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxassignmentsdockrightclickfacetfromassignmentdockpe(self,facet_name):
        """textboxassignmentsdockrightclickfacetfromassignmentdockpe"""
        try:
            Projectexplorertabutility.right_click_instance_in_assignments(facet_name)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassignmentsdockselectcontextsubmenuec(self,menu_item):
        """textboxassignmentsdockselectcontextsubmenuec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxassignmentsdockverifyfacetsaddedorremovedcontextmenupe(self,facet_name):
        """textboxassignmentsdockverifyfacetsaddedorremovedcontextmenupe"""
        try:
            Projectexplorertabutility.Verify_Facets_Added_or_Removed_context_menu_PE(facet_name)
        except Exception as ex:
            raise Exception(ex) from ex

