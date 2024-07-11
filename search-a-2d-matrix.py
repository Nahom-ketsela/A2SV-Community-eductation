class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix[0])
        n= len(matrix)

        left, right = 0, n * m - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // m][mid % m]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
           

        

        
