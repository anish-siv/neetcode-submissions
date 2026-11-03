class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for(int count : nums) {
            if(seen.contains(count)) {
                return true;
            } else { seen.add(count); }
        }
        return false;
    }
}