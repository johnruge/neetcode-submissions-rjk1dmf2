class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = {}
        def dfs(n: int) -> int:
            if n >= len(nums):
                return 0

            if n in memo:
                return memo[n]
            
            memo[n] = max(dfs(n + 1), nums[n] + dfs(n + 2))
            return memo[n]
        return dfs(0)

# memoization
        