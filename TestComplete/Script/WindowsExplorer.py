"""WindowsExplorer"""
from MapBase import MapBase

class WindowsExplorer(MapBase):
    """WindowsExplorer"""
        
    @property
    def showhiddeniconbutton(self):
        """showhiddeniconbutton"""
        return self.get_element("showhiddenicon_WindowsExplorer")
              
    @property
    def notificationareawindow(self):
        """notificationareawindow"""
        return self.get_element("notificationarea_WindowsExplorer")
              
    @property
    def commandbarbutton(self):
        """commandbarbutton"""
        return self.get_element("commandbar_WindowsExplorer")
              
    @property
    def windowsparent(self):
        """windowsparent"""
        return self.get_element("Windows_WindowsExplorer")
              
    @property
    def tabsbutton(self):
        """tabsbutton"""
        return self.get_element("tabs_WindowsExplorer")
              
    @property
    def detaillisttextbox(self):
        """detaillisttextbox"""
        return self.get_element("detaillist_WindowsExplorer")
              
    @property
    def notificationareawin11window(self):
        """notificationareawindow"""
        return self.get_element("notificationareawin11_WindowsExplorer")          
