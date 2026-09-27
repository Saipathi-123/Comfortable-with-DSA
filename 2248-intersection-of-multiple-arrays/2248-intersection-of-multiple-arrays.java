class Solution {
    public List<Integer> intersection(int[][] nums) {
        int[] freq=new int[1001];
        List<Integer> res= new ArrayList<>();
        int n=nums.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<nums[i].length;j++){
                freq[nums[i][j]]+=1;
            }
        } 
        for(int i=0;i<1001;i++){
            if(freq[i]==n){
                res.add(i);
            }
        }
        return res;
        
    }
}