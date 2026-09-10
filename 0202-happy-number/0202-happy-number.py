class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen_numbers=set()

        while True:
            sum=0
            while n>0:
                rem=n%10
                sum+=rem*rem
                n=n//10
            if sum==1:
                return True
                break
            if sum in seen_numbers:
                return False
                break
            seen_numbers.add(sum)
            n=sum
        