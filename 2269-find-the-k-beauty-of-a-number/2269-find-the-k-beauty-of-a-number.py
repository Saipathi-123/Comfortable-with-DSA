class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        count=0
        temp=num
        mod_base=10**k
        limit=10**(k-1)
        while temp>=limit:
            sub_num=temp%mod_base
            if sub_num!=0 and num%sub_num==0:
                count+=1
            temp//=10
        return count