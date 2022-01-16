def solve(s):
    digitString = ""
    characterString = ""
    for i in range(0, len(s)):
        if s[i] >= "0" and s[i] <= "9":
            digitString += s[i]
        else:
            characterString += s[i]

    sum = 0
    for i in digitString:
        sum += int(i)

    characterArr = []*len(characterString)

    for i in range(len(characterString)):
        characterArr.append(characterString[i])

    characterArrSorted = sorted(characterArr)
    characterArrSorted += str(sum)

    for i in range(len(characterArrSorted)):
        print(characterArrSorted[i], end='')
    print()


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)