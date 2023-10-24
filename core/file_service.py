import os
from core.service_base import ServiceBase

class FileService(ServiceBase):
    def dir_files(self,dir_path:str)->dict:
        file_list=os.listdir(dir_path)
        if(len(file_list)==0):
            return False
        return file_list
    
    def print_dict(self,printed_dict:dict):
        for key, value in printed_dict.items():
            if isinstance(value, dict):
                print(f"{key}:\n")
                for inner_key, inner_value in value.items():
                    print(f"  {inner_key}: {inner_value}\t\n")
            else:
                print(f"test {key}: {value} test")