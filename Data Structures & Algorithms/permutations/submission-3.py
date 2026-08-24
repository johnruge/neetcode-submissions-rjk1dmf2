class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                res.append([nums[i]] + p)

        return res

# time = n! * n^2
# space = n! * n