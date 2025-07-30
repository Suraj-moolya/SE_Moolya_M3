"""ProjectExplorerTab"""
from MapBase import MapBase

class ProjectExplorerTab(MapBase):
    """ProjectExplorerTab"""
        
    @property
    def projectbrowsertextbox(self):
        """projectbrowsertextbox"""
        return self.get_element("projectbrowser_ProjectExplorerTab")
              
    @property
    def servicemapingeditortextbox(self):
        """servicemapingeditortextbox"""
        return self.get_element("servicemapingeditor_ProjectExplorerTab")
        
    @property
    def supervisionworkspacetextbox(self):
        """supervisionworkspacetextbox"""
        return self.get_element("SupervisionWorkSpace_ProjectExplorerTab")
              
    @property
    def instancedocktextbox(self):
        """instancedocktextbox"""
        return self.get_element("instancedock_ProjectExplorerTab")
              
    @property
    def containerdocktextbox(self):
        """containerdocktextbox"""
        return self.get_element("containerdock_ProjectExplorerTab")
              
    @property
    def executablepropertytextbox(self):
        """executablepropertytextbox"""
        return self.get_element("executableproperty_ProjectExplorerTab")
        
    @property
    def assignmentsdocktextbox(self):
      """instancepropertytextbox"""
      return self.get_element("assignmentsdock_ProjectExplorerTab")

    @property
    def refineonlinewindowtextbox(self):
        """refineonlinewindowtextbox"""
        return self.get_element("Refineonlinewindow_ProjectExplorerTab")
    
    @property
    def closebutton(self):
        """closebutton"""
        return self.get_element("Close_ProjectExplorerTab")
    
    @property
    def instanceeditortextbox(self):
      """instanceeditortextbox"""
      return self.get_element("instanceeditor_ProjectExplorerTab")   
              
    @property
    def controlexecutablesproperty(self):
      """controlexecutablesproperty"""
      return self.get_element("ControlExecutablesProperty_ProjectExplorerTab") 
      
    @property
    def servercommunicationcounterpartsdeviceio(self):
      """controlexecutablesproperty"""
      return self.get_element("ServerCommunicationCounterpartsDeviceIO_ProjectExplorerTab")
      
    @property
    def communicationchanneltab(self):
      """communicationchanneltab"""
      return self.get_element("CommunicationChannelTab_ProjectExplorerTab")
      
    @property
    def networkvariabletab(self):
      """networkvariabletab"""
      return self.get_element("NetworkVariableTab_ProjectExplorerTab")
    
    @property
    def hardwareinstancetab(self):
      """hardwareinstancetab"""
      return self.get_element("HardwareInstanceTab_ProjectExplorerTab")  
      
    @property
    def managenetworkvariablestab(self):
      """managenetworkvariablestab"""
      return self.get_element("ManageNetworkVariablesTab_ProjectExplorerTab")
      
    @property
    def createinstancetab(self):
      """createinstancetab"""
      return self.get_element("CreateInstancesTab_ProjectExplorerTab")  
      
    @property
    def createtemplatetab(self):
      """createtemplatetab"""
      return self.get_element("CreateTemplateTab_ProjectExplorerTab")  
      
    @property
    def appfacetstab(self):
      """appfacetstab"""
      return self.get_element("AppFacetsTab_ProjectExplorerTab")  
      
    @property
    def deploymentfilesectiontab(self):
      """deploymentfilesectiontab"""
      return self.get_element("DeploymentFileSection_ProjectExplorerTab")  
      
    @property
    def containerseditpagetab(self):
      """containerseditpagetab"""
      return self.get_element("ContainersEditPage_ProjectExplorerTab")  
      
    @property
    def instanceeditpagetab(self):
      """instanceeditpagetab"""
      return self.get_element("InstanceEditPage_ProjectExplorerTab")  
      
    @property
    def instancelistitemtab(self):
      """instancelistitemtab"""
      return self.get_element("InstanceListItmes_ProjectExplorerTab")  
      
    @property
    def supervisioneditpagepropertiestab(self):
      """supervisioneditpagepropertiestab"""
      return self.get_element("SupervisionEdidPageProperties_ProjectExplorerTab")  
      
    @property
    def plantscadapropertiestab(self):
      """plantscadapropertiestab"""
      return self.get_element("PlantScadaHomeProperties_PropertiesTab")  
      
    @property
    def menuitemtab(self):
      """menuitemtab"""
      return self.get_element("MenuItem_PropertiesTab") 
      
    @property
    def backuprestoretab(self):
      """backuprestoretab"""
      return self.get_element("BackupRestore_PropertiesTab")  
      
    @property
    def restorepopuptab(self):
      """restorepopuptab"""
      return self.get_element("RestorePopup_PlantScadaTab")  
      
    @property
    def sidebartab(self):
      """sidebartab"""
      return self.get_element("Sidebar_PlantScadaTab")  
      
    @property
    def loginpageplantscada(self):
      """loginpageplantscada"""
      return self.get_element("LoginPage_PlantScadaTab")  
      
    @property
    def errorpopupplantscada(self):
      """errorpopupplantscada"""
      return self.get_element("ErrorPopup_PlantScadaTab")  
      
    @property
    def masterpagemainwindowplantscada(self):
      """masterpagemainwindowplantscada"""
      return self.get_element("MasterPageMainWindow_PlantScadaTab")
               
              
    @property
    def communicationchannelspanneltextbox(self):
        """communicationchannelspanneltextbox"""
        return self.get_element("CommunicationChannelsPannel_ProjectExplorerTab")
              
    @property
    def communicationdeviceiopanneltextbox(self):
        """communicationdeviceiopanneltextbox"""
        return self.get_element("CommunicationDeviceIOPannel_ProjectExplorerTab")
              
    @property
    def communicationpeertopeerpanneltextbox(self):
        """communicationpeertopeerpanneltextbox"""
        return self.get_element("CommunicationPeertoPeerPannel_ProjectExplorerTab")
        
    @property
    def servicemapdropdownbox(self):
        """servicemapdropdownbox"""
        return self.get_element("ServiceMap_ProjectExplorerTab")
        
    @property
    def mdiclientwindowtextbox(self):
        """mdiclientwindowtextbox"""
        return self.get_element("MDIClientWindow_ProjectExplorerTab")
        
    @property
    def listviewtextbox(self):
        """listviewtextbox"""
        return self.get_element("ListView_ProjectExplorerTab") 
        
    @property
    def containerpagedocktextbox(self):
        """listviewtextbox"""
        return self.get_element("containerpagedock_ProjectExplorerTab") 

    @property
    def controllerpropertytab(self):
        """controllerpropertytab"""
        return self.get_element("ControllerPropertytab_TopologyExporerTab")	
        
    @property
    def hardwareinstancetab(self):
        """hardwareinstancetab"""
        return self.get_element("HardwareInstanceTab_ProjectExplorerTab")
        
        
    @property
    def projectcontrollersettingtab(self):
        """projectcontrollersettingtab"""
        return self.get_element("ProjectControllerSetting_ProjectExplorerTab")
        
    @property
    def wpfcomboboxtextbox(self):
        """wpfcomboboxtextbox"""
        return self.get_element("wpfcombobox_ProjectExplorer")
        
    @property
    def settingspropertytab(self):
        """settingspropertytab"""
        return self.get_element("Settings_ProjectExplorerTab")
        
    @property
    def settingsdropdownpropertytab(self):
        """settingsdropdownpropertytab"""
        return self.get_element("SettingsDropDown_ProjectExplorerTab")
        
    @property
    def messageboxyesbutton(self):
        """messageboxyesbutton"""
        return self.get_element("MessageBoxYes_ProjectExplorerTab")
        
    @property
    def elementvariabletextbox(self):
        """elementvariabletextbox"""
        return self.get_element("Elementvariable_ProjectExplorerTab")
        
    @property
    def elementvariabletextboxrefine(self):
        """elementvariabletextboxrefine"""
        return self.get_element("Variable_ProjectExplorer")
       
       
    @property
    def loadp2pvariablestabcontrol(self):
        """loadp2pvariablestabcontrol"""
        return self.get_element("LoadP2PVariablesTabControl_ProjectExplorer")
        
    
 
    @property
    def unmapvariable(self):
        """unmapvariable"""
        return self.get_element("Unmapvariable_ProjectExplorer")  
        
    @property
    def remotevariablebutton(self):
        """remotevariablebutton"""
        return self.get_element("Remotevariable_ProjectExplorer") 
        
    @property
    def sourcevariablebutton(self):
        """sourcevariablebutton"""
        return self.get_element("Sourcevariable_ProjectExplorer")
        
    @property
    def animationtablewindow(self):
        """animationtablewindow"""
        return self.get_element("AnimationTable_ProjectExplorerTab") 
        
    @property
    def pagetemplatesspsettingsbutton(self):
        """pagetemplatesspsettingsbutton"""
        return self.get_element("PageTemplatesSPsettings_ProjectExplorerTab") 
    
    @property
    def addpagetemplatebutton(self):
        """addpagetemplatebutton"""
        return self.get_element("AddPageTemplateButton_ProjectExplorerTab") 
          
    @property
    def newpagetemplateradiobutton(self):
        """addpagetemplatebutton"""
        return self.get_element("New_Page_TemplateRadioButton_ProjectExplorerTab") 
        
    @property
    def closetoolbarbutton(self):
        """closetoolbarbutton"""
        return self.get_element("CloseToolBar_ProjectExplorerTab")
          
        
        
       