def solution(clothes):

    dic = dict()
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = []
        dic[kind].append(name)

    answer = 1
    for key in dic:
        answer *= (len(dic[key]) + 1)
    return answer - 1

if __name__ == "__main__":
    clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))