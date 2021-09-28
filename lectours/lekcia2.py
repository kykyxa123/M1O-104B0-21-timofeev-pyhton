# # № 1
# # решение через while
#
# i = 99
# while i > 2:
#     print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
#     i = i - 1
#     print('Take one down and pass it around', i, 'bottles of beer on the wall')
# while i > 1:
#     print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
#     i = i - 1
#     print('Take one down and pass it around,', i, 'bottle of beer on the wall')
#
# # решение через for
#
# for i in range(99, 0, -1):
#     print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
#     if i == 1:
#         print('Take one down and pass it around', i, 'bottle of beer on the wall')
#     else:
#         print('Take one down and pass it around', i, 'bottles of beer on the wall')
#
#
# # № 2
#
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')

# arr = [0, 2, 0, 4, 2, 5, 0, 8, 0, 0]
# def ziro_of_number(arr: list) -> int:
#     sum = 0
#     for i in arr:
#         if i == 0:
#             sum += 1
#     return sum
#
#
# print(ziro_of_number(arr))

def pirramide(n: int) -> None:
    