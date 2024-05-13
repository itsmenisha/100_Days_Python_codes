class Food:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale,exale")


class Fish(Food):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("i am swiming")


machli = Fish()
machli.breathe()
machli.swim()
print(machli.num_eyes)
