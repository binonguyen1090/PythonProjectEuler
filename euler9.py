def isPy(n1,n2,n3):
    a = n1 ** 2
    b = n2 ** 2
    c = n3 ** 2
    if a + b == c:
        return True

result = 1
for a in range (1, 999):
    for b in range (1, 999):
        c = 1000 - a - b
        if isPy(a, b, c):
            result = a*b*c

print(result)