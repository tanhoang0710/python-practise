
def check(num):
    for i in range(0, len(num) - 1):
        if int(num[i]) > int(num[i+1]):
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')
