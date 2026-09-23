import random
class RandomizedSet(object):

    def __init__(self):
        self.dict={}
        self.nums=[]
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.dict[val]=len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False

        last_index=self.dict[val]
        last_val=self.nums[-1]

        self.nums[last_index]=last_val
        self.dict[last_val]=last_index

        self.nums.pop()
        del self.dict[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()