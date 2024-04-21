'''Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''

#solution
class Solution:
    def fizzBuzz(self, n: int):
        answer = [(str(i+1)) for i in range(n)]
        for i in range(len(answer)):
            if int(answer[i])%3 == 0 and int(answer[i])%5 == 0:
                answer[i] = "FizzBuzz"
            elif int(answer[i])%3 == 0:
                answer[i] = "Fizz"
            elif int(answer[i])%5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i+1)
        return answer

n = int(input("Enter any number:: "))
sol = Solution()
print("The resultant array :: ",sol.fizzBuzz(n))

            
