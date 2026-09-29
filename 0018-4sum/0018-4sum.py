class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                # FIX: Check against 'i + 1' instead of '0'
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                

                left,right=j+1,len(nums)-1
                goal=target-(nums[i]+nums[j])
                while(left<right):
                    two_sum=nums[left]+nums[right]
                    if two_sum==goal:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                    elif two_sum>goal:
                        right-=1
                    else:
                        left+=1
        return res

        