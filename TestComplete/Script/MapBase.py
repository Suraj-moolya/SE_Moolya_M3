""" mapbase"""
import os
from ControlRepository import ControlRepository
from UIElement import UIElement
from ProcessIdentifier import ProcessIdentifier


class MapBase:
    """MapBase Class"""

    repository_path = os.path.abspath(
        os.path.join(os.getcwd(), "ObjectRepository\\UIControlsRepository.xml")
    )
    control_repository = ControlRepository(repository_path)
    process = ProcessIdentifier()

    def __init__(self):
        self.process_identifier = ""
        # self.component_name = ""

    def get_element(self, element_name):
        """Get Element method"""
        return self.__get_element__(self.process_identifier, element_name)

    def get_element_with_props(self, process_identifier, props):
        """Get Element and props method"""
        return self.__find__(process_identifier, props)

    def get_props(self, element_name):
        """Get props method"""
        return self.__get_props__(element_name)

    def __get_element__(self, process_identifier, element_name):
        """get element"""
        props = self.__get_props__(element_name)
        if not Project.Variables.VariableExists("screen"):
          Project.Variables.AddVariable("screen", "String")
        if props["parent"] and props["parent"][1] != "":
          if len(props["parent"]) > 2:
            Project.Variables.screen = props["parent"][2]
          else:
            if "_" in element_name:
              Project.Variables.screen = element_name.split("_")[1]
        return self.__find__(process_identifier, props)

    def __get_props__(self, element_name):
        """get properties"""
        return self.control_repository.get_object_properties(element_name)

    def __find__(self, process_identifier, props):
        """find"""
        iteration_count = 0
        if not Project.Variables.VariableExists("retry_count"):
            Project.Variables.AddVariable("retry_count", "Integer")
        Project.Variables.retry_count = 10
        if not Project.Variables.VariableExists("time_interval"):
            Project.Variables.AddVariable("time_interval", "Integer")
        Project.Variables.time_interval = 1000
        # Log.Message(Project.Variables.retry_count)
        # Log.Message(Project.Variables.time_interval)
        while iteration_count < Project.Variables.retry_count:
            element = None
            try:
                if "FullName" in props["names"]:
                    # element identification with fullname
                    return UIElement(eval(props["values"][0]))
#                
                elif props["parent"][0] == 'ControlExpert':
                    element = UIElement(
                    self.__find__element__by_process__index(props["parent"][0], props)
                    )
#                
                elif not props["parent"]:
                    element = UIElement(
                        self.__find__element__(process_identifier, props)
                    )
                else:
                    # component_name = props["parent"][0]
                    process_identifier = props["parent"][0]
                    element_name = props["parent"][1]+"_"+Project.Variables.screen
                    if props["parent"][1] == "":
                        element = UIElement(
                            self.__find__element__(process_identifier, props)
                        )
                        if element.exists:
                          if element.visible:
                            return element
                    parent = self.__get_element__(process_identifier, element_name)
                    if parent is None:
                        return None
                    if element_name == "":
                        return parent
                    element = parent.find_child(props["names"], props["values"])
                if element.exists:
                    if element.visible:
                        #Log.Message("--Element is visible")
                        return element
                    iteration_count += 1
                    Log.Message("--Element Exist but it is not visible")
                    Delay(
                        Project.Variables.time_interval,
                        "Element is not Visible, Retrying for the element.....",
                    )
                else:
                    iteration_count += 1
                    Log.Message("--Element does not Exist")
                    Delay(
                        Project.Variables.time_interval,
                        "Element does not Exists, Retrying for the element.....",
                    )
            except Exception as ex:
                iteration_count += 1
                Delay(
                    Project.Variables.time_interval,
                    "Element not found, Retrying for the element.....",
                )
                # raise Exception(ex) from ex

    def __get_element_from_process__(
        self, process_name, process_index, prop_names, prop_values
    ):
        """get element from process"""

        try:
            process = Sys.Process(process_name, process_index)
            value = process.Find(prop_names, prop_values, 50, True)
            return value
        except Exception as ex:
            name = ".".join(prop_values)
            raise Exception(name + " control not found") from ex

    def __find_element__(self, process_info, prop_names, prop_values):
        """find element"""
        element = self.__get_element_from_process__(
            process_info[0], process_info[1], prop_names, prop_values
        )
        return element

    def __find__element__(self, process_info, props):
        """find element"""
        try:
            if str(process_info).find(", ") != -1:
                processdetail = process_info.split(", ")
                processdetail[1] = processdetail[1].strip()
                # Log.Message(processdetail[1])
                i = int(processdetail[1])
                # Log.Message(i)
                processname = processdetail[0]
                process = Sys.Process(processname, i)
            else:
                if Sys.WaitProcess(process_info).Exists:
                    process = Sys.Process(
                        process_info
                    )  # pylint: disable=undefined-variable
                   # Log.Message(process_info)
            #               Log.Message("gpcsim", 2)
            return process.Find(props["names"], props["values"], 50, True)
        except Exception as ex:
            Log.Message("Process was not available")

            
    def __find__element__by_process__index(self, processname, props):
        """find element"""
        obj = None
        count = Sys.FindAllChildren('ProcessName', processname)
        #Log.Message(len(count))
        for i in range(1, len(count)+1):
          #Log.Message(f'{i} i')
          try:
            if i == 1:
              process = Sys.Process(processname)
            else:

              process = Sys.Process(processname, i)

            if process.Exists:
              obj = process.Find(props["names"], props["values"], 50, True)
              #Log.Message(f'{processname} : {i}')
              if obj.Exists:
                if obj.Visible:
                  #Log.Message(f'{processname} : {i}')
                  break
            else:
              Log.Message(f'{processname} : {i} was not available')
          except Exception as ex:
            Log.Message(f"{processname} : {i} Process was not available")
        return obj            
            
    