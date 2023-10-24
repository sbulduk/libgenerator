from di_container import DependencyInjectionContainer
from application.file_controller import FileController
from application.converter_controller import ConverterController
from application.generator_controller import GeneratorController

container = DependencyInjectionContainer()

from core.file_service import FileService
from core.converter_service import ConverterService
from core.generator_service import GeneratorService

container.register(FileService,scope=None)
container.register(ConverterService,scope=None)
container.register(GeneratorService,scope=None)
container.register(FileController,scope=None,dependencies=[FileService])
container.register(ConverterController,scope=None,dependencies=[ConverterService])
container.register(GeneratorController,scope=None,dependencies=[GeneratorService])

def handle_request(controller_name,method_name,*args,**kwargs):
    controller=container.resolve(controller_name)
    method=getattr(controller,method_name)
    return method(*args,**kwargs)