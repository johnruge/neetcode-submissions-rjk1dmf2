class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(curr, i):
            if i >= len(nums):
                res.append(curr[:])
                return

            # include nums[i]
            curr.append(nums[i])
            dfs(curr, i + 1)

            # don't include
            # to avoid dups, skip all following nums where nums[i + 1] == nums[i]
            curr.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(curr, i + 1)

        dfs([], 0)
        return res

#time = n * 2^n
#space = 2^n output list and n extra space
        