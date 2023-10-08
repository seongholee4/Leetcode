# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from typing import List


word1 = 'eiowzz'
word2 = 'acckzz'
g = 2
count = 0
for i in range(6):
    print(word1[i], word2[i])
    if word1[i] == word2[i]:
        count += 1
print(count)
if count == g:
    print(g)

words = [1,2,3]
for i, w in enumerate(words):
    print("before: ", words)
    print("popping ", w)
    words.pop(i)
    i -= 1
    print("after: ", words)