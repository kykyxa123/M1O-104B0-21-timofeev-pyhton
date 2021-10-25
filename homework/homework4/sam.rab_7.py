# ex1
def func(a):
    set_01 = set(a)
    print(len(set_01))

a = [1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 8, 9]

func(a)
# ex2
def func(j, b):
    set_1, set_2 = set(j), set(b)
    f = set_1 & set_2
    print(len(f))

j = [1, 2, 3, 4, 5, 6, 10, 11, 11, 20]
b = [1, 2, 4, 5, 11, 21]

func(j, b)