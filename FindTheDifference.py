class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_list = [i for i in t]
        print(t_list)
        s_list = [i for i in s]
        print(s_list)
        for i in s_list:
            if  i in t_list:
                t_list.remove(i)
                print(t_list)
        return (''.join(t_list))
    
sol = Solution()
s = 'abcd'
t = 'abcde'
print("difference? ",sol.findTheDifference(s,t))
