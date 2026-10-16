class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap seen (Key = number in nums : Value = index of number in nums)

        // For each num in nums
            // Compute complement (complement = target - nums[i])
            // If the complement exists in seen
                // Return int array of the current indice and the indice of the complement
            // Else
                // Add the number to seen
        // Return empty array 


        HashMap<Integer, Integer> seen = new HashMap<>(); // (Key = number in nums : Value = index of number in nums)

        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if(seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            } else { seen.put(nums[i], i); }
        }
        return new int[] {};
    }
}
