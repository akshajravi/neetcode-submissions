class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l,r = 0, ROWS - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        if matrix[mid][-1] < target or matrix[mid][0] > target:
            return False
        # at end of this section, the target should be in mid 
        l ,r = 0, len(matrix[mid]) - 1
        row = matrix[mid]
        while l <= r:
            mid = (l + r) // 2
            if row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
            else:
                return True
        return False

