"""ECWarningPopup"""
from MapBase import MapBase

class ECWarningPopup(MapBase):
    """ECWarningPopup"""
        
    @property
    def warningpopuptextbox(self):
        """warningpopuptextbox"""
        return self.get_element("Warningpopup_ECWarningPopup")
              
    @property
    def ecwarningpopupokbutton(self):
        """ecwarningpopupokbutton"""
        return self.get_element("ECwarningpopupOk_ECWarningPopup")
              
    @property
    def ecwarningpopupclosebutton(self):
        """ecwarningpopupclosebutton"""
        return self.get_element("ECwarningpopupClose_ECWarningPopup")
              
    @property
    def warningpopupectextbox(self):
        """warningpopupectextbox"""
        return self.get_element("WarningpopupEC_ECWarningPopup")
              
    @property
    def ecpopupokbutton(self):
        """ecpopupokbutton"""
        return self.get_element("ECpopupOk_ECWarningPopup")
              