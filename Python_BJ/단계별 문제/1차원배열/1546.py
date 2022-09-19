n = int(input())
data = list(map(int, input().split()))
max = max(data)

result = []
for i in data :
  result.append(i / max * 100)

print(sum(result) / n)