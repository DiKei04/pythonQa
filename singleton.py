class Singleton:
    _instance = None


    def __new__(cls):
        if cls._instance is None:
            print("creating the object")
            cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance