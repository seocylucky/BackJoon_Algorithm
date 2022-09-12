startH, startM = map(int, input().split(" "))
moreM = int(input())
plus = (startM+moreM)//60

if plus >= 1 :
    if startH+plus >= 24:
        print((startH+plus)-24, (startM+moreM)%60)
    else :
        print(startH+plus, (startM+moreM)%60)
else :
    print(startH, startM+moreM)