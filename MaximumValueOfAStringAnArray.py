class Solution:
    def maximumValue(self, strs) -> int:
        result = []
        for i in strs:
            if i.isalnum():
                result.append(len(i))
            elif i.isnumeric():
                result.append(int(i))
            
        return max(result)

sol = Solution()
#strs = ['alic3','bob','1','3','00000']
strs = ['1','01','001','0001']
print(sol.maximumValue(strs))
        