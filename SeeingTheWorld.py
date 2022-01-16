place = ['france', 'italia', 'spain', 'england', 'usa', 'japan']

numbers = [8, 12, 3, 6, 2, 20, 15, 30]
print("Before sorted: ", numbers)
for i in range(len(numbers)):
    numbers[i] *= numbers[i]
print("After sorted and squared: ", sorted(numbers, reverse=True))

arrayTest = [1, 'a', 34, 'a', 'b', 1, 'c']
res = []
for i in arrayTest:
    if i not in res:
        res.append(i)
print(len(res))


