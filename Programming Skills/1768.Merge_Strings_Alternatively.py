class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # word1: abc
        # word2: def
        # result: adbecf
        res = ""
        word2_len = len(word2)
        i = 0
        while i < len(word1):
            res += "".join(word1[i])
            if i < word2_len:
                res += "".join(word2[i])
            i+=1
        if i < word2_len:
            res += "".join(word2[i:])
        
        return res
    
s = Solution()
word1 = 'SH'
word2 = 'Lee'
res = s.mergeAlternately(word1, word2)
print(res)