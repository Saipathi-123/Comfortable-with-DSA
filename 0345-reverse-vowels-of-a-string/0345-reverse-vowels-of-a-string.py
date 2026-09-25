class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to list so we can modify it in place
        chars = list(s)
        
        l, r = 0, len(chars) - 1
        vowels = set("aeiouAEIOU")  # O(1) lookup time
        
        while l < r:
            # Move left pointer until it hits a vowel
            while l < r and chars[l] not in vowels:
                l += 1
            # Move right pointer until it hits a vowel
            while l < r and chars[r] not in vowels:
                r -= 1
                
            # Swap them directly in place
            chars[l], chars[r] = chars[r], chars[l]
            
            l += 1
            r -= 1
            
        return "".join(chars)
