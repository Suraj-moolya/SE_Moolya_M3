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
        