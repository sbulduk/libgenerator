from application.controller_base import ControllerBase
from core.service_base import ServiceBase

class DependencyInjectionContainer:
    def __init__(self):
        self._services={}
        self._controllers={}

    def register(self,component,scope,dependencies=[]):
        if issubclass(component,ServiceBase):
            self._services[component]=(scope,dependencies)
        elif issubclass(component,ControllerBase):
            self._controllers[component]=(scope,dependencies)

    def get(self, component):
        if component in self._services:
            return self._get_service(component)
        elif component in self._controllers:
            return self._get_controller(component)

    def _get_service(self,service):
        # Implement service instantiation with dependencies
        # based on registered dependencies in the container
        pass

    def _get_controller(self,controller):
        # Implement controller instantiation with dependencies
        # based on registered dependencies in the container
        pass