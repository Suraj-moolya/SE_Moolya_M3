﻿"""TopologyExporerTab"""
from MapBase import MapBase

class TopologyExplorerTab(MapBase):
    """TopologyExporerTab"""
        
    @property
    def closeabletabbutton(self):
        """closeabletabbutton"""
        return self.get_element("CloseableTab_TopologyExporerTab")
              
    @property
    def systemprojectbutton(self):
        """systemprojectbutton"""
        return self.get_element("SystemProject_TopologyExporerTab")
              
    @property
    def toolboxcatalogbutton(self):
        """toolboxcatalogbutton"""
        return self.get_element("ToolboxCatalog_TopologyExporerTab")
              
    @property
    def propertiesgridbutton(self):
        """propertiesgridbutton"""
        return self.get_element("PropertiesGrid_TopologyExporerTab")
              
    @property
    def propertydescriptiontabbutton(self):
        """propertydescriptiontabbutton"""
        return self.get_element("PropertyDescriptionTab_TopologyExporerTab")
              
    @property
    def propertyconfigurationtabbutton(self):
        """propertyconfigurationtabbutton"""
        return self.get_element("PropertyConfigurationTab_TopologyExporerTab")
              
    @property
    def propertyservicestabbutton(self):
        """propertyservicestabbutton"""
        return self.get_element("PropertyServicesTab_TopologyExporerTab")
              
    @property
    def propertyioprofiletabbutton(self):
        """propertyioprofiletabbutton"""
        return self.get_element("PropertyIOProfileTab_TopologyExporerTab")
              
    @property
    def propertysecuritytabbutton(self):
        """propertysecuritytabbutton"""
        return self.get_element("PropertySecurityTab_TopologyExporerTab")
        
    @property
    def passwordgridbutton(self):
        """passwordgridbutton"""
        return self.get_element("Passwordgrid_TopologyExporerTab")
        
    @property
    def newpasswordboxtextbox(self):
        """newpasswordboxtextbox"""
        return self.get_element("NewPasswordbox_TopologyExporerTab")
        
    @property
    def ConfirmPasswordboxtextbox(self):
        """ConfirmPasswordboxtextbox"""
        return self.get_element("ConfirmPasswordbox_TopologyExporerTab")
        
    @property
    def Closetmbutton(self):
        """Closetmbutton"""
        return self.get_element("ClosebuttonTM_TopologyExporerTab")
        
    @property
    def controllerpropertytab(self):
        """controllerpropertytab"""
        return self.get_element("ControllerPropertytab_TopologyExporerTab")
        
    @property
    def oldpasswordboxboxtextbox(self):
        """oldpasswordboxboxtextbox"""
        return self.get_element("OldPasswordBox_TopologyExporerTab")
