class Solution {
    public int removeDuplicates(int[] nums) {
        int freq=1;
        int place=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                freq++;
            }
            else{
                freq=1;
            }
            if(freq<=2){
                nums[place]=nums[i];
                place++;
            }
        }
        return place;
    }
}