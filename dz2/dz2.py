# № 1
# решение через while

i = 99
while i > 2:
    print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
    i = i - 1
    print('Take one down and pass it around', i, 'bottles of beer on the wall')
while i > 1:
    print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
    i = i - 1
    print('Take one down and pass it around,', i, 'bottle of beer on the wall')
print('Take one down and pass it around, no more bottles of beer on the wall')
print('Go to the store and buy some more, 99 bottles of beer on the wall')

# решение через for

# for i in range(99, 0, -1):
#     print(i, 'bottles of beer on the wall', i, 'bottles of beer.')
#     if i == 1:
#         print('Take one down and pass it around', i, 'bottle of beer on the wall')
#     else:
#         print('Take one down and pass it around', i, 'bottles of beer on the wall')


# № 2

for j in range(1, 101):
    if j % 3 == 0 and j % 5 == 0:
        print('FizzBuzz')
    elif j % 3 == 0:
        print('Fizz')
    elif j % 5 == 0:
        print('Buzz')
    else:
        print(j)
