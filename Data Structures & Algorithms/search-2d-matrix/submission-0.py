class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            num = matrix[mid_row][mid_col]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False