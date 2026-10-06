class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count=0
 
        summ=0
        for i in range(k):
            summ+=arr[i]

        if summ/k >=threshold:
            count+=1
        start,end=1,k
        while(end<len(arr)):
            summ=summ-arr[start-1]+arr[end]
            if summ/k >= threshold:
                count+=1
            start+=1
            end+=1
        return count

        
        