class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}

        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        for num,count in hash_map.items():
            if count==1:
                return num
                break
        