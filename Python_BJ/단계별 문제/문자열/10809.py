word = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet :
    print(word.find(i), end=' ')

    # find 메서드로 인해, alphabet 문자열 중 word 문자열 문자가 없는 경우에는 -1을 출력한다. 