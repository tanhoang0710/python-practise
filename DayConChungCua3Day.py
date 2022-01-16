t = int(input())
while t > 0:
    t -= 1
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    check, m1, m2, m3 = 0, 0, 0, 0
    while m1 < n and m2 < m and m3 < k:
        if a[m1] == b[m2] == c[m3]:
            print(a[m1], end=' ')
            check = 1
            m1, m2, m3 = m1 + 1, m2 + 1, m3 + 1
        elif a[m1] < b[m2]: m1 += 1
        elif b[m2] < c[m3]: m2 += 1
        else: m3 += 1
    if check == 0:
        print('NO')
    print()
