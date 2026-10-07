class Solution {
    public int maximumLengthSubstring(String s) {
        int left=0,right=0,ws=0;
        int[] count=new int[26];
        while(right<s.length()){
            int ind=s.charAt(right)-'a';
            if(count[ind]<2){
                count[ind]++;
                ws=Math.max(ws,right-left+1);
                right++;
            }
            else{
                int left_index=s.charAt(left)-'a';
                count[left_index]--;
                left++;
            }
        }
        return ws;
    }
}