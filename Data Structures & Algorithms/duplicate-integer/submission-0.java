class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int i = 0; i < nums.length; i++) { // Iterate through the whole array
            for(int j = i + 1; j < nums.length; j++) { // Compare it with every subsequent element
                if(nums[i] == nums[j]) { // If the number in index i is the same as the one in index j, return true
                    return true;
                }
            }
        }
        return false; // Else, return false
    }
}
