class A:
    TMP = 30

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def args_sum(self):
        return self.arg1 + self.arg2


a = A(1, 2)
b = A(3, 10)
print(a.args_sum())

# print(id(A.TMP))
# print(id(a.TMP), id(b.TMP))
# a.TMP = 15
# A.TMP = 20
# print(id(A.TMP))
# print(id(a.TMP), id(b.TMP))


