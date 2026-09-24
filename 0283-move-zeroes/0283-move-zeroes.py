class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write_ptr = 0
        
        # Step 1: Overwrite forward with non-zero elements
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != 0:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
                
        # Step 2: Fill the remaining indices with zero
        while write_ptr < len(nums):
            nums[write_ptr] = 0
            write_ptr += 1
