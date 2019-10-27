class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"x: {self.x}, y: {self.y}")

    def __repr__(self):
        print(f"Point({self.x}, {self.y})")


p1 = Point(10, 10)
p1.__str__()
p1.__repr__()
