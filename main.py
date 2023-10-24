from program import handle_request
from application.converter_controller import ConverterController
from application.file_controller import FileController
from application.generator_controller import GeneratorController
from core.converter_service import ConverterService
from core.file_service import FileService
from core.generator_service import GeneratorService
import os

def main():
    file_service=FileService()
    converter_service=ConverterService()
    generator_service=GeneratorService()

    file_controller=FileController(file_service)
    converter_controller=ConverterController(converter_service)
    generator_controller=GeneratorController(generator_service)
    
    while True:
        print("Choose an action:")
        print("1. Convert XML to Dictionary")
        print("2. Convert XML file to Dictionary")
        print("3. List Files in Directory")
        print("4. Generate .lis File")
        print("0. Exit")
        choice=input("Enter your choice: ")

        if choice=="1":
            xml_string = input("Enter the XML string: ")
            result=converter_controller.xml_string_to_dict(xml_string)
            print("Converted XML to Dictionary:")
            print(result)
        elif choice=="2":
            file_path=input("Enter the XML file path: ")
            if os.path.exists(file_path):
                with open(file_path,'r') as file:
                    xml_string=file.read()
                result=converter_controller.xml_string_to_dict(xml_string)
                print("Converted XML to Dictionary:")
                print(result)
            else:
                print(f"The file '{file_path}' does not exist.")
        elif choice=="3":
            dir_path=input("Enter the directory path: ")
            files=file_controller.dir_files(dir_path)
            print("Files in the directory:")
            for file in files:
                print(file)
        elif choice=="4":
            xml_file_path=input("Locate the xml file: ")
            xml_dict = xml_file_path
            lis_file_path=input("Enter the path for the .lis file: ")
            generator_controller.generate_lis_file(xml_dict,lis_file_path)
            print(f".lis file generated at {lis_file_path}")
        elif choice=="0":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__=="__main__":
    main()