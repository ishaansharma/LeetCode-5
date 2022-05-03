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

# Second Attempt
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:   
        top, bottom = 0, len(matrix) - 1
        row = 0
        
        while top <= bottom:
            row = top + ((bottom - top) // 2)
            
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
            
        l, r = 0, len(matrix[row]) - 1
        
        while l <= r:
            middle = l + ((r - l) // 2)
            
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False       
