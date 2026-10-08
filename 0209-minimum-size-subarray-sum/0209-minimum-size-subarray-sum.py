class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        summ=0
        left=0
        ws=float("+inf")
        for right in range(len(nums)):
            summ+=nums[right]
            while summ>=target:
                ws=min(ws,right-left+1)
                summ-=nums[left]
                left+=1
        if ws==float("+inf"):
            return 0
        else:
            return ws

        