class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        target = k * threshold

        prefix = [0] * (len(arr) + 1)
        for i in xrange(len(arr)):
            prefix[i + 1] = prefix[i] + arr[i]

        return sum(1 for i in xrange(len(arr) - k + 1) if prefix[i + k] - prefix[i] >= target)
