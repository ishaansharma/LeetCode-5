# First Attempt
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        rows = 0
        for row in range(len(matrix)):
            if matrix[row][0] <= target <= matrix[row][-1]:
               rows = row
            
        l = 0
        r = len(matrix[rows]) - 1
        while l <= r:
            middle = l + ((r - l) // 2)
            
            if matrix[rows][middle] == target:
                return True
            elif matrix[rows][middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False       
