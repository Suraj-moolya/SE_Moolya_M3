"""SupervisionProject"""
from MapBase import MapBase

class SupervisionProject(MapBase):
    """SupervisionProject"""
        
    @property
    def advancesettingswindowspbutton(self):
        """advancesettingswindowspbutton"""
        return self.get_element("advancesettingswindowSP_SupervisionProject")   
    
    @property
    def settingswindow(self):
        """settingswindow"""
        return self.get_element("settingswindowSP_SupervisionProject")
        
    @property
    def pagetemplate(self):
        """pagetemplate"""
        return self.get_element("pagetemplate_SupervisionProject")
        
    @property
    def refineapplicationbar(self):
        """refineapplicationbar"""
        return self.get_element("refineapplicationbar_SupervisionProject")
        
    @property
    def refinesystemmodelcommandbar(self):
        """refinesystemmodelcommandbar"""
        return self.get_element("commandbar_SupervisionProject")
        
    @property
    def exportdatawindow(self):
        """exportdatawindow"""
        return self.get_element("ExportDataWindow_SupervisionProject")
        
    @property
    def exportdatafilename(self):
        """exportdatafilename"""
        return self.get_element("ExportData_Filename_SupervisionProject")
        
    @property
    def exportdatafilelocation(self):
        """exportdatafilelocation"""
        return self.get_element("ExportData_Filelocation_SupervisionProject")
        
    @property
    def exportdatasave(self):
        """exportdatasave"""
        return self.get_element("ExportData_Savebutton_SupervisionProject")
        
    @property
    def refinesystemmodelmenubar(self):
        """refinesystemmodelmenubar"""
        return self.get_element("SystemModel_Menubar_SupervisionProject")
    