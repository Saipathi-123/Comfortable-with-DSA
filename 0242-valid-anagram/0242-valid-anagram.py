class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_arr=[0]*26
        if len(s)!=len(t):
            print(False)
        for i in s:
            index=ord(i)-ord("a")
            hash_arr[index]+=1
        for j in t:
            index=ord(j)-ord("a")
            hash_arr[index]-=1
        for val in hash_arr:
            if val!=0:
                return False
        return True
    
        