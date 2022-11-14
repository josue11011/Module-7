# Program Name: Unique num
# Name: Josue Cifuentes
# Date: November 12, 2022
# Purpose of a Program: To create a new list where elements are unique

def unique(lst):
    x = []
    for a in lst:
     if a not in x:
        x.append(a)
    return x
print(unique([1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]))