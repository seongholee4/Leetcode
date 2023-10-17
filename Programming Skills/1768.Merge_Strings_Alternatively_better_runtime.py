class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # word1: abc
        # word2: def
        # result: adbecf
        word1_len = len(word1)
        word2_len = len(word2)
        res = ""
        i = 0
        while i < word1_len:
            c1 = word1[i]
            res += c1
            if i < word2_len:
                res += word2[i]
            i+=1
        if i < word2_len:
            res += word2[i:]
        
        return res
    
s = Solution()
word1 = 'SH'
word2 = 'Lee'
res = s.mergeAlternately(word1, word2)
print(res)