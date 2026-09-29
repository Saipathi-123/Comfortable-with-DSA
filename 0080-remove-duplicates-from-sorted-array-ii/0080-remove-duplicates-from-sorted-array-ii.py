class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq=1
        place=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                freq+=1
            else:
                freq=1
            if freq<=2:
                nums[place]=nums[i]
                place+=1
        return place        