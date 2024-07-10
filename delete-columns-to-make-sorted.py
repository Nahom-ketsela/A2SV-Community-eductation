class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs[0])
        count=0
        
        for i in range(n):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j - 1][i]:
                    count += 1
                    break
                    
        
        return count

            
        
            
        
