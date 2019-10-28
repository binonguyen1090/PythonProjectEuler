import math
def isPrime(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

sum = 2
number = 3
while number < 2000001:
    if (isPrime(number)):
        sum += number
    number += 2
print(sum)
