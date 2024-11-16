"""AvevaScreen"""
from MapBase import MapBase

class AvevaScreen(MapBase):
    """AvevaScreen"""
        
    @property
    def mainparenttextbox(self):
        """mainparenttextbox"""
        return self.get_element("MainParent_AvevaScreen")
              
    @property
    def systreeviewtextbox(self):
        """systreeviewtextbox"""
        return self.get_element("SysTreeView_AvevaScreen")
              