class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_Map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_Map:
                return [prev_Map[diff], i]
            prev_Map[n] = i
        return []


# Input
nums = [2, 7, 11, 15]
target = 9

# Create object
solution = Solution()

# Call the function
result = solution.twoSum(nums, target)

print(result)