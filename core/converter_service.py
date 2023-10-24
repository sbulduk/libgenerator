import xml.etree.ElementTree as ET
from core.service_base import ServiceBase

class ConverterService(ServiceBase):
    def xml_to_dict(self,element)->dict:
        result = {}
        if element.text and element.text.strip():
            result[element.tag]=element.text
        for child in element:
            child_data=self.xml_to_dict(child)
            if child.tag in result:
                if isinstance(result[child.tag],list):
                    result[child.tag].append(child_data)
                else:
                    result[child.tag]=[result[child.tag],child_data]
            else:
                result[child.tag]=child_data
        return result

    def xml_string_to_dict(self,xml_string:str)->dict:
        root=ET.fromstring(xml_string)
        return {root.tag: self.xml_to_dict(root)}