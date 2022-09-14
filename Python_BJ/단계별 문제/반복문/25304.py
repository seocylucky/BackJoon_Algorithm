totalPrice = int(input())
kindNum = int(input())
oneTotalPrice = 0
sum = 0

for i in range(1, kindNum+1) :
    price, num = map(int, input().split(" "))
    oneTotalPrice = price * num
    sum = oneTotalPrice + sum

if sum == totalPrice :
    print("Yes")
else :
    print("No")
