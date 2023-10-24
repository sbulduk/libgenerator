from di_container import DependencyInjectionContainer
from application.converter_controller import ConverterController
from application.file_controller import FileController

container = DependencyInjectionContainer()

from core.converter_service import ConverterService
from core.file_service import FileService

container.register(ConverterService,scope=None)
container.register(FileService,scope=None)
container.register(ConverterController,scope=None,dependencies=[ConverterService])
container.register(FileController,scope=None,dependencies=[FileService])

def handle_request(controller_name,method_name,*args,**kwargs):
    controller=container.resolve(controller_name)
    method=getattr(controller, method_name)
    return method(*args,**kwargs)