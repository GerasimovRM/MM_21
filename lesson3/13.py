lst = [1, 2, 3, 4, 546, 5467]
lst2 = [4, 5, 6, 10, 13]
print(*lst, sep='#')
print(*map(lambda x: x ** 2, lst))

print(*filter(lambda x: x % 2 == 0, lst))

print(*enumerate(lst))
print(*enumerate(lst, 5))

print(*zip(lst, lst2))
