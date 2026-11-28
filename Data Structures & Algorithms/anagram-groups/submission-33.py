class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we know that anagrams can be counted with a hashmap
        # we can group anagrams together by their letter counts
        # use a dict with letter count as key, and list of words as value
        # letter count key should be a tuple of numbers
        words = defaultdict(list)

        for word in strs:
            # initilize alphabet array
            count = [0] * 26
            # use letter index to update array
            for letter in word:
                letter_index = (ord(letter) - ord('a'))
                count[letter_index] += 1
            words[tuple(count)].append(word)
        
        res = []
        for entry in words.values():
            res.append(entry)
        return res