class Solution {
    public int minimumRecolors(String blocks, int k) {
        int curr_whites = 0;
        int min_whites = 0;
        
        for (int i = 0; i < k; i++) {
            // FIX 1: Changed double quotes "" to single quotes '' and capitalized 'W'
            if (blocks.charAt(i) == 'W') { 
                curr_whites++;
            }
        }
        
        min_whites = curr_whites;
        
        for (int i = k; i < blocks.length(); i++) {
            // FIX 1: Changed to single quotes 'W'
            if (blocks.charAt(i) == 'W') {
                curr_whites++;
            }
            // FIX 1: Changed to single quotes 'W'
            if (blocks.charAt(i - k) == 'W') {
                curr_whites--;
            }
            // FIX 2: Corrected 'Match' to 'Math'
            min_whites = Math.min(curr_whites, min_whites); 
        }
        
        return min_whites;
    }
}
