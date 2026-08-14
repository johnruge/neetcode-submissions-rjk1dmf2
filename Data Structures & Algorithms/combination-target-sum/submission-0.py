class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        def sums(curr: List[int], currSum: int, p: int) -> None:
            if currSum == target:
                res.append(curr[:])
                return
            if currSum > target or p >= len(candidates):
                return
            
            curr.append(candidates[p])
            sums(curr, currSum + candidates[p], p)

            curr.pop()
            sums(curr, currSum, p + 1)

        sums([], 0, 0)
        return res
        
        sums([], 0, 0)
        return res

#time: O(n^(T/m))
#space: O(T/m)

            
        