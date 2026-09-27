class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        hash_table=[0]*1001
        n=len(nums)
        res=[]
        for i in range(n):
            for j in range(len(nums[i])):
                hash_table[nums[i][j]]+=1
        for i in range(len(hash_table)):
            if hash_table[i]==n:
                res.append(i)
        return res
        