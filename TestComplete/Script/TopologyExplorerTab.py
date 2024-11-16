"""TopologyExporerTab"""
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
              