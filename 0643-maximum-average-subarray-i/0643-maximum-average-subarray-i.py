class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Renamed variable from 'sum' to 'curr_sum' because 'sum' is a built-in Python function
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
            
        # FIX: Added float() to prevent truncated integer division in Python 2
        max_avg = float(curr_sum) / k 
        
        start = 1
        end = k
        
        while(end < len(nums)):
            curr_sum = curr_sum - nums[start - 1] + nums[end]
            
            # FIX: Added float() here as well
            curr_avg = float(curr_sum) / k 
            
            max_avg = max(max_avg, curr_avg)
            start += 1
            end += 1
            
        return max_avg
