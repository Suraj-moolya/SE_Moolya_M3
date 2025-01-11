import Applicationutility
import Topologyexplorerutility

from GSDAddition import GSDAddition

gsd_obj = GSDAddition()

def Handle_Duplicate_file(button):
  Topologyexplorerutility.find_and_click_button(gsd_obj.duplicatefiletabingsdadditionwindow.object, "Do not", 100)
  Topologyexplorerutility.find_and_click_button(gsd_obj.duplicatefiletabingsdadditionwindow.object, button, 100)

def click_button_in_gsd_window(button_name):
  Topologyexplorerutility.find_and_click_button(gsd_obj.homepageingsdadditionwindow.object, button_name, 100)

def select_folder_in_gsd(items):
  if isinstance(items, str):
    items = [item.strip() for item in items.split("/")]
  for item in items:
    Topologyexplorerutility.findallchildern_objecttype(
                              gsd_obj.choosefoldertabingsdadditionwindow.object, "OutlineItem", item, "Click", 
                              f"Clicked on item: {item}", f"Item with caption '{item}' not found."
                            )
def wait_for_gst_folder_select():
  updating_window = gsd_obj.loadingtabingsdadditionwindow.object
  if updating_window.WaitProperty("Exists", False, 500000):
    Log.Checkpoint("GSD Files Selected.")
  else:
    Log.Error("GSD Files did not Selected.")
                            
def delete_device_in_gsd(item):
  Topologyexplorerutility.findallchildern_objecttype(
                            gsd_obj.devicedeletetabingsdadditionwindow.object, "OutlineItem", item, "DblClick", 
                            f"Clicked on item: {item}", f"Item with caption '{item}' not found."
                          )
                          
def click_button_in_gsd_popup_window(button_name):
  Topologyexplorerutility.find_and_click_button(gsd_obj.devicedeletepopuptabingsdadditionwindow.object, button_name, 100)
                          
def click_button_in_gsd_delete_window(button_name):
  Topologyexplorerutility.find_and_click_button(gsd_obj.devicedeletetabingsdadditionwindow.object, button_name, 100)