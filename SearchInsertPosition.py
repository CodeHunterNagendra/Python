""" 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        sample = []
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            nums.append(target)
            nums.sort()
            print("elements in nums list after insert target value:: ", nums)
            return nums.index(target)

sol = Solution()
nums = list(map(int,input().split()))
target = int(input("Enter target Value:: "))
print("The elements in the list are:: ", nums)
print("The target value is:: ",target)
result = sol.searchInsert(nums,target)
print("The Insert Position is:: ", result)

        