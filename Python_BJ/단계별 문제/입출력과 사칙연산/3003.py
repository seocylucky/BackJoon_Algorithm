piece = [1, 1, 2, 2, 2, 8]
findpiece = map(int, input().split(" "))

resultpiece = [x - y for x, y in zip(piece, findpiece)]

print(*resultpiece)