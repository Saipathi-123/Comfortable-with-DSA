class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                res.append(s[i])

        l,r=0,len(res)-1
        while l<r:
            res[l],res[r]=res[r],res[l]
            l+=1
            r-=1

        vowel_index=0
        final_str=[]
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                # Put the reversed vowel back in place
                final_str.append(res[vowel_index])
                vowel_index += 1
            else:
                # Keep the consonant exactly as it was
                final_str.append(s[i])

        # Convert list of characters back into a string
        output = "".join(final_str)
        return output
        