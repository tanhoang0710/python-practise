import math

# Cach lam: tim cac so nguyen to gan nhat cua cac so nguyen to trong day roi so sanh xem hieu
# cua so ngto do voi so do so nao nho nhat
def nearest_prime(n):
    incr = -1
    multiplier = -1
    count = 1
    while True:
        if prime(n):
            return n
        else:
            n = n + incr
            multiplier = multiplier * -1
            count = count + 1
            incr = multiplier * count


def prime(n):
    if n < 2:
        return False
    sqrt = int(math.sqrt(n)) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(x) for x in input().split()]
tmp = []
for i in range(n):
    tmp.append(abs(nearest_prime(a[i]) - a[i]))
print(max(tmp))
