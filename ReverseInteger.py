"""
Question:: Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321

# Reversing a Normal interger value
class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        res = []
        for i in str_num:
            res.append(i)
        num = "".join(reversed(res))
        return (int(num))"""
        
# if the number is negative
class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(x*-1)[::-1]) * -1
        if ans < (-2**31) or ans >(2**31 -1):
            return 0
        return ans




sol = Solution()
num = int(input("Enter any Integer Number:: "))
reverse = sol.reverse(num)
print("The Reversed integer is :: ",reverse)