class Solution:
    def containsDuplicate(self, nums) -> bool:
        flag = False
        for i in range(len(nums)):
                if nums[i] in nums[i+1:]:
                    flag = True
                    break
        return flag
# best Case
        """class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for i in nums:
            if i in unique_elements:
                return True
            else:
                unique_elements.add(i)
        return False
        """
                
sol = Solution()
n = int(input("Number of elements:: "))
nums = [int(input()) for i in range(n)]
print("List elements are:: ", nums)
results = sol.containsDuplicate(nums)
print(results)