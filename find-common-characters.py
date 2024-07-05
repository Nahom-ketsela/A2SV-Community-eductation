class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
         common_chars = list(words[0])

         for word in words[1:]:
            new_common_chars = []
            for char in word:
                if char in common_chars:
                    new_common_chars.append(char)
                    common_chars.remove(char)
            common_chars = new_common_chars
        
         return common_chars
        
        
