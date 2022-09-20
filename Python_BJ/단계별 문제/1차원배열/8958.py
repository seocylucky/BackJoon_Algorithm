testCase = int(input())

for i in range(1, testCase+1) :
    oxquiz = list(input())
    cnt = 0
    score = 0
    for ox in oxquiz :
        if ox == 'O' :
            cnt = cnt + 1
            score = score + cnt 
        else :
            cnt = 0
    print(score)