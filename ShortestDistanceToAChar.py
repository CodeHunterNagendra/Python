class Solution:
    def shortestToChar(self, s: str, c: str):
        result = []
        count = 0
        for i in range(len(s)):
            if s[i] == c:
                count = 0
                result.append(count)
            else:
                if s[i+1] !=c:
                    count +=1
                result.append(count)
        return result

sol =Solution()
s = input()
c = input("Enter Search Char:: ")
print(sol.shortestToChar(s,c))
    
        