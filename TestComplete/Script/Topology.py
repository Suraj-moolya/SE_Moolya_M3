﻿"""Topology"""
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
    def primaryaddresslistdropdown(self):
        """primaryaddresslistdropdowntextbox"""
        return self.get_element("primaryaddresslistdropdown_Topology")
        
    @property
    def startenginecheckbox(self):
        """startenginecheckboxtextbox"""
        return self.get_element("startenginecheckbox_Topology")
        
    @property
    def backupdatadescriptiontextbox(self):
        """backupdatadescriptiontextbox"""
        return self.get_element("backupdatadescription_Topology")
              
    @property
    def deploydataselectiongridtextbox(self):
        """deploydataselectiongridtextbox"""
        return self.get_element("deploydataselectiongrid_Topology")