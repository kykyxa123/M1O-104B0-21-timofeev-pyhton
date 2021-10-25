# sam.rab 5
# ex 1
a = [0, 1, 2, 3, 4, 5, 6]
b = []
def operation(a, b):
    b = a[::2]
    return b

print(operation(a, b))
#
# ex 2
j = [0, 2, 56, 24, 98, 20]
h = []
def operation2(j,h):
    for i in range(1, len(j)):
        if j[i] > j[i - 1]:
            h.append(j[i])
    return h
print(operation2(j, h))
# ex 3
g = [0, 1, 2, 3, 4, 5]
def operation3(g: list) -> int:
    for i in range(1, len(g)):
        min1 = g.index(max(g))
        max1 = g.index(min(g))
        g[max1], g[min1] = g[min1], g[max1]
        return g
print(operation3(g))