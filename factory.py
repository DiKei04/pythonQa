

class Cola(object):
    def drink(Self):
        print('dring Cola')

class Sprite(object):
    def drink(self):
        print('dring Sprite')

class Facory(object):
    def __init__(self , x):
        self.x = x

    def getObject(self):
        if self.x>10:
            return Cola()
        else:
            return Sprite()

