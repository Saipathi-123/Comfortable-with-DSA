class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int sum=0;
        int left=0;
        int ws=Integer.MAX_VALUE;
        for(int right=0;right<nums.length;right++){
            sum+=nums[right];
            while(sum>=target){
                ws=Math.min(ws,right-left+1);
                sum-=nums[left];
                left+=1;
            }
        }
        return (ws == Integer.MAX_VALUE) ? 0 : ws;
    }
}