# a = input('Nhap ten: ')
# print('Hello ' + str(a) + '!')

# def sum(a, b):
#     ans = a + b
#     print(ans)
#
#
# a = int(input())
# b = int(input())
# sum(a, b)

def tinh_tong(n):
    i= 1
    s= 0
    while i <= n:
        s += i / (i+1)
        i += 1
    return s

n = int(input())
s = tinh_tong(n)
print(s)
# tinh_tong(n)