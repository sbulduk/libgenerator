from application.controller_base import ControllerBase
from core.generator_service import GeneratorService

class GeneratorController(ControllerBase):
    def __init__(self,generator_service:GeneratorService):
        self.generator_service = generator_service

    def generate_lis_file(self,xml_file_path,lis_file_path):
        self.generator_service.generate_lis_file(xml_file_path,lis_file_path)