class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        result = []
        for word in reversed(str_list):
            result.append(word)
        return (' '.join(result))
    
sol = Solution()       
s = input("Enter any Sentence: ")
print(f"Reverse Words in a String:: {sol.reverseWords(s)}")
