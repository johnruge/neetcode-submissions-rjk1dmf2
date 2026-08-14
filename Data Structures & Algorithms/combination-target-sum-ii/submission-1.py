class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(currList, currSum, i):
            if currSum == target:
                res.append(currList[:])
                return
            if i >= len(candidates) or currSum > target:
                return

            
            currList.append(candidates[i])
            dfs(currList, currSum + candidates[i], i + 1)
            
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            currList.pop()
            dfs(currList, currSum, i + 1)

        dfs([], 0, 0)
        return res

#time: O(n * 2^n)
#space: O(n * 2^n)