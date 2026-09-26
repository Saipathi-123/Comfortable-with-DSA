class Solution(object):
    def isLongPressedName(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a,b=0,0
        while a<len(s) and b<len(t):
            if s[a]==t[b]:
                a+=1
                b+=1
            else:
                if b>0 and t[b]==t[b-1]:
                    b+=1
                else:
                    return False
        while b<len(t):
            if b>0 and t[b]==t[b-1]:
                b+=1
            else:
                return False            
        return a==len(s)
        