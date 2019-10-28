def getLong(num):
    count = 0
    while num >1:
        if num % 2 == 0:
            num = num/2
            count += 1
        else:
            num = 3*num + 1
            count += 1
    return (count)

n = 999999
max = 0
while n > 1000:
    if getLong(n) > max:
        max = getLong(n)
        print(n)
    else:
        n-=1






