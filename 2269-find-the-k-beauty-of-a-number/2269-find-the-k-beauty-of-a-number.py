class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num_str=str(num)
        count=0
        for i in range(len(num_str)-k+1):
            sub_num=int(num_str[i : i + k])
            if sub_num!=0 and num%sub_num==0:
                count+=1
        return count