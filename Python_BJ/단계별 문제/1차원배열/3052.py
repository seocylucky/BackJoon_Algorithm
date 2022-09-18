numList = []
newList = []

for i in range(1, 11) :
    num = int((input()))
    a = num % 42
    numList.append(a)

for j in numList :
    if j not in newList :
        newList.append(j)

print(len(newList))

