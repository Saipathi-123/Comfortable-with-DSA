class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Find all unique characters present in s (maximum 26 items)
        unique_chars = set(s)
        
        # Track the absolute minimum index found
        min_index = float('inf')
        
        for char in unique_chars:
            # If the first index matches the last index, it appears exactly once
            if s.find(char) == s.rfind(char):
                min_index = min(min_index, s.find(char))
                
        return min_index if min_index != float('inf') else -1
