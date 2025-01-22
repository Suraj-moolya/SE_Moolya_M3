"""ProjectExplorerTabWorkFlow"""  

from GlobalTemplatesTab import GlobalTemplatesTab
from ProjectExplorerTab import ProjectExplorerTab
import Applicationutility
import Projectexplorertabutility
import Engineeringclientutility
import Actionutility
import Applicationexplorertabutility
import Controlexpertutility

class ProjectExplorerTabWorkFlow:
    """ProjectExplorerTabWorkFlow"""
    projectexplorertab_obj = ProjectExplorerTab()
    globaltemplatestab_obj = GlobalTemplatesTab()

        
    def textboxprojectbrowserrclickcontrolprojectbrowser(self,identifier):
        """textboxprojectbrowserrclickcontrolprojectbrowser"""
        try:
            Projectexplorertabutility.right_click_control_project_browser_PE2(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserselectcontextmenuitemec(self,menu_item):
        """textboxprojectbrowserselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def textboxprojectbrowserselectcontextsubmenuitemec(self,menu_item):
            """textboxprojectbrowserselectcontextsubmenuitemec"""
            try:
                Engineeringclientutility.select_Context_SubMenu_Items_EC(menu_item)
            except Exception as ex:
                raise Exception(ex) from ex 
                
    def textboxprojectbrowserrename(self,controller):
                """textboxprojectbrowserrename"""
                try:
                    Projectexplorertabutility.rename(controller)
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
            
    def assignmentsrightclickunlinkfacets(self, facet_name,action):
        """assignmentsrightclickunlinkfacets"""
        try:
            Projectexplorertabutility.right_click_instance_select_action_in_assignments(facet_name,action)
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
            Applicationutility.wait_for_execution()
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
        #try:
        Projectexplorertabutility.right_click_container_dock_context_menu_item_PE(param)
        #except Exception as ex:
            #raise Exception(ex) from ex
        
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
        Applicationutility.wait_in_seconds(2000,'wait')
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

    def rightclickinstanceselectactioninassignments(self,param, action):
            """rightclickinstanceselectactioninassignments"""
            try:
                Projectexplorertabutility.right_click_instance_select_action_in_assignments(param, action)
            except Exception as ex:
                raise Exception(ex) from ex
                
                
    def verifyassignmentsstatus(self,facet_name, status):
                """verifyassignmentsstatus"""
                try:
                    Projectexplorertabutility.verify_assignment(facet_name, status)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def projectexplorertabutilityverifyallfacetgenerationstatusassignmentdock(self):
            """projectexplorertabutilityverifyallfacetgenerationstatusassignmentdock"""
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
            
    def projectexplorertabutility_Create_Multiple_section_Containers_Dock_verify(self,param):
      """projectexplorertabutilityverifysectioncontainersdock"""
      try:
        Projectexplorertabutility.Create_Multiple_section_Containers_Dock_verify(param)
      except Exception as ex:
        raise Exception(ex) from ex
        
    def projectexplorertabutility_Drag_instance_drop_container_section(self,param):
      """projectexplorertabutilityverifysectioncontainersdock"""
      try:
        Projectexplorertabutility.Drag_instance_drop_container_section(param)
      except Exception as ex:
        raise Exception(ex) from ex

    def createfbdsections(self,num_sections):
                """createfbdsections"""
                try:
                    Projectexplorertabutility.create_fbd_section(num_sections)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def draganddropfromcontainertosection(self, controller, section):
      """draganddropfromcontainertosection"""
      try:
          Projectexplorertabutility.multidraganddrop(controller, section)
      except Exception as ex:
          raise Exception(ex) from ex
          
    def rightclickinstanceandperformaction(self, facet_name, action):
      """rightclickinstanceandperformaction"""
      try:
          Projectexplorertabutility.right_click_instance_select_action_in_assignments(facet_name, action)
      except Exception as ex:
          Log.Error(f"Error while performing right click and action: {ex}")
          raise Exception(ex) from ex
          
    def verifyassignmentsstate(self,facet_names, generation_state):
                    """verifyassignmentsstate"""
                    try:
                        Projectexplorertabutility.verify_facet_assignment_state1(facet_names, generation_state)
                    except Exception as ex:
                        raise Exception(ex) from ex
                        
    def doubleclickinstanceinassignments(self,facet_name):
                """doubleclickinstanceinassignments"""
                try:
                    Projectexplorertabutility.double_click_instance_in_assignments(facet_name)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def clickcheckboxininstanceedittor(self,instance_name):
                    """clickcheckboxininstanceedittor"""
                    try:
                        Projectexplorertabutility.click_checkbox_in_instance_editor(instance_name)
                    except Exception as ex:
                        raise Exception(ex) from ex
                        
    def savebuttoninstanceeditor(self,button_name):
            """savebuttoninstanceeditor"""
            try:
                Projectexplorertabutility.saveinstanceeditor(button_name)
            except Exception as ex:
                raise Exception(ex) from ex
                
                
    def rightclickandgeneratecontainerssection(self,container):
                """rightclickandgeneratecontainerssection"""
                try:
                    Projectexplorertabutility.rightclickandgeneratecontainers(container)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def verifyfacetbeforegenerate(self,facet_name):
                    """verifyfacetbeforegenerate"""
                    try:
                        Projectexplorertabutility.verify_facet_assignment_before_generate(facet_name)
                    except Exception as ex:
                        raise Exception(ex) from ex
    
    def verifydeviceavailbe(self, variables):
                """verifydeviceavailbe"""
                try:
                    Projectexplorertabutility.verify_device_available(variables)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def verifyhardwareinstanceavailableformapping(self, variables):
                    """verifyhardwareinstanceavailableformapping"""
                    try:
                        Projectexplorertabutility.verify_hardware_instance_available_for_mapping(variables)
                    except Exception as ex:
                        raise Exception(ex) from ex
                        
    def verifynetworkvariablemapping(self, identifiers):
                    """verifynetworkvariablemapping"""
                    try:
                        Projectexplorertabutility.verify_network_variable_mapping(identifiers)
                    except Exception as ex:
                        raise Exception(ex) from ex
                    
    def verifynetworkvariable(self, variables):
                    """verifynetworkvariable"""
                    try:
                        Projectexplorertabutility.verify_network_variable(variables)
                    except Exception as ex:
                        raise Exception(ex) from ex                                                    
                    
    def draganddropdevicetochannel(self, server):
                    """draganddropdevicetochannel"""
                    try:
                        Projectexplorertabutility.drag_and_drop_device_to_channel(server)
                    except Exception as ex:
                        raise Exception(ex) from ex
                        
    def clickonmappingtab(self, tabname):
                        """clickonmappingtab"""
                        try:
                            Projectexplorertabutility.click_on_mapping_tab(tabname)
                        except Exception as ex:
                            raise Exception(ex) from ex
                            
    def draganddropprojecttoserver(self, appfacet):
                        """draganddropprojecttoserver"""
                        try:
                            Projectexplorertabutility.project_to_hardware(appfacet)
                        except Exception as ex:
                            raise Exception(ex) from ex
                            
    def rightclickcommunicationchannel(self, server):
                        """rightclickcommunicationchannel"""
                        try:
                            Projectexplorertabutility.right_click_communication_channel(server)
                        except Exception as ex:
                            raise Exception(ex) from ex
                            
    def draganddropnetworktoserver(self, identifiers):
      try:
        Projectexplorertabutility.drag_and_drop_network_to_server(identifiers)
      except Exception as ex:
        raise Exception(ex) from ex    
        
    def buttonokselected(self):
        """buttonokselected"""
        try:
          ProjectExplorerTabWorkFlow.globaltemplatestab_obj.okduuplicatebutton.click()
        except Exception as ex:
          raise Exception(ex) from ex
          
    def createinstance(self, value):
            """createinstance"""
            try:
              Projectexplorertabutility.create_instance(value)
            except Exception as ex:
              raise Exception(ex) from ex 
              
    def verifyinstance(self, value):
            """verifyinstance"""
            try:
              Projectexplorertabutility.verify_instance(value)
            except Exception as ex:
              raise Exception(ex) from ex 
              
    def verifyfacetsinhardwaremappingeditor(self, appfacet):
            """verifyfacetsinhardwaremappingeditor"""
            try:
              Projectexplorertabutility.verify_facets_in_hardware_mapping_editor(appfacet)
            except Exception as ex:
              raise Exception(ex) from ex  
              
    def verifyservervariables(self, identifiers):
            """verifyservervariables"""
            try:
              Projectexplorertabutility.verify_server_variables(identifiers)
            except Exception as ex:
              raise Exception(ex) from ex  
              
    def doubleclickincontainer(self, identifiers):
            """doubleclickincontainer"""
            try:
              Projectexplorertabutility.double_click_in_container(identifiers)
            except Exception as ex:
              raise Exception(ex) from ex  
              
    def draganddropinstancetoeditpage(self, facetnames, option):
            """draganddropinstancetoeditpage"""
            try:
              Projectexplorertabutility.drag_and_drop_instance_to_editpage(facetnames, option)
            except Exception as ex:
              raise Exception(ex) from ex  
              
    def clickbuttononspeditpage(self, button):
            """clickbuttononspeditpage"""
            try:
              Projectexplorertabutility.click_button_on_sp_editpage(button)
            except Exception as ex:
              raise Exception(ex) from ex   
              
    def clickpropertiesonplantscada(self, button, drop_button):
            """clickpropertiesonplantscada"""
            try:
              Projectexplorertabutility.click_properties_on_plant_scada(button, drop_button)
            except Exception as ex:
              raise Exception(ex) from ex   
              
    def clickbuttonplantscada(self, button):
            """clickbuttonplantscada"""
            try:
              Projectexplorertabutility.click_button_in_aveva(button)
            except Exception as ex:
              raise Exception(ex) from ex    
              
    def verifyandselectfileplantscada(self, file_name):
            """verifyandselectfileplantscada"""
            try:
              Projectexplorertabutility.verify_and_select_file(file_name)
            except Exception as ex:
              raise Exception(ex) from ex
              
    def checkboxclickindeploymentfilesection(self, filenames):
            """checkboxclickindeploymentfilesection"""
            try:
              Projectexplorertabutility.checkbox_click_in_deployment_file_section(filenames)
            except Exception as ex:
              raise Exception(ex) from ex       
              
    def clicksidebarbuttoninplantscada(self, sidebar):
            """clicksidebarbuttoninplantscada"""
            try:
              Projectexplorertabutility.click_sidebar_button_in_plant_scada(sidebar)
            except Exception as ex:
              raise Exception(ex) from ex        
              
    def logintoplantscada(self, username, password):
            """logintoplantscada"""
            try:
              Projectexplorertabutility.login_to_plant_scada(username, password)
            except Exception as ex:
              raise Exception(ex) from ex        
              
    def clickbuttontologinscadapage(self, button):
            """clickbuttontologinscadapage"""
            try:
              Projectexplorertabutility.click_button_to_login_scada_page(button)
            except Exception as ex:
              raise Exception(ex) from ex        
              
    def clickbuttononscadapopup(self, button):
            """clickbuttononscadapopup"""
            try:
              Projectexplorertabutility.click_button_on_scada_popup(button)
            except Exception as ex:
              raise Exception(ex) from ex         
              
    def verifymasterpagemainwindow(self):
            """verifymasterpagemainwindow"""
            try:
              Projectexplorertabutility.verify_master_page_main_window()
            except Exception as ex:
              raise Exception(ex) from ex          
              
    def verifycontrolproject(self, identifier):
            """verifycontrolproject"""
            try:
              Projectexplorertabutility.verify_control_project(identifier)
            except Exception as ex:
              raise Exception(ex) from ex     

    def projectexplorertabutility_After_Generation_dialog_window_Message(self):
          """draganddropfromcontainertosection"""
          try:
              Projectexplorertabutility.After_Generation_dialog_window_Message()
          except Exception as ex:
              raise Exception(ex) from ex
       
                     
    def textboxprojectbrowserrclickonblockrefineoffline(self,identifier):
            """textboxprojectbrowserrclickonblockrefineoffline"""
            try:
                Controlexpertutility.RClick_on_Block_Refine_Offline(identifier)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def textboxcommunicationpeertopeerpanneldraganddropp2ptochannel(self,val):
        """textboxcommunicationpeertopeerpanneldraganddropp2ptochannel"""
        try:
            Projectexplorertabutility.drag_and_drop_P2P_to_channel(val)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcommunicationchannelspanneleditp2pproperties(self,param):
        """textboxcommunicationchannelspanneleditp2pproperties"""
        try:
            Projectexplorertabutility.edit_P2P_Properties(param)
        except Exception as ex:
            raise Exception(ex) from ex

    def textboxinstancedockdraginstancedropcontainerpagesp(self,template):
        """textboxinstancedockdraginstancedropcontainerpagesp"""
        try:
            Controlexpertutility.drag_instance_drop_container_page_SP(template)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxinstancedockselectvaluelistviewsvp(self,val):
        """textboxinstancedockselectvaluelistviewsvp"""
        try:
            Controlexpertutility.select_value_listview_SVP(val)
        except Exception as ex:
            raise Exception(ex) from ex

    def Navigate_to_supervision_controlproject_tab(self,val):
            """Navigatetosupervisioncontrolproject"""
            try:
                Projectexplorertabutility.Navigate_CP_SP_Tab_PE(val)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def Verify_supervision_controlproject_tab(self):
                """Navigatetosupervisioncontrolproject"""
                try:
                    Projectexplorertabutility.Verify_CP_SP_Tab_PE()
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def Map_Workstation_Supervision_project(self,Service_Engine):
                """Navigatetosupervisioncontrolproject"""
                try:
                    Projectexplorertabutility.map_workstation(Service_Engine)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def textboxprojectbrowserrclickcontrolprojectbrowser(self,identifier):
        """textboxprojectbrowserrclickcontrolprojectbrowser"""
#        try:
        Projectexplorertabutility.right_click_control_project_browser_PE(identifier)
#        except Exception as ex:
#            raise Exception(ex) from ex
        
    def textboxprojectbrowserselectcontextmenuitemec(self,menu_item):
        """textboxprojectbrowserselectcontextmenuitemec"""
        try:
            Engineeringclientutility.select_ContextMenu_Items_EC(menu_item)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockdoubleclickcontainerpe(self,identifier):
        """textboxcontainerdockdoubleclickcontainerpe"""
        try:
            Projectexplorertabutility.double_click_container_dock_context_menu_item_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxcontainerdockrightclickcontainerdockcontextmenuitempe(self,param):
        """textboxcontainerdockrightclickcontainerdockcontextmenuitempe"""
        try:
            Projectexplorertabutility.right_click_container_dock_context_menu_item_PE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowserdclickcontrolprojectbroswer(self,identifier):
        """textboxprojectbrowserdclickcontrolprojectbroswer"""
        try:
            Projectexplorertabutility.double_click_control_project_browser_PE(identifier)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxservicemapingeditorverifysupervisionmappingpe(self):
        """textboxservicemapingeditorverifysupervisionmappingpe"""
        try:
            Projectexplorertabutility.verify_supervision_service_maping_PE()
        except Exception as ex:
            raise Exception(ex) from ex
    
    def draganddropfrominstancetocontainer(self,Instance):
        """draganddropfrominstancetocontainer"""
        try:
            Projectexplorertabutility.select_instance_drag_drop_container_dock_PE(Instance)
        except Exception as ex:
            raise Exception(ex) from ex
            
    def changesettingsoption(self,option):
        """draganddropfrominstancetocontainer"""
        try:
            Projectexplorertabutility.Change_SettingsOption(option)
        except Exception as ex:
            raise Exception(ex) from ex

## scam method ##
    def yesbuttoninsettings(self):
        """draganddropfrominstancetocontainer"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.messageboxyesbutton.click()
        except Exception as ex:
            raise Exception(ex) from ex           
            
    def ClicktabitemEIOconfigwindow(self,identifiers):
        """ClicktabitemEIOconfigwindow"""
        try:
            Controlexpertutility.Click_tab_item_EIO_config_window(identifiers)
        except Exception as ex:
            raise Exception(ex) from ex
            
            
    def elementvariabledoubleclick(self):
        """elementvariabledoubleclick"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.elementvariabletextbox.double_click()
        except Exception as ex:
            raise Exception(ex) from ex 
            
    def entervariableselecthmi(self):
        """entervariableselecthmi"""
        try:
            Projectexplorertabutility.Enter_Variable_select_HMI()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def dataeditorvariableclick(self):
        """dataeditorvariableclick"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.elementvariabletextboxrefine.click()
        except Exception as ex:
            raise Exception(ex) from ex 
            
            
    def UnpackvariableP2Pconfigurationwindow(self,identifier):
                """UnpackvariableP2Pconfigurationwindow"""
                try:
                    Projectexplorertabutility.Unpack_Variable(identifier)
                except Exception as ex:
                    raise Exception(ex) from ex     

                    
    def UnmapP2Pvariablebycontextmenu(self,identifier):
                """UnmapP2Pvariablebycontextmenu"""
                try:
                    Projectexplorertabutility.Unmap_Variable(identifier)
                except Exception as ex:
                    raise Exception(ex) from ex   
                    
                    
    def UnmapP2Pvariablebykeyboardaction(self,identifier):
                """UnmapP2Pvariablebykeyboardaction"""
                try:
                    Projectexplorertabutility.Unmap_Variable_by_Keyboard_action(identifier)
                except Exception as ex:
                    raise Exception(ex) from ex     
                    
    def clickvariableelementaryinitiateanimationtabletab(self,identifier):
                """RClickVariableElementaryVariableTab"""
                try:
                    Projectexplorertabutility.Click_Variable_Elementary_Initiate_animationtable_Tab(identifier)
                except Exception as ex:
                    raise Exception(ex) from ex    
                    
    def RunPLCsimulator(self):
                """RunPLCsimulator"""
                try:
                    Projectexplorertabutility.Run_PLC_Simulator()
                except Exception as ex:
                    raise Exception(ex) from ex  
                    
                    
    def textboxprojectbrowserverifybackupdata(self,param):
                """textboxprojectbrowserverifybackupdata"""
                try:
                    Projectexplorertabutility.Verify_backup_data_PE(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                
    def textboxdraganddropremotetolocalP2P(self,param):
                """textboxprojectbrowserverifybackupdata"""
                try:
                    Projectexplorertabutility.drag_and_drop_remote_to_local_P2P(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
                    
    def textboxclickp2pcreateconsecutivevariables(self,param):
                """textboxprojectbrowserverifybackupdata"""
                try:
                    Projectexplorertabutility.Click_P2p_Create_consecutive_variables(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def textboxchangedatatypedataeditor(self,param):
                """textboxprojectbrowserverifybackupdata"""
                try:
                    Projectexplorertabutility.change_datatype_dataeditor(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def clickonvariableandchangedatavalueanimationtable(self,param):
                """textboxprojectbrowserverifybackupdata"""
                try:
                    Projectexplorertabutility.Click_on_variable_and_change_data_value_animation_table(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def textboxprojectbrowserexpandiodevicesection(self,param):
        """textboxprojectbrowserexpandiodevicesection"""
        try:
            Projectexplorertabutility.Expand_IODevice_section(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowsereditiodeviceproperties(self,param):
        """textboxprojectbrowsereditiodeviceproperties"""
        try:
            Projectexplorertabutility.Edit_IODevice_Properties(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxprojectbrowsermapiodevicesinpe(self,param):
        """textboxprojectbrowsermapiodevicesinpe"""
        try:
            Projectexplorertabutility.Map_IO_Devices(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
                    
    def changeFBDValue(self,param):
                """textboxprojectbrowserverifybackupdata"""
                try:
                    Projectexplorertabutility.change_FBD_Value(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def verifyvariablevalueFBDBlock(self,param):
                """verifyvariablevalueFBDBlock"""
                try:
                    Projectexplorertabutility.verify_variable_value_FBDBlock(param)
                except Exception as ex:
                    raise Exception(ex) from ex
                    
    def pagetemplatesspsettingsbuttonclick(self):
        """dataeditorvariableclick"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.pagetemplatesspsettingsbutton.click()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def addpagetemplatebuttonclick(self):
        """dataeditorvariableclick"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.addpagetemplatebutton.click()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def newpagetemplateradiobuttoncheck(self):
        """newpagetemplateradiobuttoncheck"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.newpagetemplateradiobutton.checkboxchecked()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def closetoolbarbuttonclick(self):
        """closetoolbarbuttonclick"""
        try:
            ProjectExplorerTabWorkFlow.projectexplorertab_obj.closetoolbarbutton.click()
        except Exception as ex:
            raise Exception(ex) from ex
            
            