class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res=[0]*(m+n)
        a,b,index=0,0,0
        while a<m and b<n:
            if nums1[a]<=nums2[b]:
                res[index]=nums1[a]
                a+=1
            else:
                res[index]=nums2[b]
                b+=1
            index+=1
        while a<m:
            res[index]=nums1[a]
            a+=1
            index+=1
        while b<n:
            res[index]=nums2[b]
            b+=1
            index+=1
        for i in range(len(res)):
            nums1[i]=res[i]
        