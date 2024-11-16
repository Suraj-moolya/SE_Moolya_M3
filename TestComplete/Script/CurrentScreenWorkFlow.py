"""CurrentScreenWorkFlow"""  

from CurrentScreen import CurrentScreen
import Applicationutility
import Actionutility
import Conditionsutility
class CurrentScreenWorkFlow:
    """CurrentScreenWorkFlow"""
    currentscreen_obj = CurrentScreen()

        
    def windowloginpageaccesstoapplication(self):
        """currentscreen_obj.loginpagewindow"""
#        try:
        Applicationutility.application_access()
        Log.Message("application access")
#        except Exception as ex:
#            raise Exception(ex) from ex
            
    def buttoncloseselected(self):
        """currentscreen_obj.closebutton"""
        CurrentScreenWorkFlow.currentscreen_obj.closebutton.click()
        
        
    def buttonengineeringclienttwolaunchengineeringclientsecondtime(self):
        """buttonengineeringclienttwolaunchengineeringclientsecondtime"""
        try:
            Actionutility.launch_engineering_client_with_secondtime()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonaepostconditionselected(self):
        """currentscreen_obj.aepostconditionbutton"""
        CurrentScreenWorkFlow.currentscreen_obj.aepostconditionbutton.click()
        
        
    def buttonaepostconditionclosealltabdeletessystem(self):
        """buttonaepostconditionclosealltabdeletessystem"""
        try:
            Conditionsutility.Post_Conditions_AE()
        except Exception as ex:
            raise Exception(ex) from ex
