class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dict={}
        crosses=0
        maxx=0
        for i in range(len(wall)):
            sum=0
            for j in range(len(wall[i])-1):
                sum+=wall[i][j]
                if sum in dict:
                    dict[sum]+=1
                else:
                    dict[sum]=1
                maxx=max(maxx,dict[sum])
        crosses=len(wall)-maxx
        return crosses


        