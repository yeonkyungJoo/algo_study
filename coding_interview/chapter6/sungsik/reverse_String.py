# 1번

inp = ["h","e","l","l","o"]
print(inp)

inp2 = inp[::-1]
print(inp2)

# 2번
inp = ["h","e","l","l","o"]

left, right = 0, len(inp) - 1

while left < right:
    inp[left], inp[right] = inp[right], inp[left]
    left += 1
    right -= 1
