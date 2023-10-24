from core.service_base import ServiceBase
from core.converter_service import ConverterService
from application.converter_controller import ConverterController
import os

class GeneratorService(ServiceBase):
    def generate_lis_file(self,xml_file_path,lis_file_path):
        if not(os.path.exists(lis_file_path)):
            with open(lis_file_path,"w") as file:
                pass
        with open(lis_file_path,"a") as file:
            converter_service=GeneratorService()
            converter_controller=ConverterController(converter_service)
            file.write("Hello")