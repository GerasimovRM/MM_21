lst = [1, 2, 3, 4]
it = map(lambda x: x ** 2, lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

lst = [1, 2, 3]
it = iter(lst)
while True:
    try:
        elem = next(it)
        print(elem)
    except StopIteration:
        break
