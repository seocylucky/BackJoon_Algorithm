import sys

testCase = int(sys.stdin.readline())

for i in range(1, testCase+1) :
    a, b = map(int, sys.stdin.readline().split(" "))
    print(a+b)