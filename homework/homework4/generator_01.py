def generator(a):
    num = 0
    for i in a:
        b = (num, i)
        yield b
        num += 1
print(list(generator(['MAI', 'Lambda'])))
print(list(generator('Billy Herrington')))
