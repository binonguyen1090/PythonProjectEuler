def isPal(num):
    copy = num
    reverse = 0
    while copy > 0:
        reverse = reverse*10 + copy % 10
        copy = int(copy /10)
    if reverse == num:
        return True
    else:
        return False
max = 0
for i in range(1000):
    for j in range(1000):
        number = i*j
        if isPal(number) :
            if number > max:
                max = number
print(max)

