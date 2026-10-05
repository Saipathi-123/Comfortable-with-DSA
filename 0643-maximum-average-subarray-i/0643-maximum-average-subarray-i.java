class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int curr_sum=0;
        for(int i=0;i<k;i++){
            curr_sum+=nums[i];
        }
        double max_avg=(double)curr_sum/k;
        int start=1;
        int end=k;
        while(end<nums.length){
            curr_sum=curr_sum-nums[start-1]+nums[end];
            double curr_avg=(double)curr_sum/k;
            max_avg=Math.max(max_avg,curr_avg);
            start++;
            end++;
        }
        return max_avg;
    }
}