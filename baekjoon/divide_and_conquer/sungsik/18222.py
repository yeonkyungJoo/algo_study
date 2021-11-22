import sys

input = sys.stdin.readline

k = int(input())
# 투에모스 수열을 알고 있어야 한다.
# n번째 원소 t를 계산하려면 n을 이진수로 써야한다.
# 1의 개수가 홀수라면 t = 1이고, 짝수면 t = 0 이다.
def thue_Morse(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    elif k % 2:
        return 1 - thue_Morse(k//2)
    else:
        return thue_Morse(k//2)
print(thue_Morse(k - 1))