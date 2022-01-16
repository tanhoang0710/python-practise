#sorted 2 day neu co vi tri nao a[i] > b[i] thi return false

def check(a, b):
    a = sorted(a)
    b = sorted(b)
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = sorted(a)
    b = sorted(b)
    if check(a, b):
        print('YES')
    else:
        print('NO')


