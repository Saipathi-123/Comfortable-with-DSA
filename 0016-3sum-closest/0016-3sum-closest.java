class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int clos_diff=nums[0]+nums[1]+nums[2];
        for(int i=0;i<nums.length-2;i++){
            int left=i+1;
            int right=nums.length-1;
            while(left<right){
                int curr_sum=nums[i]+nums[left]+nums[right];
                if(Math.abs(curr_sum-target)<Math.abs(clos_diff-target)){
                    clos_diff=curr_sum;
                }
                if(curr_sum<target){left+=1;}
                else if(curr_sum>target){right-=1;}
                else{return curr_sum;}
            }
        }
        return clos_diff;     
    }
}