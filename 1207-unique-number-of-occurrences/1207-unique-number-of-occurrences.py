class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        seen=set()
        for value in freq.values():
            if value in seen:
                return False
            seen.add(value)
        return True

        