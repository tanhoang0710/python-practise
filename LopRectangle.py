class Rectangle:
    def __init__(self, h, w, c):
        if int(h) <= 0 or int(w) <= 0:
            print('INVALID')
        else:
            self.h = h
            self.w = w
            self.c = c

    def perimeter(self):
        return (self.h + self.w) * 2

    def area(self):
        return self.h * self.w

    def color(self):
        char = self.c[0]
        return char.upper() + self.c[1:].lower()


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        t -= 1



