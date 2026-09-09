class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=float("-inf")
        sec_largest=float("-inf")
        third_largest=float("-inf")
        if len(nums)<=2:
            return max(nums)
        for i in nums:
            if i>largest:
                third_largest=sec_largest
                sec_largest=largest
                largest=i
            elif i>sec_largest and i!=largest:
                third_largest=sec_largest
                sec_largest=i
            elif i>third_largest and i!=sec_largest and i!=largest:
                third_largest=i
        if third_largest==float("-inf"):
            return max(nums)
        else:
            return third_largest
        
        
        