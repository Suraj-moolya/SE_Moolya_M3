"""SupervisionProjectWorkFlow"""  

from SupervisionProject import SupervisionProject
import Applicationutility
import Projectexplorertabutility


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
            
    def selectSPsettingheader(self,header):
            """selectSPsettingheader"""
            try:
                Projectexplorertabutility.Settings_SP(header)
            except Exception as ex:
                raise Exception(ex) from ex
                
    def verifypagetemplate(self):
        """verifypagetemplate"""
        try:
          Projectexplorertabutility.verify_page_template()
        except Exception as ex:
          raise Exception(ex) from ex
                    
    def clickonsystemmodel(self, button):
        """clickonsystemmodel"""
        try:
          Projectexplorertabutility.click_on_systemmodel(button)
        except Exception as ex:
          raise Exception(ex) from ex
          
    def clickonequipmentexportall(self, button1):
            """clickonequipmentexportall"""
            try:
              Projectexplorertabutility.click_on_equipment_exportall(button1)
            except Exception as ex:
              raise Exception(ex) from ex
              
    def exportequipment(self, name):
                """exportequipment"""
                try:
                  Projectexplorertabutility.Enter_systemName_systemlocation_ExportDataWindow_SPRefine(name)
                except Exception as ex:
                  raise Exception(ex) from ex
                  
    def exportdatasavebutton(self, btn):
                    """exportdatasavebutton"""
                    try:
                      Projectexplorertabutility.Click_on_Savebutton_in_ExportData(btn)
                    except Exception as ex:
                      raise Exception(ex) from ex
                      
    def systemmodelmenu(self, menu):
                        """refinesystemmodelmenu"""
                        try:
                          Projectexplorertabutility.Click_on_RefineSystemModel_menubar(menu)
                        except Exception as ex:
                          raise Exception(ex) from ex
    
    
            