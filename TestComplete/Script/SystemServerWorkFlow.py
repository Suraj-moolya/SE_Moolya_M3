"""SystemServerWorkFlow"""  

from SystemServer import SystemServer
import Applicationutility
import Systemserverutility
class SystemServerWorkFlow:
    """SystemServerWorkFlow"""
    systemserver_obj = SystemServer()

        
    def textboxusernameentered(self,userName1):
        """systemserver_obj.usernametextbox"""
        SystemServerWorkFlow.systemserver_obj.usernametextbox.enter_text(userName1)
        
    def textboxpasswordentered(self,password2):
        """systemserver_obj.passwordtextbox"""
        SystemServerWorkFlow.systemserver_obj.passwordtextbox.enter_text(password2)
        
    def buttonloginselected(self):
        """systemserver_obj.loginbutton"""
        SystemServerWorkFlow.systemserver_obj.loginbutton.click()
        
    def buttonClickonTabEnter(self):
            """Systemserverutility.Click_on_Tab_Enter"""
            try:
              Systemserverutility.Click_on_Tab_Enter()
            except Exception as ex:
                raise Exception(ex) from ex
                
    def buttonverifystartstopdisabled(self):
                """Systemserverutility.verify_start_stop_disabled"""
                try:
                  Systemserverutility.verify_start_stop_disabled()
                except Exception as ex:
                    raise Exception(ex) from ex
        
        
    def buttonactionmenuselected(self):
        """systemserver_obj.actionmenubutton"""
        SystemServerWorkFlow.systemserver_obj.actionmenubutton.click()
        
        
    def buttonstartserverselected(self):
        """systemserver_obj.startserverbutton"""
        SystemServerWorkFlow.systemserver_obj.startserverbutton.click()
        
    def buttonstopserverselected(self):
            """systemserver_obj.startserverbutton"""
            SystemServerWorkFlow.systemserver_obj.stopserverbutton.click()
        
        
    def buttonflowdocumentverifysystemserverready(self):
        """buttonflowdocumentverifysystemserverready"""
        try:
            Systemserverutility.check_server_ready()
        except:
            Log.Message('...')
            
    def buttonflowdocumentverifysystemserverstop(self):
            """buttonflowdocumentverifysystemserverready"""
            try:
                Systemserverutility.check_server_stop()
            except Exception as ex:
                raise Exception(ex) from ex
        
    def labelmessagedisplayed(self,content):
        """systemserver_obj.messagelabel"""
        Applicationutility.screen_displayed()
        
    def textboxlogondialogueverifycontent(self,logOnDialogue3):
        """systemserver_obj.logondialoguetextbox"""
        content = SystemServerWorkFlow.systemserver_obj.logondialoguetextbox.object
        if str(content.Text.OleValue) in logOnDialogue3:
          Log.Checkpoint(str(content.Text.OleValue))
        else:
          Log.Warning(str(content.Text.OleValue))
          Log.Message(logOnDialogue3)
          
          
    def windowconsoleverifytextinsystemserverconsole(self,verify_message):
        """windowconsoleverifytextinsystemserverconsole"""
#        try:
        Systemserverutility.check_server_console_flowdocument(verify_message)
