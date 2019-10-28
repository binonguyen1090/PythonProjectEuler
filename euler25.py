def getcount(num):
    s = str(num)
    count = list(s)
    return len(count)


f1 = 1
f2 = 1
f3 = f1 + f2
count = 1000
arr = [1,1,2]
while getcount(f3) != count:
    f1 = f2
    f2 = f3
    f3 = f1 + f2
    arr.append(f3)


print(len(arr))