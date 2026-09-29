class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return len(nums)
        place=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[place-2]:
                nums[place]=nums[i]
                place+=1
        return place
