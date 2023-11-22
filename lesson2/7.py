s = {1, 2, 3, None, True, 3.5, 1, 1}
print(s)
lst = [1, 1, 2, 2, 3, 3, False]
s2 = set(lst)
print(s2)
lst = list(s2)
print(lst)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
s1.intersection_update(s2)
print(s1)
