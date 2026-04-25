class Solution {
    public int longestConsecutive(int[] nums) {
        
        HashSet<Integer> seen = new HashSet<>();
        int seqStart = 0;
        int longestCount = 0;

        for (int i = 0; i < nums.length; i++) { // For loop to add all elements from nums to seen
            seen.add(nums[i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (!seen.contains(nums[i] - 1)) { // If seen does not contain a number less than the
                                               // current, it is the sequence start
                seqStart = nums[i]; // Assign number as sequence start

                int currentCount = 1;

                while (seen.contains(seqStart + 1)) { // While seen contains sequence start + 1
                    seqStart++;
                    currentCount++;
                }
                longestCount = Math.max(currentCount, longestCount);
            }
        }
        return longestCount;
    }
}