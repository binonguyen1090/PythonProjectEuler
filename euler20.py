n = 100
result = 1
sum = 0
for i in range (1,n+1):
    result*= i
str_result = str(result)
for i in str_result:
    sum += int(i)
print(sum)