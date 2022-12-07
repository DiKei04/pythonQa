from factory import Facory
from singleton import Singleton
if __name__ == '__main__':

    r = Facory(13)
    r.getObject().drink()

    r = Singleton()
    