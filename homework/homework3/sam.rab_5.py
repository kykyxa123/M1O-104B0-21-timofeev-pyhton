# sam.rab 5
#ex 1
# a = [0, 1, 2, 3, 4, 5, 6]
# b = []
# def operation(a, b):
#     b = a[::2]
#     return b
#
# print(operation(a, b))
#
# ex 2
# a = [0, 2, 56, 24, 98, 20]
# b = []
# def operation(a,b):
#     for i in range(1, len(a)):
#         if a[i] > a[i - 1]:
#             b.append(a[i])
#     return b
# print(operation(a, b))
# ex 3
# a = [0, 1, 2, 3, 4, 5]
# def operation(a: list) -> int:
#     for i in range(1, len(a)):
#         min1 = a.index(max(a))
#         max1 = a.index(min(a))
#         a[max1], a[min1] = a[min1], a[max1]
#         return a
# print(operation(a))