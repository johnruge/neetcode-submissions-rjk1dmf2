class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_cost = [0 for _ in range(len(cost) + 2)]
        for i in range(len(cost) - 1, -1, -1):
            min_cost[i] = cost[i] + min(min_cost[i + 1], min_cost[i + 2])
        
        return min(min_cost[0], min_cost[1])

# top down dp o(n) space and time