#        except Exception as ex:
#            raise Exception(ex) from ex
        
    def windowconsoleselectfromsystemservericon(self,element):
        """windowconsoleselectfromsystemservericon"""
        try:
            Systemserverutility.system_server_icon_rclick_on(element)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def windowconsoleselected(self,console):
        """systemserver_obj.consolewindow"""
        SystemServerWorkFlow.systemserver_obj.consolewindow.click()
        
        
    def windowconsoleverifylicenseinsystemserver(self):
        """windowconsoleverifylicenseinsystemserver"""
        try:
            Systemserverutility.check_flowdocument_license()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonloginstartsystemserver(self):
        """buttonloginstartsystemserver"""
        try:
            Systemserverutility.start_system_server()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonsettingsmenuselected(self):
        """systemserver_obj.settingsmenubutton"""
        SystemServerWorkFlow.systemserver_obj.settingsmenubutton.click()
        
        
    def buttonbasicsettingsselected(self):
        """systemserver_obj.basicsettingsbutton"""
        SystemServerWorkFlow.systemserver_obj.basicsettingsbutton.click()
        
        
    def buttonnextselected(self):
        """systemserver_obj.nextbutton"""
        SystemServerWorkFlow.systemserver_obj.nextbutton.click()
        
        
    def textboxcontrolparticipantmaxinstanceentered(self,controlParticipantMaxInstance3):
        """systemserver_obj.controlparticipantmaxinstancetextbox"""
        SystemServerWorkFlow.systemserver_obj.controlparticipantmaxinstancetextbox.enter_text(controlParticipantMaxInstance3)
        
    def buttonsaveandcloseselected(self):
        """systemserver_obj.saveandclosebutton"""
        SystemServerWorkFlow.systemserver_obj.saveandclosebutton.click()
        
        
    def windowconsoleverifynumberofcontrolinstances(self,instances):
        """windowconsoleverifynumberofcontrolinstances"""
        try:
            Systemserverutility.check_flowdocument_control_instances(instances)
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonhostingselected(self):
        """systemserver_obj.hostingbutton"""
        SystemServerWorkFlow.systemserver_obj.hostingbutton.click()
        
        
    def textboxcontrolparticipantmaxinstanceverifyinvalidcontrolinstanceinhosting(self):
        """textboxcontrolparticipantmaxinstanceverifyinvalidcontrolinstanceinhosting"""
        try:
            Systemserverutility.verify_invalid_hosting_control_instances()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttoncancelselected(self):
        """systemserver_obj.cancelbutton"""
        SystemServerWorkFlow.systemserver_obj.cancelbutton.click()
        
        
    def buttonhostingterminatealltestedapps(self):
        """buttonhostingterminatealltestedapps"""
        try:
            Systemserverutility.terminate_tested_apps()
        except Exception as ex:
            raise Exception(ex) from ex
        
    def buttonstartserververifydisabled(self):
        """systemserver_obj.startserverbutton"""
        if SystemServerWorkFlow.systemserver_obj.startserverbutton.enabled:
            Log.Error('Startserver is enabled')
        else:
            Log.Message("Startserver is disabled")
            
    def verifylogindialogue(self):
      try:
        Systemserverutility.verify_SS_LoginDialogue()
      except Exception as ex:
        raise Exception(ex) from ex 
            
    def selectoptioninserversettings(self, option):
      try:
        Systemserverutility.select_settings_submenu_systemserver(option)
      except Exception as ex:
        raise Exception(ex) from ex 
            
    def selectoptioninsystembackupshedulerdropdown(self, system):
      try:
        Systemserverutility.select_system_in_systembackupsheduler(system)
      except Exception as ex:
        raise Exception(ex) from ex 
            
    def checkboxsystembackupsheduler(self, prop):
      try:
        Systemserverutility.checkboxinsystembackup(prop)
      except Exception as ex:
        raise Exception(ex) from ex 
            
    def selectfreqbackupsheduler(self, freq):
      try:
        Systemserverutility.select_frequency_in_system_backup(freq)
      except Exception as ex:
        raise Exception(ex) from ex
        
    def systembackupsavebuttonselected(self):
        """systemserver_obj.systembackupsavebutton"""
        SystemServerWorkFlow.systemserver_obj.systembackupsavebutton.click()
            
    def confiramtionpopup(self, button):
      try:
        Systemserverutility.system_server_popup(button)
      except Exception as ex:
        raise Exception(ex) from ex
            
    def saveaswindowbutton(self, button):
      try:
        Systemserverutility.clicksaveaswindowbutton(button)
      except Exception as ex:
        raise Exception(ex) from ex
        
    def usernamedropdown(self):
      try:
        Systemserverutility.click_on_username_dropdown()
      except Exception as ex:
        raise Exception(ex) from ex
        
    def SSlogout(self,param):
      try:
        Systemserverutility.click_on_menuitem_Usericon(param)
      except Exception as ex:
        raise Exception(ex) from ex
         
    def SSlogin(self):
          try:
            Systemserverutility.click_on_login()
          except Exception as ex:
            raise Exception(ex) from ex
    
    def maintenancemode(self, mode):
      try:
        Systemserverutility.enter_maintenance_mode(mode)
      except Exception as ex:
        raise Exception(ex) from ex
        
    def entermaintenancepassword(self, password, key):
          try:
            Systemserverutility.enter_maintenance_password(password, key)
          except Exception as ex:
            raise Exception(ex) from ex
            
    def databasedeleteall(self, command, key):
              try:
                Systemserverutility.database_deleteall(command, key)
              except Exception as ex:
                raise Exception(ex) from ex
            
    def backupwindowcheckbox(self, prop):
      try:
        Systemserverutility.backup_window_checkbox(prop)
      except Exception as ex:
        raise Exception(ex) from ex
            
    def backupwindowbutton(self, button):
      try:
        Systemserverutility.backup_window_button(button)
      except Exception as ex:
        raise Exception(ex) from ex