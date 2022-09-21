testCase = int(input())

for i in range(1, testCase+1) :
    a = list(map(int, input().split(" ")))
    avg = sum(a[1:]) / a[0]
    cnt = 0
    for score in a[1:]:
        if score > avg :
            cnt += 1
    rate = cnt/a[0] * 100
    print('{0:0.3f}%'.format(rate))