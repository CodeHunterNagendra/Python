class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        str1 = ''.join(word1)
        str2 = ''.join(word2)
        if str1 == str2:
            return True
        else:
            return False

sol = Solution()
#print ("is Equivalent? ",sol.arrayStringsAreEqual(["ab", "c"], ["a","bc"]))
word1 = input().split()
print("Word1 Elements are:: ", word1)
word2= input().split()
print("word2 Elements are:: ", word2)
print("is Equivalent? ",sol.arrayStringsAreEqual(word1,word2))


