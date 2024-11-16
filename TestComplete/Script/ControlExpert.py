"""ControlExpert"""
from MapBase import MapBase

class ControlExpert(MapBase):
    """ControlExpert"""
        
    @property
    def fullscreencebutton(self):
        """fullscreencebutton"""
        return self.get_element("FullScreenCE_ControlExpert")
              
    @property
    def closefullscreencebutton(self):
        """closefullscreencebutton"""
        return self.get_element("CloseFullScreenCE_ControlExpert")
              
    @property
    def propertiesofdeviceokcebutton(self):
        """propertiesofdeviceokcebutton"""
        return self.get_element("PropertiesofdeviceOKCE_ControlExpert")
              
    @property
    def propertiesofdevicecetextbox(self):
        """propertiesofdevicecetextbox"""
        return self.get_element("PropertiesofdeviceCE_ControlExpert")
              
    @property
    def unlocksafetyprotectioncebutton(self):
        """unlocksafetyprotectioncebutton"""
        return self.get_element("UnlockSafetyProtectionCE_ControlExpert")
              
    @property
    def newdevicecetextbox(self):
        """newdevicece_ControlExpert"""
        return self.get_element("newdevicece_ControlExpert")

    @property
    def yescebuttonbutton(self):
        """YesCEbutton_ControlExpert"""
        return self.get_element("YesCEbutton_ControlExpert")