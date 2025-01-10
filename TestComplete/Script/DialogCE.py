"""DialogCE"""
from MapBase import MapBase

class DialogCE(MapBase):
    """DialogCE"""
        
    @property
    def dialogpanelcetextbox(self):
        """dialogpanelcetextbox"""
        return self.get_element("DialogPanelCE_DialogCE")
              
    @property
    def dialogpanelce2textbox(self):
        """dialogpanelcetextbox"""
        return self.get_element("DialogPanelCE2_DialogCE")
    
    @property
    def dialogpanelce3textbox(self):
        """dialogpanelcetextbox"""
        return self.get_element("DialogPanelCE3_DialogCE")
    
    @property
    def dialogpanelce4textbox(self):
        """dialogpanelcetextbox"""
        return self.get_element("DialogPanelCE4_DialogCE")
    
    @property
    def dialogokcebutton(self):
        """dialogokcebutton"""
        return self.get_element("DialogOKCE_DialogCE")
              
    @property
    def dialoglistboxcetextbox(self):
        """dialoglistboxcetextbox"""
        return self.get_element("DialogListboxCE_DialogCE")
              
    @property
    def dialoglistboxce1textbox(self):
        """dialoglistboxcetextbox"""
        return self.get_element("DialogListboxCE1_DialogCE")
        
    @property
    def startsimulatorbutton(self):
        """startsimulatorbutton"""
        return self.get_element("StartSimulator_DialogCE")
        
    @property
    def simulatorporttextbox(self):
        """simulatorporttextbox"""
        return self.get_element("SimulatorPort_DialogCE")
        
    @property
    def listofmodifiedyesbuttoncebutton(self):
          """listofmodifiedyesbuttoncebutton"""
          return self.get_element("ListofmodifiedYesbuttonCE_DialogCE")
