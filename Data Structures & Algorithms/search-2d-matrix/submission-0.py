class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + ((r - l)//2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1

        temp_lst = matrix[m]
        l, r = 0, len(temp_lst) - 1
        while l <= r:
            m = l + ((r - l)//2)
            if temp_lst[m] == target:
                return True
            elif temp_lst[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False