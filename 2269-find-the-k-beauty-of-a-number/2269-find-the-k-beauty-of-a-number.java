class Solution {
    public int divisorSubstrings(int num, int k) {
        int count = 0;
        int temp = num;
        int modBase = (int) Math.pow(10, k);
        int limit = (int) Math.pow(10, k - 1);
        while (temp >= limit) {
            int subNum = temp % modBase;
            if (subNum != 0 && num % subNum == 0) {
                count++;
            }
            temp /= 10;
        }
        return count;
    }
}
