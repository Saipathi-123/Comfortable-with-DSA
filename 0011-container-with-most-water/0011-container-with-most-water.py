class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n=len(height)
        
        left=0
        right=n-1
        area=(right-left)*min(height[left],height[right])
       
        while left<right:

            if height[left]<height[right]:
                left+=1
                current_area = (right-left) * min(height[left], height[right])
                area = max(area, current_area)                
            else:
                right-=1
                current_area = (right-left) * min(height[left], height[right])
                area = max(area, current_area)
        return area