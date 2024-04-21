""" 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0] 
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in sorted(nums):
            if i == 0:
                nums.remove(0)
                nums.append(0)
        print("after moving zeroes:: ", nums)

sol = Solution()
input = list(map(int,input().split()))
print("The Elements in the input:: ", input)
sol.moveZeroes(input)
                

        