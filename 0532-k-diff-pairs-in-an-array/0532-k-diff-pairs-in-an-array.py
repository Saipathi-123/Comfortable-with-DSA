class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map={}
        count=0
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        for i in hash_map:
            if k>0:
                if (i+k) in hash_map:
                    count+=1
            else:
                if hash_map[i]>=2:
                    count+=1
        return count
