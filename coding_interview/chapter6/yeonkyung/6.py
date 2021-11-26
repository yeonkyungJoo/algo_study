# TODO - re-try
class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = ''
        for i in range(len(s)):
            idx = 0
            while i-idx >= 0 and i+idx < len(s):
                if s[i-idx] != s[i+idx]:
                    break
                else:
                    if len(s[i-idx:i+idx+1]) >= len(result):
                        result = s[i-idx:i+idx+1]
                    idx += 1

            if i+1 < len(s) and s[i] == s[i+1]:
                idx = 0
                while i-idx >= 0 and i+idx+1 < len(s):
                    if s[i-idx] != s[i+idx+1]:
                        break
                    else:
                        if len(s[i-idx:i+idx+2]) >= len(result):
                            result = s[i-idx:i+idx+2]
                        idx += 1
        return result

if __name__ == "__main__":
    s = "ac"
    print(Solution().longestPalindrome(s))