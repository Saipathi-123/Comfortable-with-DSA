class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = 0
        r = n - 1
        pos = n - 1
        res = [0] * n  # Initializes an array of size n with zeros
        
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            
            if left > right:
                res[pos] = left
                l += 1
                pos -= 1
            else:
                res[pos] = right
                r -= 1
                pos -= 1
                
        return res
