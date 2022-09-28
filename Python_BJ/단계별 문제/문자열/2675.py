testCase = int(input())

for i in (1, testCase+1) :
    num, a = input().split(" ")
    text = ""
    for i in a :
        text += int(num)*i
    print(text)