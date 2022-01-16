class Student:
    def __init__(self, ten, d1, d2, d3):
        self.ten = ten
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def show(self):
        dtb = self.d1 * 0.1 + self.d2 * 0.3 + self.d3 * 0.6
        print(self.ten, format(dtb, '.1f'), end=' ')


ten = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())
s1 = Student(ten, d1, d2, d3)
s1.show()