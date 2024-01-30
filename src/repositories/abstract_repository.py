from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    model_table: type

    @abstractmethod
    async def add(self, model):
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, model_id):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def edit(self, model):
        raise NotImplementedError

    @abstractmethod
    async def remove(self, model_id):
        raise NotImplementedError

    @abstractmethod
    async def remove_all(self):
        raise NotImplementedError
