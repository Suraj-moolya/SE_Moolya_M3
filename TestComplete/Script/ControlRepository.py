"""ControlRepository"""
import xml.etree.ElementTree as elementTree
import copy


class ControlRepository:
    """ControlRepository Class"""
    def __init__(self, xml_file: str):
        """__init__"""
        self.xmlfile = xml_file
        self.objects = {}

    def parse_object_repository(self):
        """parse_object_repository"""
        if not self.objects:
            self.parse_xml()

    def parse_xml(self):
        """read the xml object repository file"""
        tree = elementTree.parse(self.xmlfile)
        root = tree.getroot()
        for component in root.findall('./Component'):
            #component_name = component.attrib['name']
            for ui_control in component:
                element_name = ui_control.attrib["Element"]
                element_key = "_" + element_name
                keys = list(ui_control.attrib.keys())
                values = list(ui_control.attrib.values())
                is_controltype_attribute_present = 'ControlType' in keys
                if is_controltype_attribute_present:
                    control_type_index = keys.index('ControlType')
                    del keys[control_type_index]
                    del values[control_type_index]
                parent = []
                if 'Parent' in keys:
                    parent_index = keys.index('Parent')
                    keys.pop(parent_index)
                    parent = values.pop(parent_index).split('_')
                keys.pop(0)
                values.pop(0)
                props = {'names': keys, 'values': values, 'parent': parent}
                self.objects[element_key] = props

    def get_object_properties(self, element_name):
        """get_object_properties"""
        self.parse_object_repository()
#        Log.Message(element_name)
        return self.__get_props__(self.objects["_" + element_name])

    def get_parent(self, component_element_name):
        """get_parent"""
        self.parse_object_repository()
        return self.__get_props__(self.objects[component_element_name])

    def __get_props__(self, props):
        return copy.deepcopy(props)
  