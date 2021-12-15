s = list(input())

numbers = []
for c in s:
    if c.isnumeric():
        if c != '0' or (c == '0' and numbers):
            numbers.append(c)
result = int(''.join(numbers))
print(result)

# 약수의 개수
count = 0
for i in range(1, result+1):
    if result % i == 0:
        count += 1
print(count)

