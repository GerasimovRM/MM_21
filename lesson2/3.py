lst = [1, 2, 3, 3 ]
lst[0] = 0
lst.remove(3)
lst.append(10)
lst.insert(1, 5)
elem = lst.pop(1)
lst2 = lst[:]
lst2.clear()
print(lst)

lst = [1, 2, 3]
lst2 = [4, 5, 6]
lst.extend(lst2)
print(lst)
