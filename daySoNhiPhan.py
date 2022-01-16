def solve(arr):
    ans = 0
    for i in range(n - 1):
        if arr[i] != arr[i + 1]:
            ans += 1
    return ans

n = int(input())
arr = [int(x) for x in input().split()]
res = solve(arr)
print(res)

