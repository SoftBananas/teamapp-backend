class DataBaseConfig:
    driver: str
    host: str
    port: int
    name: str
    user: str
    password: str

    def __init__(self, driver, host, port, name, user, password):
        self.driver = driver
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
