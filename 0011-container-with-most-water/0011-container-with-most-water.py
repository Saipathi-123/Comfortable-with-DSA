class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n=len(height)
        area=0
        left=0
        right=n-1
        max_area=0
        while left<right:
            area=(right-left)*min(height[left],height[right])
            max_area=max(area,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area