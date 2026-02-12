class Bird:
    def move(self):
        print("fly")

class Penguin(Bird):
    def move(self):
        print("walk")

p = Penguin()
p.move()
