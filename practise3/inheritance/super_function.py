class A:
    def __init__(self):
        self.x = 5

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 10

b = B()
print(b.x + b.y)
