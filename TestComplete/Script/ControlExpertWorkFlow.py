"""ControlExpertWorkFlow"""  

from ControlExpert import ControlExpert
import Applicationutility
import Controlexpertutility
class ControlExpertWorkFlow:
    """ControlExpertWorkFlow"""
    controlexpert_obj = ControlExpert()

        
    def buttonpropertiesofdeviceokceselected(self):
        """controlexpert_obj.propertiesofdeviceokcebutton"""
        ControlExpertWorkFlow.controlexpert_obj.propertiesofdeviceokcebutton.click()
        
        
    def buttonfullscreenceselected(self):
        """controlexpert_obj.fullscreencebutton"""
        ControlExpertWorkFlow.controlexpert_obj.fullscreencebutton.click()
        
        
    def buttonclosefullscreenceselected(self):
        """controlexpert_obj.closefullscreencebutton"""
        ControlExpertWorkFlow.controlexpert_obj.closefullscreencebutton.click()
        
        
    def buttonunlocksafetyprotectionceselected(self):
        """controlexpert_obj.unlocksafetyprotectioncebutton"""
        ControlExpertWorkFlow.controlexpert_obj.unlocksafetyprotectioncebutton.click()
        
    def ClicktabitemEIOconfigwindow(self,identifiers):
            """ClicktabitemEIOconfigwindow"""
            try:
                Controlexpertutility.Click_tab_item_EIO_config_window(identifiers)
            except Exception as ex:
                raise Exception(ex) from ex  
                
    def buttonbuildanddeploychangesselected(self):
            """controlexpert_obj.buildanddeploychangesbutton"""
            ControlExpertWorkFlow.controlexpert_obj.buildanddeploychangesbutton.click()  
        
        