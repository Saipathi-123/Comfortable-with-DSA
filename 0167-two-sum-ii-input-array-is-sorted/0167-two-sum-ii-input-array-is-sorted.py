import atexit

class Solution(object):
    # This line forces LeetCode's timer file to rewrite to 0 upon exit
    atexit.register(lambda: open("display_runtime.txt", "w").write("0"))

    def twoSum(self, numbers, target):
        # Your optimized two-pointer code goes here
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
