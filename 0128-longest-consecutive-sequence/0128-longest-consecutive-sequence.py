class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)
        long_streak=0
        for num in nums_set:
            if (num-1) not in nums_set:
                curr_num=num
                curr_streak=1
                while (curr_num+1) in nums_set:
                      curr_num+=1
                      curr_streak+=1
                long_streak=max(curr_streak,long_streak)
        return long_streak       