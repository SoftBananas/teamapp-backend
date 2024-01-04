class DataBaseConfig:
    def __init__(self,
                 driver: str,
                 host: str,
                 port: int,
                 name: str,
                 user: str,
                 password: str):
        self.driver = driver
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
