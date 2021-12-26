# 응급실
import sys
from collections import deque
sys.stdin = open('input5.txt', 'r')
N, M = map(int, input().split())
risky = list(map(int, input().split()))
r = deque(risky)
cnt = 0

