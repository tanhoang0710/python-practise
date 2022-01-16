# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Driver Code
lst1 = [5, 5, 5]
lst2 = [5, 5, 5]
print(intersection(lst1, lst2))