# 1 3 5 9
# 2 2 4 8
# 0 2 4 6
# 2 2 2 6
# 0 0 4 4
# 0 4 0 4
# 4 4 4 4
## check cac ele cua a co bang 0 tat ko de nhap input
## check cac ele cua a xem co bang nhau het chua de thoat khoi vong lap
## cong thuc a[i] = abs(a[i] - a[i + 1]) rieng a[3] = a[0] trc

def check(a):
    for i in range(4):
        if a[i] != 0:
            return False
    return True

def solution(a):
    for i in range(3):
        if a[i] != a[i + 1]:
            return False
    return True

def solve(a):
    res = 0
    while not solution(a):
        tmp = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - tmp)
        res += 1
    print(res)




while True:
    a = [int(x) for x in input().split()]
    if check(a):
        break
    solve(a)
