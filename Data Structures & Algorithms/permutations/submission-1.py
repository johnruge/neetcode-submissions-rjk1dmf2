class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        for i in range(len(nums)):
            temp = nums[:i] + nums[i + 1:]

            for p in self.permute(temp):
                res.append([nums[i]] + p)

        return res
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p[:]
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)

        # return res

# time = n! * n^2
# space = n! * n