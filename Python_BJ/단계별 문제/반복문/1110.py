num = int(input())
n = num
cycle = 0

while 1 :
        a = n // 10
        b = n % 10
        c =  (a + b) % 10
        n = (b*10) + c
        
        cycle = cycle + 1
        if(num == n) :
            break

print(cycle)