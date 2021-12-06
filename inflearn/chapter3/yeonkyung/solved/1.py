N = int(input())
for i in range(N):
    answer = 'YES'

    word = input()
    length = len(word)
    j = 0
    while j < length // 2:
        if word[j].upper() != word[length-1-j].upper():
            answer = 'NO'
            break
        j += 1
    print('#{0} {1}'.format(i+1, answer))