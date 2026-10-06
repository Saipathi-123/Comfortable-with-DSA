class Solution {
    public int maxVowels(String s, int k) {
        // Fast direct lookup array for lowercase English letters
        boolean[] isVowel = new boolean[26];
        isVowel['a' - 'a'] = true;
        isVowel['e' - 'a'] = true;
        isVowel['i' - 'a'] = true;
        isVowel['o' - 'a'] = true;
        isVowel['u' - 'a'] = true;
        
        int currentVowels = 0;
        
        

        for (int i = 0; i < k; i++) {
            if (isVowel[s.charAt(i) - 'a']) {
                currentVowels++;
            }
        }
        
        int maxVowels = currentVowels;
        

        if (maxVowels == k) {
            return k;
        }
        

        for (int i = k; i < s.length(); i++) {

            if (isVowel[s.charAt(i) - 'a']) {
                currentVowels++;
            }

            if (isVowel[s.charAt(i - k) - 'a']) {
                currentVowels--;
            }

            maxVowels=Math.max(maxVowels,currentVowels);
        }
        
        return maxVowels;
    }
}
