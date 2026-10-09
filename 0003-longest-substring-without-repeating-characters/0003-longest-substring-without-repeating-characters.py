class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left,gmax,ws=0,0,0
        nums=[0]*256
        for right in range(len(s)):
            index=ord(s[right])
            if nums[index]:
                while nums[index]:
                    nums[ord(s[left])]=False
                    left+=1
            nums[index]=True
            ws=max(ws,right-left+1)
        return ws