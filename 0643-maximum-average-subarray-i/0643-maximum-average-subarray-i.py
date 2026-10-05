class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
      
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        start = 1
        end = k
        
        while end < len(nums):

            current_sum = current_sum - nums[start - 1] + nums[end]
            max_sum = max(max_sum, current_sum)
            
            start += 1
            end += 1

        return float(max_sum) / k
