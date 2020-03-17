str1 = input("A: ")
str2 = input("B: ")

set1 = set(str1)
set2 = set(str2)

print("A Union B:", str(set1.union(set2)))
print("A Difference B:", str(set1.difference(set2)))
print("A Intersection B:", str(set1.intersection(set2)))

set3 = set1.difference(set2)
set4 = set2.difference(set1)

print("A Triangular difference B:", str(set3.union(set4)))
