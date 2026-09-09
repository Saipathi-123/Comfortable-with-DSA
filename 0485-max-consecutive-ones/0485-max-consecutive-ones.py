class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        for i in nums:
            if i:
                count = count + 1
            else:
                if count > ans:
                    ans = count
                count = 0
        if count > ans:
            ans = count
        return ans