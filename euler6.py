sumOfSquare = 0
total = 0
for i in range (1,101):
    sumOfSquare += i*i
    total += i
different = total**2 - sumOfSquare
print(different)