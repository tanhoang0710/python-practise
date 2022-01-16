def check1(n):
    sum = 0
    while n > 0:
        sum += int(n % 10)
        n /= 10

    return int(sum % 10) == 0


def check2(num):
    s = str(num)
    for i in range(0, len(s) - 2):
        if abs(int(s[i+1]) - int(s[i])) != 2:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if check2(n) and check1(n):
        print("YES")
    else:
        print('NO')