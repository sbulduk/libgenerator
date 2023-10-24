from core.file_service import FileService
from application.controller_base import ControllerBase

class FileController(ControllerBase):
    def __init__(self,file_service:FileService):
        self.file_service=file_service

    def dir_files(self,dir_path):
        return self.file_service.dir_files(dir_path)
    
    def print_dict(self,printed_dict):
        return self.file_service.print_dict(printed_dict)