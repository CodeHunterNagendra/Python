"""You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode" """

class Solution:
    def restoreString(self, s: str, indices) -> str:
        result = [0 for i in range(len(indices))]
        for idx,char in zip(indices,s):
            result[idx] = char
        return (''.join(result))
sol = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(f"{s}--> {sol.restoreString(s,indices)}")