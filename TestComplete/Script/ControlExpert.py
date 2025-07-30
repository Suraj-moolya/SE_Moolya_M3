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
    def okmodaldialoguewindowce(self):
        """okmodaldialoguewindowce"""
        return self.get_element("ModaldialogwindowNewDevice_ControlExpert")
              
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
           

    @property
    def modaldialogewindowce(self):
        """modaldialogewindowce"""
        return self.get_element("Modaldialogwindow_ControlExpert")

    @property
    def modaldialogewindowoptionsce(self):
        """modaldialogewindowoptionsce"""
        return self.get_element("ModalDialogWindowoptions_ControlExpert")

    @property
    def dropdownbtnce(self):
        """dropdownbtnce"""
        return self.get_element("dropdownbutton_ControlExpert")

    @property
    def dropdownbtnoptionce(self):
        """dropdownbtnce"""
        return self.get_element("dropdownLbutton_ControlExpert")

    @property
    def addwindowce(self):
        """addwindowce"""
        return self.get_element("AddWindow_ControlExpert")

    @property
    def devicepropertywindowce(self):
        """devicepropertywindowce"""
        return self.get_element("DevicePropertyWindow_ControlExpert")

    @property
    def toolbarpopwindowce(self):
        """toolbarpopwindowce"""
        return self.get_element("ToolPopUP_ControlExpert")
        
    @property
    def buildanddeploychangesbutton(self):
        """buildanddeploychangesbutton"""
        return self.get_element("BuildandDeployChanges_ControlExpert")


    @property
    def dropdowntabce(self):
        """toolbarpopwindowce"""
        return self.get_element("DropDownTab_ControlExpert")

    @property
    def deviceoptionstabce(self):
        """toolbarpopwindowce"""
        return self.get_element("Deviceoptions_ControlExpert")

    @property
    def additionaloptionstabce(self):
        """toolbarpopwindowce"""
        return self.get_element("Additionaloptions_ControlExpert")



