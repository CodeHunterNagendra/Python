class Solution:
    def romanToInt(self, s):
        sum=0
        prev_value = 0
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for ele in s[::-1]:
            value = roman[ele]
            if value >= prev_value:
                sum += value
            else:
                sum -= value
            prev_value = value
            
        return sum

s = input("Enter a Roman Value:: ")
sol = Solution()
total = sol.romanToInt(s)
print(total)