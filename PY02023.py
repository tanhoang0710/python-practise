def tongcs(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def solve(a):
    for i in range(1, len(a)):
        for j in range(0, i):
            if tongcs(a[i]) <= tongcs(a[j]):
                a[i], a[j] = a[j], a[i]
                if tongcs(a[i]) == tongcs(a[j]):
                    if a[i] < a[j]:
                        a[i], a[j] = a[j], a[i]
    for ele in a:
        print(ele, end=' ')
    print()


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    solve(a)
