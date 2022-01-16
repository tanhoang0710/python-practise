s = input()

numbersOf4 = s.count('4')
numbersOf7 = s.count('7')
if numbersOf4 + numbersOf7 == 4 or numbersOf4 + numbersOf7 == 7:
    print('YES')
else:
    print('NO')
