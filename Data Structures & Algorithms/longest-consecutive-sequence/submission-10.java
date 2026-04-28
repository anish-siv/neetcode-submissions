class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        int seqStart = 0;
        int longestCount = 0;

        for(int i = 0; i < nums.length; i++) {
            seen.add(nums[i]);
        }

        for(int i = 0; i < nums.length; i++) {
            if(!seen.contains(nums[i] - 1)) {
                seqStart = nums[i];
                
                int currCount = 1;

                while(seen.contains(seqStart + 1)) {
                    seqStart++;
                    currCount++;
                }
                longestCount = Math.max(longestCount, currCount);
            }
        }
        return longestCount;
    }
}
