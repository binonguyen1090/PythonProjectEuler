num = 600851475143
j = 2
arr = []
while num > 1:
    if num%j:
        j+=1
    else:
        num = num/j
        arr.append(j)
print(j)