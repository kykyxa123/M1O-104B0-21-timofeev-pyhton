# sam.rab 2
# ex 1
v1 = int(input())
v2 = int(input())

def operation(v2, v1):
    if v1 < v2:
        return v1
    elif v2 < v1:
        return v2
    elif v2 == v1:
        return "v1 = v2"
print(operation(v2, v1))

#ex2

v11 = int(input())
v22 = int(input())
v33 = int(input())

def operation2(v11, v22, v33):
    if (v11 < v22 and v11 < v33) or (v11 < v22 and v22 == v33):
        return v11
    elif (v22 < v11 and v22 < v33) or (v22 < v11 and v11 == v33):
        return v22
    elif (v33 < v11 and v33 < v22) or (v33 < v11 and v11 == v33):
        return v33
    elif v11 == v22 and v22 == v33:
        return "v12 = v22 = v33"

print(operation2(v11, v22, v33))

#ex 3

a = int(input())
b = int(input())
c = int(input())

def operation3(a, b, c,):
    count = 0
    if a == b and b == c:
        count += 3
        return count
    elif (a != b and b == c) or (a == b and b != c):
        count += 2
        return count
    elif a != b and b != c:
        count += 0
        return count

print(operation3(a, b, c))