def rotate(s, sum):
    a = list(s)
    # s1[i] = ((s1[i]-65+sum)%26)+65;
    for i in range(len(a)):
        a[i] = chr(((ord(a[i]) - 65 + sum) % 26) + 65)
    return a


def merge(s1, s2):
    # ((s1[i]-65+(s2[i]-65))%26)+65
    for i in range(len(s1)):
        s1[i] = chr((((ord(s1[i])-65)+(ord(s2[i])-65)) % 26) + 65)
    for ele in s1:
        print(ele, end='')
    print()


def solve(s):
    half = len(s) // 2
    sum1, sum2 = 0, 0
    s1 = s[:half]
    for i in range(half):
        sum1 += ord(s[i]) - 65
    s2 = s[half:]
    for i in range(half, len(s)):
        sum2 += ord(s[i]) - 65
    s1 = rotate(s1, sum1)
    s2 = rotate(s2, sum2)
    merge(s1, s2)


t = int(input())

while t > 0:
    s = input()
    solve(s)
    t -= 1
