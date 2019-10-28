def isDiv(num):
    for i in range (2, 21):
        if num % i != 0:
            return False
    return True
result = 2520
while True:
    if(isDiv(result)):
        print(result)
        break
    else:
        result += 2520