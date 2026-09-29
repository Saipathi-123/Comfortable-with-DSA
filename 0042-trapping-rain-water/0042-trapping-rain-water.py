class Solution(object):
    def trap(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        lmax,rmax,total=0,0,0
        l,r=0,len(arr)-1
        while(l<r):
            if arr[l]<=arr[r]:
                if lmax>arr[l]:
                    total+=lmax-arr[l]
                    l+=1
                else:
                    lmax=arr[l]
                    l+=1
            else:
                if rmax>arr[r]:
                    total+=rmax-arr[r]
                    r-=1
                else:
                    rmax=arr[r]
                    r-=1
        return total
                
        