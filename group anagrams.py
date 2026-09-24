from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

solution = Solution()
print(solution.groupAnagrams(strs))