class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to sort the list of numbers
        # and iterate until k is achieved
        # we will need the counts of each number
        # sorted into buckets
        # use a hashmap to bucket sort with count as key, number as value
        # but we need to get the initial list of counts
        initial_counts = defaultdict(int)
        buckets = defaultdict(list)

        for num in nums:
            initial_counts[num] += 1

        # we know need to bucket the numbers into their counts
        for num, count in initial_counts.items():
            buckets[count].append(num)

        # extract in desc order, max bucket is len(nums), we will need 
        res = []
        for i in range(len(nums), 0, -1):
            num_list = buckets[i]
            for n in num_list:
                res.append(n)
                if len(res) == k:
                    return res
        return res