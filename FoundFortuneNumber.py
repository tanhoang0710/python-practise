test = input()
t = int(test)
while t > 0:
    n = input();
    if int(n) % 100 == 86:
        print('YES')
    else:
        print('NO')
    t-=1