testCase = int(input())

for i in range(1, testCase+1) :
    a, b = map(int, input().split(" "))
    print("Case #{}:".format(i), a, "+", b, "= {}".format(a+b))