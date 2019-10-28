import time
import math
start_time = time.time()
def isPrime(num):
    for i in range (2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


arr = [2]
num = 3
while len(arr) < 10001:
    if(isPrime(num)):
        arr.append(num)
    num += 2
print(arr[-1])
print("--- %s seconds ---" % (time.time() - start_time))