from typing import List

input = [1, 2, 3, 4]

def multiple(data: List[int]) -> List[int]:
    result = []
    ptr = 1
    # 왼쪽 곱셈
    for i in range(0, len(data)):
        result.append(ptr)
        ptr = ptr * data[i]
    ptr = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(data) - 1, -1, -1):
        result[i] = result[i] * ptr
        ptr = ptr * data[i]
    return result

print(multiple(input))