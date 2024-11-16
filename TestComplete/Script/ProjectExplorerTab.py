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
    def assignmentstextbox(self):
      return self.get_element("assignments_ProjectExplorerTab")
              
