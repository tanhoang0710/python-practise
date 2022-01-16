def solve(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)  #sorted tra ve 1 mang
    s2 = sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    print(f'Test {i + 1}: ', end='')
    if solve(s1, s2):
        print('YES')
    else:
        print('NO')
