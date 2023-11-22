from itertools import count, cycle, chain, groupby, product, tee

t = count(100, 10)

print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))

# for elem in cycle([1, 2, 3]):
#     print(elem)
lst = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [3, 4, 10]
matrix = [lst, lst2, lst3]
print(*chain(*matrix))

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
          ("animal", "cat"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]
for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
    print()

lst = [1, 2, 3, 4, 5, 6]
a, b, c = tee(iter(lst), 3)

print(*product('ABCD', 'xy', repeat=2))