class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("META SINGLETON")
        print(*args, **kwargs)
        if cls not in cls._instances:
            print(*args, **kwargs)
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
