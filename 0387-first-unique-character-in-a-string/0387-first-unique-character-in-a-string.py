class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_arr=[0]*26
        for i in s:
            index=ord(i)-ord("a")
            hash_arr[index]+=1
        for j in range(len(s)):
            index=ord(s[j])-ord("a")
            if hash_arr[index]==1:
                return j
        return -1
        