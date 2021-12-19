from collections import deque
N, M = map(int, input().split())
nums = list(map(int, input().split()))

patients = deque()
for i, n in enumerate(nums):
    patients.append((i, n))

max_degree = max(patients, key=lambda x:x[1])[1]
cnt = 0
while patients:
    patient = patients.popleft()
    if patient[1] == max_degree:
        cnt += 1
        if patient[0] == M:
            print(cnt)
            break
        max_degree = max(patients, key=lambda x: x[1])[1]
    else:
        patients.append(patient)