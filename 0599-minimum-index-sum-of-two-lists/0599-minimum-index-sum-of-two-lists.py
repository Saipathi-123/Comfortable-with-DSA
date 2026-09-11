class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_sum=float("+inf")
        list1_hash={}
        result=[]
        
        for i,char in enumerate(list1):
            list1_hash[char]=i
        for j,char in enumerate(list2):
            if char in list1_hash:
                i=list1_hash[char]
                curr_sum=i+j
                if curr_sum<min_sum:
                    min_sum=curr_sum
                    result=[char]
                elif curr_sum==min_sum:
                    result.append(char)
        return result

        

        