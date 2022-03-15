class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def get_quarter(self):
        if self.x > 0:
            if self.y > 0:
                return 1
            if self.y < 0:
                return 4
        if self.x < 0:
            if self.y > 0:
                return 2
            if self.y < 0:
                return 3
        return 0


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)
        self.c = Point(x3, y3)

    def __eq__(self, other):
        if self.a.__eq__(other.a) and self.b.__eq__(other.b) and self.c.__eq__(other.c):
            return True
        return False

    def __str__(self):
        return "A({0}, {1}), B({2}, {3}), C({4}, {5})".format(
            self.a.x, self.a.y,
            self.b.x, self.b.y,
            self.c.x, self.c.y,
        )

    def quarter(self):
        if self.a.get_quarter() == self.b.get_quarter() == self.c.get_quarter() > 0:
            return True
        return False

    def exist(self):
        if 0 == abs((self.a.x-self.c.x)*(self.b.y-self.c.y)-(self.b.x-self.c.x)*(self.a.y-self.c.y)):
            return False
        return True


def one_quarter(name):
    triangles = []
    with open(name, "r") as f:
        for line in f:
            x1, y1, x2, y2, x3, y3 = (int(number) for number in line.split())
            triangle = Triangle(x1, y1, x2, y2, x3, y3)
            if triangle.exist() and triangle.quarter():
                triangles.append(triangle)
    return triangles


if __name__ == '__main__':
    for triangle in one_quarter("input files/input.txt"):
        print(triangle)