def func(lst):
    lst = lst.copy()
    lst.append(10)
    print(lst)


k = [1, 2, 3]
func(k)
print(k)