class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[index]=nums[i]
                index+=1
                i+=1
            else:
                i+=1
        return index

        