class ThiSinh:
    def __init__(self, ht, ns, d1, d2, d3):
        self.ht = ht
        self.ns = ns
        self.d1 = float(d1)
        self.d2 = float(d2)
        self.d3 = float(d3)

    def __str__(self):
        tong = format(self.d1 + self.d2 + self.d3, '.1f')
        return "{} {} {}".format(self.ht, self.ns, tong)


ten = input()
ns = input()
d1 = input()
d2 = input()
d3 = input()
ts = ThiSinh(ten, ns, d1, d2, d3)
print(ts)