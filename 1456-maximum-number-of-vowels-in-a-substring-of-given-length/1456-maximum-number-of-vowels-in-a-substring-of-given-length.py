class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count vowels in the first window of size k
        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = current_vowels
        
        # Early return if we already hit the theoretical max possible
        if max_vowels == k:
            return k
            
        # Slide the window from index k to the end of the string
        for i in range(k, len(s)):
            # Add the incoming character on the right
            if s[i] in vowels:
                current_vowels += 1
            # Remove the outgoing character on the left
            if s[i - k] in vowels:
                current_vowels -= 1
                
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                # Early return optimization
                if max_vowels == k:
                    return k
                    
        return max_vowels
