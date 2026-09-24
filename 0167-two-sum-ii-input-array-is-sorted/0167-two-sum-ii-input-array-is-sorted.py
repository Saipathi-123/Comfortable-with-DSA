class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for i, num in enumerate(numbers):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining] + 1, i + 1]
            seen[num] = i
