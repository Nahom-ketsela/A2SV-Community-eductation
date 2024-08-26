class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        original_rows = len(mat)
        original_cols = len(mat[0]) if mat else 0
        
      
        if original_rows * original_cols != r * c:
            return mat  
        
        # Flatten the original matrix into a 1D list
        flat_list = [num for row in mat for num in row]
           
        new_matrix = []
        for i in range(r):
            new_matrix.append(flat_list[i * c:(i + 1) * c])
        
        return new_matrix
