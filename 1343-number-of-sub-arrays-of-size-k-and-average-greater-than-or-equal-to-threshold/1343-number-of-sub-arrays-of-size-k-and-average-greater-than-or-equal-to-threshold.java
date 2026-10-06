import java.util.List;

class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
 
        int summ = 0;
        for (int i = 0; i < k; i++) {
            summ += arr[i];
        }

        // Note: Using (double) ensures accurate floating-point division
        if ((double) summ / k >= threshold) {
            count += 1;
        }
        int start = 1;
        int end = k;
        while (end < arr.length) {
            summ = summ - arr[start - 1] + arr[end];
            if ((double) summ / k >= threshold) {
                count += 1;
            }
            start += 1;
            end += 1;
        }
        return count;
    }
}
