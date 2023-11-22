lst = list()
for i in range(1, 20):
    if i % 2 == 1:
        lst.append(i ** 2)
print(lst)

lst = [i ** 2 for i in range(1, 20) if i % 2 == 1]

