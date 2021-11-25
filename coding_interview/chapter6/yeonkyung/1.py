class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True

        l, r = 0, len(s) - 1
        while l < r:

            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].upper() != s[r].upper():
                result = False
                break
            l += 1
            r -= 1

        return result

if __name__ == "__main__":
    print(Solution().isPalindrome(" "))
