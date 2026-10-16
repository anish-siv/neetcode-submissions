class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Create a HashSet freq

        // For each num in nums
            // If num in freq (freq.contains(nums[i]))
                // Return true
            // else
                // Add to freq (freq.add(nums[i]))
        // Return false

        Set<Integer> freq = new HashSet<>();

        for(int i = 0; i < nums.length; i++) {
            if(freq.contains(nums[i])) {
                return true;
            } else { freq.add(nums[i]); }
        }
        return false;
    }
}