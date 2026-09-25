class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[0]*n
        l,r,write_index=0,n-1,n-1
        while l<=r:
            left_sq=nums[l]*nums[l]
            right_sq=nums[r]*nums[r]

            if left_sq<right_sq:
                res[write_index]=right_sq
                r-=1
            else:
                res[write_index]=left_sq
                l+=1
            write_index-=1
        return res

        