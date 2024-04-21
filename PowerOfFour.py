class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        while n != 1:
            if  n%4 != 0:
                return False 
            n = n//4
        return True

sol = Solution()
num = int(input("Enter any number:: "))
print(f"is Power of two ? {sol.isPowerOfTwo(num)}")