"""SupervisionProjectWorkFlow"""  

from SupervisionProject import SupervisionProject
import Applicationutility
class SupervisionProjectWorkFlow:
    """SupervisionProjectWorkFlow"""
    supervisionproject_obj = SupervisionProject()

        
    def buttonadvancesettingswindowspverifydisplayed(self):
        """supervisionproject_obj.advancesettingswindowspbutton"""
        try:
            element=SupervisionProjectWorkFlow.supervisionproject_obj.advancesettingswindowspbutton
            if element is not None:
                Log.Message('advancesettingswindowSP is displayed')
            else:
                Log.Error('advancesettingswindowSP is not displayed')
        except Exception as ex:
            raise Exception(ex) from ex
            