class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        if n == 1:
            return 1
        
        for i in range(n - 1):
            temp = two
            two = one + temp
            one = temp

        return two

# 0(n) time and constant space. bottom up approach