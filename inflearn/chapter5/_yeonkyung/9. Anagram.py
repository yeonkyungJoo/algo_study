import sys
# sys.stdin = open("../input.txt", "rt")

word1 = input()
word2 = input()
result = 'YES'

dic = dict()
for c in word1:
    if c not in dic:
        dic[c] = 0
    dic[c] += 1

for c in word2:
    if c not in dic:
        result = 'NO'
        break
    dic[c] -= 1

for k, v in dic.items():
    if v != 0:
        result = 'NO'
print(result)


