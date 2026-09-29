import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            for (int j = i + 1; j < n; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                
                int left = j + 1;
                int right = n - 1;
                

                long goal = (long) target - nums[i] - nums[j];
                
                while (left < right) {
                    int two_sum = nums[left] + nums[right];
                    
                    if (two_sum == goal) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        
                        while (left < right && nums[left] == nums[left - 1]) {
                            left++;
                        }
                    } else if (two_sum > goal) {
                        right--;
                    } else {
                        left++;
                    }
                }
            }
        }
        return res;
    }
}
