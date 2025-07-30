from TopologyExplorerTab import TopologyExplorerTab
import Applicationutility
import Engineeringclientutility
import Projectexplorertabutility
import Applicationexplorertabutility
from MessageBox import MessageBox


topo_obj = TopologyExplorerTab()
msg_obj = MessageBox()



def TC_EPE_AE_0040_Replace_template_AE(parameter):
  Applicationexplorertabutility.right_click_application_browser_template_AE('MotorGP$$1.0.123')
  param = Applicationexplorertabutility.capture_template_application_browser_AE('MotorGP_1')
  Engineeringclientutility.select_ContextMenu_Items_EC('Replace Template')
  Applicationutility.wait_in_seconds(1000, 'Wait')
  msg_obj.modaldialogwindowtextbox.verify_object('Replace instance template window')
  Applicationexplorertabutility.replace_template_combo_AE('ValveGP$$1.0.100')
  if parameter == 'OK':
    msg_obj.modaldialogwindowtextbox.ocr_blockby_text('OK')
  elif parameter == 'Cancel':
    msg_obj.modaldialogwindowtextbox.ocr_blockby_text('Cancel')
  elif parameter == 'Close':
    msg_obj.modaldialogwindowtextbox.object.Close()
  Applicationutility.wait_in_seconds(3000, 'Wait')
  Applicationexplorertabutility.verify_template_replaced_AE(param)
  
  
def Generate_and_build_TC_EPE_AE_0039():
  Projectexplorertabutility.double_click_control_project_browser_PE('Containers')
  Projectexplorertabutility.right_click_control_project_browser_PE('ControlExecutable_1')
  Engineeringclientutility.select_ContextMenu_Items_EC('Generate and Build')
  Applicationutility.wait_for_execution()
  Applicationutility.wait_in_seconds(1000, 'Wait')
  Applicationutility.modal_dialog_window_button('Yes')
  Applicationutility.modal_dialog_window_button('OK')