"""OperationClientWorkFlow"""  

from OperationClient import OperationClient
import Operationclientutility

class OperationClientWorkFlow:
    """OperationClientWorkFlow"""
    operationclient_obj = OperationClient()

    def doubleclickinstanceedittorpage(self, identifier):
        """doubleclickinstanceepagedittor"""
        try:
            Operationclientutility.double_click_on_editor(identifier)
        except Exception as ex:
            raise Exception(ex) from ex 

    def verifyinstancestatustab(self):
        """verifyinstancestatustab"""
        try:
            Operationclientutility.verify_instance_edittor_status()
        except Exception as ex:
            raise Exception(ex) from ex