
def check(s):
    reversed_s = s[::-1]  # dao nguoc 1 xau
    a1 = [str(ord(c)) for c in s]  # chuyen ve ma ascci
    a2 = [str(ord(c)) for c in reversed_s]
    for i in range(1, len(a1)):
        res1 = abs(int(a1[i]) - int(a1[i-1]))
        res2 = abs(int(a2[i]) - int(a2[i-1]))
        if res2 != res1:
            return False
    return True


t = int(input())

while t > 0:
    t -= 1
    s = input()
    if check(s):
        print('YES')
    else: print('NO')