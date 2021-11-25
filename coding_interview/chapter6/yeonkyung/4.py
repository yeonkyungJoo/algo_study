from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        # "!?',;."
        paragraph = re.sub(r'[^\w]', ' ', paragraph)
        # print(paragraph)
        re_paragraph = paragraph.lower().split()

        counter = Counter(re_paragraph).most_common(len(re_paragraph))
        answer = ''
        for w, c in counter:
            if w in banned:
                continue
            answer = w
            break
        return answer

if __name__ == "__main__":
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(Solution().mostCommonWord(paragraph, banned))