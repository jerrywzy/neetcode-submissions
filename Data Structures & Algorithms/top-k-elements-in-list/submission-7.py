class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1

        sorted_by_val = sorted(num_count.items(), key=lambda item: item[1], reverse=True)

        counter = 0
        final_list = []
        for num, count in sorted_by_val:
            print(num, count)
            if counter < k:
                final_list.append(num)
                counter += 1
                print(final_list)
        return final_list