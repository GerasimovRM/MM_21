d = {}  # d = dict()
d1 = {'hi': 'привет', 'cat': 'собака?'}
print(d1['cat'])
d1['ok'] = 'Хорошо'
print(d1)
# print(d1['hdsfjh'])
print(d1.get('sfsdfd', 'нету такого'))
print(d1)
print(d1.pop('ok'))
print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())
for key, value in d1.items():
    print(key, value)


x = [1, 2, 3, 4, 5, 10, 234]
for i, elem in enumerate(x):
    print(i, elem)
