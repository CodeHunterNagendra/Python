class Solution:
    def kthDistinct(self, arr,k):
        answer = []
        for i in arr:
            if arr.count(i) == 1:
                answer.append(i)
        print('Distinct elements are:: ', answer)
        for i in range(len(answer)):
            if (i+1) == k:
                return answer[i]
        else:
            return ""

sol = Solution()
arr = input().split()
print("Elements the list are:" , arr)
k=int(input())
print(f'{k} th string in an array is:: ',sol.kthDistinct(arr,k))
