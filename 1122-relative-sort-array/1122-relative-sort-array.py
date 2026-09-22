
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Task 1 & 2: Initialize dictionary with arr2 keys
        arr2_counts = {}
        for num in arr2:
            arr2_counts[num] = 0
            
        leftovers = []
        
        # Harvest counts from arr1 and isolate leftovers
        for num in arr1:
            if num in arr2_counts:
                arr2_counts[num] += 1
            else:
                leftovers.append(num)
                
        # Reconstruct Stage 1: Build the relative sorted part
        result = []
        for num in arr2:
            for _ in range(arr2_counts[num]):
                result.append(num)
            
        # Task 3: Sort leftovers using your Counting Sort approach
        if leftovers:
            min_val = min(leftovers)
            max_val = max(leftovers)
            
            # Build frequency map for leftovers manually
            leftover_counts = {}
            for num in leftovers:
                if num in leftover_counts:
                    leftover_counts[num] += 1
                else:
                    leftover_counts[num] = 1
            
            # Reconstruct sorted leftovers and add them directly to result
            for i in range(min_val, max_val + 1):
                if i in leftover_counts:
                    for _ in range(leftover_counts[i]):
                        result.append(i)
            
        return result
