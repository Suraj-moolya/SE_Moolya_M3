"""ECWarningPopupWorkFlow"""  

from ECWarningPopup import ECWarningPopup
import Applicationutility
import Engineeringclientutility
class ECWarningPopupWorkFlow:
    """ECWarningPopupWorkFlow"""
    ecwarningpopup_obj = ECWarningPopup()

        
    def textboxwarningpopupverifywindowsmessage(self,verify_message):
        """textboxwarningpopupverifywindowsmessage"""
        try:
            Engineeringclientutility.verify_warning_popup(verify_message)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonecwarningpopupokselected(self):
        """ecwarningpopup_obj.ecwarningpopupokbutton"""
        ECWarningPopupWorkFlow.ecwarningpopup_obj.ecwarningpopupokbutton.click()
        
    def buttonecwarningpopupokselected1(self):
        """ecwarningpopup_obj.ecwarningpopupokbutton"""
        ECWarningPopupWorkFlow.ecwarningpopup_obj.ecpopupokbutton.click()
        
    def buttonecwarningpopupclosecloseecpopup(self):
        """buttonecwarningpopupclosecloseecpopup"""
        try:
            Engineeringclientutility.warning_popup_close()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxwarningpopupecverifyecpopupmessage(self,verify_message):
        """textboxwarningpopupecverifyecpopupmessage"""
        try:
            Engineeringclientutility.verify_ec_warning_popup(verify_message)
        except Exception as ex:
            raise Exception(ex) from ex
        