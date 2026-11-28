class Solution:

    def encode(self, strs: List[str]) -> str:
        # convert list to string with a delimiter 
        # delimiter should be number and a symbol, so we can track letter count 
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # decode should scan the string
        # get number before "#" and append to a list the subsequent length matching string

        # 5#Hello5#World
        res = []
        i = 0 # pointer
        
        while i < len(s):
            j = i # second pointer to find integers
            while s[j] != "#":
                j += 1
            print(i, j)
            s_length = int(s[i:j])
            i = j + 1  # set start pointer
            j = i + s_length # set stop pointer
            decoded = s[i:j]
            res.append(decoded)
            i = j # reset i to next chunk
        return res