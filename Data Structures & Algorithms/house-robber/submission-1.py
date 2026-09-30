class Solution:
    def rob(self, nums: list[int]) -> int:
        money = [0 for _ in range(len(nums) + 2)]
        for i in range(len(nums) - 1, -1, -1): 
            money[i] = max(nums[i] + money[i + 2], money[i + 1])
        return money[0]

# dp solution 0(n) space and time
