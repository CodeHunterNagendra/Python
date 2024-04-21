class Solution:
    def splitWordsBySeparator(self, words, separator: str):
        result = []
        for word in words:
            data = word.split(separator)
            for i in data:
                result.append(i)
        return result
      
sol  = Solution()
words = input().split()
print("The list elements are:: ",words)
separator = input("Enter Separator:: ")
print("Split Strings by separator:: ",sol.splitWordsBySeparator(words, separator))
