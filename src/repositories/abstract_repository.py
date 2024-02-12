from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    model_table: type

    @abstractmethod
    async def create(self, model):
        raise NotImplementedError

    @abstractmethod
    async def get(self, model_id):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def update(self, model):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, model_id):
        raise NotImplementedError

    @abstractmethod
    async def delete_all(self):
        raise NotImplementedError
