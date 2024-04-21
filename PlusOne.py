class Solution:
    def plusOne(self, digits):
        s = ''.join(map(str,digits))
        #print(s)
        i = int(s)+1
        #print(i)
        result = list(map(int,str(i)))
        return result
      

sol = Solution()
input = list(map(int,input().split()))
print("The elements in the list are:: ", input)
output= sol.plusOne(input)  #calling function to get output from class method
print("Plus One:: ", output)
        
        


        