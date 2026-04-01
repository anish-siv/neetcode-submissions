class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen_nums = new HashSet<>();

        for(int num : nums) {
            if(seen_nums.contains(num)) {
                return true;
            }
            else {
                seen_nums.add(num);
            }
        }
        return false;
    }
}