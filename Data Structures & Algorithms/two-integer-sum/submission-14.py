class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # num : index

        for i, n in enumerate(nums):
            difference = target - n
            if difference in indices:
                return [indices[difference],i]
            else:
                indices[n] = i