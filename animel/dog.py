from animel import Animal

class Dog (Animal):

    def __init__(self, km):
        super().__init__()
        self.km = km

    def run(self):
        print("dog run km "+ str(self.km))

    def dogmakesound(self):
        super().makesound('hav hav')

    def move(Self):
        print ('dog move')