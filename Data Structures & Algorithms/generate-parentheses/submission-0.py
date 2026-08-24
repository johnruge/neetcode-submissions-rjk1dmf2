class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        num_open, num_closed = 0, 0
        res = []
        def backtrack(num_open, num_closed, curr):
            if num_open > n:
                return
            if num_open == num_closed and num_closed == n:
                res.append(curr[:])
                return
            
            if num_open > num_closed:
                backtrack(num_open + 1, num_closed, curr + "(")
                backtrack(num_open, num_closed + 1, curr + ")")
            else:
                backtrack(num_open + 1, num_closed, curr + "(")

        backtrack(0, 0, "")
        return res

#time = n * 2^n
#space = n * 2^n

            

        