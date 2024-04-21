class Solution:
    def isPalindrome(self, x: int) -> bool:
        while x > 0:
            new_num = str(x)
            print(new_num)
            reverse = ''.join(reversed(new_num))
            print(reverse)
            if x == int(reverse):
                return True
            else:
                return False

num = int(input("Enter any number:: "))
s = Solution()
result = s.isPalindrome(num)
if(result == True):
    print(num, " Is a Palindrome")
else:
    print(num, "is not a Palindrome")
