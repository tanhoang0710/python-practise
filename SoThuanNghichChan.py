#kiem tra len va dao nguoc chuoi trc
def check1And3(n):
    s = str(n)
    if len(s) % 2 == 0 and s[::-1] == s:
        return True
    return False


def check2(n):
    s = str(n)
    for ele in s:
        if int(ele) % 2 == 1:
            return False
    return True


def solve(n):
    for i in range(22, n):
        if check1And3(i) and check2(i):
            print(i, end=' ')
    print()


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    solve(n)