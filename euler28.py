gap = 2
conner= 1
total = 1
while (conner< 1001*1001):
    for i in range (0,4):
        conner = conner + gap
        total += conner
    gap+= 2
print(total)
