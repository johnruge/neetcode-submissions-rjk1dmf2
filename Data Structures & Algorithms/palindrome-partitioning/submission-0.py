class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(currList, currS, i):
            if i >= len(s):
                if isPalindrome(currS):
                    res.append(currList + [currS])
                return

            if isPalindrome(currS):
                #include
                currList.append(currS)
                backtrack(currList, "", i)

                #exclude
                currList.pop()

            backtrack(currList, currS + s[i], i + 1)
        
        def isPalindrome(s):
            if not s: return False
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        backtrack([], "", 0)
        return res

# time: n * 2^n
# space: n for recursion stack and n * 2^n for extra space(forming all strings)