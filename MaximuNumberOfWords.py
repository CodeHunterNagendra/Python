class Solution:
    def mostWordsFound(self, sentences):
        count = []
        for words in sentences:
            #print(words.split())
            count.append(len(words.split()))
        return (max(count))

sol = Solution()
n = int(input("Number of sentences:: "))
sentences = list(input() for i in range(n))
print("sentences:: ", sentences)
print('most number of words found',sol.mostWordsFound(sentences))
        