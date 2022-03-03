import sys

def solution(words):

    alpha_dict = {}
    for word in words:
        for i in range(len(word)):
            if word[i] in alpha_dict:
                alpha_dict[word[i]] += 10 ** (len(word) - i - 1)
            else:
                alpha_dict[word[i]] = 10 ** (len(word) - i - 1)

    values = sorted(alpha_dict.values(), reverse=True)
    n = 9
    answer = 0
    for v in values:
        answer += v * n
        n -= 1
    return answer

if __name__ == "__main__":
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    print(solution(words))

# def solution(N, words):
#     ch_alpha = [-1] * 26
#     ch_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#     _word = [''] * 10
#     for word in words:
#         reversed_word = list(reversed(list(word)))
#         i = 0
#         for r in reversed_word:
#             _word[i] += r
#             i += 1
#
#     tmp = []
#     re_reversed_word = list(reversed(_word))
#     total = ''.join(re_reversed_word)
#     for r in re_reversed_word:
#         if r == '':
#             continue
#         _sum = 0
#
#         _r = list(r)
#         _r.sort(key=lambda x:-total.count(x))
#         for c in _r:
#             if ch_alpha[ord(c) - 65] == -1:
#                 max_idx = max(ch_num)
#                 ch_num[max_idx] = -1
#                 ch_alpha[ord(c) - 65] = max_idx
#             _sum += ch_alpha[ord(c) - 65]
#         tmp.append(_sum)
#
#     answer = 0
#     n = 0
#     for i in range(len(tmp)-1, -1, -1):
#         answer += pow(10, n) * tmp[i]
#         n += 1
#     return answer