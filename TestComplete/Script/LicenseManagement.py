"""LicenseManagement"""
from MapBase import MapBase

class LicenseManagement(MapBase):
    """LicenseManagement"""
        
    @property
    def traillicensepopupwindow(self):
        """traillicensepopupwindow"""
        return self.get_element("Traillicensepopup_LicenseManagement")
              
    @property
    def licensemanagementpopupbutton(self):
        """licensemanagementpopupbutton"""
        return self.get_element("LicenseManagementpopup_LicenseManagement")
              
    @property
    def licensemanagementokbutton(self):
        """licensemanagementokbutton"""
        return self.get_element("LicenseManagementOK_LicenseManagement")
              