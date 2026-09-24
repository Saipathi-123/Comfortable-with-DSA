class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers.insert(0,0)
        left=1
        right=len(numbers)-1
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return [left,right]
                break
            elif sum>target:
                right-=1
            elif sum<target:
                left+=1
            

        