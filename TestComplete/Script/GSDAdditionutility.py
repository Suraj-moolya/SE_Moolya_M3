import Applicationutility
import Topologyexplorerutility

from GSDAddition import GSDAddition

gsd_obj = GSDAddition()

###############################################################################
# Function : Handle_Duplicate_file
# Description : Handles duplicate file scenarios by clicking the specified button.
# Parameter : 
#   - button (str): The name of the button to click. Example: "Yes", "No".
###############################################################################
def Handle_Duplicate_file(button):
  Topologyexplorerutility.find_and_click_button(gsd_obj.duplicatefiletabingsdadditionwindow.object, "Do not", 100)
  Topologyexplorerutility.find_and_click_button(gsd_obj.duplicatefiletabingsdadditionwindow.object, button, 100)

###############################################################################
# Function : click_button_in_gsd_window
# Description : Clicks a button in the GSD addition window.
# Parameter : 
#   - button_name (str): The name of the button to click. Example: "Next", "Cancel".
###############################################################################
def click_button_in_gsd_window(button_name):
  Topologyexplorerutility.find_and_click_button(gsd_obj.homepageingsdadditionwindow.object, button_name, 100)
  
###############################################################################
# Function : select_folder_in_gsd
# Description : Selects a folder in the GSD addition window by navigating through the folder structure.
# Parameter : 
#   - items (str or list): Folder path as a string (e.g., "Folder1/Folder2") or a list of folder names.
###############################################################################
def select_folder_in_gsd(items):
  if isinstance(items, str):
    items = [item.strip() for item in items.split("/")]
  for item in items:
    Topologyexplorerutility.findallchildern_objecttype(
                              gsd_obj.choosefoldertabingsdadditionwindow.object, "OutlineItem", item, "Click", 
                              f"Clicked on item: {item}", f"Item with caption '{item}' not found."
                            )

###############################################################################
# Function : wait_for_gst_folder_select
# Description : Waits for the folder selection process to complete in the GSD addition window.
# Parameter : None
###############################################################################
def wait_for_gst_folder_select():
  updating_window = gsd_obj.loadingtabingsdadditionwindow.object
  if updating_window.WaitProperty("Exists", False, 500000):
    Log.Checkpoint("GSD Files Selected.")
  else:
    Log.Error("GSD Files did not Selected.")
                            
###############################################################################
# Function : delete_device_in_gsd
# Description : Deletes a device in the GSD addition window by double-clicking on the specified item.
# Parameter : 
#   - item (str): The name of the device to delete. Example: "Device1".
###############################################################################
def delete_device_in_gsd(item):
  Topologyexplorerutility.findallchildern_objecttype(
                            gsd_obj.devicedeletetabingsdadditionwindow.object, "OutlineItem", item, "DblClick", 
                            f"Clicked on item: {item}", f"Item with caption '{item}' not found."
                          )
                          
###############################################################################
# Function : click_button_in_gsd_popup_window
# Description : Clicks a button in the GSD device delete popup window.
# Parameter : 
#   - button_name (str): The name of the button to click. Example: "Yes", "No".
###############################################################################
def click_button_in_gsd_popup_window(button_name):
  Topologyexplorerutility.find_and_click_button(gsd_obj.devicedeletepopuptabingsdadditionwindow.object, button_name, 100)
                          
###############################################################################
# Function : click_button_in_gsd_delete_window
# Description : Clicks a button in the GSD device delete window.
# Parameter : 
#   - button_name (str): The name of the button to click. Example: "Delete", "Cancel".
###############################################################################
def click_button_in_gsd_delete_window(button_name):
  Topologyexplorerutility.find_and_click_button(gsd_obj.devicedeletetabingsdadditionwindow.object, button_name, 100)