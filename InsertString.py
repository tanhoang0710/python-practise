s1 = input()
s2 = input()

index = int(input())

s1 = s1[:index - 1] + s2 + s1[index - 1:]  # insert substring to a string

print(s1)
