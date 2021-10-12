#generator 2
def own_zip(a, b):
    if len(a) > len(b):
        length = len(b)
    else:
        length = len(a)

    for i in range(0, length):
        d = (a[i], b[i])
        yield d


print(list(own_zip('MAI', 'Lambda')))
print(list(own_zip('Hello', [5, 1, 0, 5])))