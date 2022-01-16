class SoPhuc:
    def __init__(self, pt, pa):
        self.pt = int(pt)
        self.pa = int(pa)

    def cong(self, sp):
        t = self.pt + sp.pt
        a = self.pa + sp.pa
        return SoPhuc(t, a)

    def nhan(self, sp):
        t = self.pt * sp.pt - self.pa * sp.pa
        a = self.pt * sp.pa + self.pa * sp.pt
        return SoPhuc(t, a)

    def __str__(self):
        m = abs(self.pt)
        n = abs(self.pa)
        if self.pa > 0:
            return '{} + {}i'.format(self.pt, self.pa)
        else:
            return '{} - {}i'.format(self.pt, n)


t = int(input())
while t > 0:
    t -= 1
    s = input()
    arr = s.split()
    sp1 = SoPhuc(arr[0], arr[1])
    sp2 = SoPhuc(arr[2], arr[3])
    sp3 = (sp1.cong(sp2)).nhan(sp1)
    sp4 = (sp1.cong(sp2)).nhan(sp1.cong(sp2))
    print(sp3, ', ', sp4, sep='')
