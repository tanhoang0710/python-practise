import math


class PhanSo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rutGon(self):
        t = math.gcd(self.x, self.y)
        self.x = self.x / t
        self.y = self.y / t

    def tong(self, p2):
        ts = self.x * p2.y + self.y * p2.x
        ms = self.y * p2.y
        p3 = PhanSo(ts, ms)
        p3.rutGon()
        return p3

    def __str__(self):
        return "{}/{}".format(int(self.x), int(self.y))


arr = [int(x) for x in input().split()]
p1 = PhanSo(arr[0], arr[1])
p2 = PhanSo(arr[2], arr[3])
p3 = p1.tong(p2)
print(p3)
