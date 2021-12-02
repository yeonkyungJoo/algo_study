# import re
#
# def is_Palindrome(s) -> bool:
#     inp = s.lower()
#     inp = re.sub('[^a-z0-9]', '', inp)
#     return inp == inp[::-1]
#
# str = input().rstrip()
# print(is_Palindrome(str))

def is_Palindrome(s) -> bool:
    pal_list = []
    s = s.lower()
    for str in s:
        if str.isalnum():
            pal_list.append(str)
    while len(pal_list) > 1:
        if pal_list.pop(0) != pal_list.pop():
            return False
    return True
s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = " "
print(is_Palindrome(s2))