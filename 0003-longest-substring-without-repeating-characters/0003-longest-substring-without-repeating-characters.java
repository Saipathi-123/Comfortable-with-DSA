class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ws=0,left=0;
        boolean[] nums=new boolean[256];
        for(int right=0;right<s.length();right++){
            int index=(int)s.charAt(right);
            if(nums[index]){
                while(nums[index]){
                    nums[(int)s.charAt(left)]=false;
                    left++;
                }
            }
            nums[index]=true;
            ws=Math.max(ws,right-left+1);
        }
        return ws;
    }
}