class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        
        # Move pointers through both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer for s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for t
            j += 1
            
        # If we successfully matched all characters of s, i will equal len(s)
        return i == len(s)
