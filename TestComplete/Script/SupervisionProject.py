"""SupervisionProject"""
from MapBase import MapBase

class SupervisionProject(MapBase):
    """SupervisionProject"""
        
    @property
    def advancesettingswindowspbutton(self):
        """advancesettingswindowspbutton"""
        return self.get_element("advancesettingswindowSP_SupervisionProject")
              