def func(a, b=3, *args, h=123, j=123, **kwargs):
    print(a, b)
    print(args)
    print(h, j)
    print(kwargs)


def f(a, b, c=3):
    print(a + b + c)


def func3(a, *args, arg1=123, **kwargs):
    print(a, args, arg1, kwargs)


func(123, 234, 45, 345, 345, 345, 345, 234, j=155, dshifoi=324, kl=';)', var='3154235')
print()
lst = [1, 2, 3, 4]
d = {'arg1': 1, 'arg2': 10, 'askafhdafh': 'asdfha'}
func3(*lst, **d)
func3(*lst, arg1=1, arg2=10, askafhdafh='asdfha')