class Solution(object):
    def numRescueBoats(self, nums, target):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        nums.sort()
        count=0
        i,j=0,len(nums)-1
        while i<=j:
            if nums[i]+nums[j]<=target:
                i+=1
                j-=1
            else:
                j-=1
            count+=1
        return count
        