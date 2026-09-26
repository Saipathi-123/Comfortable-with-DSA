class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        
        while left < right:
            # Calculate the area between the two pointers
            area = (right - left) * min(height[left], height[right])
            
            # Update the maximum area found so far
            max_area = max(area, max_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
