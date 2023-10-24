from core.converter_service import ConverterService
from application.controller_base import ControllerBase

class ConverterController(ControllerBase):
    def __init__(self,converter_service:ConverterService):
        self.converter_service=converter_service

    def xml_to_dict(self,element)->dict:
        return self.converter_service.xml_to_dict(element)

    def xml_string_to_dict(self,xml_string:str)->dict:
        return self.converter_service.xml_string_to_dict(xml_string)