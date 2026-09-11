class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        if len(pattern)!=len(s):
            return False
        pattern_to_word={}
        word_to_pattern={}
        for char,word in zip(pattern,s):
            if char in pattern_to_word and pattern_to_word[char]!=word:
                return False
            if word in word_to_pattern and word_to_pattern[word]!=char:
                return False
            pattern_to_word[char]=word
            word_to_pattern[word]=char
        return True