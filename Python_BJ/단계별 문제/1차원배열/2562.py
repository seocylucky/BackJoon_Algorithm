numArray = []

for i in range(9) :
    numinput = int(input())
    numArray.append(numinput)
print(max(numArray))
print(numArray.index(max(numArray))+1)