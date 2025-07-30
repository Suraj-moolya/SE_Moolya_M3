"""CurrentScreenWorkFlow"""  

from CurrentScreen import CurrentScreen
from TopologyExplorerTab import TopologyExplorerTab
from ControlExpert import ControlExpert
import Applicationutility
import Actionutility
import Conditionsutility

class CurrentScreenWorkFlow:
    """CurrentScreenWorkFlow"""
    currentscreen_obj = CurrentScreen()
    TopologyExplorerTab_obj = TopologyExplorerTab()
    ce_obj = ControlExpert()

        
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
        
    def closebuttontm(self):
        """TopologyExplorerTab_obj.Closetmbutton"""
        CurrentScreenWorkFlow.TopologyExplorerTab_obj.Closetmbutton.object.ClickButton()
        Applicationutility.wait_in_seconds(1000,"Wait")
        CurrentScreenWorkFlow.ce_obj.yescebuttonbutton.click()
        
        
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
            
    def clickokfromdbppopupwindow(self):
        """messagebox_obj.reconfirmokbutton"""
        CurrentScreenWorkFlow.TopologyExplorerTab_obj.passwordokbutton.click()
        
    def clickstartenginecheckbox(self):
        """clickstartenginecheckbox"""
        CurrentScreenWorkFlow.TopologyExplorerTab_obj.startenginecheckbox.click()
        
    def closebuttonplcbus(self):
        """TopologyExplorerTab_obj.Closetmbutton"""
        CurrentScreenWorkFlow.TopologyExplorerTab_obj.Closetmbutton.object.ClickButton()
        
    def clickyesmodificationwindow(self):
      CurrentScreenWorkFlow.ce_obj.yescebuttonbutton.click()
        
