class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        dic = dict()
        for str in strs:
            sorted_str = sorted(list(str))
            sorted_str = ''.join(sorted_str)
            if sorted_str not in dic:
                dic[sorted_str] = []
            dic[sorted_str].append(str)
        return dic.values()

if __name__ == "__main__":
    strs = ["a"]
    print(Solution().groupAnagrams(strs))