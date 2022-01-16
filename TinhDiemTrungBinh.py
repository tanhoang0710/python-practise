

n = int(input())
a = [float(x) for x in input().split()]
a.sort()
i = 1
while a[i] == a[0]:
    a.remove(a[i])
i = -2
while a[i] == a[-1]:
    a.remove(a[i])
a.remove(a[0])
a.remove(a[len(a) - 1])
# ko lam dc bang cach a = list(dict.fromtkeys(a)) vi nhu the se xoa di cac diem bang nhau ma kophai
# lon nhat hay nho nhat =>>> sai
sum = 0
for ele in a:
    sum += ele
avg = sum / len(a)
print("{:.2f}".format(avg), end='')

