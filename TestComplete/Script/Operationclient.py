"""OperationClient"""
from MapBase import MapBase

class OperationClient(MapBase):
    """OperationClient"""
        
    @property
    def instanceedittorpage(self):
        """instanceedittorpage"""
        return self.get_element("InstanceEdittorPage_OperationClient")
        
    @property
    def instancestatuspage(self):
        """instancestatuspage"""
        return self.get_element("InstanceStatusPage_OperationClient")