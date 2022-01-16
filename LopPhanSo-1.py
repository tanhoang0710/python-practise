import math


class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rutGon(self):
        t = math.gcd(self.x, self.y)
        self.x = self.x / t
        self.y = self.y / t

    def __str__(self):
        return "{}/{}".format(int(self.x), int(self.y))


x, y = [int(x) for x in input().split()]
p1 = PhanSo(x, y)
p1.rutGon()
print(p1)
