class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        curr_whi=0
        for block in blocks[:k]:
            if block.lower()=="w":
                curr_whi+=1
        min_whites=curr_whi
        
        for i in range(k,len(blocks)):
            if blocks[i].lower()=="w":
                curr_whi+=1
            if blocks[i-k].lower()=="w":
                curr_whi-=1
            min_whites=min(min_whites,curr_whi)

        return min_whites

        