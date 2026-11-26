class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build hashmap of counts, then populate a list where the index is the count
        counts = defaultdict(int) # loop through nums and count
        frequencies = []  # list where index is count [0,0,0,0,0,0,2]

        for num in nums:
            counts[num] += 1
        
        # initialize frequencies, min is 0, max is len of nums
        for i in range(len(nums) + 1):
            frequencies.append([])

        # populate frequencies
        for num, count in counts.items():
            frequencies[count].append(num)

        # get result by counting backwards
        res = []
        for i in range(len(nums), 0, -1):
            for j in frequencies[i]:
                res.append(j)
                if len(res) == k:
                    return res
