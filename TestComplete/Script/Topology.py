"""Topology"""
from MapBase import MapBase

class Topology(MapBase):
    """Topology"""
        
    @property
    def topologyexplorertreetextbox(self):
        """topologyexplorertreetextbox"""
        return self.get_element("TopologyExplorerTree_Topology")
              
    @property
    def topologydeviceeditertextbox(self):
        """topologydeviceeditertextbox"""
        return self.get_element("Topologydeviceediter_Topology")
              
    @property
    def projectdropdowntextbox(self):
        """projectdropdowntextbox"""
        return self.get_element("projectdropdown_Topology")
              
    @property
    def executablesdropdowntextbox(self):
        """executablesdropdowntextbox"""
        return self.get_element("Executablesdropdown_Topology")
              
    @property
    def newpasswordboxtextbox(self):
        """newpasswordboxtextbox"""
        return self.get_element("NewPasswordbox_Topology")
              
    @property
    def confirmpasswordboxtextbox(self):
        """confirmpasswordboxtextbox"""
        return self.get_element("ConfirmPasswordbox_Topology")
              
    @property
    def oldpasswordboxtextbox(self):
        """oldpasswordboxtextbox"""
        return self.get_element("OldPasswordBox_Topology")
              