class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counts = {}
        result = []
        
        # Step 1: Count frequencies of elements in nums1
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
            
        # Step 2: Iterate through nums2 and collect common elements
        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1  # Reduce the available frequency
                
        return result
