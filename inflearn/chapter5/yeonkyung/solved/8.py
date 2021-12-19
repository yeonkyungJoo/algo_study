N = int(input())
words = dict()
for _ in range(N):
    words[input()] = 1
for _ in range(N-1):
    words[input()] -= 1

for k, v in words.items():
    if v == 1:
        print(k)
        break

'''
from collections import deque
N = int(input())
words = deque()
use = []
for _ in range(N):
    words.append(input())
for _ in range(N-1):
    use.append(input())

for w in use:
    while words:
        p = words.popleft()
        if w != p:
            words.append(p)
        else:
            break
print(words[0])

import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())
words =[]
for _ in range(N):
    words.append(input())
#print(words)

use = []
for _ in range(N-1):
    use.append(input())
#print(use)

from collections import Counter
counter = Counter(words)
for word in use:
    counter[word] = 0

print(counter.most_common()[0][0])
'''