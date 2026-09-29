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
            if nums[i]==target:
                count+=1
                i+=1
            elif nums[j]==target:
                count+=1
                j-=1
            elif nums[i]+nums[j]==target:
                count+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]>target:
                count+=1
                j-=1
            elif nums[i]+nums[j]<target:
                count+=1
                i+=1
                j-=1
        return count
        