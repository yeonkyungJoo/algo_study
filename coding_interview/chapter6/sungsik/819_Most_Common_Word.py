# import re
# import collections
#
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
#
# def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
#     words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#              .lower().split()
#              if word not in banned]
#
#     counts = collections.Counter(words)
#     return counts.most_common(1)[0][0]
#
# mostCommonWord(paragraph, banned)

# 스스로 풀기
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

word = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
counts = collections.Counter(word)
print(counts.most_common(1)[0][0])
# print(counts)