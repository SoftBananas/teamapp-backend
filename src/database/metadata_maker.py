from sqlalchemy import MetaData

from src.database.connection import Connection


class MetadataMaker:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.metadata = MetaData()
        self.metadata.bind = self.connection.engine

    def get_metadata(self) -> MetaData:
        return self.metadata
