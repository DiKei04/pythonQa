from abc import ABC


class Animal(ABC):

    name=' '

    def __init__(self):
        self.time = 0

    def sleep(self , time=0):
        self.time = time
        print('sleep in hours: '+ str(self.time))

    def makesound(self, sound):
        self.sound = sound
        print(self.sound)

    @ABC.__abstractmethods__
    def move(slef):
        pass