class Solution:
    def removeElement(self, nums, val: int) -> int:
        result = []
        for num in nums:
            if num != val:
                result.append(num)
            else:
                continue
        print(result)
        return (len(result))


sol = Solution()
nums= list(map(int,input().split()))
print("Elements:: ", nums)
val = int(input("Enter a value:: "))
print("length after Removing Elements:: ", sol.removeElement(nums,val))
        