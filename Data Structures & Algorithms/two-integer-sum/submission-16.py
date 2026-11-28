class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a hashmap of seen nums with index, and if Difference is in hashmap, return index
        seen = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], index]
            else:
                seen[num] = index
            