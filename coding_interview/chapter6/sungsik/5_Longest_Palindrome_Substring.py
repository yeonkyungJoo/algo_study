input1 = "babad"
input2 = "bab"

def longestPalindrome(s:str) ->str:
    def is_palindrome(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result, is_palindrome(i, i), is_palindrome(i, i+1), key=len)

    return result

print(longestPalindrome(input1))
print(longestPalindrome(input2))