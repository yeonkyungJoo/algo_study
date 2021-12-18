arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')    # 파이썬에서 가장 큰 값이 저장된다
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

# 주어진 수에서도 할 수 있다.
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

# 같지만 다른 방법
arrMin = float('inf')
for x in arr:
    if x < arrMin:
        arrMin = x
print(arrMin)