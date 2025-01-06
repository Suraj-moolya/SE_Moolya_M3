"""DialogCEWorkFlow"""  

from DialogCE import DialogCE
import Applicationutility
import Controlexpertutility
from RefineOffline import RefineOffline

class DialogCEWorkFlow:
    """DialogCEWorkFlow"""
    dialogce_obj = DialogCE()
    refoff_obj = RefineOffline()

        
    def textboxdialogpanelcedblclickdialogpanelitemce(self,param):
        """textboxdialogpanelcedblclickdialogpanelitemce"""
#        try:
        Controlexpertutility.Dblclick_dialog_panel_item_CE(param)
#        except Exception as ex:
#            raise Exception(ex) from ex
        
    def textboxdialogpanelceclickdialogpanelitemce(self,param):
        """textboxdialogpanelceclickdialogpanelitemce"""
        try:
            Controlexpertutility.Click_dialog_panel_item_CE(param)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxdialoglistboxceselectbottomlistitemdialogpanelitemce(self,param):
        """textboxdialoglistboxceselectbottomlistitemdialogpanelitemce"""
#        try:
        Controlexpertutility.Select_bottom_listitem_dialog_panel_item_CE(param)
#        except Exception as ex:
#            raise Exception(ex) from ex
    def textboxdialoglistboxceselectbottomlistitemdialogpanelitemce1(self,param):
        """textboxdialoglistboxceselectbottomlistitemdialogpanelitemce"""
#        try:
        Controlexpertutility.Select_bottom_listitem_EIO_dialog_panel_item_CE(param)
#        except Exception as ex:
#            raise Exception(ex) from ex

    def buttondialogokceselected(self):
        """dialogce_obj.dialogokcebutton"""
        DialogCEWorkFlow.dialogce_obj.dialogokcebutton.click()
        #DialogCEWorkFlow.refoff_obj.parentdialogwindowcebutton.object.WaitProperty('Exists', 'None')
        
        
    def labelmessagedisplayed(self,content):
        """dialogce_obj.messagelabel"""
        Applicationutility.screen_displayed()
        
    def buttondialogstartsimulatorbutton(self):
        """dialogce_obj.dialogokcebutton"""
        DialogCEWorkFlow.dialogce_obj.startsimulatorbutton.click()
        Applicationutility.wait_in_seconds(1000,"Waiting for simulator to start")
        
    def buttondialogstartsimulatorbutton(self):
        """dialogce_obj.dialogokcebutton"""
        DialogCEWorkFlow.dialogce_obj.startsimulatorbutton.click()
        
    def textboxchangeportnumberplcsimulator(self):
        """textboxdialogpanelceclickdialogpanelitemce"""
        try:
            Controlexpertutility.change_Port_Number_PLC_Simulator()
        except Exception as ex:
            raise Exception(ex) from ex
            
    def buttonlistofmodifiedyesbuttonceselected(self):
            """dialogce_obj.listofmodifiedyesbuttoncebutton"""
            DialogCEWorkFlow.dialogce_obj.listofmodifiedyesbuttoncebutton.click()
        