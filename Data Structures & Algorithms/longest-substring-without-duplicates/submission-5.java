class Solution {
    public int lengthOfLongestSubstring(String s) {

        char[] char_array = s.toCharArray();
        int maxLen = 0;
        
        for(int i = 0; i < char_array.length; i++) {
            HashSet<Character> seen = new HashSet<>();

            for(int j = i; j < char_array.length; j++) {
                if(seen.contains(char_array[j])) {
                    maxLen = Math.max(maxLen, seen.size());
                    break;
                }
                else {
                    seen.add(char_array[j]);
                    maxLen = Math.max(maxLen, seen.size()); 
                } 
            }   
        }
        return maxLen;
    }
}
