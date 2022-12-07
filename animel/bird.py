from animel import Animal


class Bird (Animal):

    def __init__(self, km):
        super().__init__()
        self.__km = km

    def fly(self):
        print("Bird fly km "+ str(self.__km))

    def birdmakesound(self):
        super().makesound('cvi cvi')
    
    
    def move(Self):
        print ('bird move')