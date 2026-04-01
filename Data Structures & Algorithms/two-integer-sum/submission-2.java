class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen_nums = new HashMap<>(); 
        
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen_nums.containsKey(complement)) {
                return new int[] { seen_nums.get(complement), i };
            }
            seen_nums.put(nums[i], i);
        }
        return new int[] {};
    }
}