def solution(participant, completion):

    dic = dict()
    for p in participant:
        if p not in dic:
            dic[p] = 0
        dic[p] += 1

    for c in completion:
        dic[c] -= 1

    answer = ''
    for k, v in dic.items():
        if v == 1:
            answer = k
    return answer

if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution(participant, completion))