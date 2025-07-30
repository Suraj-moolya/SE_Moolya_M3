"""WindowsExplorerWorkFlow"""  

from WindowsExplorer import WindowsExplorer
import Applicationutility
import Systemserverutility
import Actionutility
class WindowsExplorerWorkFlow:
    """WindowsExplorerWorkFlow"""
    windowsexplorer_obj = WindowsExplorer()

        
    def buttonshowhiddeniconopensystemserverconsole(self):
        """buttonshowhiddeniconopensystemserverconsole"""
        try:
            Systemserverutility.rclick_system_server_show_server_console()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def parentwindowslaunchengineeringclient(self):
        """parentwindowslaunchengineeringclient"""
        try:
            Actionutility.launch_engineering_client()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def parentwindowsopendetailstabintaskmanager(self):
        """parentwindowsopendetailstabintaskmanager"""
        try:
            Actionutility.open_select_details_tab_TM()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def textboxdetaillistverifycontrolexpertinstancesintaskmanager(self,instances):
        """textboxdetaillistverifycontrolexpertinstancesintaskmanager"""
        try:
            Actionutility.check_CE_instances_TM(instances)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttontabsterminatealltestedapps(self):
        """buttontabsterminatealltestedapps"""
        try:
            Applicationutility.wait_in_seconds(2000, 'Wait')
            Applicationutility.screen_displayed()
        except Exception as ex:
            raise Exception(ex) from ex

    def buttontabsterminateec(self):
        """buttontabsterminatealltestedapps"""
        try:
            Applicationutility.wait_in_seconds(5000, 'Wait')
            Systemserverutility.close_x_EC()
            Applicationutility.wait_in_seconds(5000, 'Wait')
        except Exception as ex:
            raise Exception(ex) from ex
       