class Solution {
    public int numRescueBoats(int[] nums, int target) {
        Arrays.sort(nums);
        int count=0;
        int i=0;
        int j=nums.length-1;
        while(i<=j){
            if(nums[i]==target){
                count+=1;
                i+=1;
            }
            else if(nums[j]==target){
                count+=1;
                j-=1;
            }
            else if(nums[i]+nums[j]==target){
                count+=1;
                i+=1;
                j-=1;
            }
            else if(nums[i]+nums[j]>target){
                count+=1;
                j-=1;
            }
            else if(nums[i]+nums[j]<target){
                count+=1;
                i+=1;
                j-=1;
            }
        }
        return count;     
        
    }
}