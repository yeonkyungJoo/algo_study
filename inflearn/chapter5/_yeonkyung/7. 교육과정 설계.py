import sys
#sys.stdin = open("../input.txt", "rt")

essential = list(input())
N = int(input())
for i in range(N):

    curriculum = list(input())
    indexes = [-1 for _ in range(len(essential))]
    for index, e in enumerate(essential):
        for idx, c in enumerate(curriculum):
            if e == c:
                indexes[index] = idx
                break
    # print(indexes)

    k = 0
    result = 'YES'
    while k < len(indexes) - 1:
        if indexes[k] == -1 or indexes[k] > indexes[k+1]:
            result = 'NO'
            break
        k += 1

    print('#%d %s' %(i+1, result))
