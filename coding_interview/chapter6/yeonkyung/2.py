class Solution:
    def reverseString(self, s: list[str]) -> None:

        l, r = 0, len(s) - 1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1

if __name__ == "__main__":
    print(Solution().reverseString(["h","e","l","l","o"]))
