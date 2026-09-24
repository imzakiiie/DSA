class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False


nums = [1, 2, 3, 1]

solution = Solution()
print(solution.containsDuplicate(nums))