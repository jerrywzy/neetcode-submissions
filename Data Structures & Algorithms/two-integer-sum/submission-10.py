class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # number: index
        for i, num in enumerate(nums):
            difference = target - num
            print(i, num, difference, target)
            if difference in seen:
                return [seen[difference], i]
            else:
                seen[num] = i