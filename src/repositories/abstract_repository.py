from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add(self):
        raise NotImplementedError

    @abstractmethod
    async def find(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def edit(self):
        raise NotImplementedError

    @abstractmethod
    async def delete(self):
        raise NotImplementedError
