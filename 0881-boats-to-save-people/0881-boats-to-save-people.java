class Solution {
    public int numRescueBoats(int[] nums, int target) {
        Arrays.sort(nums);
        int count=0;
        int i=0;
        int j=nums.length-1;
        while(i<=j){
            if(nums[i]+nums[j]<=target){
                i++;
                j--;
            }
            else{
                j--;
            }
            count++;
        }

        return count;     
        
    }
}