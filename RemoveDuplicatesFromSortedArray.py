class Solution:
    def removeDuplicates(self, nums) -> int:
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                continue
        print(result)
        return (len(result))

sol = Solution()
#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(f"Length after removing duplicates: {sol.removeDuplicates(nums)}")

        