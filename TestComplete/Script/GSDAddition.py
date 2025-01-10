"""GSDAddition"""
from MapBase import MapBase

class GSDAddition(MapBase):
    """GSDAddition"""
        
    @property
    def homepageingsdadditionwindow(self):
        """homepageingsdadditionwindow"""
        return self.get_element("Homepage_GSDAddition")
        
    @property    
    def choosefoldertabingsdadditionwindow(self):
        """choosefoldertabingsdadditionwindow"""
        return self.get_element("ChooseFolderTab_GSDAddition")
        
    @property    
    def duplicatefiletabingsdadditionwindow(self):
        """duplicatefiletabingsdadditionwindow"""
        return self.get_element("DuplicateFileTab_GSDAddition")
        
    @property    
    def devicedeletetabingsdadditionwindow(self):
        """devicedeletetabingsdadditionwindow"""
        return self.get_element("DeleteDeviceTab_GSDAddition")
        
    @property    
    def devicedeletepopuptabingsdadditionwindow(self):
        """devicedeletepopuptabingsdadditionwindow"""
        return self.get_element("DeleteDevicePopupTab_GSDAddition")
        
    @property    
    def loadingtabingsdadditionwindow(self):
        """loadingtabingsdadditionwindow"""
        return self.get_element("Loading_GSDAddition")