class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            print("The numerical value of",char, "is" ,ord(char))
            result = result * 26 +ord(char) - ord('A')+1
        return result

sol = Solution()
columnTitle = input("Enter Excel column title:: ")
print (f"Excel Column Number is {sol.titleToNumber(columnTitle)}")