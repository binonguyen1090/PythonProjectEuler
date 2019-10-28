result = 2**1000

string = str(result)
l = len(string)
sum = 0
for i in range (0, l):
    sum += int(string[i])
print(sum)

