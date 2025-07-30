from GSDAddition import GSDAddition
import GSDAdditionutility

class GSDAdditionWorkFlow:
    """GSDAdditionWorkFlow"""
    gsd_obj = GSDAddition()

    def clickbuttoningsdwindow(self, button_name):
        """clickbuttoningsdwindow"""
        try:
            GSDAdditionutility.click_button_in_gsd_window(button_name)
        except Exception as ex:
            raise Exception(ex) from ex

    def selectfolderingsdwindow(self, folder_name):
        """selectfolderingsdwindow"""
        try:
            GSDAdditionutility.select_folder_in_gsd(folder_name)
        except Exception as ex:
            raise Exception(ex) from ex 

    def handleduplicatefileingsdwindow(self, button):
        """selectfolderingsdwindow"""
        try:
            GSDAdditionutility.Handle_Duplicate_file(button)
        except Exception as ex:
            raise Exception(ex) from ex 

    def deletefileingsdwindow(self, item):
        """selectfolderingsdwindow"""
        try:
            GSDAdditionutility.delete_device_in_gsd(item)
        except Exception as ex:
            raise Exception(ex) from ex  

    def clickbuttoningsddeletewindow(self, button):
        """selectfolderingsdwindow"""
        try:
            GSDAdditionutility.click_button_in_gsd_delete_window(button)
        except Exception as ex:
            raise Exception(ex) from ex   

    def clickbuttoningsddeletepopupwindow(self, button):
        """clickbuttoningsddeletepopupwindow"""
        try:
            GSDAdditionutility.click_button_in_gsd_popup_window(button)
        except Exception as ex:
            raise Exception(ex) from ex 