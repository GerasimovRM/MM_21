lst = [1, 2, 3, 10, 15, 110, 324]

lst2 = []
for elem in lst:
    lst2.append(elem ** 2)

lst3 = [elem ** 2 for elem in lst]

def func(x):
    return x ** 2

lst4 = list(map(func, lst))


