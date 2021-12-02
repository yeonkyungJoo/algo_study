# import collections
# from typing import List
#
#
# def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
#     anagrams = collections.defaultdict(list)
#
#     for word in strs:
#         anagrams[''.join(sorted(word))].append(word)
#     return list(anagrams.value())
#
# strs = ["eat","tea","tan","ate","nat","bat"]
# groupAnagrams(strs)

# import collections
#
# strs = ["eat","tea","tan","ate","nat","bat"]
#
# anagrams = collections.defaultdict(list)
# for word in strs:
#     anagrams[''.join(sorted(word))].append(word)
# print(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]

for word in strs:
    print(''.join(sorted(word)))