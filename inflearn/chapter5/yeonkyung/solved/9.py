s1 = list(input())
s2 = list(input())

upper = [0 for _ in range(26)]
lower = [0 for _ in range(26)]
for c in s1:
    if c.isupper():
        upper[ord(c) - ord('A')] += 1
    else:
        lower[ord(c) - ord('a')] += 1

for c in s2:
    if c.isupper():
        upper[ord(c) - ord('A')] -= 1
    else:
        lower[ord(c) - ord('a')] -= 1

result = 'YES'
for u in upper:
    if u != 0:
        result = 'NO'
for l in lower:
    if l != 0:
        result = 'NO'
print(result)
