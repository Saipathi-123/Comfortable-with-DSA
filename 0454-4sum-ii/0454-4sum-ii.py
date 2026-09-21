
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        map={}
        tot_count=0
        for i in nums1:
            for j in nums2:
                sum=i+j
                if sum in map:
                    map[sum]+=1
                else:
                    map[sum]=1
        for i in nums3:
            for j in nums4:
                sum=i+j
                if -(sum) in map:
                    tot_count+=map[-sum]
        return tot_count
    


        