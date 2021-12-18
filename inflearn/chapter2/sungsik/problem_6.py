# 자릿수의 합
#
N = int(input())
num_list = list(map(str, input().split()))
sum = []
max = -float('inf')
def digit_sum(x: list) -> int:
    global sum
    for x in num_list:
        tmp = 0
        for y in x:
            tmp += int(y)
        sum.append(tmp)

    for i in sum:
        global max
        if i > max:
            max = sum.index(i)
    return num_list[max]

print(digit_sum(num_list))

# N = int(input())
# num_list = list(map(int, input().split()))

# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum += x % 10
#         x = x // 10
#     return sum
# max = - 2147000000
# for x in num_list:
#     tot = digit_sum(x)
#     if tot > max:
#         max = tot
#         res = x
# print(res)
#
# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum
# max = -2147000000
# for x in num_list:
#     tot = digit_sum(x)
#     if tot > max:
#         max = tot
#         res = x
# print(res)
