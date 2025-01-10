"""CurrentScreen"""
from MapBase import MapBase

class CurrentScreen(MapBase):
    """CurrentScreen"""
        
    @property
    def collapseallbutton(self):
        """collapseallbutton"""
        return self.get_element("CollapseAll_CurrentScreen")
              
    @property
    def reportdialogwindow(self):
        """reportdialogwindow"""
        return self.get_element("ReportDialog_CurrentScreen")
              
    @property
    def partdiagramcontrolbutton(self):
        """partdiagramcontrolbutton"""
        return self.get_element("PartDiagramControl_CurrentScreen")
              
    @property
    def nodecontrolbutton(self):
        """nodecontrolbutton"""
        return self.get_element("NodeControl_CurrentScreen")
              
    @property
    def toolbarbutton(self):
        """toolbarbutton"""
        return self.get_element("ToolBar_CurrentScreen")
              
    @property
    def nodemenuitembutton(self):
        """nodemenuitembutton"""
        return self.get_element("NodeMenuItem_CurrentScreen")
              
    @property
    def controlexpertwindow(self):
        """controlexpertwindow"""
        return self.get_element("ControlExpert_CurrentScreen")
              
    @property
    def projectbrowserwindow(self):
        """projectbrowserwindow"""
        return self.get_element("ProjectBrowser_CurrentScreen")
              
    @property
    def closebutton(self):
        """closebutton"""
        return self.get_element("Close_CurrentScreen")
              
    @property
    def engineeringclienttwobutton(self):
        """engineeringclienttwobutton"""
        return self.get_element("Engineeringclienttwo_CurrentScreen")
              
    @property
    def contextmenuitemsbutton(self):
        """contextmenuitemsbutton"""
        return self.get_element("ContextMenuItems_CurrentScreen")
              
    @property
    def exportcancelbutton(self):
        """exportcancelbutton"""
        return self.get_element("ExportCancel_CurrentScreen")
              
    @property
    def exportsavebutton(self):
        """exportsavebutton"""
        return self.get_element("ExportSave_CurrentScreen")
              
    @property
    def exportfilenametextbox(self):
        """exportfilenametextbox"""
        return self.get_element("Exportfilename_CurrentScreen")
              
    @property
    def modificationpopupbutton(self):
        """modificationpopupbutton"""
        return self.get_element("Modificationpopup_CurrentScreen")
              
    @property
    def aepostconditionbutton(self):
        """aepostconditionbutton"""
        return self.get_element("abc_CurrentScreen")
              