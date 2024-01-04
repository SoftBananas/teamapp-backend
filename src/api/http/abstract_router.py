from abc import ABC, abstractmethod

from src.services.abstract_service import AbstractService


class AbstractRouter(ABC):
    service: AbstractService

    @abstractmethod
    def init_routes(self):
        pass
