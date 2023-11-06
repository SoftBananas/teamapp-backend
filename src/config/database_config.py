import os


class DataBaseConfig:
    driver: str
    host: str
    port: int
    name: str
    user: str
    password: str

    def __init__(self):
        self.__set_params()

    def __set_params(self) -> None:
        self.driver = os.environ.get("DB_DRIVER")
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
        self.name = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASSWORD")
