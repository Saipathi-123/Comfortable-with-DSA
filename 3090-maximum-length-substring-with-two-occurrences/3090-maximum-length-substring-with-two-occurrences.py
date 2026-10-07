class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left,right=0,0
        ws=0
        count=[0]*26
        while right<len(s):
            ind=ord(s[right])-ord('a')
            if count[ind]<2:
                count[ind]+=1
                ws=max(ws,right-left+1)
                right+=1
                
            else:
                leftindex=ord(s[left])-ord('a')
                count[leftindex]-=1
                left+=1
        return ws