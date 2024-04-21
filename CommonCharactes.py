class Solution:
    def commonChars(self, words):
        word = words[0]
        answer = []
        c = 0
        for char in word:
            if all(char in word for word in words[1:]):
                answer.append(char)
        return answer
            
sol = Solution()
n = int(input("Enter number of elements:: "))
words = list(input() for i in range(n))
print("The elements in the list are:: ",words)
print (sol.commonChars(words))