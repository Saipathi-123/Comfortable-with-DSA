class Solution {
    public int lengthOfLongestSubstring(String s) {
        int ws = 0;
        int left = 0;
        boolean[] nums = new boolean[256];
        
        for (int right = 0; right < s.length(); right++) {
            char current = s.charAt(right);

            if (nums[current]) {
                while (nums[current]) {
                    nums[s.charAt(left)] = false;
                    left++;
                }
            }
            
            nums[current] = true;
            ws = Math.max(ws, right - left + 1);
        }
        return ws;
    }
}
